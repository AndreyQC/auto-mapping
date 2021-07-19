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
#print(newstr3)


columns = list()

newstr3 = ''.join(newstr3.split())
newstr3 = newstr3.split('`')
newstr3 = newstr3[1:]


for i in range(0, len(newstr3)-1, 2):
    col = dict()
    col["name"] = newstr3[i]
    if '(' in newstr3[i+1]:
        newstr3[i+1] = newstr3[i+1].replace('(', ' (' ,1)
        col["type"] = newstr3[i+1][0:-1]
    else:
        col["type"] = newstr3[i+1][0:-1]
    columns.append(col)

table["columns"] = columns


with open('readywork.json', 'w') as f1:
    json.dump(table, f1)