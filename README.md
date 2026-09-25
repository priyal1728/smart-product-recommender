🛍️ AI-Based Smart Product Recommendation System

## 📌 Project Description

The **AI-Based Smart Product Recommendation System** is a web-based application that helps users find suitable products based on their requirements and preferences.

The system accepts a natural-language product request, uses **LangChain and an LLM** to understand and extract user preferences, applies **Fuzzy Logic** to evaluate and score products, and provides personalized product recommendations with an AI-generated explanation.

The application is built using **Python and Streamlit** and is designed to be deployed online using **Streamlit Community Cloud**.

---

## ✨ Main Features

* 🤖 AI-based natural-language query understanding
* 🧠 LangChain-based LLM processing
* 📝 User preference extraction from free-text input
* 🔬 Fuzzy Logic-based product evaluation
* 📊 Fuzzy membership functions and rule-based inference
* 🎯 Product recommendation and ranking
* 💡 AI-generated explanation of recommendations
* 💰 Budget-based product filtering
* 📱 Product comparison based on user preferences
* 🖥️ Simple and user-friendly Streamlit interface
* 🌐 Online deployment

---

## 🛠️ Technologies / Tech Stack

| Technology                | Purpose                        |
| ------------------------- | ------------------------------ |
| Python                    | Main programming language      |
| Streamlit                 | Web application interface      |
| LangChain                 | AI/LLM integration             |
| OpenAI API                | LLM/API service                |
| Fuzzy Logic               | Product suitability evaluation |
| scikit-fuzzy              | Fuzzy inference implementation |
| Pandas                    | Product data processing        |
| NumPy                     | Numerical processing           |
| Git                       | Version control                |
| GitHub                    | Source-code hosting            |
| Streamlit Community Cloud | Deployment                     |

---

## 📁 Project Structure

```text
smart-product-recommendation/
│
├── app.py
│
├── data/
│   └── products.csv
│
├── ai/
│   ├── __init__.py
│   └── llm_parser.py
│
├── fuzzy/
│   ├── __init__.py
│   └── fuzzy_engine.py
│
├── recommendation/
│   ├── __init__.py
│   └── recommender.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── tests/
│   ├── test_ai.py
│   └── test_fuzzy.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/priyal1728/smart-product-recommender.git
```

### 2. Open the project folder

```bash
cd smart-product-recommender
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

The project requires an API key for the AI/LLM component.

Create a `.env` file locally:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

**Important:** Never upload the actual API key to GitHub.

The `.env` file should be included in `.gitignore`.

For Streamlit Community Cloud, add the required secret through the application's **Secrets** settings.

Example placeholder:

```toml
OPENAI_API_KEY = "your_openai_api_key_here"
```

---

## ▶️ How to Run the Project

After activating the virtual environment and installing the dependencies, run:

```bash
streamlit run app.py
```

The application will open in the browser.

### How to Use

1. Open the application.
2. Enter a product requirement in natural language.
3. For example:

```text
I need a smartphone under ₹30,000
with a very good camera, strong battery
and good gaming performance.
```

4. The LangChain/LLM component understands the user's request.
5. The system extracts product preferences such as budget, camera, battery, and gaming requirements.
6. The extracted preferences are passed to the Fuzzy Logic system.
7. Fuzzy membership functions calculate the degree of suitability.
8. Fuzzy rules evaluate the products.
9. The system performs defuzzification and generates recommendation scores.
10. Products are ranked according to their fuzzy scores.
11. The AI generates a conversational explanation of the recommendations.
12. The final recommendations are displayed in the Streamlit interface.

---

## 🔄 System Workflow

```text
User Natural-Language Query
            ↓
     Streamlit Interface
            ↓
     LangChain + LLM
            ↓
   Preference Extraction
            ↓
       Fuzzification
            ↓
      Fuzzy Membership
            ↓
       Fuzzy Rules
            ↓
      Rule Evaluation
            ↓
        Aggregation
            ↓
      Defuzzification
            ↓
      Product Scoring
            ↓
    Product Ranking
            ↓
   AI Recommendation Explanation
            ↓
       Final Results
```

---

## 🧠 AI / LLM Component

The project uses **LangChain with an LLM** to perform actual natural-language processing.

The LLM understands free-text queries and extracts relevant product preferences such as:

```text
Product Category
Budget
Camera Importance
Battery Importance
Gaming Importance
Performance Importance
```

For example:

**User input:**

```text
I want a smartphone under ₹30,000
with excellent camera and battery life.
Gaming is also important.
```

The LLM can convert this into structured preferences:

```text
Category: Smartphone
Budget: ₹30,000
Camera: High
Battery: High
Gaming: Medium/High
```

These values are then provided to the Fuzzy Logic recommendation engine.

---

## 🔬 Fuzzy Logic Component

The system uses a genuine **Fuzzy Inference System** rather than simple `if-else` conditions.

The fuzzy system includes:

* Membership functions
* Fuzzification
* Fuzzy rule evaluation
* Rule aggregation
* Defuzzification

Example fuzzy rules:

```text
IF camera is excellent
AND battery is high
THEN recommendation is excellent
```

```text
IF gaming is high
AND performance is high
THEN recommendation is excellent
```

```text
IF camera is good
AND battery is good
THEN recommendation is good
```

The fuzzy system generates a numerical recommendation score that is used to rank the products.

---

## 📊 Example Output

### User Query

```text
I need a smartphone under ₹30,000
with a very good camera, strong battery
and good gaming performance.
```

### Recommended Products

```text
🥇 OnePlus Nord 4
Price: ₹29,999
Fuzzy Recommendation Score: 89.4

🥈 Redmi Note 14 Pro
Price: ₹24,999
Fuzzy Recommendation Score: 84.7

🥉 Samsung Galaxy A55
Price: ₹28,999
Fuzzy Recommendation Score: 82.1
```

The application also provides an AI-generated explanation describing why the recommended products match the user's requirements.

---

## 🌐 Live Deployment

**Live Streamlit Application:**

```text
https://smart-appuct-recommendergit-dydzwgdndchflespm9oz4y.streamlit.app/
```

---

## 💻 GitHub Repository

**Source Code:**

```text
https://github.com/priyal1728/smart-product-recommender
```

---

## 👩‍💻 Student Information

Student Name: Priyal.R.Gandhi
Roll No.: 19013
Class: TYBSCIT
Subject: Indian Knowledge Systems (IKS)
Academic Year: 2026–27

---

## 📚 References

* Streamlit Documentation
* Python Documentation
* LangChain Documentation
* OpenAI API Documentation
* Scikit-Fuzzy Documentation
* NumPy Documentation
* Pandas Documentation
* GitHub Documentation
* AI / Generative AI documentation used for the project

---
