# Sentiment Analyzer

A web app that analyzes the sentiment of any text using DistilBERT.
Enter a sentence and it tells you whether the sentiment is positive 
or negative, along with a confidence score.

**Live demo:** https://huggingface.co/spaces/daniel-massoud/sentiment-analyzer

---

## How it works

Uses DistilBERT fine-tuned on SST-2, a transformer model trained on
movie reviews. The model runs on HuggingFace infrastructure, no setup needed.

## Run it locally

    git clone https://github.com/daniel-massoud/sentiment-analyzer
    cd sentiment-analyzer
    python -m venv venv
    venv\Scripts\activate
    pip install transformers torch gradio
    python app_ui.py

## Example output

    Input:  "I love working on this project"
    Output: Positive  99.8% confidence

    Input:  "This is the worst experience I have ever had"
    Output: Negative  99.9% confidence

## Limitations

- Trained on English text only, degrades on other languages
- Binary classification only.. positive or negative, no neutral

## Tech stack

Python · HuggingFace Transformers · DistilBERT · Gradio
