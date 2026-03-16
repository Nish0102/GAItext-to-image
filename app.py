import gradio as gr

from generator import generate
from styles import styles
from safety import is_safe


def generate_image(prompt, style):

    if not is_safe(prompt):
        return "Unsafe prompt detected"

    image = generate(prompt, style)

    return image


demo = gr.Interface(

    fn=generate_image,

    inputs=[
        gr.Textbox(label="Prompt"),
        gr.Dropdown(list(styles.keys()), label="Style")
    ],

    outputs="image",

    title="AI Image Studio",
    description="Generate realistic images from text prompts"

)

demo.launch()
