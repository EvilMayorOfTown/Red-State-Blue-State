# A program that:
#	- Reads text from the files in foxnews and nytimes subdirectories;
#	- Creates two separate wordclouds from the text overlayed over the democrat.png and republican.png stencils respectively;
#	- Saves the resulting images to the root directory as foximage.png and timesimage.png;
#	- Saves the same images to imagearchive subdirectory with today's date prepended to filenames.
#
# Relies on the word cloud software package found at: https://github.com/amueller/word_cloud

import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import glob
from wordcloud import WordCloud, STOPWORDS, get_single_color_func
from datetime import date
from os import path

days = 10 # number of days headlines you want to use, contingent on the date existing in the relevant directory.
today = date.today().isoformat()

# Read the text from the specified number of foxnews subdirectory files into "foxtext" string.
foxtext = ""
list_of_fox_files = glob.glob('foxnews/*')
for _ in range(days):
    if list_of_fox_files:
        latest_fox_file = max(list_of_fox_files, key=os.path.getmtime)
        foxtext += open(latest_fox_file).read()
        list_of_fox_files.remove(latest_fox_file)

# Read the text from the specified number of nytimes subdirectory files into "nytimestext" string.		
nytimestext = ""
list_of_nytimes_files = glob.glob('nytimes/*')
for _ in range(days):
    if list_of_nytimes_files:
        latest_nytimes_file = max(list_of_nytimes_files, key=os.path.getmtime)
        nytimestext += open(latest_nytimes_file).read()
        list_of_nytimes_files.remove(latest_nytimes_file)

# read the mask image
d = path.dirname(__file__)
foxmask = np.array(Image.open(path.join(d, "republican.png")))
timesmask = np.array(Image.open(path.join(d, "democrat.png")))

# Set list of words to exclude.  Using default with a few additions. 
stopwords = set(STOPWORDS)
stopwords.add("said")
stopwords.add("say")
stopwords.add("says")

# Define color functions to feed into wordcloud recolor function
def red_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return 'rgb({:.0f}, {:.0f}, {:.0f})'.format(255, 0, 0)
def blue_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return 'rgb({:.0f}, {:.0f}, {:.0f})'.format(0, 0, 255)
    
    
# generate foxnews word cloud
foxwc = WordCloud(background_color="black", max_words=150, mask=foxmask,
               stopwords=stopwords)
foxwc.generate(foxtext)
# Apply our color function 
# For multiple color tones use get_single_color_func("red") as color function
foxwc.recolor(color_func=red_color_func)
# store to files
foxwc.to_file(path.join(d, "foximage.png"))
foxwc.to_file(path.join(d, "imagearchive/" + today + " foximage.png"))

# generate nytimes word cloud
timeswc = WordCloud(background_color="black", max_words=150, mask=timesmask,
               stopwords=stopwords)
timeswc.generate(nytimestext)
# Apply our color function
timeswc.recolor(color_func=blue_color_func)
# store to files
timeswc.to_file(path.join(d, "timesimage.png"))
timeswc.to_file(path.join(d, "imagearchive/" + today + " timesimage.png"))
