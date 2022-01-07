from pygooglenews import GoogleNews
import csv
from newspaper import Article
import nltk
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('punkt')
from pprint import pprint
from textblob import TextBlob
#from google.colab import files

# Scrapping Function to get google news (title, link)
def get_titles(search):
    stories =[]
    gn = GoogleNews(lang = 'en', country='US')
    # # do not mention AAPL (over the past 6 month 
    search = gn.search(search, when = '1d')
    newsitem = search['entries']
    for item in newsitem:
        story = {
            'Title' : item.title,
            'Read more' : item.link
        }
        stories.append(story)
    return stories

# Function to Summarize Goolge News Article + Sentiment Analysis of Google News
def summarize_artcle(url):
    article = Article(url)
    # Set up 
    article.download()
    article.parse()
    # Download Punkt
    article.download('punkt')
    article.nlp()
    summary = article.summary
    analysis = TextBlob(article.text)
    sentiment_a =""
    if analysis.polarity > 0:
      sentiment_a="positive"
    elif analysis.polarity < 0:
      sentiment_a="negative"
    else:
       sentiment_a="neutral"

    return summary,sentiment_a

#Function to save a list
def save_dict(topic, number):
    try: 
      dcts = get_titles(topic)
      news_list = []
      for x in range(number):
        dctss = dcts[x]
        url = dctss['Read more']
        try:
          summary_analysis = list(summarize_artcle(url))
          dctss['Sentiment'] = summary_analysis[1]
          dctss['Summary'] = summary_analysis[0]
        except:
          dctss['Sentiment'] = 'error'
          dctss['Summary'] ='error'
        news_list.append(dctss)
        pprint(dctss)
      return news_list 
    except:
        print('Please input useable topics, thanks or check this -> https://github.com/kotartemiy/pygooglenews#installation')

#Function to Save a CSV file
def save_to_csv(news_list):
    labels = ['Title', 'Read more','Sentiment','Summary']
    try:
        with open('news_today.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=labels)
            writer.writeheader()
            for elem in news_list:
                writer.writerow(elem)
        print("Download news_today.csv Sucessfully")
    except IOError:
        print("I/O error")

# Function to save a txt file

def save_to_txt(news_list):
    n=1
    with open("news_today.txt", 'w') as f: 
      for item in news_list: 
        f.write('-'*20+str(n)+'-'*20+'\n')
        n+=1
        for key, value in item.items(): 
          f.write('%s:\n %s\n' % (key, value))
    print("Download news_today.txt Sucessfully")

# Let's run this    
print("Hi, there!")
topic = input('Now Enter your topics to Search or Exit: ')
while topic != 'Exit':
  number = int(input('How many articles you want to search (up to 100)? '))
  news_data = save_dict(topic, number)
  try:
    save_to_txt(news_data)
    save_to_csv(news_data)
  except:
    print("Retry it again!")
  topic = input('Now Enter Your Topics to Search or Exit: ')
print('See you, hope you have a great day! ❤️')

    