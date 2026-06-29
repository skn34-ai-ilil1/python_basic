import streamlit as st

# 제목, 헤더, 서브헤더 출력
st.title("오늘은 화요일")
st.header("오늘은 Streamlit 배우는 날")
st.subheader("Streamlit으로 나만의 데모 페이지 만들기~~~!")

# 사용자 입력 받기
site_name = st.text_input("오늘 내가 만들어보고 싶은 사이트는?!")

# 입력한 내용 출력
st.write(site_name)

# 입력값을 활용한 버튼 만들기
if site_name:
    if st.button(f"{site_name} 접속하기"):
        st.success(f"{site_name} 접속 중!!!!!")