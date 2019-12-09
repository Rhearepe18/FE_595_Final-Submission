import requests
from bs4 import BeautifulSoup 
import re 
from requests import get

url = "https://theyfightcrime.org/"

male = open("Male.txt","w+")             
female = open("Female.txt","w+")                      

for i in range(0,50):
    get_request = get(url)        
    soup = BeautifulSoup(get_request.text, "html.parser")  
    link = soup.select("center p")                
    text = link[0].get_text()                        
    s = text.split("She")                   
    male.write(s[0][:-1]+"\n")                         
    split=('She'+ s[1]).split("They fight crime!")     
    female.write(split[0] + "\n")                

male.close()  
female.close()                                        

