import streamlit as st


st.set_page_config(
    page_title="Explanation — Generalized Monty Hall",
    page_icon="📘",
    layout="wide"
)
st.title("Understanding the Generalized Monty Hall Problem")

st.markdown("""
The **Monty Hall problem** is a classical probability puzzle inspired by a game show from the 1970s.
Although its rules are simple, the optimal strategy is often counterintuitive:
**switching doors significantly increases the probability of winning**.

This application presents both the **classic formulation** and a **generalized version**.

""")

# -----------------------------------------------------------
# CLASSIC MONTY HALL
# -----------------------------------------------------------
st.header("Classic Monty Hall (3 doors)")

col1, col2 = st.columns([1.5, 2])

with col1:
    st.subheader("Rules")
    st.markdown("""
    1. There are **3 closed doors**.
    2. Behind exactly **one** of them, there is a prize.
    3. The player initially chooses one door.
    4. The host, who **knows where the prize is**, opens **one of the remaining doors** that does *not* contain the prize.
    5. The player must then choose whether to **stay** with their original door or **switch** to the only unopened alternative.
    """)

with col2:
    st.subheader("Why switching is better")
    st.markdown("""
    At the initial choice, the probability that the player selects the prize is **1/3**.

    Consequently, the prize is behind one of the **two unchosen doors** with probability **2/3**.

    When the host opens *one* of these two doors and reveals that it contains no prize,
    the entire **2/3 probability mass** shifts to the single remaining closed door.

    Therefore:

    - Probability of winning by staying: **1/3**
    - Probability of winning by switching: **2/3**

    This asymmetry arises because the host’s action is **informative**,
    and the switching strategy leverages that information.
    """)


# -----------------------------------------------------------
# GENERALIZED VERSION
# -----------------------------------------------------------
st.header("Generalized Monty Hall (N doors, K opened)")

st.markdown("""
The classical Monty Hall setup can be extended by increasing the number of doors and allowing the host to
open more than one door. This generalization transforms the puzzle into a broader study of **conditional
probability**, **information revelation**, and **decision strategies**.

In this extended version, we consider:

- **N doors**
- **K doors opened by the host**
- **multiple player strategies** (stay, switch, random)


This flexibility makes the model suitable for simulation-based analysis and experimentation.

---

## **General Rules**

Let:

- **N** — total number of doors
- **1 prize** — hidden uniformly at random
- **Player selects 1 door** in the initial step

Then the host:

- Opens exactly **K doors**
- These doors must satisfy:
  - They are **not the player's initial choice**
  - They **cannot reveal the prize**
- The host is assumed to have **perfect knowledge** of the prize location and behaves consistently.

After the host opens **K doors**, the player applies one of the predefined strategies.
Each strategy leads to different probability dynamics depending on **N**, **K**, and the structure of the remaining choices.

---
""")



# -----------------------------------------------------------
# STRATEGIES
# -----------------------------------------------------------
st.header("Player Strategies")

st.subheader("Stay Strategy")
st.markdown("""
Under the **stay strategy**, the player never changes their initial choice.
No matter how many goat doors the host reveals, the player keeps the same door
from start to finish.

Since the host never opens the prize door, the initial probability of selecting the prize,
which is **1 / N**, remains unchanged.

**Staying always wins with probability:**
""")

st.latex(r"""
P(\text{win | stay}) = \frac{1}{N}
""")

st.markdown("""
This matches the classic case (1/3 for N = 3).
This strategy serves as a baseline for comparison, since it does not use the
information provided by the revealed doors.
""")


st.subheader("Switch Strategy")
st.markdown("""
There are two distinct variants of the switching strategy:

---

### **1. Single Switch (default case)**
The player waits until the host has opened all **K** goat doors and then performs **one single switch**, selecting uniformly among the remaining unopened doors.

Key intuition:

- The probability that the initial choice was incorrect is
  **(N – 1) / N**.
- After the host reveals **K** losing doors, the number of unopened, unchosen doors is
  **N – K – 1**.
- The player chooses uniformly among those remaining doors.

The analytical probability of winning under **single-switch** is:
""")

