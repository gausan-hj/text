import pandas as pd
from datetime import datetime
import json
import html

# ===== 配置 =====
SHEET_ID = "1YVa3nLUBW80j2nA4mudEqLH91RJ0FSRytmoDqmbyUJk"
SHEET_NAME = "Sheet3"

# ===== 成员名单 =====
members_list = [
    {"group": "星穹组", "name_cn": "陈展艺", "name_en": "IVAN TAN ZHAN YI", "class": "S2FA", "student_id": "22038", "order": 1},
    {"group": "星穹组", "name_cn": "侯展扬", "name_en": "HOW ZHAN YANG", "class": "S2Y", "student_id": "22100", "order": 2},
    {"group": "星穹组", "name_cn": "邱嘉瑞", "name_en": "KATHERINE KHOO JAI RUI", "class": "J3T", "student_id": "24076", "order": 3},
    {"group": "星穹组", "name_cn": "莎哈娜", "name_en": "SADHANA A/P SASU BAKIAN", "class": "J3T", "student_id": "24078", "order": 4},
    {"group": "星穹组", "name_cn": "李韡翰", "name_en": "LEE WEI HANN", "class": "J3K", "student_id": "24068", "order": 5},
    {"group": "星穹组", "name_cn": "彭绍洋", "name_en": "PEH SHAO YANG", "class": "J3T", "student_id": "24088", "order": 6},
    {"group": "星穹组", "name_cn": "梁纹璇", "name_en": "LEONG WEN XUAN", "class": "J2Y", "student_id": "25035", "order": 7},
    {"group": "星穹组", "name_cn": "尤嘉乐", "name_en": "JUSTIN YEW JIA LE", "class": "J2Y", "student_id": "25046", "order": 8},
    {"group": "星穹组", "name_cn": "许艳棋", "name_en": "KHOR YAN QI", "class": "J1Y", "student_id": "26018", "order": 9},
    {"group": "星穹组", "name_cn": "林隽毓", "name_en": "LIM JOON YI", "class": "J1Y", "student_id": "26032", "order": 10},
    {"group": "夜曜组", "name_cn": "李竑证", "name_en": "LEE HOONG ZHENG", "class": "S2FA", "student_id": "22040", "order": 1},
    {"group": "夜曜组", "name_cn": "廖若含", "name_en": "LIEW XIN YU", "class": "S2Y", "student_id": "22029", "order": 2},
    {"group": "夜曜组", "name_cn": "林芷嫣", "name_en": "LIM ZHI YAN", "class": "S2Y", "student_id": "22083", "order": 3},
    {"group": "夜曜组", "name_cn": "周柔慈", "name_en": "CHEO ROU ZHI", "class": "S2K", "student_id": "22051", "order": 4},
    {"group": "夜曜组", "name_cn": "林骏喨", "name_en": "LIM TEIK LIANG", "class": "J3T", "student_id": "24083", "order": 5},
    {"group": "夜曜组", "name_cn": "林宜彤", "name_en": "LIM YEE TONG", "class": "J2Y", "student_id": "25036", "order": 6},
    {"group": "夜曜组", "name_cn": "潘宛瑜", "name_en": "TRACY PHUAH WANYU", "class": "J2Y", "student_id": "25071", "order": 7},
    {"group": "夜曜组", "name_cn": "符传吉", "name_en": "FOO CHUAN JI", "class": "J2Y", "student_id": "25044", "order": 8},
    {"group": "夜曜组", "name_cn": "陈欣怡", "name_en": "CINDY TAN XIN YI", "class": "J2F", "student_id": "25058", "order": 9},
    {"group": "夜曜组", "name_cn": "丽亚", "name_en": "DHIYA ZULAIKHA DARWISYAH BINTI YUSNIZAN", "class": "J2F", "student_id": "25059", "order": 10},
    {"group": "夜曜组", "name_cn": "郑宜桐", "name_en": "TEH YEE THONG", "class": "J1Y", "student_id": "26024", "order": 11},
    {"group": "沧澜组", "name_cn": "浦源政", "name_en": "POH YUAN ZHENG", "class": "S2Y", "student_id": "22044", "order": 1},
    {"group": "沧澜组", "name_cn": "吴贝优", "name_en": "GOH BEI YO", "class": "S2Y", "student_id": "22021", "order": 2},
    {"group": "沧澜组", "name_cn": "林沛筠", "name_en": "LIM PEI JUN", "class": "S2Y", "student_id": "22030", "order": 3},
    {"group": "沧澜组", "name_cn": "陈诗惠", "name_en": "CHAN SHI HUI", "class": "S2FA", "student_id": "22017", "order": 4},
    {"group": "沧澜组", "name_cn": "郑憶欣", "name_en": "TEE YEE XIN", "class": "S1Y", "student_id": "23065", "order": 5},
    {"group": "沧澜组", "name_cn": "谢楷棋", "name_en": "CHEAH KHAI QI", "class": "S1T", "student_id": "23013", "order": 6},
    {"group": "沧澜组", "name_cn": "蔡善恩", "name_en": "CHUAH SHAN EN", "class": "J3F", "student_id": "24039", "order": 7},
    {"group": "沧澜组", "name_cn": "许家绮", "name_en": "KOO JIA QI", "class": "J2Y", "student_id": "25031", "order": 8},
    {"group": "沧澜组", "name_cn": "张子欣", "name_en": "TEON ZI XIN", "class": "J2F", "student_id": "25070", "order": 9},
    {"group": "沧澜组", "name_cn": "施锦轩", "name_en": "SEE JIN XUAN", "class": "J1T", "student_id": "26092", "order": 10},
]

