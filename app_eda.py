import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def run_eda():
    st.subheader('데이터 분석')

    # 데이터 로드
    df = pd.read_csv('data/50_Startups.csv')

    # 기본 통계량 보기
    if st.checkbox('기본 통계 확인하기'):
        st.write(df.describe())

    # 컬럼 선택 기능
    column = st.selectbox('컬럼을 선택하세요', df.columns)
    
    # 선택한 컬럼의 히스토그램
    fig1 = plt.figure()
    plt.hist(data=df, x=column, bins=20)
    plt.title(f'{column} 히스토그램')
    plt.xlabel(column)
    plt.ylabel('빈도수')
    st.pyplot(fig1)

    # 수치형 컬럼들의 상관관계
    st.subheader('변수 간 상관관계')
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    correlation = df[numeric_columns].corr()
    
    # 히트맵 그리기
    fig2 = plt.figure(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('상관관계 히트맵')
    st.pyplot(fig2)

    # 주별 통계
    st.subheader('주(State)별 통계')
    state_mean = df.groupby('State').mean()
    st.write('주별 평균 통계:', state_mean)

    # Scatter Plot (plotly 사용)
    st.subheader('변수 간 산점도')
    x_column = st.selectbox('X축 선택', numeric_columns)
    y_column = st.selectbox('Y축 선택', numeric_columns)
    
    fig3 = px.scatter(df, x=x_column, y=y_column, 
                     color='State', 
                     title=f'{x_column} vs {y_column}')
    st.plotly_chart(fig3)

    # Box Plot
    st.subheader('주별 수익 분포')
    fig4 = plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='State', y='Profit')
    plt.title('주별 수익 분포')
    st.pyplot(fig4)

    # 추가 분석: 상위/하위 기업
    st.subheader('수익 기준 상위/하위 기업')
    top_n = st.slider('표시할 기업 수 선택', 1, 10, 5)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f'상위 {top_n}개 기업:')
        st.write(df.nlargest(top_n, 'Profit')[['State', 'Profit', 'R&D Spend', 'Marketing Spend']])
    
    with col2:
        st.write(f'하위 {top_n}개 기업:')
        st.write(df.nsmallest(top_n, 'Profit')[['State', 'Profit', 'R&D Spend', 'Marketing Spend']])