st.latex(r"""
P(\text{win | single switch}) \;=\;
\frac{N-1}{N} \cdot \frac{1}{\,N - K - 1\,}
""")

st.markdown("""
This expression correctly reproduces the classic Monty Hall result
(**2/3** when **N = 3**, **K = 1**) and generally exceeds the stay probability for
most combinations of **N** and **K**.

---

""")

st.markdown("""
### **2. Sequential Switching**
In this variant, the player **switches after each revealed goat door**.
Every time the host opens one door, the player immediately selects
uniformly among all remaining closed doors.

Because switching occurs multiple times, the resulting probability depends
on all possible sequences of door revelations and transitions between choices.
This makes the analytical expression significantly more complex and
generally outside the scope of a simple closed-form derivation.


**Example: Sequential Switching (N = 4, K = 2)**

Consider four doors, A, B, C, D and the prize is behind one door with probability **1/4** each.

1. If the contestant's initial choice (A) is the prize (probability 1/4), switching twice leads back to A — win certain.
""")

st.latex(r"P(\text{prize}=A)=\tfrac{1}{4},\quad P(\text{win}\mid \text{prize}=A)=1")

st.markdown("2. If the prize is not in A (probability 3/4), by symmetry consider it in B. After the first reveal the contestant switches uniformly; with probability 1/2 they pick the prize (leading to final loss) and with probability 1/2 they pick a goat (leading to final win). So:")
st.latex(r"P(\text{win}\mid \text{prize}\neq A)=\tfrac{1}{2}")

st.markdown("Total win probability:")
st.latex(r"P(\text{win})=P(\text{prize}=A)\cdot P(\text{win}\mid \text{prize}=A) + P(\text{prize}\neq A)\cdot P(\text{win}\mid \text{prize} \neq A)")

st.latex(r"P(\text{win})= \tfrac{1}{4} \cdot 1 + \tfrac{3}{4} \cdot \tfrac{1}{2} = \tfrac{5}{8}=62.5\%.")




## Random Strategy
st.subheader("Random Strategy")
st.markdown("""
Under the **random strategy**, the player behaves unpredictably. In each simulation run:

- With probability **1/2**, the player **keeps** the initial choice.
- With probability **1/2**, the player **switches exactly once**, but **only after all K doors have been revealed**.

This produces an averaged outcome that serves as a neutral baseline, mixing the stay and single-switch behaviors without following a deterministic decision rule.
""")



# -----------------------------------------------------------
# INTUITION BEHIND GENERALIZATION
# -----------------------------------------------------------
st.header("Why switching is powerful in the generalized version")

st.markdown("""
In the classic Monty Hall, switching wins because:

- The initial pick has **1/N** chance of being correct
- The unpicked doors together have **(N-1)/N** chance of containing the prize
- When the host opens **K doors with no prize**, the remaining closed doors
  **concentrate** the probability mass.

The more doors you have and the more doors the host opens, the **stronger** the effect.

---

Example intuition:

- If there are **100 doors**
- You pick 1 (chance = **1%**)
- The prize is more likely in the other 99 doors (**99%**)
- The host opens **98 of them** (all goats. This is not at random!)
- Remaining closed doors: only **your door** and **1 other door**
- Switching is obviously much better (99% win)
""")


# -----------------------------------------------------------
# WRAP-UP
# -----------------------------------------------------------
st.header("Summary")

st.markdown("""
- Monty Hall is a problem where **intuition fails** and probability wins.
- The generalized version allows exploring:
  - multiple doors
  - multiple openings
  - different switching strategies
- This creates a rich space for **simulation and data visualization**.

Use the simulation page to experiment and discover patterns!
""")