# ===== 联课活动数据 =====
cca_data = [
    {"date": "2026-02-24", "activity": "活动顾问+总学长+副总学长", "activity_en": "Advisor + Head Prefect + Vice Head", "activity_ms": "Penasihat + Ketua Pengawas + Timbalan", "uniform": "校服"},
    {"date": "2026-02-26", "activity": "操步", "activity_en": "Marching", "activity_ms": "Kawad", "uniform": "体育衣"},
    {"date": "2026-03-03", "activity": "操步", "activity_en": "Marching", "activity_ms": "Kawad", "uniform": "体育衣"},
    {"date": "2026-03-05", "activity": "活动（文书+财政+查账）", "activity_en": "Activity (Secretary + Treasurer + Auditor)", "activity_ms": "Aktiviti (Setiausaha + Bendahari + Juruaudit)", "uniform": "校服"},
    {"date": "2026-03-10", "activity": "操步", "activity_en": "Marching", "activity_ms": "Kawad", "uniform": "体育衣"},
    {"date": "2026-03-12", "activity": "活动（行动组）", "activity_en": "Activity (Action Group)", "activity_ms": "Aktiviti (Kumpulan Tindakan)", "uniform": "校服"},
    {"date": "2026-03-17", "activity": "操步", "activity_en": "Marching", "activity_ms": "Kawad", "uniform": "体育衣"},
    {"date": "2026-03-31", "activity": "操步", "activity_en": "Marching", "activity_ms": "Kawad", "uniform": "体育衣"},
    {"date": "2026-04-02", "activity": "活动（值岗组）", "activity_en": "Activity (Duty Group)", "activity_ms": "Aktiviti (Kumpulan Bertugas)", "uniform": "校服"},
    {"date": "2026-04-07", "activity": "操步", "activity_en": "Marching", "activity_ms": "Kawad", "uniform": "体育衣"},
    {"date": "2026-04-09", "activity": "活动（督察组）", "activity_en": "Activity (Supervisory Group)", "activity_ms": "Aktiviti (Kumpulan Penyelia)", "uniform": "校服"},
    {"date": "2026-04-14", "activity": "操步", "activity_en": "Marching", "activity_ms": "Kawad", "uniform": "体育衣"},
    {"date": "2026-04-16", "activity": "活动（星穹组）", "activity_en": "Activity (Star Group)", "activity_ms": "Aktiviti (Kumpulan Bintang)", "uniform": "校服"},
    {"date": "2026-04-21", "activity": "操步", "activity_en": "Marching", "activity_ms": "Kawad", "uniform": "体育衣"},
    {"date": "2026-04-23", "activity": "活动（夜曜组）", "activity_en": "Activity (Moon Group)", "activity_ms": "Aktiviti (Kumpulan Bulan)", "uniform": "校服"},
    {"date": "2026-04-28", "activity": "操步", "activity_en": "Marching", "activity_ms": "Kawad", "uniform": "体育衣"},
    {"date": "2026-04-30", "activity": "活动（沧澜组）", "activity_en": "Activity (Ocean Group)", "activity_ms": "Aktiviti (Kumpulan Lautan)", "uniform": "校服"},
    {"date": "2026-05-05", "activity": "第一学期检讨", "activity_en": "First Semester Review", "activity_ms": "Semakan Semester Pertama", "uniform": "校服"},
    {"date": "2026-05-07", "activity": "操步", "activity_en": "Marching", "activity_ms": "Kawad", "uniform": "体育衣"},
]

