from dataclasses import dataclass

@dataclass
class ProfileConfig:
    sam_profile_image:str = "assets/img/linkedin_pic.jpg"
    github_profile:str = 'https://github.com/ayodelephillips'
    linkedin_profile:str ='https://www.linkedin.com/in/samuel-phillips-dev'
    resume_location:str ='assets/file/samuel_phillips_resume.docx'
    resume_file_name:str = "samuel_phillips_resume.docx"