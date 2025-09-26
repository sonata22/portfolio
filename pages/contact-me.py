import streamlit as st

st.markdown("# Contact Me")

email = "sonata24@proton.me"
mailto_link = f"mailto:{email}"

st.link_button(label=f"{email}", url=mailto_link, help="Send an email")
st.link_button(label="LinkedIn",
               url="https://www.linkedin.com/in/sonata22/",
               help="Open profile")


st.markdown("# Tech Profiles")

st.link_button(label="GitHub",
               url="https://github.com/sonata22")
st.link_button(label="LeetCode",
               url="https://leetcode.com/u/sonata22/")
st.link_button(label="CodeWars",
               url="https://www.codewars.com/users/sonata22")
st.link_button(label="HackerRank",
               url="https://www.hackerrank.com/profile/nataliia_sosnov1")
st.link_button(label="CssBattle",
               url="https://cssbattle.dev/player/sonata22")
st.link_button(label="CodePen",
               url="https://codepen.io/sonata22")
st.link_button(label="HackTheBox",
               url="https://app.hackthebox.com/profile/2049263")
st.link_button(label="TryHackMe",
               url="https://tryhackme.com/r/p/sonata22")
