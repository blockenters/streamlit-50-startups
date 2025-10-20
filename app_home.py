import streamlit as st
import pandas as pd

def run_home():
    st.subheader('스타트업 수익 예측 프로젝트')
    
    st.markdown("""
    ### 프로젝트 소개
    이 앱은 스타트업 회사의 R&D 지출, 관리 비용, 마케팅 비용 등의 데이터를 기반으로
    회사의 수익을 예측하는 머신러닝 프로젝트입니다.
    
    ### 데이터셋 정보
    - R&D Spend: 연구개발 지출 비용
    - Administration: 관리 비용
    - Marketing Spend: 마케팅 지출 비용
    - State: 스타트업 소재 주(뉴욕, 캘리포니아, 플로리다)
    - Profit: 수익 (예측 대상)
    """)
    
    # 데이터 샘플 보여주기
    data = pd.read_csv('data/50_Startups.csv')
    st.subheader('데이터 미리보기')
    st.write(data.head())
    
    st.markdown("""
    ### 사용 방법
    1. 왼쪽 사이드바의 메뉴에서 원하는 기능을 선택하세요.
    2. EDA 메뉴: 데이터 탐색적 분석 결과를 확인할 수 있습니다.
    3. ML 메뉴: 머신러닝 모델을 통해 수익을 예측해볼 수 있습니다.
    
    ### 데이터셋 기본 정보
    """)
    
    # 데이터셋 기본 정보 표시
    col1, col2 = st.columns(2)
    
    with col1:
        st.write('데이터 크기:', data.shape)
        st.write('전체 회사 수:', len(data))
    
    with col2:
        st.write('평균 수익: ${:,.2f}'.format(data['Profit'].mean()))
        st.write('최대 수익: ${:,.2f}'.format(data['Profit'].max()))