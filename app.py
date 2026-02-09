import torch
from diffusers import StableDiffusionPipeline

model_id = "Lykon/DreamShaper"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16
)

pipe.enable_model_cpu_offload()
pipe.enable_attention_slicing()

print("✅ Model loaded")

import re

blocked_words = [
    "nsfw","nude","naked","lingerie","bikini",
    "sexual","erotic","porn",

    "gore","blood","murder","kill","stab",
    "torture","corpse","behead",

    "nazi","hitler","terrorist",

    "cocaine","heroin","meth",

    "suicide","self-harm",

    "rape","molest"
]

def is_safe(prompt):
    prompt = prompt.lower()

    # match whole words only
    for word in blocked_words:
        if re.search(rf"\b{word}\b", prompt):
            return False
    return True

print("✅ Guardrails updated")

prompt = input("Enter your prompt: ")

# Minimal negative prompt (only realism helpers)
negative_prompt = "low quality, blurry"

if is_safe(prompt):
    image = pipe(
        prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=30,
        guidance_scale=7.5,
        height=512,
        width=512
    ).images[0]

    display(image)

else:
    print("❌ Unsafe prompt detected")
