import streamlit as st
import pandas as pd

# 앱 제목 설정
st.title("📚 공부 습관 대시보드")

# 1. 데이터 불러오기
df = pd.read_csv("study.csv")

# 2. 요약 지표(학생 수, 평균 점수, 평균 공부시간) 보여주기
col1, col2, col3 = st.columns(3)
col1.metric("총 학생 수", f"{len(df)}명")
col2.metric("평균 점수", f"{df['점수'].mean():.1f}점")
col3.metric("평균 공부시간", f"{df['공부시간'].mean():.1f}시간")

st.divider()

# 3. 최소 공부시간 선택 슬라이더 (사이드바)
min_hours = st.sidebar.slider(
    "최소 공부시간 선택",
    min_value=int(df["공부시간"].min()),
    max_value=int(df["공부시간"].max()),
    value=int(df["공부시간"].min())
)

# 4. 조건에 맞는 학생 데이터 필터링
filtered_df = df[df["공부시간"] >= min_hours]

# 5. 필터링된 결과 그래프 그리기
st.subheader(f"⏱️ 공부시간 {min_hours}시간 이상 학생 데이터")

# 산점도: 공부시간 vs 점수
st.write("### 📍 공부시간과 점수의 관계 (산점도)")
st.scatter_chart(data=filtered_df, x="공부시간", y="점수")

# 막대 그래프: 학생별 점수
st.write("### 📊 학생별 점수 (막대 그래프)")
st.bar_chart(data=filtered_df, x="학생ID", y="점수")