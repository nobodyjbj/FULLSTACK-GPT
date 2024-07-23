import streamlit as st

st.title("title")

with st.sidebar:
    st.title("sidebar title")
    st.text_input("input")

tab_one, tab_two, tab_three = st.tabs(["A", "B", "C"])

with tab_one:
    st.write("A")

with tab_two:
    st.write("B")

with tab_three:
    st.write("C")
