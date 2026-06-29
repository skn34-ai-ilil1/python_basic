import streamlit as st

# 페이지 제목
st.title("Counter")

# session_state에 customer_count가 없으면 0으로 초기화
if "customer_count" not in st.session_state:
    st.session_state.customer_count = 0

# 손님 추가 버튼
if st.button("손님 한 명 추가요~!"):
    st.session_state.customer_count += 1

# 초기화 버튼
if st.button("오늘 장사 끝! 손님 수 초기화할게요~"):
    st.session_state.customer_count = 0

# 현재 손님 수 출력
st.write(f"지금까지 온 손님 수: {st.session_state.customer_count}")