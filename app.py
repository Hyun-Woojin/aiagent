# 분류 모델 웹앱 만들기
import streamlit as st

# 1.기계학습 모델 파일 로드
import joblib
model = joblib.load('linear_regression_model.pkl') 

# 2.모델 설명
st.title('칼로리 소모에 따른 달릴 거리 예측 에이전트')
col1, col2,col3 = st.columns(3)      
with col1:
      st.subheader('모델 설명 ')
      st.write(' - 기계학습 알고리즘 : 선형 회귀 ')
      st.write(' - 학습 데이터 출처 : https://www.kaggle.com/code/alfredkondoro/eda-cardio-activities/input')
      st.write(' - 피드백 링크: https://docs.google.com/forms/d/e/1FAIpQLSd40XDiG3chAODACK03Yeoe5W72GW3S03VFFvXw_R_wkh80kA/viewform')
      st.write(' - 훈련    데이터 : 350건')
      st.write(' - 테스트 데이터 : 150건')
      st.write(' - 모델 정확도 : 0.99')
# 3.데이터시각화
with col2:
      st.subheader('데이터시각화1')
      st.image('시각화1.png' )  
with col3:
      st.subheader('데이터시각화2')
      st.image('시각화2.png')   

# 4. 모델 활용
st.subheader('모델 활용')

st.write('**** 목표 칼로리를 입력하세요.. 인공지능이 목표 거리를 알려드립니다! ')

a = st.number_input(' 목표 칼로리 입력 ', value=0)      

if st.button('거리측정'):           

        input_data = [[a]]      
      
        p = model.predict(input_data)        
      
        st.write('인공지능의 예측 거리는', p)


 




              
