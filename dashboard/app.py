import os
import pandas as pd

# Je récupère le chemin du fichier depuis n'importe où sur la machine
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "processed", "jobs_clean.csv")

df = pd.read_csv(DATA_PATH)

# Je m'assure que les titres sont bien en string avant de les manipuler
df["title"] = df["title"].astype(str)
df["title_lower"] = df["title"].str.lower()

html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>

<style>

/* Mes variables CSS pour gérer le thème dark/light facilement */
:root {{
    --bg:#0B0F1A;
    --card:#111827;
    --text:#ffffff;
    --muted:#94A3B8;
    --accent:#FF4FA3;
    --border:#1F2937;
}}

/* Je surcharge les variables quand l'utilisateur passe en mode clair */
body.light {{
    --bg:#F5F7FB;
    --card:#ffffff;
    --text:#0F172A;
    --muted:#64748B;
    --border:#E2E8F0;
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
    padding:18px 24px;
    background:var(--card);
    border-bottom:1px solid var(--border);
    /* Je le mets en sticky pour qu'il reste visible en scrollant */
    position:sticky;
    top:0;
    z-index:100;
}}

.header img {{
    height:48px;
}}

button {{
    cursor:pointer;
    background:none;
    border:none;
    font-size:22px;
    color:var(--text);
}}

/* HERO */

.hero {{
    padding:30px 24px 10px;
}}

.hero h1 {{
    margin:0;
    font-size:30px;
}}

.hero p {{
    color:var(--muted);
    max-width:900px;
    line-height:1.7;
}}

/* KPI */

/* 4 colonnes égales pour les cartes KPI */
.kpi {{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:16px;
    padding:20px 24px;
}}

.kpi-box {{
    background:var(--card);
    padding:22px;
    border-radius:18px;
    border:1px solid var(--border);
}}

.kpi-title {{
    color:var(--muted);
    font-size:13px;
    margin-bottom:10px;
}}

.kpi-value {{
    font-size:28px;
    font-weight:bold;
}}

/* FILTERS */

.filters {{
    display:flex;
    gap:12px;
    padding:0 24px 24px;
    flex-wrap:wrap;
}}

select {{
    padding:12px;
    border-radius:10px;
    border:1px solid var(--border);
    background:var(--card);
    color:var(--text);
    min-width:230px;
}}

/* GRID */

/* 2 graphiques côte à côte */
.grid {{
    display:grid;
    grid-template-columns:repeat(2, 1fr);
    gap:18px;
    padding:0 24px 24px;
}}

.card {{
    background:var(--card);
    border-radius:18px;
    padding:18px;
    border:1px solid var(--border);
}}

.title {{
    font-size:18px;
    font-weight:bold;
    margin-bottom:8px;
}}

.desc {{
    font-size:13px;
    color:var(--muted);
    line-height:1.6;
    margin-bottom:14px;
}}

.chart {{
    width:100%;
    height:420px;
}}

/* INSIGHTS */

.insights {{
    background:var(--card);
    margin:0 24px 30px;
    padding:22px;
    border-radius:18px;
    border:1px solid var(--border);
}}

.insights h2 {{
    margin-top:0;
}}

.insights ul {{
    padding-left:20px;
    line-height:1.9;
    color:var(--muted);
}}

.footer {{
    padding:0 24px 40px;
    color:var(--muted);
    font-size:13px;
    line-height:1.7;
}}

/* Responsive : je passe en 1 colonne sous 1100px */
@media(max-width:1100px) {{

    .grid {{
        grid-template-columns:1fr;
    }}

    .kpi {{
        grid-template-columns:repeat(2,1fr);
    }}
}}

/* Sur mobile je simplifie encore plus */
@media(max-width:700px) {{

    .kpi {{
        grid-template-columns:1fr;
    }}

    .hero h1 {{
        font-size:22px;
    }}
}}

</style>
</head>

<body>

<div class="header">
    <img id="logo" src="logo-dark.svg" />
    <button onclick="toggleTheme()" id="toggle">🌙</button>
</div>

<div class="hero">
    <h1>Data Jobs Market Analysis Dashboard</h1>

    <p>
        Ce dashboard présente une analyse des offres d'emploi Data collectées
        depuis plusieurs plateformes. L'objectif est d'identifier les tendances
        du marché, les entreprises qui recrutent, les localisations dominantes,
        les niveaux d'expérience recherchés ainsi que les compétences les plus
        demandées.
    </p>
</div>

