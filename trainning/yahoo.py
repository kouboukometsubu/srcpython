import feedparser
#feed = feedparser.parse('https://news.yahoo.co.jp/pickup/computer/rss.xml')
feed = feedparser.parse('https://news.yahoo.co.jp/rss' )
for entry in feed['entries']:
  title = entry['title']
  link = entry['link']
  print(title, ',', link)