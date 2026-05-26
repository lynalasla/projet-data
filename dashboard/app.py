import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "processed", "jobs_clean.csv")

df = pd.read_csv(DATA_PATH)

df["title"] = df["title"].astype(str)
df["title_lower"] = df["title"].str.lower()

html = f"""
<!DOCTYPE html>
<html>
<head>
<script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>

<style>

:root {{
    --bg:#0B0F1A;
    --card:#111827;
    --text:#ffffff;
    --muted:#94A3B8;
    --accent:#FF4FA3;
}}

body.light {{
    --bg:#F5F7FB;
    --card:#ffffff;
    --text:#0F172A;
    --muted:#64748B;
}}

body {{
    margin:0;
    font-family:Arial;
    background:var(--bg);
    color:var(--text);
    transition:0.3s;
}}

/* HEADER */
.header {{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:14px 20px;
    background:var(--card);
}}

.header img {{
    height:45px;
}}

/* KPI */
.kpi {{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:10px;
    padding:12px;
}}

.kpi-box {{
    background:var(--card);
    padding:12px;
    border-radius:12px;
    text-align:center;
}}

/* FILTERS */
.filters {{
    display:flex;
    gap:10px;
    padding:12px;
    flex-wrap:wrap;
}}

select {{
    padding:8px;
    border-radius:8px;
    border:none;
    background:var(--card);
    color:var(--text);
}}

/* GRID */
.grid {{
    display:grid;
    grid-template-columns:repeat(2, 1fr);
    gap:14px;
    padding:14px;
}}

.card {{
    background:var(--card);
    border-radius:14px;
    padding:14px;
    min-height:420px;
}}

.title {{
    font-size:14px;
    font-weight:bold;
}}

.desc {{
    font-size:12px;
    color:var(--muted);
    margin-bottom:10px;
}}

.chart {{
    width:100%;
    height:340px;
}}

.insights {{
    background:var(--card);
    margin:14px;
    padding:14px;
    border-radius:12px;
    color:var(--muted);
    font-size:13px;
    line-height:1.5;
}}

button {{
    cursor:pointer;
    background:none;
    border:none;
    font-size:22px;
}}

</style>
</head>

<body>

<div class="header">
    <img id="logo" src="logo-dark.svg" />
    <button onclick="toggleTheme()" id="toggle">🌙</button>
</div>

<div class="kpi">
    <div class="kpi-box">Jobs<br>{len(df)}</div>
    <div class="kpi-box">Companies<br>{df['company'].nunique()}</div>
    <div class="kpi-box">Locations<br>{df['location'].nunique()}</div>
    <div class="kpi-box">Sources<br>{df['source'].nunique()}</div>
</div>

<div class="filters">
    <select id="city" onchange="filterData()">
        <option value="all">All cities</option>
        {''.join([f'<option>{c}</option>' for c in df["location"].dropna().unique()[:20]])}
    </select>

    <select id="company" onchange="filterData()">
        <option value="all">All companies</option>
        {''.join([f'<option>{c}</option>' for c in df["company"].dropna().unique()[:20]])}
    </select>
</div>

<div class="grid">

<div class="card">
<div class="title">Top Companies</div>
<div class="desc">Distribution des offres par entreprise</div>
<div id="c1" class="chart"></div>
</div>

<div class="card">
<div class="title">Top Locations</div>
<div class="desc">Répartition géographique des offres</div>
<div id="c2" class="chart"></div>
</div>

<div class="card">
<div class="title">Sources</div>
<div class="desc">Origine des données (Adzuna, Remotive...)</div>
<div id="c3" class="chart"></div>
</div>

<div class="card">
<div class="title">Job Levels</div>
<div class="desc">Répartition junior / mid / senior</div>
<div id="c4" class="chart"></div>
</div>

<div class="card">
<div class="title">Skills signals</div>
<div class="desc">Présence des compétences dans les titres</div>
<div id="c5" class="chart"></div>
</div>

<div class="card">
<div class="title">Title complexity</div>
<div class="desc">Longueur des intitulés de poste</div>
<div id="c6" class="chart"></div>
</div>

<div class="card">
<div class="title">Company share</div>
<div class="desc">Top 5 entreprises dominantes</div>
<div id="c7" class="chart"></div>
</div>

<div class="card">
<div class="title">Location share</div>
<div class="desc">Top 5 zones géographiques</div>
<div id="c8" class="chart"></div>
</div>

</div>

<div class="insights">
<b>Analyse & insights métiers :</b><br><br>

• Le marché est fortement concentré autour de quelques grandes entreprises (Capgemini, Mirakl, etc.).<br>
• Paris domine largement les opportunités, confirmant une centralisation du marché data.<br>
• Les niveaux mid et senior sont majoritaires → marché orienté expérience.<br>
• Les mentions AI/ML sont récurrentes → forte demande en IA générative et data science.<br>
• Peu de mentions explicites de skills techniques dans les titres → importance des compétences implicites.<br><br>

Objectif métier : identifier les zones de recrutement, les compétences recherchées et la structure du marché data.
</div>

<script>

let dark = true;
const data = {df.to_json(orient="records")};

function toggleTheme() {{
    dark = !dark;
    document.body.classList.toggle("light");

    document.getElementById("logo").src =
        dark ? "logo-dark.svg" : "logo-light.svg";

    document.getElementById("toggle").innerHTML =
        dark ? "🌙" : "☀️";

    render(data);
}}

function layout() {{
    return {{
        paper_bgcolor:"rgba(0,0,0,0)",
        plot_bgcolor:"rgba(0,0,0,0)",
        font:{{color: dark ? "#fff" : "#111"}},
        margin:{{t:20,l:40,r:20,b:80}}
    }}
}}

function fixLabels(arr) {{
    return arr.map(x => x.length > 18 ? x.slice(0,18) + "..." : x);
}}

function render(filtered) {{

    let comp={{}}, loc={{}}, src={{}}, lvl={{}};
    let skills={{python:0,sql:0,aws:0,ai:0}};

    filtered.forEach(d=>{{

        comp[d.company]=(comp[d.company]||0)+1;
        loc[d.location]=(loc[d.location]||0)+1;
        src[d.source]=(src[d.source]||0)+1;
        lvl[d.level]=(lvl[d.level]||0)+1;

        let t=d.title.toLowerCase();
        if(t.includes("python")) skills.python++;
        if(t.includes("sql")) skills.sql++;
        if(t.includes("aws")) skills.aws++;
        if(t.includes("ai")) skills.ai++;
    }});

    const cfg={{responsive:true, displayModeBar:false}};

    Plotly.newPlot("c1",[
        {{x:fixLabels(Object.keys(comp)), y:Object.values(comp), type:"bar"}}
    ],layout(),cfg);

    Plotly.newPlot("c2",[
        {{x:fixLabels(Object.keys(loc)), y:Object.values(loc), type:"bar"}}
    ],layout(),cfg);

    Plotly.newPlot("c3",[
        {{labels:Object.keys(src), values:Object.values(src), type:"pie"}}
    ],layout(),cfg);

    Plotly.newPlot("c4",[
        {{x:Object.keys(lvl), y:Object.values(lvl), type:"bar"}}
    ],layout(),cfg);

    Plotly.newPlot("c5",[
        {{x:Object.keys(skills), y:Object.values(skills), type:"bar"}}
    ],layout(),cfg);

    Plotly.newPlot("c6",[
        {{x:filtered.map(d=>d.title.length), type:"histogram"}}
    ],layout(),cfg);

    Plotly.newPlot("c7",[
        {{labels:fixLabels(Object.keys(comp).slice(0,5)),
          values:Object.values(comp).slice(0,5), type:"pie"}}
    ],layout(),cfg);

    Plotly.newPlot("c8",[
        {{labels:fixLabels(Object.keys(loc).slice(0,5)),
          values:Object.values(loc).slice(0,5), type:"pie"}}
    ],layout(),cfg);

}}

function filterData() {{
    const city=document.getElementById("city").value;
    const company=document.getElementById("company").value;

    let filtered=data;

    if(city!=="all") filtered=filtered.filter(d=>d.location===city);
    if(company!=="all") filtered=filtered.filter(d=>d.company===company);

    render(filtered);
}}

render(data);

</script>

</body>
</html>
"""

output_path = os.path.join(BASE_DIR, "dashboard.html")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print("DASHBOARD FINAL OK")