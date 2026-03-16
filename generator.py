import torch
from diffusers import StableDiffusionPipeline
from styles import styles

device = "cuda" if torch.cuda.is_available() else "cpu"

model_id = "Lykon/DreamShaper"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16
)

pipe = pipe.to(device)
pipe.enable_attention_slicing()


def build_prompt(prompt, style):

    realism_boost = (
        "highly detailed, natural lighting, realistic textures, "
        "sharp focus, high dynamic range, professional photo"
    )

    final_prompt = prompt

    if style != "None":
        final_prompt += f", {styles[style]}"

    final_prompt += f", {realism_boost}"

    return final_prompt


negative_prompt = (
    "blurry, low quality, low resolution, distorted, "
    "extra fingers, extra limbs, malformed hands, bad anatomy, "
    "deformed face, unrealistic proportions, duplicate body parts, "
    "cartoon, anime, painting, illustration, cgi"
)


def generate(prompt, style):

    final_prompt = build_prompt(prompt, style)

    image = pipe(
        prompt=final_prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=35,
        guidance_scale=7.5,
        height=512,
        width=512
    ).images[0]

    return image
