from transformers import pipeline
import gradio as gr


model = pipeline(
    #"summarization",
    "text-generation"
)

def predict(prompt):
    #summary = model(prompt)[0]["summary_text"]
    #return summary
    generationResult = model(prompt)[0]["generated_text"]
    return generationResult


# create an interface for the model
with gr.Interface(predict, "textbox", "text") as interface:
    interface.launch()