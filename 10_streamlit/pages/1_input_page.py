import streamlit as st

# 페이지 제목
st.title("사용자 입력 받는 페이지")

# 2개의 컬럼 생성
col1, col2 = st.columns(2)

# 왼쪽 컬럼
with col1:
    nickname = st.text_input("닉네임 입력")

    age = st.number_input(
        "나이 입력",
        min_value=13,
        max_value=100
    )

    country = st.selectbox(
        "국적 선택",
        ['한국', '중국', '일본', '미국', '외계']
    )

    hobby = st.radio(
        "취미 선택",
        ['맛집 탐방', '영화 감상', '음악 감상', '뜨개질']
    )

    agree = st.checkbox("개인정보 제공 동의")


# 오른쪽 컬럼
with col2:
    if st.button("입력 완료"):
        st.write(f"이름이 뭐야? {nickname}")
        st.write(f"몇 살이야? {age}")
        st.write(f"어디서 왔어? {country}")
        st.write(f"취미가 뭐야? {hobby}")
        st.write(f"개인정보 제공에 동의해? {agree}")