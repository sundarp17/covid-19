#web scraping the worldometer website

import pandas as pd
import requests
import lxml.html as lh

url='https://www.worldometers.info/coronavirus/'
page = requests.get(url)
doc = lh.fromstring(page.content)
tr_elements = doc.xpath('//tr')
col=[]
i=0
for t in tr_elements[0]:
    i+=1
    name=t.text_content()
    print('%d:"%s"'%(i,name))
    col.append((name,[]))
print(len(tr_elements))
length=int(len(tr_elements)/2)
print(length)
for j in range(1,length):
    T = tr_elements[j]
    i = 0
    for t in T.iterchildren():
        data = t.text_content()
        if i > 0:
            try:
                data = int(data)
            except:
                pass
        col[i][1].append(data)
        i += 1


Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)
df = df[df['Country,Other']!='Total:']

print(df)
ex=pd.DataFrame(df).to_csv('5709Project.csv',header=True,index=None)