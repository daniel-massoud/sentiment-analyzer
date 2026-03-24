# Sentiment Analyzer

A command-line sentiment analysis tool built with Python and HuggingFace Transformers.

Give it any text and it tells you whether the sentiment is positive or negative,
along with a confidence score.

## How it works

Uses DistilBERT fine-tuned on SST-2 — a lightweight transformer model trained on
movie reviews. The model runs locally on your machine, no API calls needed.

## Setup

Clone the repo and install dependencies:

    git clone https://github.com/daniel-massoud/sentiment-analyzer
    cd sentiment-analyzer
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt

## Run it

    python app.py

## Example output

    You: I love working on this project
    Result: POSITIVE — 99.8% confidence

    You: This is the worst experience I have ever had
    Result: NEGATIVE — 99.9% confidence

## Limitations

- Model was trained on English text only. Performance degrades on other languages.
- Binary output only (positive/negative). Neutral detection is unreliable.

## Tech

- Python
- HuggingFace Transformers
- DistilBERT (distilbert-base-uncased-finetuned-sst-2-english)