# A program that:
#	- Reads text from the files in foxnews and nytimes subdirectories;
#	- Creates two separate wordclouds from the text overlayed over the democrat.png and republican.png stencils respectively;
#	- Creates a third wordcloud using the combined texts with the unicorn.png stencil;
#	- Saves the resulting images to the root directory as foximage.png, timesimage.png, and unicornimage.png;
#	- Saves the same images to imagearchive subdirectory with today's date prepended to filenames.
#
# Relies on the word cloud software package found at: https://github.com/amueller/word_cloud

import os
from PIL import Image, ImageColor
import numpy as np
import matplotlib.pyplot as plt
import glob
from wordcloud import WordCloud, STOPWORDS, get_single_color_func
from datetime import date
from os import path
import colorsys

from random import Random

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

		
# Combine text for unicorn image 		
unicorntext = foxtext + " " + nytimestext
# Code that would make unicorn use only words used by BOTH foxnews and times.
# document_1_words = foxtext.split()
# document_2_words = nytimestext.split()
# unique = list(set(document_1_words).symmetric_difference(set(document_2_words)))
# splitwords = unicorntext.split()
# resultwords  = [word for word in splitwords if word not in unique]
# unicorntext = ' '.join(resultwords)
		
# read the mask image
d = path.dirname(__file__)
foxmask = np.array(Image.open(path.join(d, "republican.png")))
timesmask = np.array(Image.open(path.join(d, "democrat.png")))
unicornmask = np.array(Image.open(path.join(d, "unicorn.png")))

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
def get_shaded_color_func(color):
    """Create a color function which returns a single and value, but with varying saturation with. 
	Accepted values are color strings as usable by PIL/Pillow.
    """
    old_r, old_g, old_b = ImageColor.getrgb(color)
    rgb_max = 255.
    h, s, v = colorsys.rgb_to_hsv(old_r / rgb_max, old_g / rgb_max,
                                  old_b / rgb_max)

    def single_color_func(word=None, font_size=None, position=None,
                          orientation=None, font_path=None, random_state=None):
        """Random color generation.

        Additional coloring method. It picks a random saturation with hue and
        value based on the color given to the generating function.
        """
        if random_state is None:
            random_state = Random()
        r, g, b = colorsys.hsv_to_rgb(h, random_state.uniform(.5, 1), v)
        return 'rgb({:.0f}, {:.0f}, {:.0f})'.format(r * rgb_max, g * rgb_max,
                                                    b * rgb_max)
    return single_color_func    
    
# generate foxnews word cloud
foxwc = WordCloud(background_color="black", max_words=150, mask=foxmask,
               stopwords=stopwords)
foxwc.generate(foxtext)
# Apply our color function 
foxwc.recolor(color_func=get_shaded_color_func("red"))
# store to files
foxwc.to_file(path.join(d, "foximage.png"))
foxwc.to_file(path.join(d, "imagearchive/" + today + " foximage.png"))

# generate nytimes word cloud
timeswc = WordCloud(background_color="black", max_words=150, mask=timesmask,
               stopwords=stopwords)
timeswc.generate(nytimestext)
# Apply our color function
timeswc.recolor(color_func=get_shaded_color_func("blue"))
# store to files
timeswc.to_file(path.join(d, "timesimage.png"))
timeswc.to_file(path.join(d, "imagearchive/" + today + " timesimage.png"))

# generate combined word cloud
unicornwc = WordCloud(background_color="black", max_words=150, mask=unicornmask,
               stopwords=stopwords)
unicornwc.generate(unicorntext)
# Apply our color function 
unicornwc.recolor(color_func=get_shaded_color_func("pink"))
# store to files
unicornwc.to_file(path.join(d, "unicornimage.png"))
unicornwc.to_file(path.join(d, "imagearchive/" + today + " unicornimage.png"))