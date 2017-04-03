Red State, Blue State can be found at www.redstatebluestate.xyz

Red State, Blue State is a word visualization project whose purpose is to represent word usage in traditionally "liberal" and "conservative" media in an interesting way.  The word cloud images are generated from  the text contained in the last ten days of headlines gathered from the New York Times and Fox News RSS feeds, which are then respectively layered over the donkey and elephant logos.  Images are generated on a daily basis, using the preceeding ten days of headlines.

Red State, Blue State does not seek to espouse a particular political  viewpoint, nor does the author believe that valid factual conclusions can be drawn from word cloud images.  Red State, Blue State is not a commercial endeavor, and no money has been received or paid by the  author.  

This project relies upon the word cloud software written by Andreas Christian Mueller, which can be found at: 
https://github.com/amueller/word_cloud

The following files are included:

  headlinescrape.py - python script that reads the headlines from the RSS feeds of the New York Times and Fox News and writes to a text file.  

  makecloud.py - python script that generates a word cloud from the scraped headlines over the donkey and elephant stencils.  
  
  democrat.png - donkey logo stencil.
  
  republican.png - republican logo stencil.  

The headlinescrape and makecloud scripts are run daily through cron or the windows task scheduler.  I have also included sample data and images generated therefrom.  
  
  
  



