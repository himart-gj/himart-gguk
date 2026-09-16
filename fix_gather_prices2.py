import re
content = open('index.html').read()
old = "totalPrice: parseInt(document.getElementById('s1-total')?.innerText.replace(/[^0-9]/g, '') || 0),payPrice: parseInt(document.getElementById('s1-pay')?.innerText.replace(/[^0-9]/g, '') || 0),finalPrice: parseInt(document.getElementById('s1-pay')?.innerText.replace(/[^0-9]/g, '') || 0),netPrice: parseInt(document.getElementById('s1-final')?.innerText.replace(/[^0-9]/g, '') || 0),lumpSum: parseInt(document.getElementById('s1-total')?.innerText.replace(/[^0-9]/g, '') || 0),subSum: parseInt(document.getElementById('s1-total')?.innerText.replace(/[^0-9]/g, '') || 0),"
new = "totalPrice: 0, payPrice: 0, finalPrice: parseInt(document.getElementById(type === '일반' ? 's3-net-lump' : 's3-net-sub')?.innerText.replace(/[^0-9]/g, '') || 0), netPrice: parseInt(document.getElementById(type === '일반' ? 's3-net-lump' : 's3-net-sub')?.innerText.replace(/[^0-9]/g, '') || 0), lumpSum: 0, subSum: 0,"
content = content.replace(old, new)
open('index.html', 'w').write(content)
