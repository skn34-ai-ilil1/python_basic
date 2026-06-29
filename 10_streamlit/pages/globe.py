from streamlit_globe import streamlit_globe
import streamlit as st

from streamlit_extras.chartjs_chart import *

"""Basic bar chart example."""
st.write("### Bar Chart")
spec = {
    "type": "bar",
    "data": {
        "labels": ["January", "February", "March", "April", "May"],
        "datasets": [{"label": "Sales", "data": [65, 59, 80, 81, 56]}],
    },
}
chartjs_chart(spec)