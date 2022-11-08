import streamlit as st
import torch
import torchvision
import yaml
from modules import *
import inference as I

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")


root_password = ' '


def main():
    save_point, model = I.load_cached_files("config.yaml")
    model.eval()    

    st.title("Mask & Gender & Age Classifier")
    with open("config.yaml") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg","png"])

    if uploaded_file:
        image_bytes = uploaded_file.getvalue()
        image = Image.open(io.BytesIO(image_bytes))

        st.image(image, caption='Uploaded Image')
        st.write("Classifying...")
        _, y_hat = I.inference_image(model, image_bytes)
        label = config['classes'][y_hat.item()]

        st.write(f'label is {label}')
    # img_file_buffer = st.camera_input("Take a picture")
    # if img_file_buffer is not None:

    #     bytes_data = img_file_buffer.getvalue()
    #     with st.spinner("Classifying..."):
    #         _, y_hat = I.inference_image(model, bytes_data)

    #     label = config["classes"][y_hat.item()]

    #     col1, col2, col3 = st.columns(3)
    #     col1.metric("Mask", label[0])
    #     col2.metric("Gender", label[1])
    #     col3.metric("Age", label[2])

    # st.title("Mask Classification Model")

    # with open("config.yaml") as f:
    #     config = yaml.load(f, Loader=yaml.FullLoader)
    




@cache_on_button_press('Authenticate')
def authenticate(password) ->bool:
    print(type(password))
    return password == root_password


password = st.text_input('password', type="password")

if authenticate(password):
    st.success('You are authenticated!')
    main()
else:
    st.error('The password is invalid.')