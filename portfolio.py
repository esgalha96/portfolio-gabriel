import streamlit as st

# ── Page config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Gabriel Esgalha · BI & Dados",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    background: #0b0f1a;
    color: #e8e4dc;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse 80% 50% at 20% -10%, rgba(99,102,241,0.18) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 110%, rgba(16,185,129,0.12) 0%, transparent 60%),
        #0b0f1a;
}

[data-testid="stHeader"], [data-testid="stToolbar"] { display: none !important; }
[data-testid="stSidebar"] { display: none !important; }

/* remove default top padding */
.block-container { padding-top: 0 !important; padding-bottom: 3rem !important; max-width: 1100px !important; }

/* ── Typography helpers ── */
.serif { font-family: 'DM Serif Display', serif; }

/* ── HERO ── */
.hero-wrap {
    padding: 80px 0 60px;
    border-bottom: 1px solid rgba(255,255,255,0.07);
    margin-bottom: 60px;
}
.hero-label {
    font-size: 0.72rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #6ee7b7;
    margin-bottom: 20px;
    font-weight: 500;
}
.hero-name {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(3rem, 6vw, 5rem);
    line-height: 1.05;
    color: #f0ece4;
    margin-bottom: 20px;
}
.hero-name span {
    font-style: italic;
    color: #818cf8;
}
.hero-tagline {
    font-size: 1.15rem;
    color: #9ca3af;
    font-weight: 300;
    max-width: 560px;
    line-height: 1.7;
    margin-bottom: 36px;
}
.hero-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 40px;
}
.badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 14px;
    border-radius: 100px;
    font-size: 0.8rem;
    font-weight: 500;
    letter-spacing: 0.02em;
}
.badge-green { background: rgba(16,185,129,0.12); color: #6ee7b7; border: 1px solid rgba(16,185,129,0.25); }
.badge-indigo { background: rgba(99,102,241,0.12); color: #a5b4fc; border: 1px solid rgba(99,102,241,0.25); }
.badge-amber { background: rgba(245,158,11,0.10); color: #fcd34d; border: 1px solid rgba(245,158,11,0.22); }

.hero-cta-row {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
}
.btn-primary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 12px 26px;
    background: linear-gradient(135deg, #6366f1, #4f46e5);
    color: #ffffff;
    text-decoration: none;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 700;
    transition: all .2s;
    box-shadow: 0 4px 20px rgba(99,102,241,0.35);
}
            
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 28px rgba(99,102,241,0.45); color: #ffffff; }
.btn-secondary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 12px 26px;
    background: rgba(255,255,255,0.08);
    color: #f0ece4;
    text-decoration: none;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 600;
    border: 1px solid rgba(255,255,255,0.22);
    transition: all .2s;
}
.btn-secondary:hover { background: rgba(255,255,255,0.14); color: #ffffff; transform: translateY(-2px); }

/* ── SECTION TITLES ── */
.section-label {
    font-size: 0.7rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: #6ee7b7;
    margin-bottom: 8px;
    font-weight: 500;
}
.section-title {
    font-family: 'DM Serif Display', serif;
    font-size: 2rem;
    color: #f0ece4;
    margin-bottom: 36px;
    line-height: 1.2;
}

/* ── CARD base ── */
.card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px;
    padding: 28px;
    transition: all .25s;
    height: 100%;
}
.card:hover {
    background: rgba(255,255,255,0.07);
    border-color: rgba(99,102,241,0.3);
    transform: translateY(-3px);
    box-shadow: 0 12px 40px rgba(0,0,0,0.3);
}

/* ── STATS ROW ── */
.stat-card {
    text-align: center;
    padding: 28px 20px;
}
.stat-number {
    font-family: 'DM Serif Display', serif;
    font-size: 2.6rem;
    color: #818cf8;
    line-height: 1;
    margin-bottom: 6px;
}
.stat-label {
    font-size: 0.82rem;
    color: #9ca3af;
    font-weight: 400;
}

/* ── EXPERIENCE ── */
.exp-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px;
    padding: 28px 32px;
    margin-bottom: 18px;
    position: relative;
    overflow: hidden;
    transition: all .25s;
}
.exp-card::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
    background: linear-gradient(180deg, #6366f1, #10b981);
    border-radius: 2px;
}
.exp-card:hover {
    background: rgba(255,255,255,0.07);
    border-color: rgba(99,102,241,0.25);
}
.exp-company {
    font-size: 0.72rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #6ee7b7;
    font-weight: 600;
    margin-bottom: 5px;
}
.exp-role {
    font-family: 'DM Serif Display', serif;
    font-size: 1.35rem;
    color: #f0ece4;
    margin-bottom: 5px;
}
.exp-period {
    font-size: 0.8rem;
    color: #6b7280;
    margin-bottom: 16px;
    font-weight: 400;
}
.exp-desc {
    font-size: 0.9rem;
    color: #9ca3af;
    line-height: 1.75;
    margin-bottom: 16px;
}
.exp-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 7px;
}
.tag {
    padding: 3px 10px;
    background: rgba(99,102,241,0.1);
    color: #a5b4fc;
    border: 1px solid rgba(99,102,241,0.2);
    border-radius: 6px;
    font-size: 0.73rem;
    font-weight: 500;
}

