import requests
from bs4 import BeautifulSoup as bs
import pyttsx3
from lxml.html import fromstring

#get url
url= str(input('Enter medium url: '))
response = requests.get(url)

#get content
def remove_tags(html):
  
    # parse html content

    soup = bs(html, "html.parser")
    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
  
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)

result = remove_tags(response.content)
print(result)

#speak and read content
engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

# the code below is to read text without downloading the mp3 file
# engine.say(result)
# engine.runAndWait()
# engine.stop()


# get title
tree = fromstring(response.content)
title = tree.findtext('.//title')
#Saving Voice to a file
engine.save_to_file(result, 'result.mp3'.format(title)) 
engine.runAndWait()
engine.stop()