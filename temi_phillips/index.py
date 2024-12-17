import streamlit as st

home_page = st.Page("home.py", title='Home', icon=":material/home:")
projects_page = st.Page("projects.py", title='Accounting Projects done', icon=":material/lightbulb:")
skills_and_tools = st.Page("skills_and_tools.py", title='Tools and relevant skills', icon=":material/build:")

pg = st.navigation([home_page, skills_and_tools, projects_page])

st.set_page_config(page_title="Meet Temiloluwa Phillips", page_icon=":material/edit:")

pg.run()