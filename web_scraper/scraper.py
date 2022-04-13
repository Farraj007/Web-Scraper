import requests
from bs4 import BeautifulSoup
import re
class webScraper:
  def __init__(self, URL):
    self.URL= URL
    self.page= requests.get(URL)
    self.soup= BeautifulSoup(self.page.content, 'html.parser')
    
  def citation_needed(self):
    counter = 0
    
    for pargraph in self.soup.find_all("p"):
        z= re.findall(r'\[+citation needed+\]', pargraph.text)
        counter += len(z)
        if '[citation needed]' in pargraph.text:
            line = pargraph.text
            print('\n',line,'\n') 
    print(counter)        
    return line, counter
     
if __name__== "__main__":
  URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
  webScraper(URL).citation_needed()
  