# ===== 多语言数据 =====
languages = {
    "zh": {"title": "学长团分数板", "search": "搜姓名/班级/学号...", "download": "生成统计图", "dark": "深色", "footer": "双击切换深色 · 颜色越浅分数越高", "heat_low": "低分", "heat_high": "高分"},
    "en": {"title": "Prefects' Scoreboard", "search": "Search name/class/id...", "download": "Download Chart", "dark": "Dark", "footer": "Double tap for dark mode · Lighter = higher score", "heat_low": "Low", "heat_high": "High"}
}

def fetch_data():
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"
    for encoding in ['utf-8-sig', 'utf-8', 'latin1']:
        try:
            df = pd.read_csv(url, header=None, encoding=encoding)
            break
        except:
            continue
    else:
        raise Exception("无法读取 Google Sheets")
    
    student_id_col = None
    for i in range(min(15, len(df))):
        row = df.iloc[i].astype(str).tolist()
        for j, cell in enumerate(row):
            if '学号' in cell or 'ID' in cell:
                student_id_col = j
                data_start = i + 1
                break
        if student_id_col is not None:
            break
    
    if student_id_col is None:
        raise Exception("未找到学号列")
    
    dates = []
    header_row = df.iloc[data_start - 1].astype(str).tolist()
    for j in range(student_id_col + 1, len(header_row)):
        if header_row[j] and 'Unnamed' not in header_row[j]:
            val = header_row[j]
            dates.append(val[:10] if '00:00' in val else val)
    
    people = []
    for member in members_list:
        found = False
        for row_idx in range(data_start, len(df)):
            row = df.iloc[row_idx]
            if student_id_col < len(row) and str(row[student_id_col]).strip() == member['student_id']:
                total = 0
                score_dict = {}
                for j, date in enumerate(dates):
                    val = row[student_id_col + 1 + j] if student_id_col + 1 + j < len(row) else None
                    if pd.notna(val):
                        try:
                            num = float(val)
                            total += num
                            if num > 0:
                                score_dict[date] = num
                        except:
                            pass
                people.append({**member, "score_dict": score_dict, "total": total})
                found = True
                break
        if not found:
            print(f"警告: 未找到 {member['name_cn']} (学号:{member['student_id']})")
    
    return people, dates

def calculate_stats(people):
    groups = {}
    for p in people:
        groups.setdefault(p['group'], []).append(p)
    
    totals = {g: sum(p['total'] for p in members) for g, members in groups.items()}
    sorted_groups = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    rank_map = {g: i+1 for i, (g, _) in enumerate(sorted_groups)}
    
    for g, members in groups.items():
        avg = totals[g] / len(members)
        rank = rank_map[g]
        if rank == 1:
            for p in members:
                p['reward'] = 'P' if p['total'] >= avg / 2 else 'F'
        elif rank == 2:
            for p in members:
                p['reward'] = 'P' if p['total'] >= avg else 'F'
        else:
            top3 = sorted(members, key=lambda x: x['total'], reverse=True)[:3]
            top3_names = [t['name_cn'] for t in top3]
            for p in members:
                p['reward'] = 'P' if p['name_cn'] in top3_names else 'F'
    
    return groups, totals, rank_map

