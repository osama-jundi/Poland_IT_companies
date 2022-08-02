from os import path
import json
import requests
from bs4 import BeautifulSoup
def write_json(new_data, filename='sample.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
url="https://www.gov.pl/web/poland-businessharbour-en/itspecialist"
filename="sample.json"
response=requests.get(url)
html=response.text
soup=BeautifulSoup(html,'html.parser')
title=soup.title.text.strip()

first_company=soup.find_all("summary")[0].text

companies=soup.find_all("summary")

details=soup.find_all("details")
dictionary = {
    "name": "",
    "email": "",
    "www": "",
    
}

listdict=[dictionary] 
# Serializing json
json_object = json.dumps(listdict, indent=4)
count=0
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
for detail in details:
    
    dictionary["name"]=detail.text.splitlines()[0]
    list1=detail.text.splitlines()
    
    print(list1)
    for i in range(1,len(list1)):
        try:
            if(list1[i][0]=='w' or list1[i][0]=='W'):
                dictionary["www"]=list1[i]
            
            
        except:
            pass
        try:
            if(list1[i][0]=='e' or list1[i][0]=='C' or list1[i][0]=='M' or list1[i][0]=='f'):
                dictionary["email"]=list1[i]
            elif(list1[i][0]==""):
                dictionary["email"]=""
            elif(list1[i][1]=="o") :
                dictionary["email"]=list1[i]
            else:
                dictionary["email"]=""
                
            
        except:
            
            pass
    listdict.append(dictionary)
    
    
    write_json(dictionary)
    dictionary["www"]=""
    dictionary["email"]=""
    
