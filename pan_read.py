 
import re

file = open('output.txt', 'r', encoding='utf-8')
text = file.read()
print(type(text))

pan = text.splitlines()
ans = []
if 'नाम NAME' in pan:
    name_index = pan.index('नाम NAME')
    name_index +=1
    ans.append(pan[name_index])


if "= का नाम FATHER'S NAME" in pan:
    father_name_index = pan.index("= का नाम FATHER'S NAME")
    father_name_index +=1
    ans.append(pan[father_name_index])

pan_number_regex = re.compile(r'^[a-zA-Z]{5}[0-9]{4}[a-zA-Z]$')
pan_number = list(filter(pan_number_regex.match, pan))
ans.append(pan_number)





# print(pan)
# print(hi)