import openai

class GPTAnalyzer:
    def __init__(self, api_key):
        openai.api_key = "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"

    def generate_summary(self, text):
        response = openai.Completion.create(
            engine="davinci-002",
            prompt=text,
            max_tokens=150
        )
        summary = response.choices[0].text.strip()
        return summary

    def analyze_sentiment(self, text):
        response = openai.Completion.create(
            engine="davinci-002",
            prompt=f"Sentiment of the following text: {text}",
            max_tokens=20
        )
        sentiment = response.choices[0].text.strip()
        return sentiment

    def extract_demands(self, text):
        response = openai.Completion.create(
            engine="davinci-002",
            prompt=f"Extract demands from the following text: {text}",
            max_tokens=100
        )
        demands = response.choices[0].text.strip()
        return demands

    def analyze_information(self, discussions):
        summaries = {}
        sentiments = {}
        demands = {}

        for topic, posts in discussions.items():
            combined_text = ' '.join([f"{post[0]} {post[1]}" for post in posts])

            summary = self.generate_summary(combined_text)
            summaries[topic] = summary
            sentiment = self.analyze_sentiment(combined_text)
            sentiments[topic] = sentiment
            demands[topic] = self.extract_demands(combined_text)

        return summaries, sentiments, demands