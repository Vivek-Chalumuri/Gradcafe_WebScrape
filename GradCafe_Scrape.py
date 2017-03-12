import urllib2
import pandas as pd
from bs4 import BeautifulSoup

gradcafe = "https://thegradcafe.com/survey/index.php?q=computer+science&t=a&o=&pp=50"
req = urllib2.Request(gradcafe, headers={'User-Agent' : "Chrome Browser"}) 
con = urllib2.urlopen(req)

soup = BeautifulSoup(con)
right_table = soup.find('table',class_="results narrow-table")

A,B,C,D,E,F = [],[],[],[],[],[]

for row in right_table.findAll("tr"):
    cells = row.findAll("td")
    A.append(cells[0].find(text=True))
    B.append(cells[1].find(text=True))
    C.append(cells[2].find(text=True))
    D.append(cells[3].find(text=True))
    E.append(cells[4].find(text=True))
    F.append(cells[5].find(text=True))
    
df = pd.DataFrame(A, columns=['Institute'])
df['Program'] = B
df['Decision'] = C
df['St'] = D
df['Date Added'] = E
df['Notes'] = F

df.drop(df.index[0])  

df.to_csv("gradcafe.csv", header=False, encoding="utf-8") 
