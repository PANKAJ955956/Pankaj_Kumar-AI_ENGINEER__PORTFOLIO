GH="https://github.com/PANKAJ955956/"
LI="https://www.linkedin.com/in/pankaj-kumar-472a29294/"
PAGES=[("index.html","Home"),("about.html","About"),("experience.html","Experience"),("projects.html","Projects"),("certifications.html","Certifications"),("achievements.html","Achievements"),("contact.html","Contact")]
def chips(l):return '<div class="chips">'+''.join(f'<span class="chip">{x}</span>' for x in l)+'</div>'
def shell(fn,title,body,head=""):
    nav=''.join(f'<li><a href="{f}"{" class=on aria-current=page" if f==fn else ""}>{n}</a></li>' for f,n in PAGES)
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Pankaj Kumar – AI Engineer</title>
<meta name="description" content="Pankaj Kumar – AI/ML Engineer specialising in Generative AI, RAG, LLMs, agentic AI and MCP, with a data science and analytics foundation.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Sora:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css"></head><body>
<header><div class="wrap nav"><a class="brand" href="index.html">Pankaj<span>.ai</span></a>
<button class="burger" aria-label="Menu" aria-expanded="false">☰</button><nav aria-label="Main"><ul>{nav}</ul></nav></div></header>
<main>{body}</main>
<footer><div class="wrap"><span>© 2026 Pankaj Kumar. Built for GitHub Pages.</span><span><a href="{GH}">GitHub</a> · <a href="{LI}">LinkedIn</a> · <a href="https://leetcode.com/u/PankajKumar_DS/">LeetCode</a></span></div></footer>
<script src="js/main.js"></script></body></html>'''
def head(t,p):return f'<div class="page-head"><div class="wrap"><h1>{t}</h1><p>{p}</p></div></div>'

# ---- data
PROJ=[
("Customer Support Copilot","genai","Enterprise assistant that answers support queries with RAG, LangGraph agent workflows and persistent conversation memory.",["RAG","LangGraph","LangChain","Vector DB"],"AI-Powered-Customer-Support-Copilot"),
("ResearchMind AI","genai agents","Multi-agent research system: a LangGraph pipeline plans questions, searches the web, analyses findings against your own PDFs, and writes a report.",["LangGraph","Agents","RAG","Python"],"ResearchMind-AI"),
("QuizGen AI","genai","Turns PDF/DOCX/TXT notes into grounded, difficulty-controlled MCQ quizzes with a full RAG pipeline (parse, chunk, embed, retrieve, generate).",["RAG","ChromaDB","FastAPI","Streamlit"],"QuizGen-AI-Intelligent-Study-Notes-Quiz-Generator"),
("AI Coding & Interview Copilot","genai","Resume analysis, AI code review, voice mock interviews and adaptive feedback in one interview-prep platform.",["LLMs","RAG","FastAPI","React"],"AI-coding-interview-copilot"),
("Accessibility Captioning","genai","Real-time captioning with speaker diarization, plus RAG-based lecture summaries, key takeaways, definitions and action items.",["ASR","Diarization","RAG"],"Ai-powered-accessibility-captioning"),
("Multimodal Misinformation Detector","genai ml","Scores news claims by analysing text and images together with a PyTorch fusion model behind a FastAPI service.",["PyTorch","Multimodal","FastAPI","React"],"multimodal-misinformation-news-detector"),
("Policy & Process RAG System","genai","Search and question answering over organisational policies with source-cited answers.",["RAG","LLMs","Python"],"AI-Powered-Policy-Process-Management-System-using-RAG"),
("Worldometer RAG Chatbot","genai","Chatbot for global statistics built on Worldometer data, Flask, LangChain and ChromaDB.",["LangChain","ChromaDB","Flask"],"Worldometer-AI-RAG-Based-Global-Statistics-Chatbot"),
("Intelligent Video Analytics","cv","Real-time webcam/CCTV platform combining OpenCV preprocessing, YOLOv8 detection and multi-object tracking.",["YOLOv8","OpenCV","Tracking"],"Intelligent-Video-Analytics-System"),
("Intelligent Driving Assistant","cv","Lane detection, traffic sign and signal recognition, object tracking and risk assessment in one pipeline.",["Computer Vision","YOLO","Python"],"AI-Powered-Intelligent-Driving-Assistant"),
("PPE Detection for Worker Safety","cv","Real-time computer vision and compliance engine for industrial safety monitoring.",["YOLO","Computer Vision"],"PPE-Detection-for-Industrial-Worker-Safety"),
("Predictive Maintenance Digital Twin","ml","Equipment failure forecasting, anomaly detection, remaining-useful-life estimation and digital twin simulation.",["Anomaly Detection","RUL","Simulation"],"predictive-maintenance-digital-twin"),
("Global Disease Outbreak Forecasting","ml","Early-warning system for outbreaks using machine learning and deep learning.",["ML","Deep Learning","Forecasting"],"Global-Disease-Outbreak-Forecasting-System"),
("AI Health Risk Prediction","ml","Predicts diabetes, heart disease and lung risk with a React + Flask app and analytics dashboard.",["Scikit-learn","Flask","React"],"AI-Health-Risk-Prediction-Platform"),
("AI Career Mentor for Students","genai ml","Analyses profiles and resumes to recommend career paths, placement readiness and skill gaps.",["NLP","ML","Python"],"AI-Career-Mentor-for-Students"),
("ECHO Virtual Eco-Herbal Garden","cv","Award-winning AYUSH platform: YOLOv8 plant recognition, therapy recommendations, multilingual voice interaction. Published research.",["YOLOv8","Full-stack","Voice"],"Virtual-Eco-Herbal-Garden-2.0"),
("Krishi Mitra AI","cv","Offline-first multimodal assistant that helps farmers diagnose crop health.",["Multimodal","Offline-first"],"KRISHI_MITRA_AI"),
("iTunes Music Store Analysis","data","SQL, Python, Power BI and Tableau analysis to find revenue gaps.",["SQL","Power BI","Tableau"],"Itune_Music_Store_DataAnalysis"),
("Sales Forecast – Time Series","data ml","Retail sales forecasting with multiple ML and time-series models.",["Time Series","Scikit-learn"],"-Sales-Forecast--Time-Series-Forecasting"),
("Customer Segmentation","data ml","Clustering model that groups customers to target financial products.",["KMeans","Clustering"],"Customer-Segmentation-using-clustering-model"),
("UrbanThreads Q4 Analysis","data","Sales and returns analysis with Pandas, Excel and a business insights report.",["Pandas","EDA","Excel"],"urbanthreads-q4-data-analysis"),
]
def pcard(p,feat=False):
    n,c,d,t,r=p
    return f'<article class="card" data-cat="{c}"><h3>{n}</h3><p>{d}</p>{chips(t)}<div class="links"><a href="{GH}{r}">View code</a></div></article>'

# ---- HOME
home=f'''<section class="hero"><div class="wrap"><div class="hero-grid"><div>
<h1>Hi, I'm Pankaj Kumar.</h1>
<p class="role">I build <b id="typed" data-words='["RAG applications","agentic AI workflows","LLM-powered products","MCP-connected tools","computer vision systems"]'>RAG applications</b></p>
<p class="lead">AI/ML Engineer at TheSmartBridge, working on Generative AI, retrieval-augmented generation and multi-agent systems. My base is data science and analytics, so I care about evaluation, data quality and shipping things that work.</p>
<div class="btns"><a class="btn pri" href="projects.html">See my projects</a><a class="btn sec" href="contact.html">Get in touch</a><a class="btn sec" href="{LI}">LinkedIn</a></div></div>
<div class="photo"><img src="images/profile.jpg" alt="Portrait of Pankaj Kumar"><span class="tag">Open to AI/ML roles · Delhi NCR</span></div></div>
<div class="stats"><div class="stat"><b>20+</b><span>AI/ML projects on GitHub</span></div><div class="stat"><b>34</b><span>Licenses &amp; certifications</span></div><div class="stat"><b>#1</b><span>Branch topper, B.Tech CSE (DS)</span></div><div class="stat"><b>3</b><span>Talks &amp; conference presentations</span></div></div></div></section>
<section><div class="wrap"><div class="sh"><h2>What I work on</h2><p>Four areas, with GenAI as the main focus.</p></div>
<div class="grid g2">
<div class="card"><h3>Generative AI &amp; RAG</h3><p>Document ingestion, chunking, embeddings, retrieval and grounded generation with source citations.</p>{chips(["LLMs","LangChain","ChromaDB","FAISS"])}</div>
<div class="card"><h3>Agentic AI &amp; MCP</h3><p>Multi-agent pipelines with planning, tool use, memory, and MCP connectors to external tools and data.</p>{chips(["LangGraph","Agents","MCP","Tool use"])}</div>
<div class="card"><h3>Computer vision &amp; multimodal</h3><p>Detection, tracking and text-plus-image models for safety, agriculture and misinformation.</p>{chips(["YOLOv8","OpenCV","PyTorch"])}</div>
<div class="card"><h3>Data science &amp; analytics</h3><p>EDA, feature engineering, forecasting and dashboards that turn data into decisions.</p>{chips(["SQL","Pandas","Power BI","Tableau"])}</div></div></div></section>
<section class="alt"><div class="wrap"><div class="sh"><h2>Featured projects</h2></div><div class="grid g3">{''.join(pcard(p) for p in PROJ[:3])}</div><p style="margin-top:22px"><a href="projects.html"><b>All projects</b></a></p></div></section>'''

# ---- ABOUT
def sk(t,l):return f'<div class="card"><h3>{t}</h3>{chips(l)}</div>'
about=head("About","AI engineer with a data science foundation.")+f'''<section><div class="wrap"><div class="grid g2" style="align-items:start"><div>
<p class="lead" style="max-width:none">I'm a B.Tech graduate in Computer Science &amp; Engineering (Data Science) from SRMCEM, Lucknow, finishing with First Division with Distinction. I started with data analysis and machine learning, and now build LLM applications: RAG systems, agents and multimodal tools.</p>
<p class="lead" style="max-width:none">Since May 2026 I've been an AI/ML Engineer Intern at TheSmartBridge, building GenAI proofs of concept and end-to-end ML workflows. Outside work I contribute to open source (OpenPrinting) and speak at student tech conferences.</p></div>
<div class="card"><h3>At a glance</h3><p><b>Role:</b> AI/ML Engineer (Generative AI, RAG, agents)<br><b>Education:</b> B.Tech CSE (Data Science), 2023–2026, CGPA 8.78<br><b>Location:</b> Noida, India · open to Delhi NCR<br><b>Languages:</b> English, Hindi<br><b>Interests:</b> Travel photography, teaching, open source</p></div></div></div></section>
<section class="alt"><div class="wrap"><div class="sh"><h2>Skills</h2></div><div class="grid g3">
{sk("Generative AI",["LLMs","RAG","Prompt engineering","Agentic AI","LangChain","LangGraph","MCP","Multi-agent systems"])}
{sk("Machine learning",["Python","Scikit-learn","PyTorch","Feature engineering","Time series","Clustering","YOLOv8","OpenCV"])}
{sk("Data &amp; analytics",["SQL","Pandas","NumPy","EDA","Power BI","Tableau","Excel"])}
{sk("Backend &amp; APIs",["FastAPI","Flask","REST APIs","Node.js","MongoDB"])}
{sk("Vector search",["ChromaDB","FAISS","Embeddings","Semantic search"])}
{sk("Tools &amp; cloud",["Git","Docker","Cloud deployment","GitHub Pages","Jira"])}</div></div></section>
<section><div class="wrap"><div class="sh"><h2>Education</h2></div><div class="timeline">
<div class="job"><h3>B.Tech, Computer Science &amp; Engineering (Data Science)</h3><div class="when">2023 – 2026 · SRMCEM, Lucknow · CGPA 8.78</div><ul><li>First Division with Distinction (AKTU); 9.44 SGPA in the 8th semester</li><li>Branch topper in the 3rd and 4th year (Smt. Nirmala Agarwal Memorial Award)</li></ul></div>
<div class="job"><h3>Class 12 (PCM)</h3><div class="when">2019 – 2020 · S.K.I.C College</div><ul><li>First Class, 72%</li></ul></div>
<div class="job"><h3>Class 10</h3><div class="when">2017 – 2018 · S.K.I.C College</div><ul><li>First Class with Distinction, 81%</li></ul></div></div></div></section>'''

# ---- EXPERIENCE
def job(t,org,when,pts):return f'<div class="job"><h3>{t} · {org}</h3><div class="when">{when}</div><ul>'+''.join(f'<li>{x}</li>' for x in pts)+'</ul></div>'
exp=head("Experience","Internships and hands-on training, most recent first.")+'<section><div class="wrap"><div class="timeline">'+''.join([
job("AI/ML Engineer Intern","TheSmartBridge","May 2026 – Present · Noida (on-site)",["Building GenAI applications with LLMs, RAG, LangChain, LangGraph and AI agents","Built end-to-end ML workflows: preprocessing, feature engineering, training, evaluation and deployment","Delivered AI proofs of concept using vector databases, REST APIs and cloud tooling","Worked with mentors on documentation and client-focused deliverables"]),
job("Data Analyst Intern","Labmentix","Aug 2025 – Dec 2025 · Remote",["Cleaned and analysed real-world datasets with Python, SQL and Pandas","Ran EDA and built visual reports to support business decisions","Applied predictive modelling to data-driven business problems"]),
job("Web Development Intern","IBM – NASSCOM PBEL","Jul 2025 – Aug 2025 · Remote",["60+ hours of project-based training","Built a full-stack weather web app (HTML, CSS, JavaScript, Node.js, MongoDB, REST APIs) with real-time data and responsive UI"]),
job("AI/ML Intern","Internshala","Jan 2025 – Jun 2025 · Remote",["Built supervised and unsupervised models on real datasets","Used SQL and Power BI to communicate insights","Completed the 8-week Machine Learning with AI course with a 92% score"]),
job("Data Science &amp; AI/ML Intern","YBI Foundation","Jul 2024 – Dec 2024 · Lucknow",["Built predictive models with Python on real-world datasets","Practised the full workflow: preprocessing, EDA, visualisation, feature engineering"]),
])+'</div></div></section>'

# ---- PROJECTS
projects=head("Projects","Generative AI first, with computer vision, ML and analytics work alongside.")+f'''<section><div class="wrap"><div class="filters" role="group" aria-label="Filter projects">
<button class="on" data-f="all">All</button><button data-f="genai">GenAI &amp; RAG</button><button data-f="agents">Agents</button><button data-f="cv">Computer vision</button><button data-f="ml">ML</button><button data-f="data">Analytics</button></div>
<div class="grid g3">{''.join(pcard(p) for p in PROJ)}</div><p style="margin-top:28px">More on <a href="{GH}"><b>GitHub</b></a>.</p></div></section>'''

# ---- CERTS
CERTS=[("AI and Cybersecurity Awareness","TCS iON · MPIT-CoE / TCS Foundation","Sep 2026","Responsible AI, data privacy, cyber threats"),
("Orchestrate Multi-agent Workflows with Gemini Enterprise","Google Cloud Skills Boost (skill badge)","Sep 2026","Multi-agent design and agentic workflow automation"),
("AI Agents for Beginners","Simplilearn SkillUp","2025","Generative AI agents"),
("Machine Learning with AI","Internshala Trainings","2025","Python, regression, classification, clustering · 92% score"),
("Project-Based Experiential Learning (Web Development)","IBM – NASSCOM PBEL","2025","60+ hours, full-stack project"),
("Data Science Internship Certificate","Labmentix","2025","Data analytics and ML"),
("Data Science Internship Certificate","YBI Foundation","2024","Data analysis and ML"),
("ISRO Mission EDA project certificate","ISRO","2025","Exploratory analysis of missions 1975–2022"),
("Introduction to Large Language Models","Google Cloud","","LLM fundamentals"),
("WeCP skill badge","WeCP","2025","Technical and problem-solving assessment")]
certs=head("Certifications","A selection of my 34 licenses and certifications. The full, verifiable list is on Credly and LinkedIn.")+'<section><div class="wrap"><div class="grid g2">'+''.join(f'<div class="card"><h3>{a}</h3><span class="meta">{b}{" · "+c if c else ""}</span><p>{d}</p></div>' for a,b,c,d in CERTS)+f'</div><div class="btns" style="margin-top:28px"><a class="btn pri" href="https://www.credly.com/users/pankaj-kumar.59367139">Credly profile</a><a class="btn sec" href="{LI}#licenses_and_certifications">LinkedIn licenses</a></div></div></section>'

# ---- ACHIEVEMENTS
AW=[("1","Best B.Tech Project Award – First Prize, with Gold Medal (2026)","ECHO – Smart Virtual Eco Herbal Garden, awarded by the Department of AIML &amp; DS, SRMCEM."),
("2","Branch topper, 3rd and 4th year","Smt. Nirmala Agarwal Memorial Award, B.Tech CSE (Data Science)."),
("3","B.Tech with First Division with Distinction","AKTU, 2025–26, with a 9.44 SGPA in the final semester."),
("4","Published research paper","“ECHO: Engineering a Context-Aware Herbal Intelligence Platform”, Global Journal of Computer and Engineering Technology; presented at the 2026 UoP–IITR–AIMT International Conference."),
("5","Presenter, IIT Roorkee conference 2025","“Digitization of AYUSH Herbal Knowledge using Modern Web &amp; AI Technologies”."),
("6","Speaker, Opportunity Open Source Conference 4.0","IIIT Allahabad. Talk: “AI Overload: How Careless AI Usage Is Quietly Hurting Pull Request Quality”."),
("7","Open source contributor, OpenPrinting","Legacy drivers: researching and preserving historical Linux printer-driver software."),
("8","Showcased at Innovation Festival","Regional Science City, Lucknow."),
("9","AKTU awareness programme certificate","Three-day programme on health, pollution and environment, recognised by the Vice-Chancellor.")]
ach=head("Achievements","Awards, publications and talks.")+'<section><div class="wrap"><div class="grid g2">'+''.join(f'<div class="card award"><div class="ic">{i}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i,t,d in AW)+'</div></div></section>'

# ---- CONTACT
contact=head("Contact","Open to AI/ML engineering roles in Delhi NCR (Noida, Gurugram) and remote.")+f'''<section><div class="wrap"><div class="contact-list">
<div class="card"><b>Email</b><a href="mailto:pankaj955956@gmail.com">pankaj955956@gmail.com</a></div>
<div class="card"><b>Phone</b><a href="tel:+919559933956">+91 95599 33956</a></div>
<div class="card"><b>Location</b>Noida, Uttar Pradesh, India</div>
<div class="card"><b>Profiles</b><span class="links"><a href="{LI}">LinkedIn</a><a href="{GH}">GitHub</a><a href="https://leetcode.com/u/PankajKumar_DS/">LeetCode</a></span></div></div>
<div class="btns" style="margin-top:28px"><a class="btn pri" href="mailto:pankaj955956@gmail.com">Send an email</a></div></div></section>'''

for fn,t,b in [("index.html","Home",home),("about.html","About",about),("experience.html","Experience",exp),("projects.html","Projects",projects),("certifications.html","Certifications",certs),("achievements.html","Achievements",ach),("contact.html","Contact",contact)]:
    open(fn,"w").write(shell(fn,t,b))
