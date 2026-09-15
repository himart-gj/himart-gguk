import re

content = open('index.html').read()
old = """const subHp = Array.from(document.querySelectorAll('.hp-sub-row')).map(row => ({ val: row.querySelector('.hp-val').value, cnt: parseInt(row.querySelector('.hp-cnt').value) }));
return {"""
new = """const subHp = Array.from(document.querySelectorAll('.hp-sub-row')).map(row => ({ val: row.querySelector('.hp-val').value, cnt: parseInt(row.querySelector('.hp-cnt').value) }));
const memoCust = document.getElementById('i-memo-customer')?.value || '';
const memoMy = document.getElementById('i-memo')?.value || '';
return {"""

content = content.replace(old, new)

old_ret = "subCardTier, subCash, subHp"
new_ret = "subCardTier, subCash, subHp, memoCust, memoMy"
content = content.replace(old_ret, new_ret)

open('index.html', 'w').write(content)