<div class="kpi">

    <!-- Statistiques globales calculées directement depuis le DataFrame -->
    <div class="kpi-box">
        <div class="kpi-title">Total Jobs</div>
        <div class="kpi-value">{len(df)}</div>
    </div>

    <div class="kpi-box">
        <div class="kpi-title">Companies</div>
        <div class="kpi-value">{df['company'].nunique()}</div>
    </div>

    <div class="kpi-box">
        <div class="kpi-title">Locations</div>
        <div class="kpi-value">{df['location'].nunique()}</div>
    </div>

    <div class="kpi-box">
        <div class="kpi-title">Sources</div>
        <div class="kpi-value">{df['source'].nunique()}</div>
    </div>

</div>

<div class="filters">

    <!-- Je limite à 20 options pour ne pas surcharger les dropdowns -->
    <select id="city" onchange="filterData()">
        <option value="all">All locations</option>
        {''.join([f'<option>{c}</option>' for c in df["location"].dropna().unique()[:20]])}
    </select>

    <select id="company" onchange="filterData()">
        <option value="all">All companies</option>
        {''.join([f'<option>{c}</option>' for c in df["company"].dropna().unique()[:20]])}
    </select>

</div>

<div class="grid">

<div class="card">
    <div class="title">Top Recruiting Companies</div>

    <div class="desc">
        Cette visualisation montre les entreprises publiant le plus d'offres.
        Elle permet d'identifier les principaux recruteurs du marché Data.
    </div>

    <div id="c1" class="chart"></div>
</div>

<div class="card">
    <div class="title">Top Job Locations</div>

    <div class="desc">
        Analyse géographique des opportunités afin d'identifier les zones où la
        demande en profils Data est la plus forte.
    </div>

    <div id="c2" class="chart"></div>
</div>

<div class="card">
    <div class="title">Data Sources Distribution</div>

    <div class="desc">
        Répartition des offres selon les plateformes utilisées pour la collecte
        des données.
    </div>

    <div id="c3" class="chart"></div>
</div>

<div class="card">
    <div class="title">Experience Levels</div>

    <div class="desc">
        Comparaison des niveaux d'expérience demandés dans les offres :
        junior, mid et senior.
    </div>

    <div id="c4" class="chart"></div>
</div>

<div class="card">
    <div class="title">Skills Detection</div>

    <div class="desc">
        Détection des compétences mentionnées dans les titres des offres afin
        d'identifier les technologies les plus visibles.
    </div>

    <div id="c5" class="chart"></div>
</div>

<div class="card">
    <div class="title">Job Title Complexity</div>

    <div class="desc">
        Distribution de la longueur des intitulés de poste. Cette analyse aide
        à comprendre la complexité et la spécialisation des rôles proposés.
    </div>

    <div id="c6" class="chart"></div>
</div>

<div class="card">
    <div class="title">Top Companies Share</div>

    <div class="desc">
        Part des principales entreprises dans l'ensemble des offres collectées.
    </div>

    <div id="c7" class="chart"></div>
</div>

<div class="card">
    <div class="title">Top Locations Share</div>

    <div class="desc">
        Répartition des offres entre les principales zones géographiques.
    </div>

    <div id="c8" class="chart"></div>
</div>

</div>

<div class="insights">

<h2>Business Insights</h2>

<ul>

<li>
Le marché est fortement concentré autour de quelques entreprises majeures
comme Capgemini, Mirakl et plusieurs sociétés spécialisées IA/Data.
</li>

<li>
Paris représente la localisation dominante, ce qui confirme la centralisation
des opportunités Data en Île-de-France.
</li>

<li>
Les postes Mid et Senior sont majoritaires, montrant que les entreprises
recherchent principalement des profils expérimentés.
</li>

<li>
Les termes liés à l'IA, au Machine Learning et à l'AI Engineering apparaissent
fréquemment, indiquant une montée importante des besoins en IA générative.
</li>

<li>
Les plateformes Adzuna et Remotive permettent de combiner marché local et
opportunités internationales remote.
</li>

<li>
Les intitulés de postes deviennent plus spécialisés et hybrides :
AI Engineer, GenAI, NLP, Data Scientist Senior, etc.
</li>

</ul>

</div>

<div class="insights">

<h2>Méthodologie</h2>

<ul>
<li>Collecte des données depuis plusieurs APIs et plateformes d'emploi.</li>
<li>Transformation et nettoyage des données avec Pandas.</li>
<li>Stockage et préparation des données pour l'analyse.</li>
<li>Visualisation interactive avec Plotly.</li>
<li>Création d'un dashboard analytique HTML dynamique.</li>
</ul>

</div>

<div class="footer">

<b>Objectif métier :</b><br><br>

