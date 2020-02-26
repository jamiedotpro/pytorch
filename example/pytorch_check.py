# -*- coding: utf-8 -*-

import torch


print('pytorch version:', torch.__version__)

print('torch.cuda.is_available():', torch.cuda.is_available())

if torch.cuda.device_count() > 0:
    print("Let's use", torch.cuda.device_count(), "GPUs!")
