import torch
import torch.nn as nn
from torchvision import models
from typing import Tuple

class VIT_V1_KHS(nn.Module):
    def __init__(self):
        super(VIT_V1_KHS, self).__init__()
        self.backborn = models.vit_b_16(weights = models.ViT_B_16_Weights.IMAGENET1K_SWAG_E2E_V1)
        self.backborn.heads = nn.Sequential(nn.Linear(768, 18))

    def forward(self, x):
        x = self.backborn(x)
        return x

def load_model(save_point) -> VIT_V1_KHS:
    model = VIT_V1_KHS()
    model.load_state_dict(save_point.weights)
    return model