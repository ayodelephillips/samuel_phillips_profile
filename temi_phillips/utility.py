from dataclasses import dataclass
from pathlib import Path

@dataclass
class ProfileConfig:
    sam_profile_image:str = f"{Path(__file__).resolve().parent}/assets/img/linkedin_pic.jpg"
    github_profile:str = 'https://github.com/ayodelephillips'
    linkedin_profile:str ='https://www.linkedin.com/in/samuel-phillips-dev'
    resume_location:str = f"{Path(__file__).resolve().parent}/assets/file/samuel_phillips_resume.docx"
    resume_file_name:str = "samuel_phillips_resume.docx"