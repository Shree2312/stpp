## SMART TASK PRIORITY PREDICTOR

## Software Requirements Specification (SRS)

## 1. Introduction

## 1.1 Project Overview

Smart Task Priority Predictor is a Python-based web application that helps users decide which tasks should be handled first. The system collects simple task information such as deadline, urgency, business impact, estimated effort, and number of dependencies. It then calculates a priority score and uses a basic machine-learning classification model to suggest a priority category.

The project is designed as an intermediate-level internship project. The main learning focus is on Python programming, Flask API development, SQLite database handling, Pandas data processing, basic machine learning with Scikit-learn, form validation, CRUD operations, CSV processing, and basic testing.

| Item | Description |
| --- | --- |
| Project Name | Smart Task Priority Predictor |
| Domain | Python Web Development + Basic Data Analytics + Basic Machine Learning |
| Target Users | Project members, team leads, and individual users |
| Main Purpose | Suggest a suitable priority for tasks |
| Primary Output | Priority category and priority score |
| Application Type | Web application |
| Difficulty | Intermediate |

## 1.2 Problem Statement

Users may have several tasks with different deadlines, effort requirements, urgency levels, business impacts, and dependencies. Manually comparing all these factors can be time-consuming and inconsistent. The system provides a simple and repeatable way to calculate and suggest task priority.

## 1.3 Purpose

- Allow users to create and manage tasks.

- Calculate a priority score using understandable business rules.

- Use a basic machine-learning model to suggest Low, Medium, High, or Critical priority.

- Display the reasons that affected the score using simple rule-based messages.

- Allow users to manually change the suggested priority.

- Store task and prediction history for later analysis.

- Provide CSV upload for basic batch prediction

## 1.4 Scope

## In Scope:

- User registration and login using simple Flask session handling.

- Task creation, viewing, editing, deletion, and status updates.

- SQLite database for application data.

- Synthetic or CSV-based task dataset.

- Basic data cleaning and feature preparation with Pandas.

- Priority score calculation using weighted rules.


- Decision Tree Classifier using Scikit-learn.

- Basic model evaluation using accuracy and classification report.

- Simple explanation based on task values and business rules.

- CSV batch prediction.

- Basic charts for task priority distribution.

- Unit and integration testing with Pytest.

## Out of Scope:

- Cloud platforms and cloud deployment.

- Docker or container orchestration.

- CI/CD pipelines and GitHub Actions.

- Jira, Slack, Teams, Asana, Trello, or calendar integrations.

- PostgreSQL or other enterprise database systems.

- JWT/OAuth authentication.

- SHAP, LIME, XGBoost, deep learning, NLP, LLMs, or generative AI.

- Automatic model drift detection or automatic retraining.

- Advanced resource allocation or team scheduling.

- Mobile application development.

- Real-time distributed processing.

## 2. System Architecture

## 2.1 Logical Architecture

The system follows a simple three-part structure. The user interacts with the Flask web interface. Flask handles validation, task operations, and prediction requests. SQLite stores application data, while the machine-learning module loads a saved Scikit-learn model.

| Component | Responsibility |
| --- | --- |
| HTML/CSS Web Interface | Forms, task list, dashboard, prediction result display. |
| Flask Application | Routes, validation, session handling, task operations, prediction flow. |
| SQLite Database | Users, tasks, predictions, and override history. |
| Pandas Module | CSV reading, cleaning, feature preparation, and batch processing. |
| Scikit-learn Model | Basic classification of task priority. |
| Priority Rule Module | Calculates a simple score and creates readable reasons. |
| Joblib Model File | Stores the trained model for later predictions. |

## 2.2 Basic Prediction Flow

- 1. User enters task information.

- 2. Flask validates the entered values.

- 3. The system calculates simple derived values such as days remaining.

- 4. The rule-based priority score is calculated.

- 5. The trained Decision Tree model predicts a priority category.

- 6. The application compares the model result with the score range.

- 7. The final priority category and score are shown to the user.

- 8. Simple reasons are displayed based on deadline, urgency, impact, effort, and dependencies.

- 9. The prediction is stored in SQLite.


## 3. Project Objectives

- 10. Build a working Flask web application for task management.

- 11. Implement basic CRUD operations using SQLite.

- 12. Create a simple and understandable priority scoring formula.

- 13. Prepare a task dataset using Pandas.

- 14. Train a Decision Tree Classifier using Scikit-learn.

- 15. Evaluate the model using a test dataset.

- 16. Provide a clear priority result without advanced explainability libraries.

