import streamlit as st
from utility import ProfileConfig
from pathlib import Path

# Set page title
st.title("About Me")

# Add a section for the user's photo
st.image(f"{Path(__file__).resolve().parent}/assets/img/linkedin_pic.jpg", width=350, )  # Replace with your photo URL or local path


# Career Summary
st.header("Career Summary")
st.write("""
Welcome to my page. My name is Samuel Phillips, a Senior Data Engineer with close on 4 years experince in Data Engineering.
I specialize in Big Data, Machine Learning, and efficient ETL pipelines, working with cutting-edge tools like BigQuery, DBT, Dataform, among others.
Some of the projects I have done are shown in the project section of my profile.
Feel free to take a look
""")

# Key Skills (from the resume)
st.markdown("### Key Skills")
st.write("""
- **Programming**: Python, JavaScript, Django, Flask.
- **Data Engineering**: Airflow, Snowflake, BigQuery, DBT, Azure Data Warehouse.
- **Data Science**: TensorFlow, Scikit-learn, NumPy, Pandas.
- **Cloud**: Google Cloud Platform (GCP), Azure.
- **Tools**: Docker, Git, Dataform.
""")

# Add LinkedIn and GitHub links
st.markdown("### Find Me Online")
st.markdown(f"""
- [GitHub Profile]({ProfileConfig().github_profile})  
- [LinkedIn Profile]({ProfileConfig().linkedin_profile})
""")

# Career Evolution showing the migration from software engineering to data engineering and now AI/Machine Learning.
st.markdown("### Career Evolution")
st.markdown(
    """
        - Year 1-2: Software Engineering
        - Year 2-4: Data Engineering
        - Year 5: Data & Machine Learning Engineering
""")

# Resume download section
st.markdown("### Download My Resume")
with open(ProfileConfig().resume_location, "rb") as file:
    st.download_button(
        label="Download Resume",
        data=file,
        file_name=ProfileConfig().resume_file_name,
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
