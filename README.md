# 🎨 AI Image Studio — Text-to-Image Generator
 
> Generate stunning AI images from text prompts using **Stable Diffusion XL Turbo** — with style presets, img2img, batch generation, and one-click Hugging Face deployment.
 
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Diffusers-yellow?logo=huggingface)
![Gradio](https://img.shields.io/badge/UI-Gradio-orange)
![License](https://img.shields.io/badge/License-MIT-green)
 
---
 
## 🚀 Features
 
- **Text-to-Image Generation** — Convert any text prompt into a high-quality AI image
- **Image-to-Image (img2img)** — Upload a reference image and transform it with a prompt
- **Style Presets** — Realistic, Anime, Painting, Cyberpunk, Watercolor, Sketch, Cinematic
- **Negative Prompt Support** — Tell the model what *not* to generate for cleaner results
- **Batch Generation** — Generate up to 4 images in a single run
- **Advanced Controls** — Tune inference steps, guidance scale, seed, and resolution
- **Downloadable Images** — Save any generated image with one click
- **GPU Accelerated** — Fast generation via SDXL Turbo (4 steps vs 30+ for standard SDXL)
- **Safety Filter** — Automatic prompt moderation before generation
 
---
 
## 🛠 Tech Stack
 
| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Deep Learning | PyTorch |
| Diffusion Model | Stable Diffusion XL Turbo (HuggingFace Diffusers) |
| UI | Gradio 4.x |
| Image Processing | PIL (Pillow) |
| Deployment | Hugging Face Spaces / Google Colab / Local GPU |
 
---
 
## ⚙️ Installation & Setup
 
### Prerequisites
 
- Python 3.10+
- CUDA-compatible GPU (recommended: T4 or better)
- 8GB+ VRAM for SDXL Turbo
 
### 1. Clone the Repository
 
```bash
git clone https://github.com/Nish0102/GAItext-to-image.git
cd GAItext-to-image
```
 
### 2. Install Dependencies
 
```bash
pip install -r requirements.txt
```
 
### 3. Run the App
 
```bash
python app.py
```
 
The Gradio interface will open at `http://localhost:7860`.
 
---
 
## ▶️ Quick Start (Google Colab)
 
Run directly in your browser — no local GPU needed:
 
```python
!git clone https://github.com/Nish0102/GAItext-to-image.git
%cd GAItext-to-image
!pip install -r requirements.txt
!python app.py --share  # Generates a public URL
```
 
> Make sure to select **T4 GPU** under Runtime → Change runtime type.
 
---
 
## 🖥 Usage
 
### Text to Image Tab
 
1. Enter a descriptive **prompt** (e.g. *"a futuristic city at sunset, neon lights, rain"*)
2. Optionally add a **negative prompt** (e.g. *"blurry, watermark, low quality"*)
3. Choose a **style preset**
4. Adjust **steps**, **guidance scale**, **seed**, and **resolution**
5. Click **Generate** — results appear in the gallery
 
### Image to Image Tab
 
1. Upload a **reference image**
2. Enter a prompt describing the transformation
3. Set **transform strength** (0.1 = subtle, 1.0 = full transformation)
4. Click **Transform**
 
### Tips for Best Results
 
- Use detailed, descriptive prompts — more detail = better images
- Add lighting cues: *"golden hour", "studio lighting", "soft bokeh"*
- Use negative prompts to fix common issues: *"no blur, no extra limbs, no watermark"*
- For SDXL Turbo, set guidance scale to `0.0` and steps to `4` for fastest results
- Fix the seed to reproduce the exact same image with tweaked prompts
 
---
