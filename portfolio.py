import streamlit as st
import pandas as pd
import numpy as np

def overview():
    st.title("Overview")

pg = st.navigation([
    st.Page(overview, title="Overview"),
    st.Page("./pages/about-me.py", title="About Me"),
    st.Page("./pages/certifications.py", title="Certifications"),
    st.Page("./pages/contact-me.py", title="Contact Me"),
    st.Page("./pages/contributions.py", title="Contributions"),
    st.Page("./pages/projects.py", title="Projects"),
    st.Page("./pages/resume.py", title="Resume"),
    st.Page("./pages/tech-stack.py", title="Tech Stack"),
    st.Page("./pages/testimonials.py", title="Testimonials"),
])
pg.run()
