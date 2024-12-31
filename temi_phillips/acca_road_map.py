import streamlit as st
import streamlit.components.v1 as components


# CSS for styling
st.markdown(
    """
    <style>
    .path-container {
        display: flex;
        justify-content: center;
        margin: 50px 0;
    }
    .path {
        display: flex;
        align-items: center;
    }
    .stage {
        text-align: center;
        font-size: 16px;
        margin: 0 30px;
    }
    .stage.green {
        color: white;
        background-color: green;
        padding: 20px;
        border-radius: 50%;
        width: 150px;
        height: 150px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .stage.red {
        color: white;
        background-color: orange;
        padding: 20px;
        border-radius: 50%;
        width: 150px;
        height: 150px;
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
        animation: blink 1s infinite;
    }
    @keyframes blink {
        50% {
            opacity: 0.5;
        }
    }
    .line {
        height: 5px;
        background-color: grey;
        flex-grow: 1;
        margin: 0 10px;
    }
    .subjects {
        margin-top: 10px;
        font-size: 14px;
        color: #555;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main header
st.title("📈 My ACCA Roadmap")



# Roadmap visualization
st.markdown(
    """
    <div class="path-container">
        <div class="path">
            <div class="stage green">Applied Knowledge</div>
            <div class="line"></div>
            <div class="stage green">Applied Skills</div>
            <div class="line"></div>
            <div class="stage red">Strategic Professional</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("""
This roadmap tracks my journey through the ACCA Pathways:
- **Applied Knowledge** ✅
  - Subjects: 
      - Business and Technology (BT) ✅
      - Management Accounting (MA) ✅
      - Financial Accounting (FA) ✅
_____________________________________
         
- **Applied Skills** ✅
  - Subjects: 
      - Corporate and Business Law (LW) ✅
      - Performance Management (PM) ✅ 
      - Taxation (TX) ✅
      - Financial Reporting (FR) ✅
      - Audit and Assurance (AA) ✅
      - Financial Management (FM) ✅
_______________________________________
         
- **Strategic Professional** 🟡
  - Subjects: 
      - Strategic Business Reporting 🟡
      - Advanced Audit and Assurance 🟡 
      - Strategic Business Leader 🟡
      - Advanced Taxation 🟡
         """)



# Footer message
st.write("Stay tuned as I conquer the Strategic Professional pathway and achieve ACCA certification!")
