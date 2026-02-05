import streamlit as st
import os

ss = st.session_state

image_folder = "image"
image_files = os.listdir(image_folder)
image_files.sort()

if "products" not in ss:
    ss.products = {}
    for image_file in image_files:
        product_name = image_file[:-4]
        ss.products[product_name] = {
            "image_path": image_folder + "/" + image_file,
            "price": 10,
            "stock": 10,
        }


st.title("購物平台")

coLNum = st.number_input("請輸入欄位數", min_value=1, max_value=5, value=3, step=1)
cols = st.columns(coLNum)
counter = 0

for name, details in ss.products.items():
    with cols[counter % coLNum]:
        st.image(details["image_path"], use_container_width=True)
        st.write(f"## {name}")
        st.write(f"價格: {details['price']}")
        st.write(f"庫存: {details['stock']}")
    counter += 1
