# Smart Task Priority Predictor - Implementation Plan

This plan outlines the development of the Smart Task Priority Predictor, a Python-based web application designed as an intermediate-level internship project. The application will help users manage tasks and determine their priority using a combination of business rules and a Scikit-learn Decision Tree Classifier.

## User Review Required

> [!IMPORTANT]
> Please review this plan, which is based directly on the provided Software Requirements Specification (SRS).
> You mentioned that this is a group project and that you will provide additional instructions. Please provide them so I can incorporate them before we begin execution.

## Open Questions

- What are the additional instructions for this group project?
- Are there specific portions of this project you want me to focus on, or should we divide the work?

## Proposed Architecture and Phases

We will follow the directory structure and the 12 implementation phases outlined in the SRS.

### Project Structure
```text
smart_task_priority_predictor/
│
├── app.py
├── database.py
├── models.py
├── prediction.py
├── preprocessing.py
├── train_model.py
├── requirements.txt
├── task_priority.db
│
├── data/
│   └── tasks.csv
│
├── models/
│   └── priority_model.pkl
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── tasks.html
│   ├── task_form.html
│   └── task_detail.html
│
├── static/
│   └── style.css
│
└── tests/
    ├── test_priority.py
    ├── test_validation.py
    └── test_tasks.py
```

### Implementation Phases

We will implement the project following the phases defined in Section 22 of the SRS:

- **Phase 1: Setup**
  - Initialize the project structure.
  - Create `requirements.txt` (Flask, pandas, numpy, scikit-learn, joblib, matplotlib, pytest).
  - Set up basic Flask `app.py` with routing skeletons.
- **Phase 2 & 3: Database & CRUD**
  - Implement `database.py` and `models.py` using SQLite.
  - Create tables: Users, Tasks, Predictions, Override History.
  - Implement basic user authentication (registration, login/logout via Flask sessions).
  - Implement task creation, viewing, editing, and deletion routes and templates.
- **Phase 4: Validation & Rules**
  - Add form validation for task inputs.
  - Implement the business rules for the rule-based priority score calculation.
- **Phase 5, 6, 7 & 8: Machine Learning Integration**
  - Implement `preprocessing.py` for data cleaning.
  - Create a synthetic dataset generator or use a sample CSV for `data/tasks.csv`.
  - Implement `train_model.py` to train a Decision Tree Classifier and save it using `joblib`.
  - Connect the loaded model to the Flask application for real-time single-task prediction.
- **Phase 9: Dashboard & UI**
  - Develop the main dashboard.
  - Add simple Matplotlib charts for priority distribution.
  - Style the application using basic HTML, CSS, and Bootstrap.
- **Phase 10: Batch Processing**
  - Implement the CSV batch prediction feature with upload and download capabilities.
- **Phase 11 & 12: Testing & Finalization**
  - Write unit and integration tests using `pytest`.
  - Final review against SRS requirements.

## Verification Plan

### Automated Tests
- Run `pytest tests/` to execute unit tests for priority calculation, validation, and task operations.

### Manual Verification
- Register a new user and log in.
- Create several tasks with varying urgency, impact, effort, and deadlines to verify dynamic priority scoring and model predictions.
- Test manual overrides.
- Upload a sample CSV file to verify batch prediction functionality and result downloads.
- Verify dashboard charts and statistics update correctly.