def generate_html(people, dates, groups, totals, rank_map):
    group_html = ""
    for group_name, members in groups.items():
        scores = [m['total'] for m in members]
        max_s = max(scores) if scores else 1
        min_s = min(scores) if scores else 0
        
        group_html += '<div class="group-card">'
        group_html += f'<div class="group-header"><div class="group-title">{group_name}</div><div class="group-badge">第{rank_map[group_name]}名</div></div>'
        group_html += '<div class="table-container"><table class="member-table"><thead><tr><th>#</th><th>姓名</th><th>班级</th><th>学号</th><th>总分</th><th>奖</th></tr></thead><tbody>'
        
        for m in members:
            if max_s > min_s:
                heat = int(((m['total'] - min_s) / (max_s - min_s)) * 8) + 1
                heat = min(9, max(1, heat))
            else:
                heat = 5
            reward_display = '✅' if m['reward'] == 'P' else '❌'
            group_html += f'<tr><td>{m["order"]}</td><td><div class="name-cn">{html.escape(m["name_cn"])}</div><div class="name-en">{html.escape(m["name_en"][:30])}</div></td><td>{m["class"]}</td><td>{m["student_id"]}</td><td><span class="total-heat" style="background: var(--heat-{heat});">{int(m["total"])}</span></td><td><span class="reward-{m["reward"]}">{reward_display}</span></td></tr>'
        
        group_html += '</tbody></table></div></div>'
    
    rank_cards = ''.join([f'<div class="rank-card" onclick="scrollToGroup(\'{g}\')"><div class="rank-score">{int(totals[g])}</div><div>{g}</div><div class="rank-note">第{rank_map[g]}名</div></div>' for g in totals.keys()])
    
    now = datetime.now().strftime('%m/%d %H:%M')
    
    html_content = f'''<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>学长团分数板</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        :root {{
            --bg: #f5f7fc; --card: white; --text: #1a2b3c; --text-light: #5a6b7a;
            --border: #e1e8f0; --heat-1: #083344; --heat-3: #155e75; --heat-5: #0284c7;
            --heat-7: #7dd3fc; --heat-9: #e0f2fe; --reward-P: #dcfce7; --reward-F: #fee2e2;
        }}
        body.night-mode {{
            --bg: #0f1825; --card: #1e2a3a; --text: #e6edf5; --text-light: #94a3b8;
            --border: #2d3a4d; --heat-1: #000814; --heat-3: #003566; --heat-5: #1a5a8a;
            --heat-7: #3a7aaa; --heat-9: #5a9aca; --reward-P: #1f4a3a; --reward-F: #562b2b;
        }}
        body {{ font-family: system-ui, sans-serif; background: var(--bg); color: var(--text); padding: 12px; transition: 0.2s; }}
        .container {{ max-width: 800px; margin: 0 auto; }}
        .header {{ background: var(--card); border-radius: 20px; padding: 16px; margin-bottom: 16px; }}
        .title {{ font-size: 1.5rem; font-weight: 600; margin-bottom: 12px; }}
        .toolbar {{ display: flex; gap: 8px; margin-bottom: 12px; flex-wrap: wrap; }}
        button {{ background: var(--card); border: 1px solid var(--border); border-radius: 30px; padding: 8px 16px; cursor: pointer; color: var(--text); }}
        .download-btn {{ background: #eab308; font-weight: 600; border: none; color: #1a2b3c; }}
        input {{ width: 100%; padding: 10px 16px; border: 1px solid var(--border); border-radius: 30px; background: var(--card); color: var(--text); }}
        .rank-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 20px; }}
        .rank-card {{ background: var(--card); border-radius: 16px; padding: 12px; text-align: center; cursor: pointer; }}
        .rank-score {{ font-size: 1.6rem; font-weight: 700; }}
        .rank-note {{ font-size: 0.7rem; color: var(--text-light); }}
        .group-card {{ background: var(--card); border-radius: 20px; padding: 16px; margin-bottom: 16px; }}
        .group-header {{ display: flex; justify-content: space-between; margin-bottom: 12px; padding-bottom: 8px; border-bottom: 1px solid var(--border); }}
        .group-title {{ font-size: 1.2rem; font-weight: 600; }}
        .group-badge {{ background: #eab308; padding: 2px 8px; border-radius: 20px; font-size: 0.8rem; color: #1a2b3c; }}
        .table-container {{ overflow-x: auto; }}
        .member-table {{ width: 100%; border-collapse: collapse; min-width: 500px; font-size: 0.85rem; }}
        .member-table th, .member-table td {{ padding: 8px 6px; text-align: left; border-bottom: 1px solid var(--border); }}
        .name-cn {{ font-weight: 600; }}
        .name-en {{ font-size: 0.65rem; color: var(--text-light); }}
        .total-heat {{ padding: 2px 8px; border-radius: 12px; font-weight: 600; color: white; }}
        .reward-P, .reward-F {{ padding: 2px 8px; border-radius: 12px; display: inline-block; min-width: 32px; text-align: center; }}
        .reward-P {{ background: var(--reward-P); color: #166534; }}
        .reward-F {{ background: var(--reward-F); color: #991b1b; }}
        body.night-mode .reward-P {{ color: #bbf7d0; }}
        body.night-mode .reward-F {{ color: #fecaca; }}
        .reminder-btn {{ position: fixed; bottom: 20px; right: 20px; background: #eab308; padding: 14px 24px; border-radius: 60px; font-weight: 600; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.2); color: #1a2b3c; }}
        .footer {{ margin-top: 20px; text-align: center; font-size: 0.7rem; color: var(--text-light); }}
    </style>
</head>
<body>
<div class="container">
    <div class="header">
        <div class="title">🏫 学长团分数板</div>
        <div class="toolbar">
            <button class="download-btn" onclick="alert(\'统计图功能开发中\')">📊 生成统计图</button>
            <button onclick="toggleLang()">🌐 语言</button>
            <button onclick="toggleTheme()">🌓 深色</button>
        </div>
        <input type="text" id="search" placeholder="🔍 搜姓名/班级/学号...">
        <div style="font-size:0.7rem; margin-top:8px; color:var(--text-light)">更新时间: {now}</div>
    </div>
    
    <div class="rank-grid" id="rankGrid">
        {rank_cards}
    </div>
    
    <div id="groupsContainer">
        {group_html}
    </div>
    
    <div class="reminder-btn" onclick="showTomorrow()">🔔 明天穿什么？</div>
    <div class="footer">👆 双击切换深色 · 颜色越浅分数越高 · 数据每日更新</div>
</div>

<script>
    const CCA = {json.dumps(cca_data, ensure_ascii=False)};
    let lang = 'zh';
    const texts = {json.dumps(languages, ensure_ascii=False)};
    
    function toggleTheme() {{
        document.body.classList.toggle('night-mode');
    }}
    
    function toggleLang() {{
        lang = lang === 'zh' ? 'en' : 'zh';
        document.querySelector('.title').innerHTML = '🏫 ' + texts[lang].title;
        document.querySelector('#search').placeholder = texts[lang].search;
        document.querySelector('.download-btn').innerHTML = '📊 ' + texts[lang].download;
        document.querySelector('.footer').innerHTML = texts[lang].footer;
    }}
    
    function showTomorrow() {{
        const tomorrow = new Date();
        tomorrow.setDate(tomorrow.getDate() + 1);
        const dateStr = tomorrow.toISOString().split('T')[0];
        const act = CCA.find(a => a.date === dateStr);
        if (act) {{
            alert('📅 明天(' + dateStr + ')\\n👕 穿: ' + act.uniform + '\\n📋 活动: ' + act.activity);
        }} else {{
            alert('📅 明天(' + dateStr + ')\\n✅ 没有联课活动');
        }}
    }}
    
    function scrollToGroup(group) {{
        const cards = document.querySelectorAll('.group-card');
        for (let card of cards) {{
            if (card.querySelector('.group-title').innerText === group) {{
                card.scrollIntoView({{ behavior: 'smooth' }});
                break;
            }}
        }}
    }}
    
    document.getElementById('search').addEventListener('input', (e) => {{
        const term = e.target.value.toLowerCase();
        const rows = document.querySelectorAll('.member-table tbody tr');
        for (let row of rows) {{
            const name = row.querySelector('.name-cn')?.innerText.toLowerCase() || '';
            const cls = row.children[2]?.innerText.toLowerCase() || '';
            row.style.display = name.includes(term) || cls.includes(term) ? '' : 'none';
        }}
    }});
    
    let lastTap = 0;
    document.addEventListener('touchstart', (e) => {{
        const now = Date.now();
        if (now - lastTap < 200) toggleTheme();
        lastTap = now;
    }});
    
    document.addEventListener('keydown', (e) => {{
        if (e.code === 'Space') {{
            e.preventDefault();
            toggleTheme();
        }}
    }});
    
    if (window.matchMedia('(prefers-color-scheme: dark)').matches) {{
        document.body.classList.add('night-mode');
    }}
</script>
</body>
</html>'''
    
    return html_content

def main():
    print("=" * 50)
    print("学长团分数板生成器")
    print("=" * 50)
    
    try:
        people, dates = fetch_data()
        print(f"✅ 找到 {len(people)} 位成员")
        
        groups, totals, rank_map = calculate_stats(people)
        
        html = generate_html(people, dates, groups, totals, rank_map)
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        
        print("✅ 已生成 index.html")
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        raise

if __name__ == "__main__":
    main()
