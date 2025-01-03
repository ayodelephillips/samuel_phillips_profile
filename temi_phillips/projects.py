import streamlit as st
from utility import project_done


# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        h1 {
            color: #2c3e50;
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 20px;
        }
        h2 {
            color: #2980b9;
            font-size: 1.8em;
            margin-top: 30px;
            margin-bottom: 15px;
        }
        p, li {
            font-size: 1.1em;
            color: #2c3e50;
            line-height: 1.6;
        }
        .project-container {
            background-color: #ffffff;
            border: 1px solid #eaeaea;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .divider {
            border: none;
            height: 2px;
            background-color: #2980b9;
            margin: 20px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Introduction
st.title("📊 Accounting Projects Showcase")
st.write("""
Welcome to my portfolio of accounting projects. Below, you'll find detailed case studies that highlight my expertise in financial management, 
data analysis, and software tools like Xero and Excel. These projects reflect my problem-solving abilities and my attention to detail in delivering accurate and actionable financial insights.
""")

# Define the project data

# Display each project in styled containers
for project, detail in project_done.items():
    with st.container():
        st.markdown(f"""
                    <div class='project-container'>
                    <h2>{project}</h2>
                    <p>{detail}</p>
                    </div>
                    """, 
                    unsafe_allow_html=True)
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# Add a footer
# st.markdown("""
#     <footer style="text-align: center; margin-top: 50px; font-size: 0.9em; color: #7f8c8d;">
#         Created by [Your Name] | Contact: [Your Email] | LinkedIn: [Your LinkedIn Profile]
#     </footer>
# """, unsafe_allow_html=True)
