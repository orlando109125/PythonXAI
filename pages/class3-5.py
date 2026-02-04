import streamlit as st
import random
import time

ss = st.session_state


if "target" not in ss:
    ss.target = random.randint(0, 100)
if "min_val" not in ss:
    ss.min_val = 0
if "max_val" not in ss:
    ss.max_val = 100

st.title("猜數字遊戲")

num = st.number_input(
    f"請輸入一個數字在 {ss.min_val} 和 {ss.max_val} 之間的整數:",
    min_value=ss.min_val,
    max_value=ss.max_val,
    step=1,
)

if st.button("猜"):
    if num < ss.min_val or num > ss.max_val:
        st.warning("輸入無效，請再試一次。")
    elif num < ss.target:
        st.success("太小了，請再試一次。")
        ss.min_val = num + 1
    elif num > ss.target:
        st.success("太大了，請再試一次。")
        ss.max_val = num - 1
    else:
        st.success("恭喜你！猜對了！")
        st.balloons()
        # Reset the game
        ss.target = random.randint(0, 100)
        ss.min_val = 0
        ss.max_val = 100
    time.sleep(1)
    st.rerun()
