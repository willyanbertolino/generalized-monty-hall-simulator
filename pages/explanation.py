import streamlit as st

st.set_page_config(
    page_title="Explanation — Generalized Monty Hall",
    page_icon="📘",
    layout="wide"
)

st.title("📘 Understanding the Generalized Monty Hall Problem")

st.markdown("""
The **Monty Hall problem** is a famous probability puzzle based on a 1970s TV show.
Surprisingly, **switching doors dramatically increases your chance of winning**.

This page explains the **classic version** and how we **generalize it** to:
- **N doors**
- **K doors opened by the host**
- **different player strategies**
""")


# -----------------------------------------------------------
# CLASSIC MONTY HALL
# -----------------------------------------------------------
st.header("🎯 Classic Monty Hall (3 doors)")

col1, col2 = st.columns([1.5, 2])

with col1:
    st.subheader("Rules")
    st.markdown("""
    1. There are **3 doors**.  
    2. Behind **1** door: a prize.  
    3. Player picks a door.  
    4. The host opens **one** of the *other* doors with **no prize**.  
    5. Player chooses to **stay** or **switch**.  
    """)

with col2:
    st.subheader("Why switching wins")
    st.markdown("""
    Initially, the chance of picking the prize is **1/3**.

    Therefore, the chance that the prize is behind **a door the player did NOT choose**
    is **2/3**.

    When the host opens a losing door, he **transfers the entire 2/3 probability**
    to the **remaining closed door**.

    So:

    - Staying wins: **1/3**  
    - Switching wins: **2/3**  
    """)


# -----------------------------------------------------------
# GENERALIZED VERSION
# -----------------------------------------------------------
st.header("🧩 Generalized Monty Hall (N doors, K opened)")

st.markdown("""
To generalize the problem, we allow:

### **• N total doors**  
### **• K doors opened by the host**  
### **• Several possible strategies**

This turns the puzzle into a rich playground for probability simulation.

--- 

## 🔢 General Rules

Let:

- **N** = total number of doors  
- **1 prize** hidden behind one door  
- **Player initially picks 1 door**

The host then:

- Opens **K doors**  
- These must be:
  - **not chosen by the player**
  - **not containing the prize**
- After opening K doors, the player applies a **strategy**.

---
""")


# -----------------------------------------------------------
# STRATEGIES
# -----------------------------------------------------------
st.header("🧠 Player Strategies")

st.subheader("1️⃣ stay")
st.markdown("""
The player keeps their original choice.  
This is the baseline strategy.
""")

st.subheader("2️⃣ switch_once")
st.markdown("""
The player switches **only one time**, right after the host opens K doors.  
They choose randomly among the remaining closed doors.
""")

st.subheader("3️⃣ switch_until_end")
st.markdown("""
The player keeps switching to another closed door until **only one door remains**.

This behaves like an "aggressive switching" strategy and often outperforms the others
in the generalized case.
""")


# -----------------------------------------------------------
# INTUITION BEHIND GENERALIZATION
# -----------------------------------------------------------
st.header("💡 Why switching is powerful in the generalized version")

st.markdown("""
In the classic Monty Hall, switching wins because:

- The initial pick has **1/N** chance of being correct  
- The unpicked doors together have **(N−1)/N** chance of containing the prize  
- When the host opens **K doors with no prize**, the remaining closed doors  
  **concentrate** the probability mass.

The more doors you have and the more doors the host opens, the **stronger** the effect.

---

Example intuition:

- If there are **100 doors**  
- You pick 1 (chance = **1%**)  
- The prize is more likely in the other 99 doors (**99%**)  
- The host opens **98 of them** (all goats!)  
- Remaining closed doors: only **your door** and **1 other door**  
- Switching is obviously much better  
""")


# -----------------------------------------------------------
# WRAP-UP
# -----------------------------------------------------------
st.header("🎉 Summary")

st.markdown("""
- Monty Hall is a problem where **intuition fails** and probability wins.  
- The generalized version allows exploring:
  - multiple doors  
  - multiple openings  
  - different switching strategies  
- This creates a rich space for **simulation and data visualization**.  

Use the simulation page to experiment and discover patterns!
""")
