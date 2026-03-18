import torch
import random
from diffusers import AutoPipelineForText2Image, AutoPipelineForImage2Image
from styles import styles

# Load SDXL Turbo — much faster than standard SDXL
pipe = AutoPipelineForText2Image.from_pretrained(
    "stabilityai/sdxl-turbo",
    torch_dtype=torch.float16,
    variant="fp16"
).to("cuda")

pipe_img2img = AutoPipelineForImage2Image.from_pretrained(
    "stabilityai/sdxl-turbo",
    torch_dtype=torch.float16,
    variant="fp16"
).to("cuda")

def generate(prompt, negative_prompt, style, steps, guidance, seed, num_images, width, height):
    style_prompt = styles.get(style, "")
    full_prompt = f"{style_prompt}, {prompt}" if style_prompt else prompt
    generator = torch.manual_seed(int(seed)) if seed != -1 else torch.manual_seed(random.randint(0, 99999))

    images = pipe(
        prompt=full_prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=steps,      # Only 1-4 needed for Turbo!
        guidance_scale=guidance,        # Use 0.0 for Turbo
        num_images_per_prompt=num_images,
        width=width,
        height=height,
        generator=generator
    ).images
    return images

def generate_img2img(prompt, init_image, strength, style, steps, guidance):
    style_prompt = styles.get(style, "")
    full_prompt = f"{style_prompt}, {prompt}" if style_prompt else prompt

    image = pipe_img2img(
        prompt=full_prompt,
        image=init_image,
        strength=strength,
        num_inference_steps=steps,
        guidance_scale=guidance,
    ).images[0]
    return image
