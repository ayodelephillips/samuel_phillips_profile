import streamlit as st
from utility import skills
from utility import ProfileConfig
from pathlib import Path

# Custom CSS for styling
st.markdown("""
    <style>
        /* General background styling */
        .main { 
            background-color: #f9f9f9;  /* Soft light gray */
            font-family: 'Arial', sans-serif;
        }
        
        /* Header Title styling */
        .header-title {
            color: #008080;  /* Soft teal */
            font-weight: bold;
            text-align: center;
            font-size: 36px;
            margin-bottom: 10px;
        }
        
        /* Subheader styling */
        .subheader {
            color: #2c3e50;  /* Calming blue */
            font-size: 24px;
            margin-bottom: 10px;
        }

        /* Centering images */
        .image-center {
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
""", unsafe_allow_html=True)

# Page title and introduction
st.markdown("<h1 class='header-title'>Welcome to My Portfolio</h1>", unsafe_allow_html=True)
st.write("Hi there! I’m an **Assistant Management Accountant** with a passion for providing impactful financial insights, improving processes, and driving business growth.")


st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image(ProfileConfig().temi_profile_image, caption="Ibukunoluwa Temiloluwa Phillips", width=400)
st.markdown("</div>", unsafe_allow_html=True)

st.write("""
I am ACA-certified and completing my ACCA finals. My expertise lies in management accounting, 
financial reporting, budgeting, and advanced modeling. I excel in collaborating with stakeholders 
to deliver strategic solutions and streamline operations.
""")

st.write("""
With a track record of providing insightful financial analysis and operational efficiency, I specialize in:  
- Management Accounting  
- Financial Reporting and Analysis  
- Budgeting and Forecasting  
- Process Improvements and Automation  
""")

# Key Skills Section
st.markdown("<h2 class='subheader'>Key Skills</h2>", unsafe_allow_html=True)
for skill in skills:
    st.markdown(f"- {skill}")

# Certifications Section
st.markdown("<h2 class='subheader'>Certifications</h2>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image(ProfileConfig().aca_certification, caption="ACA Certification", width=400)
st.markdown("</div>", unsafe_allow_html=True)



# Find Me Online
st.markdown("<h2 class='subheader'>Find Me Online</h2>", unsafe_allow_html=True)
st.markdown(f"""
    - 🌐 [LinkedIn Profile]({ProfileConfig().linkedin_profile})  
    - 📧 Email: [temiloluwadeyanju@gmail.com](mailto:temiloluwadeyanju@gmail.com)
""")

# Resume download section
st.markdown("<h2 class='subheader'>Download My Resume</h2>", unsafe_allow_html=True)
try:
    with open(ProfileConfig().resume_location, "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name=ProfileConfig().resume_file_name,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            help="Download a copy of my resume to learn more about my experience and skills."
        )
except FileNotFoundError:
    st.error("Resume file not found. Please check the configuration.")

# Footer Section
st.markdown("---")
st.markdown("Thank you for visiting my portfolio! Feel free to reach out for collaborations or opportunities. 😊")
