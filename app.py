import streamlit as st

st.title("学术文献搜索 Demo")
keyword = st.text_input("请输入关键词：")
if st.button("开始搜索"):
    st.write(f"你输入了：{keyword}")

import requests

response = requests.get("https://api.github.com")
data = response.json()
print(data["current_user_url"])