- 17. Support CSV batch prediction for a reasonable number of records.

- 18. Allow manual priority overrides with a stored reason.

- 19. Write basic unit and integration tests.

## 4. Functional Requirements

## 4.1 User Management

| ID | Requirement |
| --- | --- |
| FR-01 | The system shall allow a user to register with name, email, and password. |
| FR-02 | The system shall allow a registered user to log in and log out. |
| FR-03 | The system shall keep the logged-in user in a Flask session. |
| FR-04 | A user shall only view and modify their own tasks. |

## 4.2 Task Management

| ID | Requirement |
| --- | --- |
| FR-05 | Users shall create new tasks. |
| FR-06 | Users shall view a list of their tasks. |
| FR-07 | Users shall edit task details. |
| FR-08 | Users shall delete tasks. |
| FR-09 | Users shall update task status. |
| FR-10 | Users shall search and filter tasks by status and priority. |
| FR-11 | Tasks shall be displayed in priority order when requested. |

## 4.3 Task Input Fields

| Field | Type | Rule |
| --- | --- | --- |
| Task Name | Text | Required |
| Description | Text | Optional |
| Deadline | Date | Required; should not be before creation date |
| Estimated Effort | Decimal | Greater than 0 |
| Business Impact | Integer | 1 to 10 |
| Urgency | Integer | 1 to 10 |
| Dependency Count | Integer | 0 or greater |
| Task Type | Choice | Development, Testing, Design, Documentation, Other |
| Status | Choice | Not Started, In Progress, Blocked, Completed, Cancelled |

## 4.4 Prediction Requirements

| ID | Requirement |
| --- | --- |
| FR-12 | The system shall calculate a priority score from 0 to 100. |
| FR-13 | The system shall classify tasks as Low, Medium, High, or Critical. |
| FR-14 | The system shall use a Decision Tree Classifier for basic prediction. |
| FR-15 | The system shall show the predicted score and category. |
| FR-16 | The system shall show simple rule-based reasons for the result. |
| FR-17 | The system shall store each prediction with the task. |


## 4.5 Manual Override

- The user can select a different priority after seeing the prediction.

- A reason is required for the override.

- The original prediction and the new priority are stored.

## 5. Business Rules

| Rule ID | Rule Description | Implementation |
| --- | --- | --- |
| BR-01 | Completed tasks are not given a new priority. | Check status before prediction. |
| BR-02 | Cancelled tasks are not included in priority ranking. | Exclude cancelled tasks. |
| BR-03 | Deadline cannot be earlier than creation date. | Date validation. |
| BR-04 | Business impact must be between 1 and 10. | Range validation. |
| BR-05 | Urgency must be between 1 and 10. | Range validation. |
| BR-06 | Estimated effort must be greater than 0. | Positive-value validation. |
| BR-07 | A task with a deadline today receives high deadline | Score rule. |
|   | points. |   |
| BR-08 | An overdue task receives the highest deadline points. | Score rule. |
| BR-09 | Four or more dependencies add extra priority points. | Dependency rule. |
| BR-10 | Manual priority changes must have a reason. | Required override field. |

## 6. Priority Calculation Logic

The scoring logic is intentionally simple so that interns can understand and implement it without advanced mathematics. The score is calculated from four main factors: business impact, urgency, deadline, and dependencies. Effort is used as a small adjustment.

## 6.1 Score Formula

The score is then adjusted for effort and limited to a range of 0 to 100.

## 6.2 Deadline Points

| Deadline Situation | Points |
| --- | --- |
| Overdue | 20 |
| Due today or within 2 days | 15 |
| Due within 7 days | 10 |
| Due within 14 days | 7 |
| More than 14 days | 3 |

## 6.3 Effort Adjustment

- Estimated effort below 3 hours: add 5 points because the task is a quick win.

- Estimated effort above 20 hours: subtract 5 points.

- Other effort values: no adjustment.

## 6.4 Score to Priority Mapping

| Score | Priority |
| --- | --- |
| 80-100 | Critical |
| 60-79 | High |
| 40-59 | Medium |
| 0-39 | Low |


## 7. Machine Learning Requirements

## 7.1 ML Approach

The machine-learning part is limited to a single supervised classification problem. A Decision Tree Classifier is recommended because it is easy for interns to understand, train, visualize, and explain. The model predicts one of four classes: Low, Medium, High, and Critical.

## 7.2 Input Features

- Days to deadline

- Estimated effort

- Business impact

- Urgency

