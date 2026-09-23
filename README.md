# 🛡️ CodeSentinel — Repository Risk & Change Intelligence Platform

**Repository-level static analysis, risk scoring, and developer prioritization.**

CodeSentinel is a developer infrastructure tool that analyzes public GitHub repositories, detects potentially risky code structures, evaluates complexity indicators, ranks files by priority, and generates actionable recommendations for developers.

Instead of manually reviewing every file in a repository, CodeSentinel helps answer an important engineering question:

> **Which files should I review or fix first?**

---

## 🚀 Project Overview

Modern software repositories can contain dozens or hundreds of source files. Identifying complex or potentially risky code manually can be time-consuming.

CodeSentinel automates repository-level analysis by:

* Fetching source files from public GitHub repositories.
* Performing multi-file Python code analysis.
* Detecting syntax issues.
* Measuring code complexity indicators.
* Detecting nested loops.
* Evaluating code quality indicators.
* Calculating risk scores.
* Assigning risk levels.
* Ranking files according to priority.
* Generating actionable developer recommendations.
* Presenting repository-level insights through a dashboard.

The platform transforms static code analysis into an actionable **Repository Intelligence** workflow.

---

## ✨ Key Features

### 📂 1. GitHub Repository Analysis

Analyze public GitHub repositories using the following format:

```text
owner/repository
```

Example:

```text
ShivanshiSharma05/ai-code-assistant-test
```

The system fetches supported source files and performs automated multi-file analysis.

---

### 🔍 2. Multi-File Code Analysis

CodeSentinel analyzes multiple files instead of requiring developers to submit individual code snippets.

For each supported file, the system evaluates:

* Syntax issues
* Code complexity indicators
* Loop count
* Nested loops
* Code quality
* Optimization indicators
* Risk level
* Risk score
* Priority score
* Developer recommendations

---

### 🚨 3. Risk Classification

Files are classified according to detected complexity and quality indicators.

| Risk Level | Description                                                                   |
| ---------- | ----------------------------------------------------------------------------- |
| 🔴 HIGH    | Code with higher-risk complexity or structural indicators requiring attention |
| 🟠 MEDIUM  | Code that should be reviewed or improved                                      |
| 🟢 LOW     | Code with relatively low detected risk indicators                             |

> Risk levels are based on the implemented static-analysis and scoring rules. They are indicators for prioritization, not proof of bugs or security vulnerabilities.

---

### 📊 4. Risk Scoring

CodeSentinel calculates risk scores using multiple code characteristics, including:

* Code quality indicators
* Loop count
* Nested loop complexity
* Deeply nested logic
* Complex code structures

Example:

```text
File: complex.py

Risk Level: HIGH
Risk Score: 9
Priority Score: 9
```

---

### 🔥 5. Developer Priority Queue

Files are ranked according to their priority scores.

This helps developers determine:

> **What should I review or fix first?**

The priority ranking allows developers to focus their attention on files with higher detected risk indicators.

---

### 🎯 6. Developer Action Plan

CodeSentinel groups files into actionable categories.

#### 🔥 Fix Immediately

Files with high-risk scores that may require immediate review because of complexity or maintainability indicators.

#### ⚠️ Improve Soon

Files that require additional review, refactoring, or optimization.

#### ✅ Healthy Files

Files with relatively low detected risk indicators and no immediate action suggested by the implemented rules.

---

### 📈 7. Repository Intelligence Dashboard

The Streamlit dashboard provides:

* Total files analyzed
* High-risk file count
* Medium-risk file count
* Low-risk file count
* Risk distribution
* Developer priority queue
* Developer action plan
* Detailed file analysis
* File-level recommendations

---

## 📸 Screenshots

### 1. CodeSentinel Dashboard

The main dashboard provides the repository input interface and platform overview.

![CodeSentinel Dashboard](screenshots/dashboard-home.png)

---

### 2. Repository Overview

The Repository Overview tab displays file counts, risk metrics, and the risk distribution chart.

![Repository Overview](screenshots/repository-overview.png)

---

