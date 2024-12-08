import streamlit as st

home_page = st.Page("home.py", title='Home', icon=":material/home:")
projects_page = st.Page("projects.py", title='Projects done', icon=":material/lightbulb:")
skills_and_tools = st.Page("skills_and_tools.py", title='Skills and Tools', icon=":material/build:")
technical_writings = st.Page("technical_writings.py", title='Blogs and technical writings', icon=":material/article:")

pg = st.navigation([home_page, skills_and_tools, projects_page, technical_writings])

st.set_page_config(page_title="Meet Samuel Phillips", page_icon=":material/edit:")

pg.run()