- Dependency count

- Task type

## 7.3 Target

Priority_Label with four possible values: Low, Medium, High, Critical.

## 7.4 Training Process

- 20. Load the dataset using Pandas.

- 21. Check required columns and data types.

- 22. Remove or fill simple missing values.

- 23. Convert task type into numeric columns using one-hot encoding.

- 24. Create days-to-deadline.

- 25. Split the dataset into 80% training and 20% testing data.

- 26. Train a Decision Tree Classifier.

- 27. Evaluate the model on the test data.

- 28. Save the trained model using Joblib.

## 7.5 Model Evaluation

| Metric | Purpose | Suggested Target |
| --- | --- | --- |
| Accuracy | Overall percentage of correct predictions. | >= 75% |
| Precision | Checks how often predicted classes are correct. | >= 70% |
| Recall | Checks how many relevant cases are identified. | >= 70% |
| F1-Score | Balances precision and recall. | >= 70% |

The target values are practical internship-level goals rather than strict production guarantees. The model must be evaluated on unseen test data.

## 8. Dataset Requirements

## 8.1 Dataset Source

During development, interns may generate a synthetic dataset using Python or prepare a CSV file with realistic task examples. The dataset should contain enough examples for each priority category.


## 8.2 Dataset Fields

| Field | Type | Description |
| --- | --- | --- |
| task_id | Integer | Unique task identifier |
| created_date | Date | Task creation date |
| deadline_date | Date | Expected completion date |
| estimated_effort | Decimal | Expected effort in hours |
| business_impact | Integer | Business value from 1 to 10 |
| urgency | Integer | Urgency from 1 to 10 |
| dependency_count | Integer | Number of dependent tasks |
| task_type | Text | Task category |
| priority_label | Text | Low, Medium, High, Critical |

## 8.3 Simple Data Generation Logic

```
score = (impact * 4) + (urgency * 3) + (dependency_count * 2) + deadline_points
if effort < 3:
score += 5
elif effort > 20:
score -= 5
score = max(0, min(100, score))
if score >= 80:
label = "Critical"
elif score >= 60:
label = "High"
elif score >= 40:
label = "Medium"
else:
label = "Low"
```

## 9. Data Preprocessing

- 29. Read the CSV file using Pandas.

- 30. Check that all required columns are present.

- 31. Convert date columns into date format.

- 32. Check numerical values and valid ranges.

- 33. Fill simple missing numerical values using the median when appropriate.

- 34. Fill missing task type values with 'Other'.

- 35. Remove duplicate task IDs.

- 36. Calculate days-to-deadline.

- 37. Convert task type to numeric columns using one-hot encoding.

- 38. Split the data into training and testing data before training.

The preprocessing logic should be kept in a separate Python file so it can be reused during training and prediction.


## 10. Prediction Service

## 10.1 Single Prediction Flow

- 39. Receive task details from the Flask form.

- 40. Validate the input.

- 41. Calculate days to deadline.

- 42. Calculate the priority score.

- 43. Load the saved Decision Tree model.

- 44. Prepare the model input in the same format used during training.

- 45. Get the predicted priority class.

- 46. Use the score ranges as the final priority if the model and score disagree.

- 47. Generate simple reasons using rules.

- 48. Save the prediction.

- 49. Display the result.

## 10.2 Explanation Logic

No SHAP, LIME, or other advanced explainability technology is required. The application creates three simple messages from the input values.

- High urgency: 'Urgency is high and increases the priority.'

- High business impact: 'Business impact is high and increases the priority.'

- Near deadline: 'The deadline is close and increases the priority.'

- Many dependencies: 'The task has several dependencies and may affect other work.'

- Very high effort: 'High effort slightly reduces the score.'

- Quick win: 'Low effort makes this a useful quick-win task.'

## 11. Batch Prediction

- User uploads a CSV file through the web interface.

- The system checks required columns.

- Invalid rows are reported with simple error messages.

- Valid rows are processed using the same prediction logic as single tasks.

- The results include the original task information, priority score, and priority label.

- The user can download the results as a CSV file.

Recommended internship limit: up to 500 tasks per upload for the initial version.

## 12. API Requirements

The application uses Flask routes. The API is intentionally small and suitable for learning.

