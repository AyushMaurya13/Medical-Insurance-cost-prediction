# 🏥 Medical Insurance Cost Prediction  

##  Overview  
This project predicts **annual medical insurance charges** for individuals based on factors such as age, BMI, smoking habits, and region.  
The goal is to build a **Machine Learning regression model** that helps insurance companies and hospitals estimate costs more accurately.  

---

## Dataset  
- **Source:** Kaggle – [Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)  
- **Features:**  
  - `age`: Age of the individual  
  - `sex`: Gender (male/female)  
  - `bmi`: Body Mass Index  
  - `children`: Number of children/dependents  
  - `smoker`: Smoking status (yes/no)  
  - `region`: Residential area (northeast, northwest, southeast, southwest)  
- **Target:**  
  - `charges`: Medical insurance cost  

---

## ⚙️ Project Workflow  
1. **Data Preprocessing**  
   - Handle categorical variables (`sex`, `smoker`, `region`) using encoding  
   - Standardize numerical features (e.g., BMI, age)  

2. **Exploratory Data Analysis (EDA)**  
   - Visualized age, BMI, and smoking habits against medical charges  
   - Checked for outliers and feature correlations  

3. **Model Training**  
   - Tried  regression model:  
     - Linear Regression  
   - Evaluated using **R² Score & RMSE**  

4. **Model Saving**  
   - Best model saved as `insurance_model.pkl` using `joblib`  

5. **Deployment**  
   - Streamlit web app for easy predictions  

---

##  Streamlit Web App  
You can interact with the model using a simple **Streamlit app**.  

### Example Input:
- Age: `30`  
- BMI: `25.4`  
- Children: `2`  
- Smoker: `No`  
- Region: `Northwest`  
## Author - Ayush Kumar Maurya
