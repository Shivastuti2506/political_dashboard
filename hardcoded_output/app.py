from flask import Flask, render_template, request
from analysis.gpt import GPTAnalyzer

app = Flask(__name__)

# Function to get hot topics 
def get_hot_topics(city):
    return ["Sample Topic 1", "Sample Topic 2", "Sample Topic 3", "Sample Topic 4", "Sample Topic 5"]

# Function to get relevant discussions from Reddit (hardcoded sample data)
def get_relevant_discussions(topics):
    discussions = {}
    for topic in topics:
        discussions[topic] = [
            f"Discussion 1 for {topic}",
            f"Discussion 2 for {topic}",
            f"Discussion 3 for {topic}",
        ]
    return discussions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    city = request.form.get('city')

    topics = get_hot_topics(city)
    discussions = get_relevant_discussions(topics)
    
    gpt = GPTAnalyzer("your_openai_api_key")

    # For testing purposes, generate dummy summaries, sentiments, and demands
    summaries = {topic: f"Summary for {topic}" for topic in topics}
    sentiments = {topic: "Positive" for topic in topics}
    demands = {topic: "No specific demands identified" for topic in topics}

    return render_template('results.html', topics=topics, discussions=discussions, summaries=summaries, sentiments=sentiments, demands=demands)

if __name__ == '__main__':
    app.run(debug=True)
