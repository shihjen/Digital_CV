from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / 'styles' / 'main.css'
resume_file = current_dir / 'files' / 'Tan Shih Jen_CV.pdf'


# --- GENERAL SETTINGS ---
PAGE_TITLE = 'Digital CV | Tan Shih Jen'
PAGE_ICON = ':clipboard:'
NAME = 'Tan Shih Jen'
DESCRIPTION = """
Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = 'e1094875@u.nus.edu'
CONTACT = '+65 8145 4991'
SOCIAL_MEDIA = {
    'LinkedIn': 'https://www.linkedin.com/in/tan-shih-jen-99546b306',
    'GitHub': 'https://github.com/shihjen',
    'Kaggle': 'https://www.kaggle.com/tanshihjen',
}
PROJECTS = {
    "🟧 Early Detection of Non-alcoholic Fatty Liver Disease (NAFLD)-Associated Hepatocellular Carcinoma (HCC) by Machine Learning": " ",
    "🟧 Kidney Failure Risk Prediction in Intensive Care Unit (ICU) Patients": "https://github.com/shihjen/AKI_Prediction_ICU_Patients",
    "🟧 Automated Tracking System for Oligomer and Sequencing Services": "https://shihjen-oligomer-usage-tracker-system-streamlit-app-p14hpv.streamlit.app/?embed_options=dark_theme",
    "🟧 BCEAD Research Laboratory Website (Assistant Professor Chris Sham's Laboratory)": "https://bcead.github.io/chris-sham-lab/",
}

SKILLS = [
'🟧 Programming: `Python`, `R`',
'🟧 Data processing/wrangling: `SQL`, `pandas`, `numpy`',
'🟧 Data Visulization: `Matplotlib`, `Seaborn`, `Plotly`',
'🟧 Machine Learning: `Scikit-learn`, `RapidMiner`, `SIMCA`',
'🟧 Web development: `HTML`, `CSS`',
'🟧 Model deployment: `Streamlit`'
]


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout='centered')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #F28C28;">

  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#selected-projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#publication">Publication</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contact">Contact</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()    

profile_pic = Image.open('image/profile_img.jpg')

# --- HERO SECTION ---
container_hero = st.container(border=True)
container_hero.markdown('<h1 style = "color:#F28C28; text-align:left;"> <i>Curriculum Vitae</i> </h1>', unsafe_allow_html=True)

col1, col2 = container_hero.columns(2)
with col1:
    st.image(profile_pic, width=280)
        # --- SOCIAL LINKS ---
    cols = col1.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

with col2:
    st.markdown('''
    <h2 style = "color:#FFAA33;"> Tan Shih Jen </h2>
    ''', unsafe_allow_html=True)
    st.markdown('''
    <div id="contact">
    <h5> Contact </h5>
    </div>
    ''', unsafe_allow_html=True)
    st.write(':e-mail:', EMAIL)
    st.write(':telephone_receiver:', CONTACT)
    #st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )





# --- SUMMARY ---
container = st.container(border=True)
container.markdown('''
            <h3 style = "color:#FFAA33; text-align:center;"> 👨‍💻 Summary </h3>
            ''', unsafe_allow_html=True)
container.write('---')
container.markdown('''
<div style="text-align: justify;">
With 8 years of hands-on experience in research laboratories, I specialize in managing lab operations and research funding. 
I am passionate about integrating new technologies into my professional and personal life. 
Acknowledging the growing significance of data and data-driven decision-making, 
I have enhanced my data literacy through analytics coursework at NUS and am currently pursuing a part-time Master's in Biomedical Informatics to advance my data science expertise. 
I am dedicated to extracting actionable insights from data and converting them into strategic solutions. 
With a solid background in analytical methods and proficiency in machine learning, data visualization, and natural language processing, 
I am eager to bring innovative solutions and a fresh perspective to problem-solving in the workplace.
</div>
''', unsafe_allow_html=True)
container.write('\n')


# --- SKILLS ---
container1 = st.container(border=True)
container1.markdown('''
            <h3 style = "color:#FFAA33; text-align:center;"> 🔧 Technical Skills </h3>
            ''', unsafe_allow_html=True)
container1.write('---')
for skill in SKILLS:
    container1.write(skill)


# --- Projects ---
container2 = st.container(border=True)
container2.markdown('''
            <div id = "selected-projects" >
            <h3 style = "color:#FFAA33; text-align:center;">💻 Selected Projects</h3>
            </div>
            ''', unsafe_allow_html=True)
container2.write("---")
for project, link in PROJECTS.items():
    container2.write(f"[{project}]({link})")



# --- EDUCATION ---
container3 = st.container(border=True)
container3.markdown('''
            <div id = "education">
            <h3 style = "color:#FFAA33; text-align:center;"> 🎓 Education </h3>
            </div>
            ''', unsafe_allow_html=True)
container3.write("---")

# --- Education 1
container3.markdown('''**Master of Science (Biomedical Informatics) - Analytic Specialization** 
            <br> National University of Singapore, Singapore
            <br> *Aug 2022 - Jul 2024*''', unsafe_allow_html=True)

MASTER = [
'🟧 GPA: 4.15/5.00',
'🟧 Capstone Project: Early Detection of Non-alcoholic Fatty Liver Disease (NAFLD) - Associated Hepatocellular Carcinoma (HCC) by Machine Learning.'
]

for itm in MASTER:
    container3.write(itm)



# --- Education 2
container3.write('\n')
container3.write('\n')
container3.markdown('''**Bachelors of Science (Honours) Biochemistry** 
            <br> University Putra Malaysia, Malaysia
            <br> *Sep 2011 - Jun 2015*''', unsafe_allow_html=True)
BACHELOR = [
'🟧 GPA: 3.95/4.00',
'🟧 Graduated with First Class Honors.',
'🟧 Vice Chancellor\'s List: Semester 1 Academic Year 2011/2012, Semester 2 Academic Year 2014/2015.',
'🟧 Dean\'s List: Semester 2 Academic Year 2011/2012, Semester 1 Academic Year 2012/2013, Semester 2 Academic Year 2012/2013, Semester 1 Academic Year 2013/2014.',
'🟧 Final Year Project: Antihyperglycemic and Antioxidative Potentials of Malaysian Banana (Musa sp.) Flower Extracts.',
'🟧 Poster presentation at the 26th Intervarsity Biochemistry Seminar.'
]

for itm in BACHELOR:
    container3.write(itm)


# --- WORK EXPERIENCE ---
container4 = st.container(border=True)
container4.markdown('''
            <div id="experience">
            <h3 style = "color:#FFAA33; text-align:center;"> 💼 Work Experience </h3>
            </div>
            ''', unsafe_allow_html=True)
container4.write("---")

# --- JOB 1
container4.markdown('''**Laboratory Technologist** 
            <br> Dapartment of Microbiology & Immunology, Yong Loo Lin School of Medicine, National University of Singapore, Singapore
            <br> *Jan 2019 - Present*
            ''', unsafe_allow_html=True)

LT = [
'🟧 Led undergraduate practical classes for LSM3232 Microbiology (Practical 1-3) and LSM3225 Molecular Microbiology in Human Diseases (Practical 4), providing technical and logistics support to faculty, instructors, and teaching assistants.',
'🟧 Supported the Assistant Professor Chris Sham Lok-To in managing research grants by overseeing budget allocation, tracking expenditures, and preparing financial reports. Implemented Python programming to automate the tracking and management of oligomer orders and sequencing service usage in the research lab.',
'🟧 Served as the safety lead in Assistant Professor Chris Sham Lok-To\'s laboratory. Conducted laboratory safety induction training for new students and staff before they commenced their projects.',
'🟧 Prepared, reviewed, and maintained Standard Operating Procedures (SOP) and Risk Assessments (RA) for the PI research lab and department core facilities.',
'🟧 Implemented and monitored laboratory safety practices, ensuring compliance with University and national regulations.'
]


for itm in LT:
    container4.write(itm)

# --- JOB 2
container4.write('\n')
container4.write('\n')
container4.markdown('''**Research Assistant** 
            <br> Laboratory of Natural Products, Institute of Bioscience, University Putra Malaysia, Malaysia
            <br> *Sep 2015 - Feb 2018*
            ''', unsafe_allow_html=True)

RA = [
'🟧 Conducted metabolomics study on natural products.',
'🟧 Wrote research proposal and assisted in the grant application.',
'🟧 Ensured proper maintenance and management of the husbandry and animal facility.',
'🟧 Managed procurement tasks, including sourcing and purchasing laboratory supplies.'
]

for itm in RA:
    container4.write(itm)

# --- JOB 3
container4.write('\n')
container4.write('\n')
container4.markdown('''**QA/QC Intern** 
            <br> Rida Fruits Sdn Bhd, Malaysia
            <br> *Jun 2014 - Aug 2014* 
            ''', unsafe_allow_html=True)

INTERN = [
'🟧 Performed QC inspection and routine laboratory tests of incoming raw materials, intermediate products, packaging, and finished goods with established sampling and testing protocols.',
'🟧 Prepared QA and QC reports.',
'🟧 Performed sensory evaluation on raw materials and finished products.',
'🟧 Executed food safety standards in compliance with HACCP and HALAL requirements.'
]

for itm in INTERN:
    container4.write(itm)

# --- CERTIFICATION & PROFESSIONAL DEVELOPMENT ---
container5 = st.container(border=True)
container5.markdown('''
            <h3 style = "color:#FFAA33; text-align:center;"> 📜 Certification & Professional Development </h3>
            ''', unsafe_allow_html=True)
container5.write("---")
container5.markdown(
    """
