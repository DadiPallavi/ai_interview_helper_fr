import streamlit as st
import requests as rq
st.title("AI Interview preparation helper bot")
serv_loc= st.secrets["SERV_LOC"]
with st.form("Details"):
    Topic=st.text_input("enter lang-topic:--")
    level=st.selectbox("choose level",["Easy","Medium","Advanced"])
    ways=st.multiselect("choose any of below",["MCQS","Theory Questions","Coding Questions"])
    st.write(ways)
    if st.form_submit_button():
        prompt=f"""
        i need to prepare for inetrview and i want 
        you to give me the best content 
        and 
        i want {Topic} related these list of ways {ways}
        at {level} level 
        """
        response=rq.post(f"{serv_loc}/generate",json={"prompt":prompt})
        st.write(response.json()["answer"])
        

