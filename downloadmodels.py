import gdown


gdown.download('https://drive.google.com/u/0/uc?id=1dw8PKVkLfISzNtUu3gqGh83NBO83ZQ5n&export=download', "./experiments/pretrained_models/HINet-GoPro.pth", quiet=False)
gdown.download('https://drive.google.com/u/0/uc?id=1uYH8XvLgrn-Vg6L0NjUcO2Fblhqrc8TU&export=download', "./experiments/pretrained_models/HINet-REDS.pth", quiet=False)
gdown.download('https://drive.google.com/file/d/1QwQUVbk6YVOJViCsOKYNykCsdJSVGRtb', "./experiments/pretrained_models/model_deblurring.pth", quiet=False)
gdown.download('https://drive.google.com/uc?id=1pwcOhDS5Erzk8yfAbu7pXTud606SB4-L', "./experiments/pretrained_models/Restormer-GoPro.pth", quiet=False)
