import streamlit as st

col1,col2,col3 = st.columns([1,2,1])
col1.title("Welcome to my Web App!")
col2.image("image.jpg", width = 480)
col3.metric(label = "Temperature", value = "24^C", delta = "-1.4%")
st.file_uploader("Upload a Photo")
st.camera_input("Smile please :)")
