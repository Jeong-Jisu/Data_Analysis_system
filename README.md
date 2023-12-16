# Data_Analysis_system
Development of Data Analysis System for Determining Product Quaility of Injection Molding Machine Results


### stack
PyQT, QT Designer, Python, Statistics, ML/DL etc.

---
<br>
<br>

## Main.py 
![image01](https://github.com/Jeong-Jisu/Data_Analysis_system/assets/112859100/cb774b1b-062c-422a-b52f-65c56dfdba0f)

- 파일 : local 저장소 혹은 데이터베이스에서 데이터 파일을 불러오는 기능 수행
- Data Frame : 불러온 데이터 파일의 내용을 사용자에게 보여주는 기능 수행
- Data Info : 샘플의 총 개수와 양품/불량의 개수
- Data Chart : 데이터 결과 클래스에 대한 분포도
- Option : 사용자가 선택하는 개수와 속성만을 Data Frame 창에서 볼 수 있도록 하는 기능 수행
- 데이터 분석으로 가기 : 현재 결과 클래스에 영향을 끼치는 속성을 찾는 화면으로 이동
- 분석화면(1D)로 가기 : 양품과 불량에 영향을 끼치는 속성 중 1개를 선택하여 그래프로 시각화 하여 사용자에게 제공
- 분석화면(2D)로 가기 : 양품과 불량에 영향을 끼치는 속성 중 2개를 선택하여 그래프로 시각화 하여 사용자에게 제공
- 학습화면으로 가기 : 원하는 데이터를 학습(딥러닝)시키는 기능 수행


<br>
<br>

## Data_analysis.py
![image02](https://github.com/Jeong-Jisu/Data_Analysis_system/assets/112859100/3d177821-913b-427a-9ea3-7c968109a35c)
- 이상/결측치 제거 : IQR값을 이용하여 데이터의 이상치를 제거하고, 결측이 있는 데이터를 삭제한다.
- Object Type 제거 : 속성 중 수치형 데이터가 아닌 Object형 데이터를 삭제한다.
- 선형 회귀 분석 : 선형회귀모델을 사용하여 stepwise방법으로 결과 클래스에 영향을 주는 속성을 찾는다. 
- 정규화 검정 : 선형 회귀 분석을 통해 찾은 속성들이 정규 분포를 따르는지 검정하고 이를 통해 모수 검정/ 비모수 검정 실행 여부를 판단한다. 
- 독립 T 검정 : 두 집단의 평균 차이를 검증하기 위해 실행
- 데이터 분석 시작 : 등분산 검정이 시행된 피처에 대해 독립 t test를 시행하여 결과클래스에 영향을 끼치는 속성을 찾는다.
- Progress : 각 분석 버튼의 진행 상태를 시각적으로 표현한다.
- 창 닫기 : 현재 창을 종료한다.
- Description : 각 단계별 데이터 분석에 대한 간략한 설명과 분석 결과를 표시한다. 
- Graph : 모든 검정이 완료되어 최종적으로 선택된 피처에 대해 다양한 그래프 형식(Axvline, HistPlot, PointPlot 등)으로 사용자에게 G/NG에 대한 정보를 제공한다. 

※ 데이터 분석 과정에선 샘플링 데이터를 사용하나 그래프 상에서는 보여지는 데이터는 전체 데이터임

<br>
<br>

## Analysis_1d.py
![image03](https://github.com/Jeong-Jisu/Data_Analysis_system/assets/112859100/6cc9ab13-6f68-412a-97c0-35ab93ec3980)

- Graph : G/NG 데이터에 대해 Select Feature에서 선택된 속성에 대해 Select Graph Type에서 지정한 그래프를 사용자에게 보여주는 기능
- Select Graph Type : 다양한 그래프 형식(Boxplot, Pointplot, Axvline 등)을 선택할 수 있는 기능
- Select Feature : 보고자 하는 속성을 선택할 수 있는 기능

<br>
<br>

## Analysis_2d.py
![image04](https://github.com/Jeong-Jisu/Data_Analysis_system/assets/112859100/cc4f2d49-6d7f-41ba-9a7d-3e5a7a8bcee9)

- Graph 2D : G/NG 데이터에 대해 Select Feature에서 선택된 속성에 대해 Select Graph Type에서 지정한 그래프를 사용자에게 보여주는 기능
- Select Graph Type : 다양한 그래프 형식( Jointplot, Kdeplot, Regplot 등)을 선택할 수 있는 기능
- Select Feature 1/2 : 보고자 하는 속성을 선택할 수 있는 기능

<br>
<br>

## Learning.py
![image05](https://github.com/Jeong-Jisu/Data_Analysis_system/assets/112859100/37d9b00e-8f29-44cb-8348-66da1af314f5)

- Training Data File : 트레이닝 할 데이터 파일을 업로드한다.
- Test Data File : 테스트할 데이터 파일을 업로드한다.
- Result : G/NG에 예측에 대한 성능평가와 전체적인 정확도를 보여주는 기능 
