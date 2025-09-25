import streamlit as st
import pandas as pd
import numpy as np

# Define pages
resume = st.Page("./pages/resume.py", title="Resume")
projects = st.Page("./pages/projects.py", title="Projects")
tech_stack = st.Page("./pages/tech-stack.py", title="Tech Stack")
certifications = st.Page("./pages/certifications.py", title="Certifications")
contributions = st.Page("./pages/contributions.py", title="Contributions")
contact_me = st.Page("./pages/contact-me.py", title="Contact Me")

# Set up navigation
pg = st.navigation([resume,
                    projects,
                    tech_stack,
                    certifications,
                    contributions,
                    contact_me])

# Run the selected page
pg.run()