| Method | Route | Purpose |
| --- | --- | --- |
| GET | / | Open dashboard/login page. |
| POST | /register | Create a user account. |
| POST | /login | Log in a user. |
| GET | /logout | Log out the user. |
| GET | /tasks | Display user's tasks. |
| GET | /tasks/create | Display task creation form. |
| POST | /tasks/create | Create task and generate prediction. |
| GET | /tasks/<id> | View task details. |
| GET/POST | /tasks/<id>/edit | Edit task. |
| POST | /tasks/<id>/delete | Delete task. |
| POST | /tasks/<id>/override | Override priority. |
| POST | /predict | Predict priority for entered task data. |
| POST | /predict/batch | Process uploaded CSV. |
| GET | /download/<file> | Download batch result. |


## 13. Database Design

## 13.1 Users Table

| Column | Type | Description |
| --- | --- | --- |
| user_id | Integer | Primary key |
| name | Text | User name |
| email | Text | Unique email |
| password | Text | Stored password value for the local internship project |
| created_at | DateTime | Registration time |

## 13.2 Tasks Table

| Column | Type | Description |
| --- | --- | --- |
| task_id | Integer | Primary key |
| user_id | Integer | Task owner |
| title | Text | Task name |
| description | Text | Optional description |
| deadline | Date | Task deadline |
| estimated_effort | Float | Estimated hours |
| business_impact | Integer | 1 to 10 |
| urgency | Integer | 1 to 10 |
| dependency_count | Integer | Number of dependencies |
| task_type | Text | Task category |
| status | Text | Current task status |
| created_at | DateTime | Creation time |

## 13.3 Predictions Table

| Column | Type | Description |
| --- | --- | --- |
| prediction_id | Integer | Primary key |
| task_id | Integer | Related task |
| priority_score | Float | Score from 0 to 100 |
| priority_label | Text | Low/Medium/High/Critical |
| model_prediction | Text | Decision Tree result |
| created_at | DateTime | Prediction time |

## 13.4 Override History Table

| Column | Type | Description |
| --- | --- | --- |
| override_id | Integer | Primary key |
| task_id | Integer | Related task |
| original_priority | Text | Original priority |
| new_priority | Text | User-selected priority |
| reason | Text | Reason for changing priority |
| created_at | DateTime | Override time |


## 14. Frontend/UI Requirements

## 14.1 Login/Register

- Registration form with name, email, and password.

- Login form with email and password.

- Simple validation messages.

## 14.2 Dashboard

- Total tasks.

- Critical, High, Medium, and Low task counts.

- Overdue task count.

- Simple bar chart of priority distribution.

- Recent tasks list.

## 14.3 Task List

- Task name.

- Deadline.

- Priority.

- Priority score.

- Status.

- Edit and delete actions.

- Search and filter options.

## 14.4 Task Creation/Edit

- Form containing all required task fields.

- Validation before submission.

- Prediction result after submission.

- Priority score and category display.

- Simple explanation messages.

- Manual override option.

## 14.5 Batch Prediction Page

- CSV upload control.

- Validation message for incorrect files.

- Prediction result preview.

- Download button.

## 15. Error Handling

| Situation | Expected Response |
| --- | --- |
| Missing required field | Show validation message beside the field. |
| Invalid impact/urgency | Show message that value must be 1-10. |
| Invalid effort | Show message that effort must be greater than 0. |
| Invalid deadline | Ask user to enter a valid deadline. |
| Incorrect login | Show 'Invalid email or password'. |
| Task not found | Show a simple not-found page. |
| Invalid CSV | Show missing/incorrect column details. |
| Model file missing | Show prediction service error and log the problem. |
| Database error | Show a general error message and log the error. |


## 16. Security Requirements

Security is kept at a basic internship level. The project should demonstrate safe input handling and user access without introducing advanced authentication infrastructure.

- Use Flask sessions for login state.

- Validate all form inputs on the server side.

- Use parameterized SQLite queries or SQLAlchemy ORM to avoid unsafe SQL construction.

- Do not display internal error details to users.

- Keep the secret key in a local configuration file or environment variable.

- Users should only access their own tasks.

- Do not store unnecessary personal information.

Advanced requirements such as JWT, OAuth, rate limiting, enterprise identity management, HTTPS infrastructure configuration, and API gateways are intentionally excluded.

## 17. Testing Requirements

## 17.1 Unit Testing

| Area | Tests |
| --- | --- |
| Priority Score | Check score for low, medium, high, overdue, and dependency cases. |
| Validation | Check invalid impact, urgency, effort, and deadline. |
| Feature Preparation | Check days-to-deadline and task-type encoding. |
| Prediction | Check that the model returns one of four valid labels. |
| Database | Check task create, read, update, and delete operations. |

