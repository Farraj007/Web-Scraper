import requests
from bs4 import BeautifulSoup
import re
class webScraper:
  def __init__(self, URL):
    self.URL= URL
    self.page= requests.get(URL)
    self.soup= BeautifulSoup(self.page.content, 'html.parser')
    self.searchfor= self.soup.find_all(string=re.compile("citation needed"))
  def get_citations_needed_count(self):
    count=len(self.searchfor)
    print(count)
    return 
  
  def get_citations_needed_report(self):
    for paragraph in self.soup.find_all('p'):
      occurrences=paragraph.text.count('[citation needed]')
      if '[citation needed]' in paragraph.text:
        if occurrences >1:
          for i in range(occurrences):
            subpara = paragraph.text.strip().split('[citation needed]')[i]+'[citation needed]'
            print('\n',subpara,'\n')    

        else:
          subpara = paragraph.text.strip().split('[citation needed]')[0]+'[citation needed]'
          print('\n',subpara,'\n')    
    return 
     
if __name__== "__main__":
  URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
  
  webScraper(URL).get_citations_needed_count()
  webScraper(URL).get_citations_needed_report()
  
  