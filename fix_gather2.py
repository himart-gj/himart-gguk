import re
content = open('index.html').read()
old = "const subHp = Array.from(document.querySelectorAll('.hp-sub-row')).map(row => ({ val: row.querySelector('.hp-val').value, cnt: parseInt(row.querySelector('.hp-cnt').value) }));\nreturn {"
new = "const subHp = Array.from(document.querySelectorAll('.hp-sub-row')).map(row => ({ val: row.querySelector('.hp-val').value, cnt: parseInt(row.querySelector('.hp-cnt').value) }));\nconst memoCust = document.getElementById('i-memo-customer')?.value || '';\nconst memoMy = document.getElementById('i-memo')?.value || '';\nreturn {"
content = content.replace(old, new)
open('index.html', 'w').write(content)