/* ── SKILLS ── */
.skill-section { margin-bottom: 28px; }
.skill-category {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    color: #6b7280;
    margin-bottom: 12px;
    font-weight: 500;
}
.skill-chips { display: flex; flex-wrap: wrap; gap: 8px; }
.chip {
    padding: 7px 14px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 8px;
    font-size: 0.83rem;
    color: #d1d5db;
    font-weight: 400;
    transition: all .2s;
    cursor: default;
}
.chip:hover {
    background: rgba(99,102,241,0.15);
    border-color: rgba(99,102,241,0.4);
    color: #a5b4fc;
}

/* ── CONTACT CARD ── */
.contact-item {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 16px;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    margin-bottom: 12px;
    transition: all .2s;
}
.contact-item:hover {
    background: rgba(99,102,241,0.08);
    border-color: rgba(99,102,241,0.25);
}
.contact-icon {
    width: 38px; height: 38px;
    background: rgba(99,102,241,0.15);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
    flex-shrink: 0;
}
.contact-label {
    font-size: 0.72rem;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 2px;
}
.contact-value {
    font-size: 0.9rem;
    color: #e8e4dc;
    font-weight: 400;
}

/* ── DIVIDER ── */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.08), transparent);
    margin: 56px 0;
}

/* ── CERT CARD ── */
.cert-card {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    padding: 18px;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    margin-bottom: 10px;
    transition: all .2s;
}
.cert-card:hover {
    background: rgba(16,185,129,0.06);
    border-color: rgba(16,185,129,0.2);
}
.cert-icon {
    width: 36px; height: 36px;
    background: rgba(16,185,129,0.15);
    border-radius: 9px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    flex-shrink: 0;
}

