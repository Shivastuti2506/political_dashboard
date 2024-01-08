from flask import Flask, render_template, request
from analysis.gpt import GPTAnalyzer
from newsapi import NewsApiClient
import praw

app = Flask(__name__)
api_key = '2f0f328e6bff48cb8e3083483c421501'

def get_top_news(api_key, country='us'):
    newsapi = NewsApiClient(api_key=api_key)
    top_news = newsapi.get_top_headlines(country=country, language='en', page_size=5)
    articles = top_news.get('articles', [])
    print(articles)
    return articles


def get_hot_topics(city):
    main_li=[]
    li=get_top_news(api_key)
    for i in range(len(li)):
        main_li.append([li[i]['title'], li[i]['description']])
    return main_li

def scrape_reddit_posts(query, subreddit_name='all', num_posts=5):
    reddit = praw.Reddit(client_id='TDXJPEjESa_0Q9NkTCcbag',
                         client_secret='MGTn-uqTqQvHCvvFFMqK6UTNMaJd-A',
                         user_agent='sentiment')

    subreddit = reddit.subreddit(subreddit_name)
    
    # Perform a search for the given query in the specified subreddit
    search_results = subreddit.search(query, sort='relevance', time_filter='all', limit=num_posts)

    # Extract and return the relevant information from the search results
    posts = []
    for submission in search_results:
        posts.append({
            'title': submission.title,
            'url': submission.url
        })

    return posts

def get_relevant_discussions(topics):
    post={}
    for topic in topics:
        final=[]
        reddit_posts = scrape_reddit_posts(topic, subreddit_name='news', num_posts=5)
        print('here', len(reddit_posts))
        for i in range(len(reddit_posts)):
                final.append([reddit_posts[i]['title'], reddit_posts[i]['url']])
        if len(final)==0:
            post[topic[0]]= [" No relevant discussions found"]
        else:
            post[topic[0]]= final
    return post


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    city = request.form.get('city')

    topics = get_hot_topics(city)
    discussions = get_relevant_discussions(topics)

    return render_template('results.html', topics=topics, discussions=discussions, summaries={}, sentiments={}, demands={})

if __name__ == '__main__':
    app.run(debug=True)

