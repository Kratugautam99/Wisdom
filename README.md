# Wisdom 📚✨

> A curated learning hub of Python, SQL, DSA and data-science practice—packed with tutorials, code samples, eBooks and real datasets for hands-on mastery.

---
## 🚀 Table of Contents
- [ℹ️ About](#-about)  
- [💽 Features](#-features)  
- [📂 Structure](#-structure)  
- [⚙️ Installation](#️-installation)  
- [▶️ Usage](#️-usage)  
- [🤝 Contributing](#-contributing)  
- [📜 License](#-license)  

---
## ℹ️ About
**Wisdom** is your one-stop repo for sharpening programming and analytics skills. It brings together:  
- Python practice scripts (syntax, OOP, scripts & mini-projects)  
- SQL assignments & cheat-sheets for querying relational data  
- Core data-science libraries (Pandas, NumPy, Matplotlib, Seaborn) with hands-on tutorials and CSV/JSON datasets  
- DSA fundamentals—implementations of arrays, linked lists, stacks, queues, trees & common algorithms  
- Curated eBooks, notes & exercises to guide structured revision  

Whether you’re a student, job-seeker or self-learner, dive in for daily practice, quick reference, or deep exploration!  

---
## 💽 Features
- 🔍 **Tutorial-Driven**: Step-by-step notebooks & code samples  
- 📊 **Real Datasets**: CSV/JSON data files to explore and visualize  
- 🛠️ **Hands-On Exercises**: End-to-end practice for every topic  
- 📚 **Reference Library**: Ebooks & markdown guides for offline reading  
- 🔄 **Modular Layout**: Pick and choose what to learn next
  
---
## 📂 Structure

```text
.
├── .github/                          # CI workflows, issue/pr templates
├── Python Works/                     # Python practice materials
│   ├── DSAQs in Python by Goodrich et al./  
│   ├── Pandas-Matplotlib-Seaborn/  
│   ├── Practice File/  
│   ├── test AVIFs/  
│   ├── test CSVs/  
│   ├── test PDFs/  
│   ├── test Text/  
│   └── Wisdom/                      
├── Eurekathon-2024/                  # This is the Internal Hackathon Version of SIH conducted in my college.
│   ├── BeachDatasetFinal.csv  
│   ├── Smart India Hackathon.7z
│   ├── SmartIndiaHackathonMLModelFinal.ipynb 
├── SQL Resume Challenge/             # SQL practice assignments
│   ├── Problems/  
│   ├── Solutions/  
│   └── SQL-Practice/  
├── SECURITY.md                       # Security policy  
└── README.md   
```

---
## ⚙️ Installation
1. Clone this repo  
   ```bash
   git clone https://github.com/Kratugautam99/Wisdom.git
   cd Wisdom
   ```
2. (Optional) Create a virtual environment  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```
   
---   
## ▶️ Usage
- Browse **tutorials/** for step-by-step Jupyter notebooks  
- Open **python/** and **dsa/** to run practice scripts:  
  ```bash
  python "Python Works/{FileName}"
  ```
- Study **sql/** examples by loading scripts in your SQL client  
- Visualize data:  
  ```python
  import pandas as pd
  import matplotlib.pyplot as plt

  df = pd.read_csv('data/sales.csv')
  df.plot(kind='bar')
  plt.show()
  ```
---
## 🤝 Contributing

**Contributions welcome!**
1. Fork the repo
2. Create a feature branch (git checkout -b feat/YourTopic)
3. Commit your changes (git commit -m "Add your feature")
4. Push (git push origin feat/YourTopic) & open a PR

---
## 📜 License
Distributed under the MIT License. See LICENSE for details.

