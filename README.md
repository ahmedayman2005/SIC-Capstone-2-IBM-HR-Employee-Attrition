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
From page 7 of the presentation:  
- **HR Managers** → detect at-risk employees early  
- **Data Analysts** → support retention strategies  
:contentReference[oaicite:3]{index=3}

---

##  Project Files  
| File | Description |
|------|-------------|
| `Capstone 2 IBM HR Employee Attrition.ipynb` | Complete analysis, preprocessing, modeling |
| `SIC Capstone 2 Presentation.pdf` | Presentation slides with visuals and insights |
| `app.py` | Streamlit deployment script |
| `data/` |  dataset used |

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
As shown on **page 11**, preprocessing included: :contentReference[oaicite:5]{index=5}

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
Attrition highest in the **first 0–2 years**, declines after.  

### **4️⃣ Department Breakdown**  
- Sales → highest attrition (20.6%)  
- Research & Development → lowest (13.8%)  

### **5️⃣ Education Level**  
Employees with **lower education levels leave the most**.  

### **6️⃣ Work-Life Balance**  
Poor work–life balance → **31.2% attrition**  
Good balance → much lower  

---

##  Dashboard  
A full interactive dashboard visualizing attrition across:

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

With:  
- **GridSearchCV**  
- **RandomizedSearchCV**  
- **SMOTEENN** for class imbalance  


### **Top Features (Random Forest)**  
- MonthlyIncome  
- JobLevel  
- TotalWorkingYears  
- StockOptionLevel  
- Age  
- DailyRate  
- YearsAtCompany  


---

##  Deployment  
An interactive **Streamlit app** was built to predict attrition using 8 key features:

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
*(From page 26)*  
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

##  How to Run the Streamlit App

### Install dependencies:
```bash
pip install -r requirements.txt
