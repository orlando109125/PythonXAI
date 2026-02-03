import streamlit as st

st.title("數字金字塔")
height = st.number_input("請輸入一個整數", min_value=1, max_value=9, value=5, step=1)

st.write("數字金字塔")
for i in range(1, height + 1):
    st.write(str(i) * i)


st.title("箭頭金字塔")
arrow_height = st.number_input(
    "請輸入箭頭的層數", min_value=1, max_value=9, value=5, step=1
)
st.write("箭頭金字塔")
output = ""
for i in range(1, arrow_height + 1):
    output = output + " " * (arrow_height - i) + "*" * (2 * i - 1) + "\n"
for i in range(arrow_height - 1, 0, -1):
    output = output + " " * (arrow_height - 1) + "*" + "\n"

st.write(f"```\n\n{output}```")
