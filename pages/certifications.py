import streamlit as st
import pandas as pd

st.markdown("# Certifications")

certificates = pd.DataFrame({
  'Name': [
      "Elegant Automation Frameworks with Python and Pytest",
      "Advanced Course in Programming (Python)",
      "Introduction to Programming (Python)",
      "Python (Basic)",
      "Pentesting Bootcamp",
      "Level 1 Python Certification",
  ],
  'Issuer': [
      "Udemy",
      "University of Helsinki",
      "University of Helsinki",
      "HackerRank",
      "Robot_dreams",
      "Robocorp",
  ],
  # 'Stack': [
  #     "python, pytest",
  #     "python",
  #     "python",
  #     "python",
  #     "",
  #     "python",
  # ],
  'Date': [
      "Jul, 2025",
      "Sep, 2025",
      "Feb, 2025",
      "Jan, 2025",
      "Sep, 2024",
      "Feb, 2024",
  ],
  'Credential': [
      "https://www.udemy.com/certificate/UC-61c2c09f-4a84-4766-836f-475cf2fa78d9/",
      "https://certificates.mooc.fi/validate/5qz396rm7z8",
      "https://certificates.mooc.fi/validate/c6eeortgxre",
      "https://www.hackerrank.com/certificates/iframe/92db333f790c",
      "https://lms.robotdreams.cc/certificate/cba8bcb6c75df79f59c2821001032e63",
      "https://downloads.robocorp.com/certificates/level1python/fec3bf67-a68b-4735-96cb-7c1ae0e8f750.pdf",
  ],
})

st.data_editor(
    certificates,
    column_config={
        "Credential": st.column_config.LinkColumn(
            display_text="Link"
        ),
    },
    hide_index=True,
)

