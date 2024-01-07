from flask import Flask, render_template, request
from analysis.gpt import GPTAnalyzer
from newsapi import NewsApiClient

app = Flask(__name__)
api_key = '2f0f328e6bff48cb8e3083483c421501'

def get_top_news(api_key, country='us'):
    newsapi = NewsApiClient(api_key=api_key)
    top_news = newsapi.get_top_headlines(country=country, language='en', page_size=5)
    articles = top_news.get('articles', [])
    print(articles)
    return articles

def get_hot_topics(city):
    li=get_top_news(api_key)
    main_li = []
    for i in range(len(li)):
        main_li.append([li[i]['title'], li[i]['description']])
    return main_li

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
    # discussions = get_relevant_discussions()
    # gpt = GPTAnalyzer("your_openai_api_key")

    # summaries = {topic: f"Summary for {topic}" for topic in topics}
    # sentiments = {topic: "Positive" for topic in topics}
    # demands = {topic: "No specific demands identified" for topic in topics}

    return render_template('results.html', topics=topics, discussions={}, summaries={}, sentiments={}, demands={})

if __name__ == '__main__':
    app.run(debug=True)