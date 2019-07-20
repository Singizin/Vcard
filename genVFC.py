import  os
import re
new_contact = 'BEGIN:VCARD\nVERSION:3.0\nN:{name1}\nFN:{name}\nTEL;TYPE=CELL:{num}\nEND:VCARD'

f = open('files/3FEN.txt','r', encoding='utf-8')
n = open('files/3fen.vcf','a',encoding='utf-8')

for line in f:
    #string = f.readline()
    people = list(line.split())
    if len(people) < 4:
        continue
    name1 = str('FEN {} {} {}'.format(people[0], people[1], people[2]))
    name = str('FEN {} {} {} '.format(people[0], people[1], people[2]))
    num = re.sub('[()_-]','',people[3])
    new = new_contact.format(name1 = name1,name = name,num = num)
    n.write(new+'\n')
    #i = i + 1

f.close()
n.close()