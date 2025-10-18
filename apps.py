import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

with st.container():
    st.subheader("Hi, Rares.")
    st.title("meow :tada:")
    st.write("idk :wave:")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Despre Rares")
        st.write("1. i plac barbatii dar nu vrea sa ne spuna ca e un femboy shy.")
        st.write("2. se muta cu dragan cand are un coleg de la care invata multe")
        st.write("3. nj, e chill")

    with right_column:
        st.header("Ce face el in ore?")
        st.write("1. beleste pula.")
        st.write("2. il atinge pe auras")
        st.write("3. habar n-am")

with st.container():
    st.write("---")
    st.header("Contactati-l pe rares")
    st.write("Instagram: @11rraresss")
    st.write("Whatsapp: +40 772 115 104")
    st.write("Sunati-l la orice ora ca rspunde futu-l in gura")