## 17.2 Integration Testing

- Login -> task creation -> prediction -> database save.

- Task edit -> new prediction -> database update.

- Task override -> override history save.

- CSV upload -> prediction -> result download.

## 17.3 Acceptance Criteria

- A user can register and log in successfully.

- A user can create, view, edit, and delete tasks.

- Invalid task inputs are rejected.

- A valid task receives a score from 0 to 100.

- A valid task receives one of four priority labels.

- Prediction details are saved in SQLite.

- Manual overrides are saved with a reason.

- CSV batch prediction works for valid files.

- The basic ML model achieves a reasonable test result, with 70%+ accuracy as an initial target.

## 18. Logging and Basic Monitoring

Only simple application logging is required. Interns should use Python's logging module to record important development and application events.

- Application started.

- User login success/failure.

- Task created/updated/deleted.

- Prediction generated.

- CSV processing started/completed.

- Unexpected errors.


Advanced model drift dashboards, time-series monitoring, automatic alerts, and performance monitoring platforms are not required.

## 19. Configuration Requirements

| Setting | Example |
| --- | --- |
| FLASK_SECRET_KEY | Local secret value |
| DATABASE_PATH | task_priority.db |
| MODEL_PATH | models/priority_model.pkl |
| DATA_PATH | data/tasks.csv |
| DEBUG | True during development |

## 20. Technology Stack

| Layer | Technology | Level / Purpose |
| --- | --- | --- |
| Language | Python | Core programming |
| Web Framework | Flask | Basic web application and routes |
| Database | SQLite | Local relational database |
| Data Processing | Pandas | CSV and data preparation |
| Numerical Processing | NumPy | Basic calculations |
| Machine Learning | Scikit-learn | Decision Tree Classifier |
| Model Saving | Joblib | Save/load trained model |
| Frontend | HTML + CSS + Bootstrap | Simple user interface |
| Charts | Matplotlib | Basic dashboard charts |
| Testing | Pytest | Unit and integration tests |
| Version Control | Git | Source code management |

The above stack is intentionally limited to commonly understandable technologies. No cloud service, CI/CD platform, container platform, enterprise database, advanced ML library, or AI service is required.


## 21. Project Folder Structure

## 22. Implementation Phases

| Phase | Work | Expected Skill |
| --- | --- | --- |
| Phase 1 | Set up Flask project and basic pages. | Python + Flask basics |
| Phase 2 | Create SQLite database and tables. | Python + SQLite |
| Phase 3 | Implement task CRUD operations. | Flask routes + database |
|   |   | operations |
| Phase 4 | Implement validation and business rules. | Python conditions + form |
|   |   | validation |
| Phase 5 | Prepare task dataset using Pandas. | Pandas + basic data cleaning |
| Phase 6 | Create priority score calculation. | Python logic + arithmetic |
| Phase 7 | Train Decision Tree Classifier. | Scikit-learn basics |
| Phase 8 | Connect saved model to Flask. | Python + Joblib + Flask |
| Phase 9 | Add dashboard and charts. | HTML/CSS + Matplotlib |
| Phase 10 | Add CSV batch prediction. | Pandas + file handling |
| Phase 11 | Write tests and fix issues. | Pytest + debugging |
| Phase 12 | Prepare documentation and local demo. | Documentation + |
|   |   | presentation |


## 23. Risks and Mitigation

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Small or unbalanced dataset | Medium | Create more realistic examples and check class counts. |
| Poor model accuracy | Medium | Clean data, review features, and tune simple Decision Tree |
|   |   | settings. |
| Incorrect user input | Medium | Validate all fields before prediction. |
| Wrong priority suggestion | High | Show score/reasons and allow manual override. |
| CSV format errors | Medium | Validate columns and report invalid rows. |
| Database mistakes | Medium | Use simple schema and test CRUD operations. |
| Model file missing | Medium | Show a clear error and provide a training step. |

## 24. Assumptions and Constraints

## 24.1 Assumptions

- Users provide reasonably accurate urgency, impact, and effort values.

- The initial dataset can be synthetic.

- The application is primarily used on a local development machine.

- The model is retrained manually when the dataset changes.

- Users understand that the prediction is a recommendation and not a guaranteed decision.

## 24.2 Constraints

- SQLite is intended for the internship version and small datasets.

- The application does not provide enterprise-scale deployment.

- Only basic machine learning is required.

- Batch prediction is intended for small to medium CSV files.

- No external project-management integrations are required.

## 25. Future Enhancements

