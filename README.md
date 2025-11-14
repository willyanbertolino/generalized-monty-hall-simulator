📘 Generalized Monty Hall Simulator
Interactive Streamlit App • Probability Simulation • Data Science Portfolio Project
🚪 Overview

This project is an interactive Streamlit app that simulates the generalized Monty Hall problem, allowing:

N total doors

K doors opened by the host

customizable player strategies

thousands of Monte Carlo simulations

visual comparison of strategies

The goal is to show how probability behaves in counter-intuitive scenarios and demonstrate good practices for:

simulation modeling

interface design using Streamlit

clean code and modularization

data visualization

statistical reasoning

🎮 Live Demo

(If you publish on Streamlit Cloud, add the link here)

https://<your-app>.streamlit.app

📂 Project Structure
montyhall-generalizado/
│── app.py → Main Streamlit app
│── simulation.py → Batch simulation logic
│── requirements.txt → Dependencies
│── README.md → Project documentation
│
├── logic/
│ ├── **init**.py
│ └── montyhall.py → Core Monty Hall game mechanics
│
└── pages/
└── explanation.py → Detailed explanation page inside the app

🧠 How the Simulation Works

1. Prize placement

A single door is randomly selected to contain the prize.

2. Player chooses a door

This is a uniform random choice among all N doors.

3. Host opens K doors

The host must reveal doors that contain no prize and are not the player’s pick.

4. Player strategy is applied

Available strategies:

🔹 stay

Keep the original door.

🔹 switch_once

Switch to another closed door after K doors are opened.

🔹 switch_until_end

Keep switching until only one closed door remains.

5. Win or lose

The simulation records 1 (win) or 0 (loss).

Running thousands of simulations reveals the true probability distribution.

📊 Example Results

(Add screenshots of your Streamlit app here)

[Insert image: bar plot comparing strategies]
[Insert image: explanation page screenshot]

Typical behavior:

Staying has probability ≈ 1/N

Switching often significantly outperforms staying

In large N (e.g., 100 doors), switching becomes overwhelmingly better

▶️ How to Run

1. Clone the repository
   git clone https://github.com/<your-username>/montyhall-generalized.git
   cd montyhall-generalizado

2. (Optional) Create a virtual environment
   python -m venv venv
   source venv/bin/activate # Linux/macOS
   venv\Scripts\activate # Windows

3. Install dependencies
   pip install -r requirements.txt

4. Run the app
   streamlit run app.py

Open your browser at:

http://localhost:8501

🧪 Technologies Used

Python 3.9+

Streamlit

Pandas

Matplotlib

Monte Carlo simulation

📌 Features

✔️ Full generalization for N doors

✔️ Host opens K doors with no prize

✔️ Multiple strategies

✔️ Statistical simulation with thousands of runs

✔️ Interactive visualizations

✔️ Educational explanation page

✔️ Modular, clean code

✔️ App ready for deployment

⚙️ Possible Extensions

You can extend this project easily with:

strategy probabilities (e.g., “switch with probability p”)

multi-round opening of doors

optimal strategy derivation

analytical formulas (not just simulation)

animations of the door selection

comparing host behaviors (random host, biased host…)

👨‍💻 Author

Your Name
Data Science • Statistics • Simulation Modeling

Add your LinkedIn/GitHub:

GitHub: https://github.com/<your-username>
LinkedIn: https://www.linkedin.com/in/<your-profile>

⭐ If you like this project…

Give it a star on GitHub — it helps visibility and credibility!

🎉 Pronto!

Esse README está em nível profissional, perfeito para um projeto de portfólio.
