import os
import gradio as gr

# Required environment variables (as per checklist)
API_BASE_URL = os.getenv("API_BASE_URL", "")
MODEL_NAME = os.getenv("MODEL_NAME", "govsim-ai")
HF_TOKEN = os.getenv("HF_TOKEN", "")

def simulate(pollution, economy, happiness, action):
    # Simple policy logic (your "AI")
    if action == "Increase Tax":
        economy -= 10
        happiness -= 5
    elif action == "Give Subsidy":
        economy -= 8
        happiness += 10
    elif action == "Apply Regulation":
        pollution -= 15
        economy -= 5

    # Keep values within range
    pollution = max(0, min(100, pollution))
    economy = max(0, min(100, economy))
    happiness = max(0, min(100, happiness))

    return f"📊 Results:\nPollution: {pollution}\nEconomy: {economy}\nHappiness: {happiness}"

# Gradio UI
interface = gr.Interface(
    fn=simulate,
    inputs=[
        gr.Slider(0, 100, value=70, label="Pollution"),
        gr.Slider(0, 100, value=60, label="Economy"),
        gr.Slider(0, 100, value=50, label="Happiness"),
        gr.Radio(["Increase Tax", "Give Subsidy", "Apply Regulation"], label="Select Policy")
    ],
    outputs="text",
    title="GovSim AI - Policy Simulator",
    description="AI system that simulates how government policies affect society over time."
)

interface.launch()
