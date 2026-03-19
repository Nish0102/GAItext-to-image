import gradio as gr
from generator import generate, generate_img2img
from styles import styles, list_styles
from safety import is_safe, get_block_reason

# ---------------------------
# STYLE KEYS
# ---------------------------

style_choices = list_styles()  # uses helper from upgraded styles.py

# ---------------------------
# HANDLER FUNCTIONS
# ---------------------------

def generate_image(prompt, negative_prompt, style, steps, guidance, seed, num_images, width, height):
    if not prompt.strip():
        return [], "⚠️ Please enter a prompt."

    reason = get_block_reason(prompt)
    if reason:
        return [], reason

    try:
        images = generate(prompt, negative_prompt, style, steps, guidance, seed, num_images, width, height)
        return images, f"✅ Generated {len(images)} image(s) successfully."
    except Exception as e:
        return [], f"❌ Error: {str(e)}"


def generate_from_image(prompt, init_image, strength, style, steps, guidance):
    if not prompt.strip():
        return None, "⚠️ Please enter a prompt."

    if init_image is None:
        return None, "⚠️ Please upload a reference image."

    reason = get_block_reason(prompt)
    if reason:
        return None, reason

    try:
        image = generate_img2img(prompt, init_image, strength, style, steps, guidance)
        return image, "✅ Image transformed successfully."
    except Exception as e:
        return None, f"❌ Error: {str(e)}"


# ---------------------------
# UI
# ---------------------------

with gr.Blocks(
    title="AI Image Studio",
    theme=gr.themes.Default(primary_hue="orange")
) as demo:

    gr.Markdown("""
    # 🎨 AI Image Studio
    Generate stunning images from text using **Stable Diffusion XL Turbo**.
    > 💡 **Tip:** For SDXL Turbo, use **Steps = 4** and **Guidance Scale = 0.0** for fastest results.
    """)

    with gr.Tabs():

        # ---- TAB 1: Text to Image ----
        with gr.Tab("🖼 Text to Image"):
            with gr.Row():

                # Left column — inputs
                with gr.Column(scale=1):
                    prompt = gr.Textbox(
                        label="Prompt",
                        placeholder="a futuristic city at night, glowing neon lights, rain soaked streets...",
                        lines=3
                    )
                    negative_prompt = gr.Textbox(
                        label="Negative Prompt",
                        value="blurry, low quality, watermark, text, logo",
                        lines=2
                    )
                    style = gr.Dropdown(
                        choices=style_choices,
                        label="Style",
                        value="Cyberpunk"       # ✅ fixed — valid key from styles.py
                    )

                    with gr.Row():
                        steps = gr.Slider(
                            minimum=1, maximum=50, value=4,   # ✅ default 4 for Turbo
                            step=1, label="Inference Steps"
                        )
                        guidance = gr.Slider(
                            minimum=0.0, maximum=15.0, value=0.0,  # ✅ default 0.0 for Turbo
                            step=0.5, label="Guidance Scale"
                        )

                    with gr.Row():
                        seed = gr.Number(label="Seed (-1 = random)", value=-1)
                        num_images = gr.Slider(1, 4, value=1, step=1, label="Number of Images")

                    with gr.Row():
                        width = gr.Dropdown(
                            choices=[512, 768, 1024],
                            label="Width", value=512       # ✅ default 512 — safer for VRAM
                        )
                        height = gr.Dropdown(
                            choices=[512, 768, 1024],
                            label="Height", value=512
                        )

                    btn = gr.Button("🎨 Generate", variant="primary", size="lg")

                # Right column — outputs
                with gr.Column(scale=1):
                    gallery = gr.Gallery(
                        label="Generated Images",
                        columns=2,
                        height=500,
                        show_download_button=True
                    )
                    status_txt = gr.Textbox(
                        label="Status",
                        interactive=False,
                        max_lines=2
                    )

            btn.click(
                fn=generate_image,
                inputs=[prompt, negative_prompt, style, steps, guidance, seed, num_images, width, height],
                outputs=[gallery, status_txt]
            )

        # ---- TAB 2: Image to Image ----
        with gr.Tab("🔁 Image to Image"):
            with gr.Row():

                # Left column — inputs
                with gr.Column(scale=1):
                    img_prompt = gr.Textbox(
                        label="Prompt",
                        placeholder="transform this into a cyberpunk scene...",
                        lines=3
                    )
                    init_image = gr.Image(
                        label="Reference Image",
                        type="pil"
                    )
                    strength = gr.Slider(
                        0.1, 1.0, value=0.75,
                        step=0.05,
                        label="Transform Strength (0.1 = subtle, 1.0 = full)"
                    )
                    img_style = gr.Dropdown(
                        choices=style_choices,
                        label="Style",
                        value="Photorealistic"   # ✅ fixed — valid key
                    )
                    with gr.Row():
                        img_steps = gr.Slider(1, 50, value=4, step=1, label="Steps")
                        img_guidance = gr.Slider(0.0, 15.0, value=0.0, step=0.5, label="Guidance Scale")

                    img_btn = gr.Button("🔁 Transform", variant="primary", size="lg")

                # Right column — outputs
                with gr.Column(scale=1):
                    img_output = gr.Image(label="Output", height=500)
                    img_status = gr.Textbox(
                        label="Status",
                        interactive=False,
                        max_lines=2
                    )

            img_btn.click(
                fn=generate_from_image,
                inputs=[img_prompt, init_image, strength, img_style, img_steps, img_guidance],
                outputs=[img_output, img_status]
            )

    gr.Markdown("""
    ---
    Built with [Gradio](https://gradio.app) · Model: [SDXL Turbo](https://huggingface.co/stabilityai/sdxl-turbo)
    """)

demo.launch()
