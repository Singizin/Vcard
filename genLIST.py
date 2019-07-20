import  os
import re
new_contact = 'BEGIN:VCARD\nVERSION:3.0\nN:{name1}\nFN:{name}\nTEL;TYPE=CELL:{num}\nEND:VCARD'

f = open('files/contacts.vcf','r', encoding='utf-8')
n = open('files/contact_list.txt','a',encoding='utf-8')
people = []
for line in f:
    #string = f.readline()
    if line[0:3] == 'FN:':
        people.append(line[3::].split())
    else:
        continue
print(people)
people.sort()
for i in people:
    n.write('{}\t{}\t{}\t{}\n'.format(i[0],i[1],i[2],i[3]))
f.close()
n.close()