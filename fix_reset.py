import re

content = open('index.html').read()
old = "['i-name', 'i-c-phone', 'i-manager', 'i-no', 'l-dc', 'l-pt-tot', 'l-pt-use', 'l-cash', 's-cash'].forEach"
new = "['i-name', 'i-c-phone', 'i-manager', 'i-no', 'l-dc', 'l-pt-tot', 'l-pt-use', 'l-cash', 's-cash', 'i-memo-customer', 'i-memo'].forEach"

content = content.replace(old, new)
open('index.html', 'w').write(content)
