import streamlit as st
import google.generativeai as genai
from PIL import Image
genai.configure(api_key="AIzaSyDIsIw5HuHSpT39xmCh2QERN8Pey-JLWh0")
model=genai.GenerativeModel('gemini-2.5-flash')
st.header("Image Analytics")
uploaded_file=st.file_uploader("upload an image",type=['png','jpg','jpeg'])

if uploaded_file is not None:
    st.image(Image.open(uploaded_file))
prompt=st.text_input("How may i help you")

if st.button("GET RESPONCE"):
    img=Image.open(uploaded_file)
    model=genai.GenerativeModel('gemini-2.5-flash')
    response=model.generate_content([prompt,img])
    st.markdown(response.text)
