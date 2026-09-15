import re
content = open('index.html').read()
old = "if (data.subHp) data.subHp.forEach(hp => { addHpRow('sub'); const r = document.getElementById('sub-hp-container').lastElementChild; if(r){ r.querySelector('.hp-val').value = hp.val; r.querySelector('.hp-cnt').value = hp.cnt; } });\ncalc();"
new = "if (data.subHp) data.subHp.forEach(hp => { addHpRow('sub'); const r = document.getElementById('sub-hp-container').lastElementChild; if(r){ r.querySelector('.hp-val').value = hp.val; r.querySelector('.hp-cnt').value = hp.cnt; } });\nif(document.getElementById('i-memo-customer')) document.getElementById('i-memo-customer').value = data.memoCust || '';\nif(document.getElementById('i-memo')) document.getElementById('i-memo').value = data.memoMy || '';\ncalc();"

content = content.replace(old, new)
open('index.html', 'w').write(content)
