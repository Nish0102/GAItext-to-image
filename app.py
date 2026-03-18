import gradio as gr
from generator import generate, generate_img2img
from styles import styles
from safety import is_safe

def generate_image(prompt, negative_prompt, style, steps, guidance, seed, num_images, width, height):
    if not is_safe(prompt):
        return []
    images = generate(prompt, negative_prompt, style, steps, guidance, seed, num_images, width, height)
    return images

def generate_from_image(prompt, init_image, strength, style, steps, guidance):
    if not is_safe(prompt):
        return None
    return generate_img2img(prompt, init_image, strength, style, steps, guidance)

with gr.Blocks(title="AI Image Studio") as demo:
    gr.Markdown("# 🎨 AI Image Studio")

    with gr.Tabs():
        with gr.Tab("Text to Image"):
            with gr.Row():
                with gr.Column():
                    prompt = gr.Textbox(label="Prompt", lines=3)
                    negative_prompt = gr.Textbox(label="Negative Prompt", value="blurry, low quality, watermark", lines=2)
                    style = gr.Dropdown(list(styles.keys()), label="Style", value="Realistic")
                    with gr.Row():
                        steps = gr.Slider(10, 50, value=30, step=1, label="Inference Steps")
                        guidance = gr.Slider(1, 15, value=7.5, step=0.5, label="Guidance Scale")
                    with gr.Row():
                        seed = gr.Number(label="Seed (-1 = random)", value=-1)
                        num_images = gr.Slider(1, 4, value=1, step=1, label="Number of Images")
                    with gr.Row():
                        width = gr.Dropdown([512, 768, 1024], label="Width", value=1024)
                        height = gr.Dropdown([512, 768, 1024], label="Height", value=1024)
                    btn = gr.Button("Generate", variant="primary")
                with gr.Column():
                    gallery = gr.Gallery(label="Generated Images", columns=2)
            btn.click(generate_image, inputs=[prompt, negative_prompt, style, steps, guidance, seed, num_images, width, height], outputs=gallery)

        with gr.Tab("Image to Image"):
            with gr.Row():
                with gr.Column():
                    img_prompt = gr.Textbox(label="Prompt", lines=3)
                    init_image = gr.Image(label="Reference Image", type="pil")
                    strength = gr.Slider(0.1, 1.0, value=0.75, step=0.05, label="Transform Strength")
                    img_style = gr.Dropdown(list(styles.keys()), label="Style")
                    img_steps = gr.Slider(10, 50, value=30, step=1, label="Steps")
                    img_guidance = gr.Slider(1, 15, value=7.5, step=0.5, label="Guidance Scale")
                    img_btn = gr.Button("Transform", variant="primary")
                with gr.Column():
                    img_output = gr.Image(label="Output")
            img_btn.click(generate_from_image, inputs=[img_prompt, init_image, strength, img_style, img_steps, img_guidance], outputs=img_output)

demo.launch()
