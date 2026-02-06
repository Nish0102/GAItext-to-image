# app.py
"""
AI Text-to-Image Generator
Generative AI project using Stable Diffusion XL (public model)
"""

import torch
from diffusers import StableDiffusionXLPipeline
from PIL import Image
from IPython.display import display

# -----------------------------
# CONFIG
# -----------------------------
MODEL_ID = "stabilityai/stable-diffusion-xl-base-1.0"
STYLES = ["Realistic", "Anime", "Painting"]

# -----------------------------
# LOAD MODEL
# -----------------------------
print("Loading model... This may take a few minutes the first time.")
pipe = StableDiffusionXLPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16
)
pipe = pipe.to("cuda")
print("Model loaded successfully!")

# -----------------------------
# USER INPUT
# -----------------------------
print("\nAvailable styles:", ", ".join(STYLES))
prompt = input("Enter your text prompt: ")
style = input(f"Enter style ({'/'.join(STYLES)}): ").strip()

# Enhance prompt based on style
if style.lower() == "anime":
    prompt += ", anime style, colorful, cute"
elif style.lower() == "painting":
    prompt += ", painting style, brush strokes, artistic"
else:
    prompt += ", realistic, high detail"

# -----------------------------
# GENERATE IMAGE
# -----------------------------
print("\nGenerating image...")
image = pipe(prompt=prompt, num_inference_steps=30).images[0]

# Display in notebook / Colab
display(image)

# Save locally
filename = "generated_image.png"
image.save(filename)
print(f"Image saved as {filename}")
