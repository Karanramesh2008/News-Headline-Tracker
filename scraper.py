import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
headers={"User-Agent":"Mozilla/5.0"}
def get_headlines():
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,"html.parser")

    heading=soup.find_all(['h2'])
    d=[]
    for h in heading:
        h=h.text.strip()
        if len(h)>20:
            if h not in d:
                d.append(h)
    return d

def search(headlines:list,keyword:str)->list:
    d=[]
    for a in headlines:
        if keyword.lower() in a.lower():
            d.append(a)
    return d

