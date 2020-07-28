import os
import re
new_contact = 'BEGIN:VCARD\nVERSION:3.0\nN:{name1}\nFN:{name}\nTEL;TYPE=CELL:{num}\nEND:VCARD'

f = open('files/obzvon.txt','r')
# n = open('files/3fen.vcf','a',encoding='utf-8')

i = 0
people = []
for line in f:
    new = []
    i = i + 1
    print('{}\t{}'.format(i, line))
    # try:
    if re.search(email_pat, line):
        from_to = re.search(email_pat, line).span()
        found_email = line[from_to[0]:from_to[1]]
        print(found_email)
        line = re.sub(found_email, '', line)
        new.append(found_email)
    else:
        pass
    if re.search(number_pat, line):
        from_to = re.search(number_pat, line).span()
        found_number = line[from_to[0]:from_to[1]]
        refound = re.sub('[-]', '\-', found_number)
        print(refound)
        line = re.sub('{}'.format(refound), '', line)
        new.append(found_number)
        print(found_number)
    else:
        pass
    if re.search(name, line):
        print(list(line))
        print(re.search(name, line))
        from_to = re.search(name, line).span()
        found_name = line[from_to[0]:from_to[1]]
        line = re.sub(found_name, '', line)
        new.append(found_name)
        print(found_name)
    else:
        pass
    people.append(new)
    # except Exception:
    #     if re.match(clear,line):
    #         continue
print(people)
f.close()