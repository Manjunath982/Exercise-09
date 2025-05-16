import requests


API_KEY = 'YOUR_API_KEY'
BASE_URL = 'https://newsapi.org/v2/everything'


def fetch_news(topic, language='en', sort_by='publishedAt'):
    params = {
        'q': topic,
        'apiKey': API_KEY,
        'language': language,
        'sortBy': sort_by
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


def display_news(news_data):
    if news_data and 'articles' in news_data:
        for article in news_data['articles']:
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']}")
            print(f"URL: {article['url']}")
            print('-' * 80)
    else:
        print("No news available.")


if __name__ == '__main__':
    topics = ['technology', 'sports', 'business', 'health']

    for topic in topics:
        print(f"Fetching news on: {topic}")
        news_data = fetch_news(topic)
        display_news(news_data)
        print('\n' + '=' * 80 + '\n')
 


