import re
import os

f=open('new.txt','r',encoding='utf-8')
f=f.read()
f=re.sub(' {1,}','',f)
print(f)
with open('newupdate.txt', 'w', encoding='utf-8') as k:
    k.write(f)

f = open('total2gai.txt', 'r', encoding='utf-8')
f = f.read()
result = []
for s in f:
    result.append(s)

text = ' '.join(result)
with open('charvectors.txt', 'w', encoding='utf-8') as g:
    g.write(text)