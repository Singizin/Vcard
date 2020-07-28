import  os
import re
new_contact = 'BEGIN:VCARD\nVERSION:3.0\nN:{name1}\nFN:{name}\nTEL;TYPE=CELL:{num}\nEND:VCARD'

f = open('files/obzvon.txt','r')
n = open('files/2020bezfen.vcf','a',encoding='utf-8')

for line in f:
    #string = f.readline()
    people = list(line.split(';'))
    print(people)
    if len(people) < 4:
        continue
    name1 = str('xx FEN {} {} {} {} {}'.format(people[0], people[1], people[2], people[3], people[4]))
    name = str('xx FEN {} {} {} {} {}'.format(people[0], people[1], people[2], people[3], people[4]))
    num = re.sub('[()_-]','',people[-2])
    new = new_contact.format(name1 = name1,name = name,num = num)
    n.write(new+'\n')
    #i = i + 1

f.close()
n.close()