import time
import numpy as np
import pandas as pd
import streamlit as st



st.header(":rainbow[Welcome to Streamlit!]", divider="grey")

def stream_data():
    for word in "Let's try to do some cool stuff here, you have plenty of options".split(" "):
        yield word + " "
        time.sleep(0.05)

st.write_stream(stream_data)

time.sleep(0.2)



col1, col2, col3 = st.columns(3)

col2.link_button("Streamlit Docs", "https://docs.streamlit.io/develop/api-reference", type="primary")
time.sleep(0.2)
if col1.button("Click me"):

    st.balloons()
st.write("")
if col3.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')



time.sleep(0.1)
txt = st.text_area(
    "Some text",
    "Be creative, explore, ask, and play around and you can get awesomeone interfere with 0 effort"
    "because someone else did the work for you"
)

time.sleep(0.1)

df = pd.DataFrame(
    {
        "col1": np.random.randn(1000) / 50 + 37.76,
        "col2": np.random.randn(1000) / 50 + -122.4,
        "col3": np.random.randn(1000) * 100,
        "col4": np.random.rand(1000, 4).tolist(),
    }
)
st.map(df, latitude="col1", longitude="col2", size="col3", color="col4")