Ce dashboard aide à comprendre les tendances du marché Data afin de :
identifier les entreprises qui recrutent, cibler les compétences demandées,
analyser les zones géographiques stratégiques et suivre l'évolution des
besoins autour de l'IA et de la Data Science.

</div>

<script>

let dark = true;

// Je charge toutes les données une seule fois au démarrage
const data = {df.to_json(orient="records")};

function toggleTheme() {{

    dark = !dark;

    document.body.classList.toggle("light");

    // Je change le logo selon le thème
    document.getElementById("logo").src =
        dark ? "logo-dark.svg" : "logo-light.svg";

    document.getElementById("toggle").innerHTML =
        dark ? "🌙" : "☀️";

    // Je re-render les graphiques pour mettre à jour les couleurs
    render(data);
}}

// Je centralise les options Plotly pour garder un style cohérent
function layout() {{

    return {{

        paper_bgcolor:"rgba(0,0,0,0)",
        plot_bgcolor:"rgba(0,0,0,0)",

        font:{{
            color: dark ? "#fff" : "#111",
            size:12
        }},

        margin:{{
            t:30,
            l:60,
            r:30,
            b:120
        }},

        xaxis:{{
            tickangle:-35,
            automargin:true
        }},

        yaxis:{{
            automargin:true
        }}
    }}
}}

// Je tronque les labels trop longs pour éviter que ça déborde
function shorten(arr) {{

    return arr.map(x =>
        x.length > 20 ? x.slice(0,20) + "..." : x
    );
}}

// Je trie par valeur décroissante et je prends les N premiers
function topEntries(obj, limit=8) {{

    return Object.entries(obj)
        .sort((a,b)=>b[1]-a[1])
        .slice(0,limit);
}}

function render(filtered) {{

    let comp={{}};
    let loc={{}};
    let src={{}};
    let lvl={{}};

    // Je cherche les skills directement dans les titres de poste
    let skills={{
        python:0,
        sql:0,
        aws:0,
        ai:0
    }};

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

    const cfg={{
        responsive:true,
        displayModeBar:false
    }};

    const topComp = topEntries(comp);
    const topLoc = topEntries(loc);

    // Graphique 1 : top entreprises
    Plotly.newPlot("c1",[{{

        x:shorten(topComp.map(x=>x[0])),
        y:topComp.map(x=>x[1]),
        type:"bar"

    }}],layout(),cfg);

    // Graphique 2 : top localisations
    Plotly.newPlot("c2",[{{

        x:shorten(topLoc.map(x=>x[0])),
        y:topLoc.map(x=>x[1]),
        type:"bar"

    }}],layout(),cfg);

    // Graphique 3 : répartition des sources en donut
    Plotly.newPlot("c3",[{{

        labels:Object.keys(src),
        values:Object.values(src),
        type:"pie",
        hole:.45

    }}],layout(),cfg);

    // Graphique 4 : niveaux d'expérience
    Plotly.newPlot("c4",[{{

        x:Object.keys(lvl),
        y:Object.values(lvl),
        type:"bar"

    }}],layout(),cfg);

    // Graphique 5 : skills détectés dans les titres
    Plotly.newPlot("c5",[{{

        x:Object.keys(skills),
        y:Object.values(skills),
        type:"bar"

    }}],layout(),cfg);

    // Graphique 6 : histogramme de la longueur des titres
    Plotly.newPlot("c6",[{{

        x:filtered.map(d=>d.title.length),
        type:"histogram"

    }}],layout(),cfg);

    // Graphiques 7 & 8 : parts de marché top 5 entreprises et localisations
    Plotly.newPlot("c7",[{{

        labels:shorten(topComp.slice(0,5).map(x=>x[0])),
        values:topComp.slice(0,5).map(x=>x[1]),
        type:"pie"

    }}],layout(),cfg);

    Plotly.newPlot("c8",[{{

        labels:shorten(topLoc.slice(0,5).map(x=>x[0])),
        values:topLoc.slice(0,5).map(x=>x[1]),
        type:"pie"

    }}],layout(),cfg);
}}

// Filtrage dynamique selon ville et entreprise sélectionnées
function filterData() {{

    const city = document.getElementById("city").value;
    const company = document.getElementById("company").value;

    let filtered = data;

    if(city !== "all") {{
        filtered = filtered.filter(d=>d.location===city);
    }}

    if(company !== "all") {{
        filtered = filtered.filter(d=>d.company===company);
    }}

    render(filtered);
}}

// Premier rendu au chargement de la page
render(data);

</script>

</body>
</html>
"""

# Je génère le fichier HTML dans le même dossier que ce script
output_path = os.path.join(BASE_DIR, "dashboard.html")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print("DASHBOARD FINAL OK")