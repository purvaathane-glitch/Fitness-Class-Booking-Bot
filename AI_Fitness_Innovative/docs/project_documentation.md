📘 Project Documentation
AI Predictive Gym Engagement System---

1️⃣ Problem Statement

Gym businesses often struggle with member retention. 
This project aims to predict member retention risk, renewal probability, and fitness progress using machine learning.

2️⃣ Objectives

- Predict gym member retention risk
- Calculate renewal probability
- Recommend personalized engagement plans
- Forecast projected weight after 8 weeks
- Provide analytics visualization
- Build a user-friendly web interface

3️⃣ Methodology

1. Collect engagement-related input:
   - Attendance
   - Consistency Score
   - Weight
   - Goal

2. Train Machine Learning model using Scikit-Learn.
3. Use Flask framework to deploy model.
4. Display predictions dynamically on web page.
5. Generate analytics graph.

4️⃣ ML Algorithm Used

Linear Regression (Scikit-Learn)

Why?
- Simple
- Efficient
- Suitable for numerical prediction
- Easy deployment in Flask

5️⃣ Dataset Used

A synthetic (manually created) dataset was used for training.

Features:
- Attendance (0–30)
- Consistency Score (1–10)
- Weight
- Goal category

Target:
- Retention probability
- Risk classification
- Weight forecast

6️⃣ Architecture Diagram

User Input (HTML Form)
        ↓
Flask App (app.py)
        ↓
Machine Learning Model (train_model.py)
        ↓
Prediction Logic
        ↓
Result Display Page
        ↓
Analytics Graph (Matplotlib)

7️⃣ Screenshots

(Insert screenshots of:)
- Home Page
- Prediction Result
- Analytics Dashboard
- GitHub Repository

8️⃣ Future Scope

- Real dataset integration
- Database support
- Admin dashboard
- Cloud deployment
- AI chatbot integration
- Mobile application version

👩‍💻 Developed By

Purva Shital Athane
