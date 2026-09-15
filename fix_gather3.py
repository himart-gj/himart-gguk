import re
content = open('index.html').read()

pattern = r"const subHp = Array\.from\(document\.querySelectorAll\('\.hp-sub-row'\)\)\.map\(row => \(\{ val: row\.querySelector\('\.hp-val'\)\.value, cnt: parseInt\(row\.querySelector\('\.hp-cnt'\)\.value\) \}\)\);(.*?)return \{"
new = "const subHp = Array.from(document.querySelectorAll('.hp-sub-row')).map(row => ({ val: row.querySelector('.hp-val').value, cnt: parseInt(row.querySelector('.hp-cnt').value) }));\\nconst memoCust = document.getElementById('i-memo-customer')?.value || '';\\nconst memoMy = document.getElementById('i-memo')?.value || '';\\nreturn {"

content = re.sub(pattern, new, content, flags=re.DOTALL)
open('index.html', 'w').write(content)
