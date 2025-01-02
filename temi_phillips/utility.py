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


project_done = {
    'Project 1: Profit and Loss for Limited Liability Companies using Xero and Excel': """
    Challenges faced while preparing profit and loss accounts for limited liability companies.
    **Challenge 1: Misclassification of Accruals**
    - **Problem**: While preparing the profit and loss account in Xero, some expenses were recorded on a cash basis instead of an accrual basis, leading to underreporting of liabilities within the reporting period.
    - **Solution**: I identified the misclassified entries using Xero’s transaction reporting feature and flagged them for adjustment. I exported the expense data into Excel and created a reconciliation table to distinguish between accrued expenses and paid amounts. After verifying the adjustments, I updated the records in Xero, ensuring the profit and loss account reflected all outstanding obligations.

    **Challenge 2: Missing Accrued Income Entries**
    - **Problem**: Revenue earned but not yet invoiced was omitted, causing an understatement of income in the profit and loss account.
    - **Solution**: I reviewed the contracts and revenue schedules in Excel to identify unrecorded accrued income. Using this data, I created manual journal entries in Xero to record the accrued income. This adjustment ensured that the financials accurately matched the period's earned revenue.

    **Challenge 3: Incorrect Treatment of Prepayments**
    - **Problem**: Certain prepayments, such as insurance and rent, were fully expensed in the current month instead of being allocated over the appropriate periods, leading to inconsistencies in expense reporting.
    - **Solution**: I utilized Xero’s prepayment feature to allocate the expense across the applicable periods. To ensure accuracy, I created a schedule in Excel detailing the prepayment amounts and their allocation over the months. I then cross-referenced this schedule with Xero’s reports to confirm the adjustments aligned with the accounting standards.

    **Challenge 4: Overlooked Manual Adjustments**
    - **Problem**: Manual journal adjustments for prior months were overlooked, causing discrepancies between the profit and loss account and the balance sheet.
    - **Solution**: I used Xero’s audit trail to review historical journal entries and exported them into Excel for detailed analysis. After identifying the missed adjustments, I reconciled them in Xero and verified the profit and loss account was consistent with the balance sheet and supporting schedules.

    **Challenge 5: Inconsistent Data from Stakeholders**
    - **Problem**: Delayed or incomplete submission of data, such as invoices or expense claims, disrupted the preparation of the profit and loss account.
    - **Solution**: I developed a structured Excel template for stakeholders to submit their data, which streamlined the process and reduced errors. I periodically imported the submitted data into Xero to ensure the profit and loss account was updated promptly. Additionally, I scheduled periodic reminders to stakeholders to encourage timely submissions.
    """,
    'Project 2: Balance Sheet Reconciliation': """
    **Scenario 1: Discrepancy in Bank Reconciliation**
    - **Problem**: While reconciling bank accounts using Xero, I noticed discrepancies between the recorded transactions and the bank statement, such as duplicate entries and unrecorded direct debits.
    - **Solution**: I utilized Xero’s bank reconciliation tools to identify and flag the discrepancies. After isolating the errors, I cross-referenced the transactions with supporting documents and corrected the entries. I then used Excel to perform iterative checks, ensuring all adjustments matched the statement balances.

    **Scenario 2: Missing Documentation for Transactions**
    - **Problem**: During the reconciliation of the accounts payable section, some supplier invoices were missing, leading to incomplete records in Xero.
    - **Solution**: I reached out to stakeholders to retrieve the missing invoices and temporarily tagged the transactions as "unreconciled" in Xero. I created a tracking sheet in Excel to log the outstanding items, which allowed me to follow up systematically. Once the documentation was provided, I updated Xero to reflect the accurate balances.

    **Scenario 3: Incorrect Categorization of Entries**
    - **Problem**: Some transactions were miscategorized, leading to inaccuracies in balance sheet accounts like fixed assets being included in operating expenses.
    - **Solution**: I used Xero’s transaction categorization feature to identify misclassified entries. After reassigning the correct accounts, I performed a pivot table analysis in Excel to validate that all adjustments aligned with the reporting structure. This ensured the financial statements were accurate and compliant with accounting standards.

    **Scenario 4: Unreconciled Opening Balances**
    - **Problem**: Historical data in the balance sheet contained unreconciled opening balances, causing discrepancies in the trial balance.
    - **Solution**: I traced the issue back using Xero’s audit trail functionality to identify unadjusted entries. I exported the relevant data to Excel and applied a reconciliation formula to calculate the adjustments required. I then updated the balance sheet in Xero, ensuring the issue did not impact future reporting cycles.

    **Scenario 5: Delayed Stakeholder Input**
    - **Problem**: Timely reconciliation was hindered due to delays in receiving expense reports and petty cash documentation.
    - **Solution**: I implemented a streamlined workflow in Excel, where stakeholders could input their expense details into a shared template. I periodically imported this data into Xero, reducing manual input and ensuring timely updates. Additionally, I provided training sessions on how to submit documents promptly to avoid future delays.
    """,
    'Project 3: Preparing Forecasts for Company ABC': """
    **Challenge 1: Inconsistent Historical Data**
    - **Problem**: While using Xero to extract historical data for forecasting, discrepancies in revenue and expense categorization caused inconsistencies, making it difficult to identify accurate trends.
    - **Solution**: I reviewed Xero’s transaction history to identify and correct misclassified entries. I exported the historical profit and loss data into Excel, where I applied data cleansing techniques, such as sorting and filtering, to ensure consistency. Once the data was standardized, I imported the adjusted figures back into Xero to use them as a reliable baseline for forecasting.

    **Challenge 2: Uncertain Market Conditions**
    - **Problem**: Market volatility introduced uncertainty in projecting revenue and expenses, leading to overly optimistic or conservative forecasts.
    - **Solution**: I prepared multiple forecast scenarios in Excel, including best-case, worst-case, and most-likely outcomes, based on historical data extracted from Xero. Using Xero’s budgeting tool, I set up these scenarios and incorporated variables such as seasonal trends and expected market conditions. This approach allowed me to present flexible, data-driven forecasts to stakeholders.

    **Challenge 3: Lack of Detailed Cash Flow Integration**
    - **Problem**: While preparing the profit and loss forecast in Xero, cash flow implications of accrued income and prepayments were overlooked, leading to gaps in the forecast.
    - **Solution**: I created a detailed cash flow schedule in Excel, incorporating elements like payment timelines for accrued income and prepayment amortization. This schedule was linked to the profit and loss forecast from Xero, ensuring both reports were aligned. I regularly updated the schedule in Xero to reflect the real-time financial position.

    **Challenge 4: Unreliable Input from Stakeholders**
    - **Problem**: Delayed or incomplete data submissions from department heads hindered the accuracy of expense projections.
    - **Solution**: I developed a standardized Excel template for stakeholders to submit their budget estimates and justifications. After consolidating the inputs, I used Xero’s forecasting tools to integrate these estimates into the broader financial forecast. I also implemented a review process to validate the data before finalizing the forecast.

    **Challenge 5: Difficulty Identifying Expense Drivers**
    - **Problem**: Some overhead costs lacked clear drivers, making it challenging to forecast accurately.
    - **Solution**: I conducted a cost analysis in Excel, using historical data from Xero to identify trends and patterns. For indirect costs, I allocated expenses based on logical drivers (e.g., headcount, revenue percentages) and incorporated these allocations into Xero’s budgeting module. This ensured that the forecast was both comprehensive and reasonable.
    """
}


if __name__ =="__main__":
    display_pdf(ProfileConfig().aca_certification)
