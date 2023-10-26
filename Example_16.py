# names start with s or r or v
#  names start with character starts from p to t

import re

#name="sachin"
#name="rahul"
#name="chetan"
name1="vishal"
name="tnet"

list1=re.findall(r"^[srv]\w*", name1)
list2=re.findall(r"^[p-t]\w*", name)

print(list1)
print(list2)


