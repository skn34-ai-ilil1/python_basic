import streamlit as st
import requests
from streamlit_lottie import st_lottie
from datetime import datetime

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="김건우 자기소개서",
    page_icon="🚀",
    layout="wide"
)
# ===============================
# LOTTIE
# ===============================

def load_lottie(url):

    res = requests.get(url)

    if res.status_code == 200:
        return res.json()

    return None

animation = load_lottie(
"https://assets10.lottiefiles.com/packages/lf20_w51pcehl.json"
)

# ===============================
# CSS
# ===============================

st.markdown(
"""
<style>


.stApp {

background:

linear-gradient(
135deg,
#020617,
#111827
);

color:white;

}



h1 {

font-size:70px !important;

background:

linear-gradient(
90deg,
#38bdf8,
#a855f7
);

-webkit-background-clip:text;

color:transparent;

}



.card {


background:

rgba(255,255,255,0.08);


border-radius:30px;


padding:30px;


border:

1px solid rgba(255,255,255,.15);


backdrop-filter:

blur(20px);


box-shadow:

0 20px 50px rgba(0,0,0,.4);


}



.badge {


display:inline-block;


padding:

8px 18px;


border-radius:

30px;


background:

linear-gradient(
90deg,
#06b6d4,
#6366f1
);


margin:5px;


font-weight:bold;


}


[data-testid="stSidebar"] h1 {
    font-size:25px !important;
}

</style>

""",
unsafe_allow_html=True
)

# ===============================
# SIDEBAR
# ===============================

with st.sidebar:


    st.title("🚀 Portfolio")


    page = st.radio(

        "MENU",

        [
            "Home",
            "Profile",
            "Skills",
            "Projects",
            "Contact"
        ]

    )


# ===============================
# HOME
# ===============================


if page=="Home":


    col1,col2 = st.columns(
        [1.2,1]
    )


    with col1:


        st.title(
            "김건우 🚀"
        )


        st.subheader(
            "AI & Data Developer"
        )


        st.write(
"""
기술을 배우고,
문제를 해결하고,
서비스를 만드는 개발자입니다.

꾸준한 성장과 실행을 중요하게 생각합니다.
"""
)



        st.markdown(

"""
<span class="badge">
Python
</span>

<span class="badge">
AI
</span>

<span class="badge">
Data
</span>

<span class="badge">
Streamlit
</span>

""",

unsafe_allow_html=True

)


    with col2:


        if animation:

            st_lottie(
                animation,
                height=350
            )


# ===============================
# PROFILE
# ===============================


elif page=="Profile":


    st.header(
        "👨‍💻 Profile"
    )


    c1,c2,c3 = st.columns(3)


    data=[

    ("🎂","1993"),

    ("📚","독서"),

    ("🏋️","운동")

    ]


    for col,item in zip(
        [c1,c2,c3],
        data
    ):


        with col:


            st.markdown(

f"""

<div class="card">


<h1>
{item[0]}
</h1>


<h2>
{item[1]}
</h2>


</div>

""",

unsafe_allow_html=True

)


# ===============================
# SKILLS
# ===============================


elif page=="Skills":


    st.header(
        "🛠 Skills"
    )


    skills={

    "Python":90,

    "Streamlit":85,

    "Data Analysis":25,

    "AI":20

    }


    for name,value in skills.items():


        st.write(
            name
        )


        st.progress(
            value/100
        )

# ===============================
# PROJECT
# ===============================


elif page=="Projects":

    st.header(
        "🚀 Projects"
    )

    c1,c2,c3 = st.columns(3)

    projects=[("🌐 Portfolio","Streamlit 제작")]

    for col,p in zip(
        [c1,c2,c3],
        projects
    ):

        with col:
            st.markdown(

f"""

<div class="card">


<h2>
{p[0]}
</h2>


<p>
{p[1]}
</p>


</div>

""",

unsafe_allow_html=True
)


# ===============================
# CONTACT
# ===============================


elif page=="Contact":

    st.header("📬 Contact")
    st.markdown(

"""
<div class="card">

<p>

📧 Email : free.rjs103@gmail.com

<br>

🐙 GitHub : https://github.com/ilil1

<br>

📝 Blog : https://velog.io/@ilil1

</p>

</div>

""",

unsafe_allow_html=True
)




st.divider()


st.caption(

f"""
© {datetime.now().year}
Kim Geonwoo Portfolio
"""

)