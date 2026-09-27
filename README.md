Student Details
Student Name: Pentakota Hemanth
Institution: VIT Bhopal University
Academic Year: 2026–2027

<div align="center">

# 🀏 Deadline Domino
### *Academic Workload & Task Flow Planner*

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#license)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#testing)
[![Dependencies](https://img.shields.io/badge/dependencies-zero--external-orange.svg)](#requirements)

---

**Submitted by:** Pentakota Hemanth (Reg No: `26MIM10061`)  
**Institution:** VIT Bhopal University | **Course:** CSE 1021 - Intro to Problem Solving & Programming  
**Faculty Guide:** Dr. Adarsh Patel | **Academic Year:** 2026–2027  

---

</div>

## 📌 Executive Summary

Academic life often presents students with concurrent, competing commitments—ranging from programming labs and theoretical problem sets to continuous assessment tests and project revisions. Traditional flat task lists present assignments in static chronological or creation order without evaluating the combined impact of effort required and urgency. 

**Deadline Domino** addresses this challenge through a lightweight, algorithmic command-line application that models the "domino effect" of academic task buildup: **when a high-effort, high-urgency task is delayed, it triggers a cascading backlog across all subsequent deadlines.**

---

## 🎯 Key Innovation: The Domino Score Algorithm

Rather than relying on simple creation-date sorting, Deadline Domino dynamically ranks pending tasks using a custom mathematical heuristic:

$$\text{Domino Score} = \text{Estimated Hours} \times \text{Urgency Weight}$$

Where:
* **Estimated Hours ($H$):** Positive integer representing total duration required.
* **Urgency Level ($U$):** Discrete scalar assigned by the user:
  * `1` = Low Urgency
  * `2` = Medium Urgency
  * `3` = High Urgency

### Repeated-Selection Ranking Engine
The system processes tasks using a custom **Repeated-Selection Algorithm** operating directly on nested list structures without reliance on standard built-in sorting routines (`sort()`) or third-party ORMs/libraries.

```text
       [ Task: Python Lab (6 hrs, Urgency 3) ] ──> Domino Score = 18 (CRITICAL)
                         │
                         ▼
       [ Task: Math Homework (2 hrs, Urgency 2) ] ──> Domino Score = 4
                         │
                         ▼
       [ Task: English Essay (1 hr, Urgency 1) ] ──> Domino Score = 1
```

---

## ✨ Features

- 📝 **Task Management**: Full task board tracking title, subject, estimated hours, urgency, score, and state.
- 🧮 **Algorithmic Prioritization**: Auto-generates domino execution sequences based on risk metrics.
- 📊 **Workload Analytics**: Categorizes systemic academic risk dynamically:
  - `CLEAR`: 0 pending hours
  - `LIGHT`: 1–5 pending hours
  - `BUSY`: 6–12 pending hours
  - `DOMINO RISK`: > 12 pending hours
- 📚 **Subject Aggregation**: Real-time per-course workload accumulation and reporting.
- 🛡️ **Fault-Tolerant CLI**: Defensive input validation intercepting non-numeric inputs, empty strings, and out-of-bounds selections.
- 🧪 **Unit Testing Framework**: Integrated test suites for system verification.

---

## 📂 Project Structure

```text
Deadline_Domino/
│
├── main.py                     # Primary entry-point driver & CLI menu interface
├── requirements.txt            # Zero-dependency specification
├── README.md                   # System documentation & usage manual
├── PROJECT_REPORT.md           # Formal academic submission report
├── PROJECT_STATEMENT.md        # Technical problem definition
│
├── src/                        # Modular application components
│   ├── assignments.py          # Task lifecycle & management operations
│   ├── attendance.py           # Attendance tracking module
│   ├── database.py             # SQLite data access layer
│   ├── performance.py          # Marks & academic grading system
│   ├── reports.py              # Workload risk & analytics engine
│   ├── student.py              # Student profile management
│   ├── study_planner.py        # Study session planner
│   └── validation.py           # Robust CLI input validation wrappers
│
└── tests/                      # Automated unit testing suite
    └── test_modules.py         # Test cases for modules and pipeline validation
```

---

## ⚙️ Requirements & System Prerequisites

- **Runtime Environment:** Python 3.10 or higher recommended.
- **External Dependencies:** **None.** Uses pure Standard Library packages (`sqlite3`, `unittest`, `sys`, `os`).

---

## 🚀 Quick Start & Execution

### 1. Clone or Extract the Project
```bash
git clone https://github.com/your-username/Deadline-Domino.git
cd Deadline-Domino
```

### 2. Run the Application
Execute the entry-point script in your terminal:

**Windows:**
```powershell
python main.py
```

**Linux / macOS:**
```bash
python3 main.py
```

---

## 🧪 Running Unit Tests

To execute the automated test suite and check system stability across boundary conditions and edge cases, run:

```bash
python -m unittest discover -s tests -v
```

---

## 💻 Sample Terminal Session

```text
===================================================================
   DEADLINE DOMINO - ACADEMIC WORKLOAD & TASK FLOW PLANNER
===================================================================
1. Add New Task
2. View Current Task Board
3. Show Domino Priority Order (Highest Workload First)
4. Mark Task as Completed
5. Delete Task
6. View Workload Risk Report
7. View Subject Summary
8. Exit System
-------------------------------------------------------------------
Select an option (1-8): 3

--- DOMINO PRIORITY ORDER (HIGHEST WORKLOAD FIRST) ---
1. Python Lab Report    | Subject: CSE101     | Score: 18
2. Mathematics Sets     | Subject: MAT201     | Score: 6
3. Physics Seminar      | Subject: PHY102     | Score: 4
```

---

## 🗺️ Roadmap & Future Enhancements

- [ ] **File I/O Persistence:** JSON/CSV fallback export for offline portability.
- [ ] **Calendar Integration:** Native `datetime` parsing for automated countdowns.
- [ ] **Heuristic Scheduling:** Implementation of Shortest Job First (SJF) and Earliest Deadline First (EDF) strategies.
- [ ] **Desktop GUI:** Tkinter-based interactive visual task board.

---

## 📜 License

This project is submitted as an academic submission for **VIT Bhopal University**. Licensed under the [MIT License](LICENSE).