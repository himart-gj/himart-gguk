import re

content = open('index.html').read()

# Update HTML label
content = content.replace('<span class="text-xs font-bold text-rose-800">기타 혜택 (상품권, 추가할인 등)</span>', '<span class="text-xs font-bold text-rose-800">추가혜택</span>')

# Update addLumpBenefitRow function
old_func = """<select class="input-box w-[30%] text-[10px] b-type" onchange="calc()">
<option value="cashback">추가 캐시백</option>
<option value="gift">상품권</option>
<option value="naver">네이버포인트 적립</option>
<option value="discount">추가즉시할인</option>
</select>"""
new_func = """<select class="input-box w-[30%] text-[10px] b-type" onchange="calc()">
<option value="discount">즉시할인</option>
<option value="etc">기타</option>
</select>"""
content = content.replace(old_func, new_func)

# Update calc logic for parsing benefit rows
old_calc_parsing = """    document.querySelectorAll('.benefit-lump-row').forEach(row => {
        const type = row.querySelector('.b-type').value;
        const desc = row.querySelector('.b-desc').value || (type==='cashback'?'추가 캐시백':type==='gift'?'상품권':type==='naver'?'네이버포인트':'추가 즉시할인');
        const val = parseInt(row.querySelector('.b-val').value) || 0;
        if(val > 0) {
            if(type === 'discount') {
                extraDc += val;
                benefitRows.push({type: 'dc', desc, val});
            } else if(type === 'cashback') {
                extraCash += val;
                benefitRows.push({type: 'cash', desc, val});
            } else if(type === 'gift') {
                extraCash += val;
                benefitRows.push({type: 'gift', desc, val});
            } else if(type === 'naver') {
                extraCash += val;
                benefitRows.push({type: 'naver', desc, val});
            }
        }
    });"""

new_calc_parsing = """    document.querySelectorAll('.benefit-lump-row').forEach(row => {
        const type = row.querySelector('.b-type').value;
        const desc = row.querySelector('.b-desc').value || (type==='discount'?'즉시할인':'기타');
        const val = parseInt(row.querySelector('.b-val').value) || 0;
        if(val > 0) {
            if(type === 'discount' || type === 'dc') {
                extraDc += val;
                benefitRows.push({type: 'dc', desc, val});
            } else {
                extraCash += val;
                benefitRows.push({type: 'etc', desc, val});
            }
        }
    });"""
content = content.replace(old_calc_parsing, new_calc_parsing)

# Update calc logic for rendering benefit rows
old_calc_rendering = """    benefitRows.filter(b=>b.type==='cash').forEach(b => {
        s1CashRows += `<tr><td class="bg-gray-50 text-gray-800">(-) [캐시백] ${b.desc}</td><td class="text-right text-blue-600">- ${format(b.val)} 원</td></tr>`;
    });
    benefitRows.filter(b=>b.type==='gift').forEach(b => {
        s1CashRows += `<tr><td class="bg-gray-50 text-gray-800">(-) [상품권] ${b.desc}</td><td class="text-right text-green-600">- ${format(b.val)} 원</td></tr>`;
    });
    benefitRows.filter(b=>b.type==='naver').forEach(b => {
        s1CashRows += `<tr><td class="bg-gray-50 text-gray-800">(-) [네이버포인트] ${b.desc}</td><td class="text-right text-green-600">- ${format(b.val)} 원</td></tr>`;
    });"""

new_calc_rendering = """    benefitRows.filter(b=>b.type==='etc').forEach(b => {
        s1CashRows += `<tr><td class="bg-gray-50 text-gray-800">(-) [추가혜택] ${b.desc}</td><td class="text-right text-blue-600">- ${format(b.val)} 원</td></tr>`;
    });"""
content = content.replace(old_calc_rendering, new_calc_rendering)

open('index.html', 'w').write(content)