### 3. Developer Priority Queue

The Priority Queue displays analyzed files ordered by risk score.

![Developer Priority Queue](screenshots/priority-queue.png)

---

### 4. Developer Action Plan

The Action Plan organizes files into review categories and displays recommendations.

![Developer Action Plan](screenshots/action-plan.png)

---

### 5. Detailed File Analysis

The File Details tab provides individual file-level metrics and recommendations.

![Detailed File Analysis](screenshots/file-details.png)

---

## 🏗️ System Architecture

```text
                 ┌─────────────────────────┐
                 │    GitHub Repository    │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │     GitHub Service      │
                 │   Repository Fetching   │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │   Repository Analyzer   │
                 │    Multi-File Analysis  │
                 └────────────┬────────────┘
                              │
               ┌──────────────┼──────────────┐
               ▼              ▼              ▼
      ┌────────────────┐ ┌──────────────┐ ┌──────────────────┐
      │ Code Analysis  │ │ Risk Analysis│ │ Repository       │
      │ Complexity     │ │ Risk Scoring │ │ Intelligence     │
      └────────┬───────┘ └──────┬───────┘ └────────┬─────────┘
               │                │                  │
               └────────────────┼──────────────────┘
                                │
                                ▼
                 ┌─────────────────────────┐
                 │     FastAPI Backend     │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │   Streamlit Dashboard   │
                 └─────────────────────────┘
```

---

## 🛠️ Technology Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* JWT Authentication
* GitHub REST API

### Analysis Engine

* Python AST
* Custom complexity analysis
* Risk analysis
* Repository intelligence
* Priority scoring algorithm

### Frontend and Visualization

* Streamlit
* Pandas
* Matplotlib

---

## 📂 Project Structure

```text
CodeSentinel/
│
├── backend/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── repositories.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── security.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── repository.py
│   │   ├── analysis.py
│   │   └── issue.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── repository.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── repository_analyzer.py
│   │   ├── repository_intelligence.py
│   │   └── risk_analyzer.py
│   │
│   ├── tests/
│   │   └── __init__.py
│   │
│   ├── analyzer.py
│   ├── github_service.py
│   ├── main.py
│   ├── model.py
│   ├── create_tables.py
│   └── requirements.txt
│
├── frontend/
│   └── app.py
│
├── screenshots/
│   ├── dashboard.png
│   └── hard-test.png
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

> The structure above should match the actual repository. If a file or directory has a different name in your current project, use the actual name from your repository.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ShivanshiSharma05/CodeSentinel.git
cd CodeSentinel
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

#### Windows

```powershell
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If your backend uses a separate requirements file, install that file according to the repository structure.

---

## 🔐 Environment Configuration

Create a `.env` file in the appropriate project directory.

Example:

