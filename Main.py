import sys
import os
import pymysql # 데이터베이스 연결 시에만 사용
import pymssql
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PyQt5.QtGui import QIntValidator

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5.QtWidgets import *
from PyQt5 import uic

from Data_analysis import Data_analysis
from Analysis_1d import Analysis_1d
from Analysis_2d import Analysis_2d
from Learning import Learning

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path("Main.ui")
form_main = uic.loadUiType(form)[0]

class MainWindow(QMainWindow, QWidget, form_main):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

        # 데이터 프레임
        self.DF = pd.DataFrame()
        self.DF_sample = pd.DataFrame()
        self.scroll = QScrollArea()
        self.topFiller = QWidget()  # 위젯생성

        # 메뉴 이벤트
        self.action_open_api.triggered.connect(lambda state, widget=self.table_dataframe: self.openApiFunction(state, widget)) # 데이터베이스 연결
        self.action_open_local.triggered.connect(lambda state, widget=self.table_dataframe: self.openLocalFunction(state, widget))
        self.action_exit.triggered.connect(lambda state: self.exitFunction())

        # 버튼 클릭 이벤트
        self.btn_data_analysis.clicked.connect(self.btnClicked_data_analysis)
        self.btn_analysis_1d.clicked.connect(self.btnClicked_analysis_1d)
        self.btn_analysis_2d.clicked.connect(self.btnClicked_analysis_2d)
        self.btn_learning.clicked.connect(self.btnClicked_learning)
        self.pushButton.clicked.connect(self.dialog_open)

        # plot 적용을 위한 초기화
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout_datachart.addWidget(self.canvas)
        self.layout_datachart.addWidget(self.toolbar)

        # 피처 리스트
        self.feature_list = []

    def getDF(self):
        return self.DF




    # 열기(API) 함수
    def openApiFunction(self, state, widget):

        self.dialog = QDialog()
        self.InnerLayOut = QVBoxLayout()

        self.LineEdit = QLineEdit()
        self.LineEdit2 = QLineEdit()

            # 라인 텍스트
        self.LineEdit.setPlaceholderText("시작날짜 입력: 2022-10-01")
        self.LineEdit2.setPlaceholderText("종료날짜 입력: 2022-10-18")
        #LineEdit.setValidator(QIntValidator(1, len(self.DF), self)) # (1~샘플의 개수자리)까지 입력가능

        # 버튼 생성

        self.btnRun = QPushButton("확인")
        self.btnRun.clicked.connect(lambda state, widget=self.table_dataframe: self.realApiFunction(self.dialog, state, widget,"\'" + str(self.LineEdit.text()) + " 00:00:00\'", "\'" +str(self.LineEdit2.text()) + " 00:00:00\'"))

            # Layout에 붙이기

        self.InnerLayOut.addWidget(self.LineEdit)
        self.InnerLayOut.addWidget(self.LineEdit2)
        self.InnerLayOut.addWidget(self.btnRun)
        # 위젯 설정
        self.dialog.setLayout(self.InnerLayOut)
        self.dialog.setWindowTitle('Date Select')
        self.dialog.setWindowModality(0)  ## Qt 에러
        self.dialog.resize(500, 200)
        self.dialog.show()
        #self.dialog.exec()

    #def showDialog(self):


    def realApiFunction(self, dialog, state, widget, startDate, endDate):
        dialog.close()
        float_64 = ['CycleTime', 'InjTime', 'RecoveryT', 'Cushion', 'InjSpeed', 'ThroatTemp', 'HPTransPrs',
                    'HPTransPos', 'Oily', 'Moisture', 'Ebi', 'Eai', 'paintTemp', 'supportTemp', 'supportHumidity',
                    'pportRTemp', 'supportRHumidity', 'ApplyS', 'PatternS', 'ApplyP', 'PatternP', 'TEMP', 'HUMIDITY',
                    'RTEMP', 'RHUMIDITY', 'DP001', 'DP002', 'DP003', 'DP004', 'DP005', 'DP006', 'DP007', 'DP008',
                    'DP009', 'SPTEMP', 'SPHUMIDITY', 'WH1ACTIONTEMPP', 'WH1INTEMP', 'WH1OUTTEMP', 'WH1INFLUX',
                    'WH2ACTIONTEMPP', 'WH2INTEMP', 'WH2OUTTEMP', 'WH2INFLUX', 'WH3ACTIONTEMPP', 'WH3INTEMP',
                    'WH3OUTTEMP', 'WH3INFLUX', 'WH4ACTIONTEMPP', 'WH4INTEMP', 'WH4INFLUX', 'CTACTIONTEMPP',
                    'CTPRESSURE', 'CTOUTTEMP', 'OUTTEMP', 'OUTHUMIDITY', 'MI_TEST_RESULT']
        int_64 = ['uvlamp_cycletime', 'InjPress', 'TotalShot', 'INPUT', 'SprayS', 'SprayP', 'DRYING', 'Temp1', 'Temp2',
                  'Temp3', 'Temp4', 'Temp5', 'Temp6', 'Temp7', 'Temp8', 'Temp9', 'UvTemp1', 'UvTemp2', 'UvTemp3',
                  'UvTemp4', 'UvTemp5', 'UvTemp6', 'UvTemp7', 'UvTemp8', 'UvTemp9', 'UvTemp10', 'LABORATOR',
                  'HP1ACTIONTEMPP', 'HP1ACTIONTEMPS', 'HP1ENDTEMP', 'HP2ACTIONTEMPP', 'HP2ACTIONTEMPS', 'HP2ENDTEMP',
                  'WH1ACTIONTEMPS', 'WH2ACTIONTEMPS', 'WH3ACTIONTEMPS', 'WH4ACTIONTEMPS', 'WH4OUTTEMP', 'CTACTIONTEMPS',
                  'PAMCALE_RESULT']

        host_name = '????'
        host_port = ????
        username = '????'
        password = '????'
        database_name = '???'
        server = '***.***.***.**'


        db = pymysql.connect(
            host=host_name,  # MySQL Server Address
            port=host_port,  # MySQL Server Port
            user=username,  # MySQL username
            password=password,  # password for MySQL username
            database=database_name,  # Database name
            charset='utf8'
        )


        sql = "select * from INJECTION_SORT where TIME_STAMP between {} and {}".format(startDate,endDate)
        df = pd.read_sql(sql, db)

        # 전처리(dtype 변경)
        for i, col in enumerate(df.columns):
            if col in float_64:
                df[col] = df[col].astype('float64')
            elif col in int_64:
                df[col] = df[col].astype('int64')

        df.rename(columns={'PARAMETER_VALUE': 'RESULT'}, inplace=True)

        print(df)
        self.DF = df.copy()
        self.create_dataframe(widget, df.head(10))
        self.show_datainfo(df)
        self.show_datachart(df)

    # 열기(Local) 함수
    def openLocalFunction(self, state, widget):
        fname = QFileDialog.getOpenFileName(self, "파일 열기", "", "CSV files (*.csv)")

        if fname[0]:
            df = pd.read_csv(fname[0])
            self.DF = df.copy()
            self.create_dataframe(widget, df.head(10))
            self.show_datainfo(df)
            self.show_datachart(df)

    # 끝내기 함수
    def exitFunction(self):
        sys.exit(app.exec_())

    # window 창닫기 이벤트(고유)
    def closeEvent(self, QCloseEvent):
        re = QMessageBox.question(self, "종료 확인", "종료 하시겠습니까?", QMessageBox.Yes | QMessageBox.No)
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def create_dataframe(self, widget, df):
        widget.setRowCount(len(df.index))
        widget.setColumnCount(len(df.columns))
        widget.setHorizontalHeaderLabels(df.columns)

        for row_index, row in enumerate(df.index):
            for col_index, col in enumerate(df.columns):
                widget.setItem(row_index, col_index, QTableWidgetItem(str(df.loc[row][col])))

    def dialog_open(self):
        if len(self.getDF()) != 0:
            global dialog, cb, LineEdit

            dialog = QDialog()
            InnerLayOut = QVBoxLayout()
            groupbox = QGroupBox('CheckBox')
            scroll = QScrollArea()
            vbox = QVBoxLayout()
            LineEdit = QLineEdit()

            cb = []
            for i, col in enumerate(self.DF.columns):
                cb.append(QCheckBox("{}".format(col)))
                vbox.addWidget(cb[i])
            groupbox.setLayout(vbox)

            scroll.setWidget(groupbox)
            scroll.setWidgetResizable(True)

            # 라인 텍스트
            LineEdit.setPlaceholderText("시각화할 데이터 개수 입력(1~{})".format(len(self.DF)))
            LineEdit.setValidator(QIntValidator(1, len(self.DF), self)) # (1~샘플의 개수자리)까지 입력가능

            # 버튼 생성
            btnRun = QPushButton("Set Selected Features")
            btnRun.clicked.connect(self.setFeature)

            # Layout에 붙이기
            InnerLayOut.addWidget(scroll)
            InnerLayOut.addWidget(LineEdit)
            InnerLayOut.addWidget(btnRun)

            # 위젯 설정
            dialog.setLayout(InnerLayOut)
            dialog.setWindowTitle('Set Feature')
            dialog.setWindowModality(0)  ## Qt 에러
            dialog.resize(300, 200)
            dialog.show()
        else:
            QMessageBox.critical(self, 'Error', '데이터 파일을 먼저 불러와주시길 바랍니다.')

    def setFeature(self):
        # LineEdit 텍스트 입력 여부 확인
        if LineEdit.text() == "":
            QMessageBox.critical(dialog, 'Error', '시각화할 데이터의 개수를 입력 바랍니다.')
        else:
            textList = []
            for i, col in enumerate(self.DF.columns):
                if (cb[i].isChecked() == True):
                    textList.append(cb[i].text())

            # feature 체크 여부 확인
            if len(textList) == 0:
                QMessageBox.critical(dialog, 'Error', 'Feature를 최소 1개 이상 선택 바랍니다.')
            else:
                DF_sample = self.DF.loc[:, textList]
                self.create_dataframe(self.table_dataframe, DF_sample.head(int(LineEdit.text())))
                dialog.close()

    def show_datainfo(self, df):
        self.textEdit_sample.setText(str(len(df)))
        self.textEdit_good.setText(str(len(df[df['RESULT'] == 'GOOD'])))
        self.textEdit_bad.setText(str(len(df[df['RESULT'] != 'GOOD'])))

    def show_datachart(self, df): # 그래프 띄우는 거
        self.fig.clear()
        vc = (df['RESULT'].value_counts().to_frame().reset_index())
        vc = vc.drop(0)
        self.ax = self.fig.add_subplot(111)
        sns.barplot(ax=self.ax, x=vc['RESULT'], y=vc['index'], data=vc)
        self.ax.set(xlabel=None, ylabel=None)
        self.ax.grid(True, axis='x', alpha=0.5, linestyle='--')
        self.fig.tight_layout()
        self.canvas.draw()

    def btnClicked_data_analysis(self):
        if len(self.getDF()) != 0:
            self.dataAnalysis = Data_analysis(self.getDF(), self.feature_list)
            self.dataAnalysis.show()
        else:
            QMessageBox.critical(self, 'Error', '데이터 파일을 먼저 불러와주시길 바랍니다.')

    def btnClicked_analysis_1d(self):
        if len(self.getDF()) != 0:
            self.analy1d = Analysis_1d(self.getDF())
            self.analy1d.show()
        else:
            QMessageBox.critical(self, 'Error', '데이터 파일을 먼저 불러와주시길 바랍니다.')

    def btnClicked_analysis_2d(self):
        if len(self.getDF()) != 0:
            self.analy2d = Analysis_2d(self.getDF())
            self.analy2d.show()
        else:
            QMessageBox.critical(self, 'Error', '데이터 파일을 먼저 불러와주시길 바랍니다.')

    def btnClicked_learning(self):
        self.learn = Learning(self.feature_list, self.getDF())
        self.learn.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
