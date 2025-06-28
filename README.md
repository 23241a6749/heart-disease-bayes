# Heart Disease Prediction using Bayesian Networks

This project uses a **Bayesian Network** to model and predict the likelihood of heart disease based on features from the UCI Heart Disease dataset. The model is trained using Maximum Likelihood Estimation and performs probabilistic inference with visual outputs.

## 📁 Project Structure
```
bayes-heart-disease/
├── heart_disease.csv
├── cleaned_heart_disease.csv
├── main.py
├── images/
│   ├── bayesian_network.png
│   ├── p_chol_given_target_1.png
│   ├── p_thalach_given_target_0.png
│   └── p_target_given_age.png
└── README.md
```

## 📌 Features Used
- `age`
- `fbs` (fasting blood sugar)
- `chol` (serum cholesterol)
- `thalach` (maximum heart rate)
- `target` (0 = no disease, 1 = disease)

## ⚙️ How It Works
1. **Load and Clean Data**  
   The dataset is loaded, duplicates and missing values are removed, and numerical features are normalized using `MinMaxScaler`.
2. **Model Definition**  
   A Bayesian Network is defined with the following dependencies:  
   - `age → fbs → target`  
   - `target → chol`  
   - `target → thalach`
3. **Training**  
   The network is trained using Maximum Likelihood Estimation on the cleaned dataset.
4. **Inference**  
   - `P(target | age=valid)`  
   - `P(chol | target=1)`  
   - `P(thalach | target=0)`
5. **Visualization**  
   The model structure and inference results are plotted and saved into the `images/` directory.

## 📊 Visualizations

### 1. Bayesian Network Structure  
![Bayesian Network](images/bayesian_network.png)

### 2. Cholesterol Distribution (Given Heart Disease)  
![P(chol | target=1)](images/p_chol_given_target_1.png)

### 3. Max Heart Rate Distribution (Given No Heart Disease)  
![P(thalach | target=0)](images/p_thalach_given_target_0.png)

### 4. Heart Disease Probability Based on Age  
![P(target | age)](images/p_target_given_age.png)

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bayes-heart-disease.git
   cd bayes-heart-disease
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python main.py
   ```

## ✅ Requirements
- Python 3.8+
- `pgmpy`
- `matplotlib`
- `pandas`
- `scikit-learn`
- `networkx`
---

© 2025 Bayesian Heart Disease Project
