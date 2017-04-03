#  A simple program to scrape the headlines from a specified RSS feed and write the text 
#  to a specified textfile.  Contains prebuilt functions for foxnews and nytimes.  

import feedparser
from datetime import date

today = date.today().isoformat()

#function to scrape foxnews headlines and write to "[DATE] foxwords.txt"
def foxScrape():
    
    #create file
    filename = "foxnews/" + today + " foxwords.txt"
    foxFile = open(filename, 'w')

    # get headlines from Fox News website
    url = 'http://feeds.foxnews.com/foxnews/latest'
    parse = feedparser.parse(url)
    
    for i in range(len(parse.entries)):
        line = parse.entries[i].title
        line = line.replace("&rsquo;", "'")
        line = line.replace("&lsquo;", "'")
        foxFile.write(line.encode('utf8') + "\n")
    
    foxFile.close()

#function to scrape nytimes headline and write to "[DATE] timeswords.txt"
def timesScrape():
    
    #create file
    filename = "nytimes/" + today + " timeswords.txt"
    timesFile = open(filename, 'w')

    # get headlines from NYTimes website
    url = 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
    parse = feedparser.parse(url)
    
    for i in range(len(parse.entries)):        
        line = parse.entries[i].title
        line = line.replace("&rsquo;", "'")
        line = line.replace("&lsquo;", "'")
        timesFile.write(line.encode('utf8') + "\n")
    
    timesFile.close()

#function to scrape RSS headlines of specified site and write to specified file
def newsScrape(url, filename):
        
    #create file
    filename = today + " " + filename
    newsFile = open(filename, 'w')
    
    # get headlines from specified site
    parse = feedparser.parse(url)
    
    for i in range(len(parse.entries)):        
        line = parse.entries[i].title
        line = line.replace("&rsquo;", "'")
        line = line.replace("&lsquo;", "'")
        newsFile.write(line.encode('utf8') + "\n")
    
    newsFile.close()
  
