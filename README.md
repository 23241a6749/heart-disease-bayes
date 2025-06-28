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
![Bayesian Network]![bayesian_network](https://github.com/user-attachments/assets/a4cf5eff-f458-4bb8-be25-92ae6ef31cf9)


### 2. Cholesterol Distribution (Given Heart Disease)  
![P(chol | target=1)]![p_chol_given_target_1](https://github.com/user-attachments/assets/9cd62606-333d-46ca-9bbf-eded76708e05)


### 3. Max Heart Rate Distribution (Given No Heart Disease)  
![P(thalach | target=0)]![p_thalach_given_target_0](https://github.com/user-attachments/assets/b4d1acb6-1ad4-4a0f-b473-a59c88d60e3d)


### 4. Heart Disease Probability Based on Age  
![P(target | age)]![p_target_given_age](https://github.com/user-attachments/assets/e7b310ad-179a-411f-99c8-a952dfb42233)


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
