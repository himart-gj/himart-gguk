import re
content = open('index.html').read()
content = content.replace('<div class="text-right text-xs font-bold text-gray-600 mb-3">\n<p class="mb-0.5">총 적립포인트: <span id="s1-pt-tot-view" class="text-gray-900">0</span> P</p>\n<p class="text-blue-700">포인트 잔액 (사용 후): <span id="s1-pt-remain">0</span> P</p>\n</div>', '<div id="s1-pt-container" class="text-right text-xs font-bold text-gray-600 mb-3 hidden">\n<p class="text-blue-700">L.POINT 잔액 (사용 후): <span id="s1-pt-remain" class="text-gray-900">0</span> P</p>\n</div>')

# In calc()
old_calc = "setTxt('s1-pt-tot-view', format(lPtTot)); setTxt('s1-pt-remain', format(Math.max(0, lPtTot - lPtUse)));"
new_calc = """
    const lPtRemain = Math.max(0, lPtTot - lPtUse);
    const ptCont = document.getElementById('s1-pt-container');
    if (ptCont) {
        if (lPtRemain <= 0) {
            ptCont.classList.add('hidden');
        } else {
            ptCont.classList.remove('hidden');
            setTxt('s1-pt-remain', format(lPtRemain));
        }
    }
"""
content = content.replace(old_calc, new_calc)
open('index.html', 'w').write(content)
