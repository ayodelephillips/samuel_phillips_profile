import streamlit as st

home_page = st.Page("home.py", title='Home', icon=":material/home:")
projects_page = st.Page("projects.py", title="Accounting Projects Showcase", icon="📊")
acca_road_map = st.Page("acca_road_map.py", title='ACCA Roadmap', icon=":material/build:")

pg = st.navigation([home_page, acca_road_map, projects_page])

st.set_page_config(page_title="Meet Temiloluwa Phillips", page_icon=":material/edit:")

pg.run()