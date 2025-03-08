import streamlit as st

sentiment_mapping = ["This was not good at all ❌", "This is all?🤨", "Meh 😐", "Looks good 👍", "This is awesome!🚀"]
selected = st.feedback(options="faces")
if selected is not None:
    print(selected)
    if selected == 0:
        st.markdown(
            f":red[You selected **{sentiment_mapping[selected]}**. Thank you for your answer]"
        )
    if selected == 1:
        st.markdown(
            f":orange[You selected **{sentiment_mapping[selected]}**. Thank you for your answer]"
        )
    if selected == 2:
        st.markdown(
            f":green[You selected **{sentiment_mapping[selected]}**. Thank you for your answer]"
        )
    if selected == 3:
        st.markdown(
            f":blue[You selected **{sentiment_mapping[selected]}**. Thank you for your answer]"
        )
    if selected == 4:
        st.markdown(
            f":rainbow[You selected **{sentiment_mapping[selected]}**. Thank you for your answer]"
        )
