# Generalized Monty Hall Simulator 🚪🎲  
A probability exploration tool built with **Python** and **Streamlit**

---

🔗 **Live App:** https://meu-app.streamlit.app/  
*(Você pode ajustar esse link após o deploy.)*

---

## 📸 Screenshots

![Simulator](images/simulator.png)
![Compare](images/compare.png)

---

## 📘 Overview

This application provides an interactive environment to explore the **generalized Monty Hall problem**, a probability puzzle involving partial information, conditional probability, Bayesian updating, and strategic decision-making.

While the classic Monty Hall scenario involves **3 doors** and **1 revealed door**, this simulator extends the concept to:

- **N doors**  
- **K doors revealed by the host**  
- Multiple player strategies  
- Simulation-based probability estimation  
- Analytical formulas (where applicable)

The app allows users to experiment with different settings and visualize how the probability of winning changes across strategies and configurations.

---

## 🧠 Why Generalize Monty Hall?

Real-world decision problems rarely involve only three options.  
Generalizing the Monty Hall structure helps demonstrate concepts such as:

- Decision-making under uncertainty  
- Information asymmetry  
- Conditional probability  
- Bayesian reasoning  
- The benefits of simulation when closed-form formulas are difficult or impossible

This tool is especially useful in **education**, **statistical reasoning**, **game theory**, and **data science** demonstrations.

---

## 🎮 Features

### ✔ Interactive Configuration
- Choose number of doors (**N**)
- Choose number of doors the host reveals (**K**)
- Select the player’s strategy
- Configure number of simulation runs

### ✔ Supported Strategies
- **Stay** (never change the initial choice)  
- **Single Switch** (switch once after all doors are revealed)  
- **Sequential Switching** (switch after every reveal — analytically complex)  
- **Random** (50% stay, 50% single-switch)

### ✔ Simulation Outputs
- Winning probability (empirical estimate)
- Bayes table for probability propagation  
- Raw simulation results  
- Comparison of all strategies in a bar chart

### ✔ Explanation Page
A complete conceptual guide covering:
- Classic Monty Hall (3 doors)
- Mathematical intuition
- Generalization to N and K
- Derivations for stay and single-switch formulas
- Sequential-switch demonstration for N=4, K=2

---

## 📐 Mathematical Formulas (Included in App)

### **Stay Strategy**
\[
P(\text{win | stay}) = \frac{1}{N}
\]

### **Single Switch**
\[
P(\text{win | single switch}) 
    = \frac{N - 1}{N} \cdot \frac{1}{N - K - 1}
\]

### **Sequential Switch**
No simple closed-form exists for general **N, K** — simulation is required.

The explanation page includes a full worked example for:  
**N = 4, K = 2 → P(win) = 62.5%**

---

## 🛠 Installation

```bash
git clone https://github.com/willyanbertolino/generalized-monty-hall-simulator.git
cd generalized-monty-hall-simulator
pip install -r requirements.txt
streamlit run app.py

```

---

## 👨‍💻 Autor - **Willyan Bertolino**