```env
GITHUB_TOKEN=your_github_personal_access_token

DATABASE_URL=postgresql://username:password@localhost:5432/database_name

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### Security Notes

* Do not upload your actual `.env` file to GitHub.
* Do not commit passwords, API tokens, or secret keys.
* Use `.env.example` for configuration documentation.
* Rotate any credential that has accidentally been exposed.

---

## ▶️ Running the Application

### Run the Backend

Open a terminal in the project directory:

```powershell
cd backend
uvicorn main:app --reload
```

Backend server:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

### Run the Frontend

Open a second terminal:

```powershell
cd frontend
streamlit run app.py
```

The Streamlit dashboard will open in your browser.

---

## 🔗 API Endpoints

### Authentication

| Method | Endpoint       | Description               |
| ------ | -------------- | ------------------------- |
| POST   | `/auth/signup` | Register a new user       |
| POST   | `/auth/login`  | Log in a user             |
| GET    | `/auth/me`     | Retrieve the current user |

### Repository Management

| Method | Endpoint                        | Description           |
| ------ | ------------------------------- | --------------------- |
| GET    | `/repositories/`                | Retrieve repositories |
| POST   | `/repositories/`                | Add a repository      |
| GET    | `/repositories/{repository_id}` | Retrieve a repository |
| DELETE | `/repositories/{repository_id}` | Delete a repository   |

### Code Analysis

| Method | Endpoint                     | Description                 |
| ------ | ---------------------------- | --------------------------- |
| POST   | `/generate-code/`            | Generate code               |
| POST   | `/generate-comment/`         | Generate code comments      |
| POST   | `/generate-inline-comments/` | Generate inline comments    |
| POST   | `/analyze/`                  | Analyze code                |
| POST   | `/analyze-repo/`             | Analyze a GitHub repository |

> Verify endpoint names against the current FastAPI routes before making changes to this table.

---

## 🧪 Risk Detection Testing

CodeSentinel was tested using files with different complexity levels:

```text
complex.py
medium.py
simple.py
```

### Example Results

| File         | Complexity | Risk Level | Priority |
| ------------ | ---------- | ---------- | -------- |
| `complex.py` | `O(n^k)`   | 🔴 HIGH    | 9        |
| `medium.py`  | `O(n^k)`   | 🔴 HIGH    | 9        |
| `simple.py`  | `O(1)`     | 🟢 LOW     | 0        |

Example analysis response:

```json
{
  "message": "Repository analysis completed successfully",
  "summary": {
    "total_files": 3,
    "high_risk": 2,
    "medium_risk": 0,
    "low_risk": 1
  }
}
```

The test demonstrates that the system can differentiate between code structures with different detected complexity and risk indicators.

---

## 📊 Example File Analysis

```json
{
  "complex.py": {
    "bugs": "No syntax errors",
    "complexity": "O(n^k)",
    "quality_score": 7,
    "risk_level": "HIGH",
    "risk_score": 9,
    "priority_score": 9,
    "line_count": 22,
    "loop_count": 5,
    "recommendation": "Fix immediately. This file has high complexity or deeply nested logic that may affect performance and maintainability."
  }
}
```

---

## 🧠 Engineering Workflow

CodeSentinel combines repository fetching, static analysis, risk scoring, and file prioritization into one workflow.

```text
GitHub Repository
        │
        ▼
Automatic Multi-File Analysis
        │
        ▼
Complexity Detection
        │
        ▼
Risk Scoring
        │
        ▼
Priority Ranking
        │
        ▼
Developer Action Plan
```

The goal is not to replace general-purpose AI assistants. CodeSentinel focuses on an automated repository-analysis workflow that helps developers identify which files deserve attention first.

---

## 🎯 Key Engineering Contributions

* Built a FastAPI-based backend for repository analysis.
* Integrated GitHub repository fetching.
* Designed multi-file Python static analysis.
* Used Python AST-based analysis and structural indicators.
* Developed risk scoring and priority ranking logic.
* Created a Streamlit dashboard for repository intelligence.
* Added authentication and database-backed repository management.
* Validated risk classification using a test repository with different code complexity levels.

---

## 🔮 Future Improvements

Potential future improvements include:

* Git commit comparison
* Change-based risk regression detection
* Historical repository risk tracking
* Pull request analysis
* GitHub Actions integration
* Code smell detection
* Security analysis integrations
* Support for additional programming languages
* Team-based dashboards
* Repository risk trend analysis

These improvements are optional extensions and are not required for the current project version.

---

## 👩‍💻 Author

**Shivanshi Sharma**

B.Tech Computer Science Engineering

Aspiring Software Engineer | Software Development | AI & Machine Learning Enthusiast

* GitHub: [ShivanshiSharma05](https://github.com/ShivanshiSharma05)
* Project Repository: [CodeSentinel](https://github.com/ShivanshiSharma05/CodeSentinel)

---

## ⭐ Final Takeaway

CodeSentinel transforms repository review from a manual process into a structured workflow:

```text
Manual Repository Review
        │
        ▼
Time-Consuming File Inspection
        │
        ▼
Automated Multi-File Analysis
        │
        ▼
Complexity and Risk Detection
        │
        ▼
Priority Ranking
        │
        ▼
Actionable Developer Recommendations
```

> **CodeSentinel helps developers understand what to review or fix first in their repositories.**
