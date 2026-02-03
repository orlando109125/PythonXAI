import streamlit as st

st.title("數字輸入練習")
number = st.number_input("請輸入一個數字", min_value=0, max_value=100, value=50, step=1)
st.write(f"你輸入的數字是: {number}")

st.title("成績等第判斷")

score = st.number_input("請輸入成績", min_value=0, max_value=100, value=85, step=1)

if score >= 90:
    st.write("等第: A")
elif score >= 80:
    st.write("等第: B")
elif score >= 70:
    st.write("等第: C")
elif score >= 60:
    st.write("等第: D")
else:
    st.write("等第: F")

st.write(f"你的成績等第是: {grade}")

if st.button(點擊我):
    st.write("按鈕被點擊了！")
if st.balloons():
    
    st.buttons(下雪按鈕)
    if st.button("點我", key="snow"):
        st.snow()