/* ── FOOTER ── */
.footer {
    text-align: center;
    padding: 40px 0 20px;
    border-top: 1px solid rgba(255,255,255,0.06);
    color: #4b5563;
    font-size: 0.82rem;
}
.footer span { color: #6366f1; }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
# HERO
# ═══════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero-wrap">
    <div class="hero-label">📍 Campinas, São Paulo</div>
    <div class="hero-name">Gabriel <span>Esgalha</span></div>
    <div class="hero-tagline">
        Especialista em BI e Análise Comercial Estratégica.
        Transformo dados complexos em decisões de negócio no setor imobiliário —
        com Power BI, Python e automações que reduzem custo operacional.
    </div>
    <div class="hero-badges">
        <span class="badge badge-green">📊 Power BI &amp; DAX</span>
        <span class="badge badge-indigo">🐍 Python · Machine Learning</span>
        <span class="badge badge-amber">🏗️ Setor Imobiliário</span>
        <span class="badge badge-green">⚙️ Automação de Processos</span>
        <span class="badge badge-indigo">💼 Salesforce · CRM</span>
    </div>
    <div class="hero-cta-row">
        <a class="btn-primary" href="https://www.linkedin.com/in/gabriel-esgalha" target="_blank" style="color: #ffffff;">🔗 LinkedIn</a>
        <a class="btn-secondary" href="mailto:gabrielesgalhar1@hotmail.com">✉️ Enviar e-mail</a>
        <a class="btn-primary" href="https://api.whatsapp.com/send?phone=5518997187131&text=Oi%2C+vim+pelo+seu+site%21" style="color: #ffffff;">
            📱 Enviar WhatsApp
        </a>
    </div>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
# STATS
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div class="section-label">Números</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Resultados em destaque</div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
stats = [
    ("8+", "Anos de experiência em dados"),
    ("3+", "ERPs e CRMs integrados"),
    ("15+", "Dashboards entregues"),
    ("6", "Empresas do setor imobiliário atendidas"),
]
cols = [c1, c2, c3, c4]
for col, (num, label) in zip(cols, stats):
    with col:
        st.markdown(f"""
        <div class="card stat-card">
            <div class="stat-number">{num}</div>
            <div class="stat-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)


st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
# SOBRE
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div class="section-label">Sobre</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Quem sou eu</div>', unsafe_allow_html=True)

col_text, col_gap, col_edu = st.columns([3, 0.3, 2])

with col_text:
    st.markdown("""
    <div class="card" style="padding: 32px; font-size: 0.95rem; line-height: 1.85; color: #b0b8c8;">
        <p style="margin-bottom: 16px;">
            Sou <strong style="color: #f0ece4;">Engenheiro Civil</strong> com especialização em 
            <strong style="color: #a5b4fc;">Business Intelligence e Análise Comercial</strong>.
            Atuo há mais de 8 anos transformando dados brutos em vantagem competitiva real para empresas do setor imobiliário.
        </p>
        <p style="margin-bottom: 16px;">
            Minha expertise combina <strong style="color: #6ee7b7;">modelagem técnica de dados</strong> com 
            visão de negócio estratégica, criando soluções que não apenas exibem números, mas orientam 
            decisões da liderança com precisão.
        </p>
        <p>
            Tenho experiência sólida com integrações de dados em múltiplos sistemas (Salesforce, Sienge, Sênior), 
            desenvolvimento de modelos preditivos em Python e construção de pipelines automatizados que 
            reduzem drasticamente o tempo operacional das equipes.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_edu:
    st.markdown("""
    <div class="card" style="padding: 28px;">
        <div style="font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.2em; color: #6b7280; margin-bottom: 16px; font-weight: 500;">🎓 Formação</div>
        <div style="margin-bottom: 24px;">
            <div style="font-family: 'DM Serif Display', serif; font-size: 1.05rem; color: #f0ece4; margin-bottom: 4px;">Engenharia Civil</div>
            <div style="font-size: 0.82rem; color: #6ee7b7; margin-bottom: 3px;">UNESP — Ilha Solteira</div>
            <div style="font-size: 0.78rem; color: #6b7280;">Bacharel · 2015 – 2019</div>
        </div>
        <div style="height: 1px; background: rgba(255,255,255,0.07); margin-bottom: 20px;"></div>
        <div style="font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.2em; color: #6b7280; margin-bottom: 14px; font-weight: 500;">📜 Certificações</div>
        <div class="cert-card">
            <div class="cert-icon">🏆</div>
            <div>
                <div style="font-size: 0.88rem; color: #e8e4dc; font-weight: 500;">Power BI Especialista</div>
                <div style="font-size: 0.75rem; color: #6b7280;">Certificação avançada</div>
            </div>
        </div>
        <div class="cert-card">
            <div class="cert-icon">📈</div>
            <div>
                <div style="font-size: 0.88rem; color: #e8e4dc; font-weight: 500;">Power BI: Do Zero ao Pro</div>
                <div style="font-size: 0.75rem; color: #6b7280;">Formação completa</div>
            </div>
        </div>
        <div class="cert-card">
            <div class="cert-icon">🌍</div>
            <div>
                <div style="font-size: 0.88rem; color: #e8e4dc; font-weight: 500;">The World of Concrete</div>
                <div style="font-size: 0.75rem; color: #6b7280;">Las Vegas · 2019</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════
# DESTAQUES / PROJETOS
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div class="section-label">Projetos</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Entregas de impacto</div>', unsafe_allow_html=True)

projects = [
    {
        "icon": "🔮",
        "title": "Sales Forecasting com Machine Learning",
        "desc": "Modelo preditivo de vendas em Python que antecipa tendências e suporta o planejamento estratégico da diretoria, com integração direta ao pipeline comercial.",
        "stack": "Python · Scikit-learn · Pandas · Power BI",
        "color": "#6366f1",
    },
    {
        "icon": "📡",
        "title": "Dashboard de Leads em Tempo Real",
        "desc": "Monitoramento em tempo real do funil comercial — da captação de leads à conversão — com controle de pastas CEF, performance por regional e ranking de corretores.",
        "stack": "Power BI · DAX · SQL · Salesforce",
        "color": "#10b981",
    },
    {
        "icon": "⚡",
        "title": "Automação de Extração de Dados",
        "desc": "Pipeline automatizado via SOQL/SQL que reduz drasticamente o tempo de resposta da operação, eliminando processos manuais repetitivos da equipe comercial.",
        "stack": "SOQL · SQL · Python · Power BI",
        "color": "#f59e0b",
    },
]

p1, p2, p3 = st.columns(3)
for col, proj in zip([p1, p2, p3], projects):
    with col:
        st.markdown(f"""
        <div class="card" style="padding: 28px; border-top: 3px solid {proj['color']}40;">
            <div style="font-size: 2rem; margin-bottom: 16px;">{proj['icon']}</div>
            <div style="font-family: 'DM Serif Display', serif; font-size: 1.1rem; color: #f0ece4; margin-bottom: 12px; line-height: 1.3;">{proj['title']}</div>
            <div style="font-size: 0.86rem; color: #9ca3af; line-height: 1.7; margin-bottom: 18px;">{proj['desc']}</div>
            <div style="font-size: 0.75rem; color: {proj['color']}; font-weight: 500; letter-spacing: 0.03em;">{proj['stack']}</div>
        </div>
        """, unsafe_allow_html=True)


st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════
# EXPERIÊNCIA
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div class="section-label">Carreira</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Experiência profissional</div>', unsafe_allow_html=True)

experiences = [
    {
        "company": "Pacaembu Construtora",
        "role": "Analista Comercial Estratégico Sênior",
        "period": "Out 2024 – Presente · São Paulo, SP",
        "desc": "Desenvolvimento de modelos de Sales Forecasting em Python para predição de vendas, antecipando tendências e suportando o planejamento estratégico da diretoria. Estruturação de dashboards em Power BI (M/DAX/SQL) para monitoramento em tempo real de leads e conversão. Controle de pastas por status (Aprovados/Reprovados CEF) e performance por empreendimento e regional. Automatização de extração de dados via SOQL/SQL, reduzindo tempo de resposta da operação.",
        "tags": ["Python", "Machine Learning", "Power BI", "DAX", "SQL", "SOQL", "Salesforce", "Sales Forecasting"],
    },
    {
        "company": "MoneyMio",
        "role": "Cofundador",
        "period": "Abr 2024 – Dez 2025 · Remoto",
        "desc": "Cofundação de startup com foco em soluções financeiras. Atuação estratégica e técnica no desenvolvimento do produto, integrando expertise em dados e visão de negócio.",
        "tags": ["Empreendedorismo", "Produto", "BI", "Estratégia"],
    },
    {
        "company": "BRNPAR Empreendimentos Imobiliários",
        "role": "Analista de Planejamento",
        "period": "Fev 2023 – Out 2024 · Araras, SP",
        "desc": "Coleta, modelagem e tratamento de dados para suporte ao planejamento estratégico. Desenvolvimento de relatórios, dashboards e monitoramento de KPIs. Automação de processos, planejamento financeiro e análise de viabilidade de empreendimentos. Gerenciamento de projetos de BI e treinamento de equipes.",
        "tags": ["Power BI", "Excel", "Python", "KPIs", "Planejamento Financeiro", "Viabilidade"],
    },
    {
        "company": "brio Incorporadora",
        "role": "Analista de Planejamento & Controle PL",
        "period": "Dez 2022 – Fev 2023",
        "desc": "Atuação em planejamento e controle de projetos imobiliários, com análise de indicadores e suporte à gestão estratégica.",
        "tags": ["Planejamento", "Controle", "BI"],
    },
    {
        "company": "BRNPAR Empreendimentos Imobiliários",
        "role": "Analista de Controladoria",
        "period": "Jan 2021 – Out 2022 · Araras, SP",
        "desc": "Análise e controle financeiro com foco em dados operacionais. Suporte à controladoria com relatórios gerenciais e indicadores de desempenho.",
        "tags": ["Controladoria", "Excel", "ERP Sienge", "Relatórios Gerenciais"],
    },
    {
        "company": "Soft-line Soluções em Sistemas",
        "role": "Programador Web",
        "period": "Mai 2020 – Jan 2021 · Araçatuba, SP",
        "desc": "Desenvolvimento de sistemas web e automações. Criação de interfaces e integração de dados entre plataformas.",
        "tags": ["Web", "Full Stack", "Automação"],
    },
]

for exp in experiences:
    tags_html = "".join([f'<span class="tag">{t}</span>' for t in exp["tags"]])
    st.markdown(f"""
    <div class="exp-card">
        <div class="exp-company">{exp["company"]}</div>
        <div class="exp-role">{exp["role"]}</div>
        <div class="exp-period">📅 {exp["period"]}</div>
        <div class="exp-desc">{exp["desc"]}</div>
        <div class="exp-tags">{tags_html}</div>
    </div>
    """, unsafe_allow_html=True)


st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
# HABILIDADES
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div class="section-label">Stack</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Habilidades & Tecnologias</div>', unsafe_allow_html=True)

col_skills1, col_skills2 = st.columns(2)

skills_left = {
    "📊 Business Intelligence": ["Power BI", "DAX", "Power Query (M)", "Data Modeling", "KPIs & Métricas"],
    "🐍 Linguagens & Dados": ["Python", "SQL", "SOQL", "Pandas", "Scikit-learn"],
    "🤖 Machine Learning": ["Sales Forecasting", "Modelos Preditivos", "Análise de Séries Temporais"],
}

skills_right = {
    "🏢 CRM & ERP": ["Salesforce", "CRM Multidados", "Sienge (ERP)", "Sênior (ERP)"],
    "⚙️ Automação & Web": ["Automação de Processos", "Full Stack Web", "Integração de Dados"],
    "📁 Produtividade": ["Excel Avançado", "Google Sheets", "Office 365"],
}

def build_skills_html(skills_dict):
    inner = ""
    for cat, items in skills_dict.items():
        chips = "".join([
            f'<span style="padding:7px 14px; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:8px; font-size:0.83rem; color:#d1d5db; font-family:DM Sans,sans-serif; display:inline-block;">{s}</span>'
            for s in items
        ])
        inner += (
            '<div style="margin-bottom:22px;">'
            f'<div style="font-size:0.7rem; text-transform:uppercase; letter-spacing:0.2em; color:#6b7280; margin-bottom:10px; font-weight:500; font-family:DM Sans,sans-serif;">{cat}</div>'
            f'<div style="display:flex; flex-wrap:wrap; gap:8px;">{chips}</div>'
            '</div>'
        )
    return (
        '<div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); '
        'border-radius:14px; padding:28px;">' + inner + '</div>'
    )

with col_skills1:
    st.markdown(build_skills_html(skills_left), unsafe_allow_html=True)

with col_skills2:
    st.markdown(build_skills_html(skills_right), unsafe_allow_html=True)


st.markdown('<div class="divider"></div>', unsafe_allow_html=True)



# ═══════════════════════════════════════════════════════════════════
# CONTATO
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div class="section-label">Contato</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Vamos conversar?</div>', unsafe_allow_html=True)

col_contact, col_cta = st.columns([2, 1.5])

with col_contact:
    st.markdown("""
    <div class="contact-item">
        <div class="contact-icon">✉️</div>
        <div>
            <div class="contact-label">E-mail</div>
            <div class="contact-value">gabrielesgalhar1@hotmail.com</div>
        </div>
    </div>
    <div class="contact-item">
        <div class="contact-icon">🔗</div>
        <div>
            <div class="contact-label">LinkedIn</div>
            <div class="contact-value">linkedin.com/in/gabriel-esgalha</div>
        </div>
    </div>
    <div class="contact-item">
        <div class="contact-icon">📍</div>
        <div>
            <div class="contact-label">Localização</div>
            <div class="contact-value">Campinas, São Paulo</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_cta:
    st.markdown("""
    <div class="card" style="padding: 32px; text-align: center;">
        <div style="font-family: 'DM Serif Display', serif; font-size: 1.3rem; color: #f0ece4; margin-bottom: 12px; line-height: 1.3;">
            Pronto para transformar dados em resultados?
        </div>
        <div style="font-size: 0.86rem; color: #9ca3af; margin-bottom: 24px; line-height: 1.6;">
            Estou disponível para conversar sobre BI, automação e análise estratégica.
        </div>
        <a class="btn-primary" href="https://api.whatsapp.com/send?phone=5518997187131&text=Oi%2C+vim+pelo+seu+site%21" style="display: inline-flex; justify-content: center; width: 100%; color: #ffffff;">
            📱 Enviar WhatsApp
        </a>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════
st.markdown("""
<div class="footer">
    Feito por <span>Gabriel Esgalha</span> · 2026 &nbsp;·&nbsp; 
    BI · Python · Power BI · Setor Imobiliário
</div>
""", unsafe_allow_html=True)
