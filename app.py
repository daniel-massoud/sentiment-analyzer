from transformers import pipeline

# Load the model once at startup
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze(text):
    result = sentiment_model(text)[0]
    label = result["label"]
    score = round(result["score"] * 100, 1)
    return label, score

def main():
    print("=== Sentiment Analyzer ===")
    print("Type any text and I'll tell you if it's positive or negative.")
    print("Type 'quit' to exit.\n")

    while True:
        text = input("You: ").strip()

        if text.lower() == "quit":
            print("Bye.")
            break

        if text == "":
            print("Please type something.\n")
            continue

        label, score = analyze(text)
        print(f"Result: {label} — {score}% confidence\n")

main()