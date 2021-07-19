import json
import re

re1 =  '(\W|^)CREATE\s{0,10}EXTERNAL\s{0,10}TABLE(\W|$)'
re2 = '(\()'
re4 = '(\W\))'

table = dict()


with open('failrabota.hql', 'r') as f:
    c = f.read()
c = c.replace('\n', '')
c = ' '.join(c.split())
#print(c)


regex_num = re.compile(re1)
s = regex_num.search(c)  
newstr = c[int(s.end()):len(c)]#первая строка без тейбла
#print(newstr)


regex_num1 = re.compile(re2)
s = regex_num1.search(newstr) 
newstr1 = newstr[0:int(s.start())-1]#строка с тейблнеймом
tablename = newstr1.split('.')
table["database"] = tablename[0][1:-1]
table["tablename"] = tablename[-1][1:-1]
#print(table)


newstr2 = newstr[int(s.start())+1:len(c)]
regex_num2 = re.compile(re4)
s = regex_num2.search(newstr2) 
#print(newstr2)
newstr3 = newstr2[0:int(s.start())]
newstr3 = newstr3.split()
#print(newstr3)


columns = list()
dud = []
cou = 0
for i in range(len(newstr3)):
    if '`' in newstr3[i]:
        dud.append(cou)
    cou += 1


for i in range(len(dud)-1):
    col = dict()
    something = newstr3[dud[i]+1:dud[i+1]]
    col["name"] = newstr3[dud[i]]
    col["type"] = something
    columns.append(col)
table["columns"] = columns


with open('readywork.json', 'w') as f1:
    json.dump(table, f1)