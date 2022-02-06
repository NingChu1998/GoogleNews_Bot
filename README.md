![png](https://github.com/NingChu1998/GoogleNews_Bot/blob/main/Google%20News%20Bot.png?raw=true)

--------------------------------------------------------------------------------
#### 🤖 Google News Bot written in Python can replaces yourself to collect,  analyze and organize news you're interested in.

##  Features
- Fetch dataset of news from Google News
- Automatically summarizing and shortening articles
- Automatically determine whether news is positive, negative or neutral
- Organize news dataset to csv file and txt file 

##  Tech

#### Google News Bot uses a number of Python Modules to work properly:
- [pygooglenews](https://github.com/kotartemiy/pygooglenews) for scrapping google news data
- [newspaper](https://github.com/codelucas/newspaper) for extracting & curating articles
- [nltk](https://www.nltk.org) for Text summarization [NLP]
- [pprint](https://clay-atlas.com/us/blog/2021/06/13/python-en-pprint/) for modify output text
- [textblob](https://textblob.readthedocs.io/en/dev/) for sentiment analysis[NLP]

##  Installation

Google News Bot requires [Python](https://www.python.org/) 3+ to run
 
#### Clone the Repository from github
 ```sh
git clone https://github.com/NingChu1998/GoogleNews_Bot.git
```

#### Install all the requirements
 ```sh
pip install -r requirements.txt
```
#### Running the application
```
Run the googlenewsbot.py
```

---
## Input
- Example: Serach "ADA" coin related news

![](https://github.com/NingChu1998/GoogleNews_Bot/blob/main/demo.gif?raw=true)

## Output
- Example: Search "Tesla" related news and its outcome files

<img src ="https://github.com/NingChu1998/GoogleNews_Bot/blob/main/googlenewbot_txt.png" alt="Cover" width="40%"/>
<img src ="https://github.com/NingChu1998/GoogleNews_Bot/blob/main/googlenewsbot_csv.png" alt="Cover" width="50%"/>

