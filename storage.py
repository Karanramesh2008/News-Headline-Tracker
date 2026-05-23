import json
import os
file='saved_headlines.json'
def save_headlines(headlines:str):
    d=load_headlines()
    if headlines not in d:
        d.append(headlines)
        with open(file,"w") as f:
            json.dump(d,f)
    return

def load_headlines():
    if os.path.exists(file):
        with open(file,"r") as f:
            c=json.load(f)
    else:
        c=[]
    return c

def delete_headlines(key:str):
    d=load_headlines()
    if key in d:
        d.remove(key)
        with open(file,"w") as f:
            json.dump(d,f)
    

delete_headlines('d')
