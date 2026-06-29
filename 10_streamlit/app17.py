import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import pandas as pd
# 가상 데이터 생성: 시간에 따른 주가 변동 시뮬레이션
days = np.linspace(1, 100, 100)  # 100일간의 데이터
stock_price = 100 + np.random.normal(0, 1, 100).cumsum()  # 랜덤하게 변동하는 주가

# 그래프 생성
fig, ax = plt.subplots()
ax.plot(days, stock_price, label="Stock Price", color='blue', linestyle='-', marker='o')
ax.set_title("100일 동안의 주가 변동")
ax.set_xlabel("날짜")
ax.set_ylabel("주가 (단위: $)")
ax.legend()

# Streamlit에서 그래프 출력
st.pyplot(fig)


# 가상 데이터 생성: 월별 매출 및 이익 데이터
data = pd.DataFrame({
    '월': pd.date_range(start='2024-01-01', periods=12, freq='ME'),
    '매출': [500, 600, 700, 800, 900, 850, 950, 1100, 1050, 1200, 1250, 1300],
    '이익': [50, 60, 70, 85, 90, 80, 95, 100, 105, 110, 120, 130]
})

# Altair 차트 생성
chart = alt.Chart(data).mark_line(point=True).encode(
    x='월:T',
    y='매출:Q',
    tooltip=['월:T', '매출:Q', '이익:Q']
).properties(
    title="2024년 월별 매출 및 이익"
)

# 차트 출력
st.altair_chart(chart, use_container_width=True)

import streamlit as st
import pandas as pd

# 가상 데이터 생성
df = pd.DataFrame({
    '이름': ['홍길동', '김철수', '이영희'],
    '점수': [85, 90, 95]
})

# CSV로 변환
csv = df.to_csv().encode('utf-8')

# 다운로드 버튼
st.download_button(label="CSV 다운로드", data=csv, file_name='data.csv', mime='text/csv')