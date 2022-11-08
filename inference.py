from typing import Tuple
import torch
import streamlit as st
from modules import *

@st.cache(allow_output_mutation=True)
def load_cached_files(config_path:str)  -> "tuple[SavePoint, VIT_V1_KHS]":
    save_point = load_savepoint(config_path)
    model = load_model(save_point)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    return save_point, model
    
def inference_image(model: VIT_V1_KHS, image_bytes: bytes) -> Tuple[torch.Tensor, torch.Tensor]:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    tensor = transform_image(image_bytes=image_bytes).to(device)
    outputs = model.forward(tensor)

    _, y_hat = outputs.max(1)
    return tensor, y_hat
