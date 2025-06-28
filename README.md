# Heart Disease Prediction using Bayesian Networks  
This project predicts the presence of heart disease using a Bayesian Network model trained on medical data. It utilizes the `pgmpy` library in Python to build and infer from a probabilistic graphical model.  
## 🔍 Overview  
The dataset (`heart_disease.csv`) includes the following features: Age, Sex, Chest pain type, Resting blood pressure, Cholesterol, Fasting blood sugar, Resting ECG, Maximum heart rate achieved, Exercise-induced angina, ST depression, Number of major vessels, Thalassemia, and Target (0 = no heart disease, 1 = heart disease). The goal is to predict the probability of heart disease (target) based on these features using a Bayesian Network.  
## 🛠️ Setup Instructions  
1. Clone the repository  
   `git clone https://github.com/23241a6749/heart-disease-bayes.git && cd heart-disease-bayes`  
2. Create and activate a virtual environment  
   `python -m venv venv && venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/macOS)  
3. Install dependencies  
   `pip install -r requirements.txt`  
4. Run the project  
   `python main.py`  
## 📁 Project Structure  
`heart-disease-bayes/`  
├── `heart_disease.csv` – Input dataset  
├── `main.py` – Main script to train & predict  
├── `requirements.txt` – Python dependencies  
└── `.gitignore` – To ignore venv and large files  
## 🧪 Features  
- Label encoding for categorical data  
- Manual definition of Bayesian Network structure  
- Parameter learning using Maximum Likelihood Estimation (MLE)  
- Interactive CLI-based prediction using probabilistic inference  
## 📝 Sample Usage  
When executed, the script prompts for input values such as age, cholesterol, etc., and returns the predicted probability of having heart disease based on the trained Bayesian Network.  
## ⚠️ Notes  
- Do not push the `venv/` folder to GitHub  
- Avoid committing files over 100MB (e.g., `.dll`, `.lib`)  
- Use Git LFS if large files are essential  
## 👨‍💻 Author  
GitHub: [@23241a6749](https://github.com/23241a6749)  
## 📜 License  
This project is licensed under the [MIT License](LICENSE)  
