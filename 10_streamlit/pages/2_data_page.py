# pages/2_character_page.py

import streamlit as st
import pandas as pd

# 페이지 제목
st.title("게임 캐릭터의 인지도")

# DataFrame 생성
data = pd.DataFrame({
    "캐릭터": ["전사", "법사", "힐러", "탱커", "랜덤"],
    "선택횟수": [120, 95, 150, 80, 111],
    "승률 (%)": [52, 48, 56, 60, 49],
    "인지도 (%)": [25, 20, 30, 15, 22]
})

# 데이터 표 출력
st.dataframe(data)

# 선택횟수 막대 그래프
st.subheader("캐릭터별 선택횟수")

# 인덱스를 캐릭터로 설정
choice_data = data.set_index("캐릭터")[["선택횟수"]]

st.bar_chart(choice_data)


# 승률 선 그래프
st.subheader("캐릭터별 승률 (%)")

# 인덱스를 캐릭터로 설정
win_rate_data = data.set_index("캐릭터")[["승률 (%)"]]

st.line_chart(win_rate_data)