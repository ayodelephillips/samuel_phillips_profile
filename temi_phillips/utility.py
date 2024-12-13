from dataclasses import dataclass
from pathlib import Path
import base64
import streamlit as st

@dataclass
class ProfileConfig:
    temi_profile_image:str = f"{Path(__file__).resolve().parent}/assets/img/linkedin_pic.jpg"
    aca_certification:str = f"{Path(__file__).resolve().parent}/assets/img/ACA_Cert.jpg"
    linkedin_profile:str ='https://www.linkedin.com/in/temiloluwa-phillips'
    resume_location:str = f"{Path(__file__).resolve().parent}/assets/file/Temiloluwa Phillips Resume v1.pdf"
    resume_file_name:str = "Temiloluwa Phillips Resume v1.pdf"



# Embed the PDF in an iframe
def display_pdf(file_path = ProfileConfig().aca_certification):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

    return pdf_display

skills = [
    "Statutory and Management Accounting",
    "Financial Reporting and Analysis",
    "Balance Sheet Reconciliation",
    "Tax Compliance (VAT)",
    "Financial Forecasting and Budgeting",
    "Bank and Cash Reconciliation",
    "Process Improvements and Automation",
    "Advanced Excel and Financial Modeling",
    "Client Relationship Management",
    "Accounting Software (Xero, Sage 50, QuickBooks, OK Finance)"
]




if __name__ =="__main__":
    display_pdf(ProfileConfig().aca_certification)
