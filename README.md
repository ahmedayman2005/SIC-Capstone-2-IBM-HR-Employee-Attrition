#  Capstone Project 2 — IBM HR Analytics Employee Attrition Prediction
Samsung Innovation Campus — AI Track

---

##  Problem Statement  
Employee attrition is one of the costliest challenges for HR teams.  
Replacing an employee leads to:

- Loss of experience  
- Lower productivity  
- Higher onboarding costs  

Key questions addressed:

- Does salary influence attrition?  
- Do younger employees leave more?  
- Does poor work–life balance cause turnover?  
- Which departments have the highest attrition?  

---

##  Target Audience  
- **HR Managers** → detect at-risk employees early  
- **Data Analysts** → support retention strategies  

---

##  Project Files  
| File | Description |
|------|-------------|
| `Capstone 2 IBM HR Employee Attrition.ipynb` | Complete data analysis, preprocessing & modeling |
| `SIC Capstone 2 Presentation.pdf` | Final project presentation |
| `app.py` | Streamlit deployment script |
| `data/` | Dataset used |

---

##  Dataset Overview  
- Shape: **1470 rows × 35 columns**  
- Contains both **numerical** and **categorical** features  
- Important features include:  
  - Age  
  - MonthlyIncome  
  - TotalWorkingYears  
  - YearsAtCompany  
  - JobRole  
  - OverTime  
  - BusinessTravel  
  - WorkLifeBalance  
  - Satisfaction scores  

---

##  Data Preprocessing  
Data cleaning & preprocessing included:

- Creating categorical bins  
- Dropping columns with a single value  
- Encoding categorical features  
- Standard scaling for numerical features  

---

##  Key Visual Insights  

### **1️⃣ Income vs Attrition**  
Employees with **lower monthly incomes leave more often**.

### **2️⃣ Age + Years at Company**  
Young and new employees have the **highest attrition rates**.

### **3️⃣ Total Working Years**  
Attrition is highest during the **first 0–2 years**, then declines.

### **4️⃣ Department Breakdown**  
- Sales → highest attrition (20.6%)  
- R&D → lowest (13.8%)

### **5️⃣ Education Level**  
Employees with **lower education levels leave the most**.

### **6️⃣ Work-Life Balance**  
Poor work–life balance → **31.2% attrition**  
Good balance → significantly lower.

---

##  Dashboard  
An interactive dashboard visualizes attrition by:

- Gender  
- Salary  
- Job Role  
- Marital status  
- Education  
- Department  

---

##  Modeling & Performance  
Models applied:

- Logistic Regression  
- Random Forest  
- SVM  
- XGBoost  

Model optimization:

- **GridSearchCV**  
- **RandomizedSearchCV**  
- **SMOTEENN** for handling class imbalance  

### **Top Features (Random Forest)**  
- MonthlyIncome  
- JobLevel  
- TotalWorkingYears  
- StockOptionLevel  
- Age  
- DailyRate  
- YearsAtCompany  

---

##  Deployment (Streamlit App)  
The deployed app uses **8 key features**:

- Job Level  
- Percent Salary Hike  
- Years With Manager  
- Number of Companies Worked  
- Total Working Years  
- Age  
- Monthly Income  
- Distance From Home  

---

##  Insights Summary  
- No training → **25% attrition**  
- Very unhappy employees → **20% attrition**  
- Frequent travel increases attrition  
- Low work involvement increases attrition  

---

##  Limitations  
- Small sample size  
- Missing education levels  
- Limited job diversity  
- Lacks external factors  

---

##  Requirements  
Install all dependencies:

```bash
pip install -r requirements.txt