- :large_orange_square: CITI Health Information Privacy and Security (HIPS) <br> *CITI Program* | Jan 2024

- :large_orange_square: AICP Python for Artificial Intelligence and Machine Learning <br> *National University of Singapore* | Dec 2023
- :large_orange_square: Data Literacy Programme (DLP) - Advanced: Survey Analytics <br> *National University of Singapore* | Nov 2023
- :large_orange_square: Artificial Intelligence Competency Course (Intermediate) <br> *National University of Singapore* | Jul 2023
- :large_orange_square: Data Literacy Programme (DLP) - Intermediate: Applied Regression Models using R <br> *National University of Singapore* | Jul 2023
- :large_orange_square: Data Literacy Programme (DLP) - Intermediate: Customer Analytics <br> *National University of Singapore* | Jul 2023
- :large_orange_square: Professional Certificate in Basic Artificial Intelligence and Machine Learning <br> *National University of Singapore* | Jul 2023
- :large_orange_square: Data Visualization Begins With Me <br> *National University of Singapore* | Jun 2023
- :large_orange_square: Database Creation, Manipulation, and Querying with SQL <br> *National University of Singapore* | Apr 2023
- :large_orange_square: Artificial Intelligence Competency Course (Foundation) <br> *National University of Singapore* | Jul 2022
- :large_orange_square: Python Programming <br> *National University of Singapore* | May 2022
- :large_orange_square: Data Literacy Programme (DLP) - Basic <br> *National University of Singapore* | Mar 2022
""", unsafe_allow_html=True
)


# --- PUBLICATION ---
container6 = st.container(border=True)
container6.markdown('''
            <div id="publication">
            <h3 style = "color:#FFAA33; text-align:center;"> 📋 Publication </h3>
            </div>
            ''', unsafe_allow_html=True)
container6.write("---")

container6.markdown(
    """
- :large_orange_square: [Nuclear magnetic resonance spectroscopy and liquid chromatography–mass spectrometry metabolomics studies on non-organic soybeans versus organic soybeans (<i>Glycine max</i>), and their fermentation by <i>Rhizopus oligosporus</i>](https://pubmed.ncbi.nlm.nih.gov/36426592/)
<br>Journal of the Science of Food and Agriculture | Nov 25, 2022 <br>

- :large_orange_square: [Potency of Selected Berries, Grapes, and Citrus Fruit as Neuroprotective Agents](https://pubmed.ncbi.nlm.nih.gov/32565853/)
<br>Evidence-based complementary and alternative medicine : eCAM | Jun 30, 2020 <br>

- :large_orange_square: [Evaluation of banana (<i>Musa</i> sp.) flowers of selected varieties for their antioxidative and anti-hyperglycemic potentials](http://ifrj.upm.edu.my/23%20(05)%202016/(21).pdf)
<br> International Food Research Journal | Jan 28, 2016
""", unsafe_allow_html=True
)

