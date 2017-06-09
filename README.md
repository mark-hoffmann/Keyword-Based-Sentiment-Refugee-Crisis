# Keyword Based Sentiment Analysis
## Syrian Refugee Crisis


This was a simple proof of concept for using a dictionary based approach to sentiment analysis following the Syrian Refugee Crisis. 

Data was scraped from various news sources with relating stories and and parsed with BeautifulSoup. 
The idea behind this approach was to try and incorporate positive, negative, and neutral words along with polarity amplifiers and polarity flippers.

Documents were subset based on sentances with countries mentioned in them. Arc diagrams were made with countries mentioned most together along with the sentiment scores.

Very hacked together for a PoC

Interesting TODO's:
* Track Sentiment through time to view time series of sentiment by country
* Use expanded corpus to measure not just positive / negative, but more emotions as well
* Expand to using a deep learning approach of RNN's and bi-directional LSTM's
