import streamlit as st
import urllib.parse

st.markdown("# Contact Me")

# Via Email
email = "sonata24@proton.me"
mailto_link = f"mailto:{email}"

st.link_button(label=f"{email}", url=mailto_link, help="Send an email")

st.link_button(label="LinkedIn",
               url="https://www.linkedin.com/in/sonata22/",
               help="Open profile")


st.markdown("# Tech Profiles")

st.link_button(label="GitHub",
               url="https://github.com/sonata22")



# Maybe also list public profiles here so that they could be checked out