- Use a larger real-world task dataset.

- Try Random Forest after the basic Decision Tree version is complete.

- Add more task filters and dashboard charts.

- Add email notifications in a future version.

- Add project-level task grouping.

- Add user feedback analysis.

- Add deployment to a simple hosting environment as a separate project phase.

Advanced features such as LLM integration, generative AI, deep learning, automatic retraining, cloud orchestration, real-time drift detection, and external project-management integrations are deliberately left outside this internship version.

## 26. Deliverables

- 50. Working Flask web application.

- 51. SQLite database file and database setup script.

- 52. Training dataset or synthetic dataset generator.

- 53. Data preprocessing script.

- 54. Priority scoring module.

- 55. Trained Decision Tree model file.

- 56. Single-task prediction functionality.

- 57. CSV batch prediction functionality.

- 58. Basic dashboard with charts.


- 59. Unit and integration test files.

- 60. README with installation and execution instructions.

- 61. Final project demonstration.

## 27. Installation and Execution

Recommended local setup:

- 62. Install Python 3.10 or later.

- 63. Create a virtual environment.

- 64. Install packages from requirements.txt.

- 65. Create or load the SQLite database.

- 66. Prepare the training dataset.

- 67. Run train_model.py to train and save the model.

- 68. Run app.py.

- 69. Open the local Flask application in a browser.

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python train_model.py
python app.py
```

## 28. Recommended requirements.txt

```
Flask
pandas
numpy
scikit-learn
joblib
matplotlib
pytest
```

## 29. Intern Skill Expectations

The project is intentionally structured around skills that an intern can learn and demonstrate during a normal internship. The expected skills are intermediate rather than advanced.

| Skill Area | Expected Ability |
| --- | --- |
| Python | Functions, lists/dictionaries, conditions, loops, modules, file handling, exceptions |
| Flask | Routes, forms, templates, request handling, sessions |
| SQLite | Tables, primary/foreign keys, CRUD queries |
| Pandas | Read CSV, clean data, create columns, filter rows |
| Machine Learning | Train/test split, Decision Tree, prediction, basic metrics |
| Web UI | HTML forms, CSS, Bootstrap basics |
| Testing | Write simple unit tests and API/route tests |
| Debugging | Read errors, use print/logging, isolate and fix issues |
| Git | Basic add, commit, branch, and push workflow |

## 30. Final Acceptance Criteria

- 70. The application starts successfully on a local machine.

- 71. A user can register, log in, and log out.

- 72. A logged-in user can create and manage tasks.

- 73. The application validates task inputs correctly.

- 74. A priority score between 0 and 100 is generated.


- 75. The system displays Low, Medium, High, or Critical priority.

- 76. A Decision Tree model is used for the basic prediction component.

- 77. The prediction can be stored and viewed with the task.

- 78. Users can override a prediction with a reason.

- 79. CSV batch prediction produces a downloadable result.

- 80. The dashboard displays basic task counts and a priority chart.

- 81. Core functionality is covered by basic automated tests.

- 82. The project can be demonstrated without cloud services or advanced infrastructure.

## Appendix A: Simple Prediction Example

| Input | Example Value |
| --- | --- |
| Deadline | 2 days from today |
| Estimated Effort | 6 hours |
| Business Impact | 9/10 |
| Urgency | 9/10 |
| Dependencies | 4 |
| Task Type | Development |

Example calculation: business impact contributes 36 points, urgency contributes 27 points, four dependencies contribute 8 points, and a near deadline contributes 15 points. The initial score is therefore 86 before any effort adjustment, resulting in a Critical priority.

## Appendix B: Simple Model Training Pseudocode

```
load dataset
clean dataset
create days_to_deadline
encode task_type
split X and y
split into training and testing sets
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(accuracy_score(y_test, predictions))
save model using joblib
```

## Appendix C: Version Change Summary

| Removed / Simplified | Intermediate Replacement |
| --- | --- |
| FastAPI | Flask |
| PostgreSQL | SQLite |
| JWT authentication | Flask session login |
| XGBoost / Gradient Boosting | Decision Tree Classifier |
| Classification + Regression | Classification + simple rule-based score |
| SHAP / LIME | Rule-based explanation messages |
| Model drift monitoring | Basic manual model evaluation |
| Model registry / rollback | Single saved model file |
| Docker / Docker Compose | Local Python execution |
| CI/CD | Basic Git workflow |
| Advanced performance monitoring | Python logging |
| Large-scale batch processing | Small CSV batch processing |
