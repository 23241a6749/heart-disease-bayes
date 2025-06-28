# Heart Disease Prediction using Bayesian Networks

This project predicts the probability of heart disease using a Bayesian Network built with `pgmpy`. It involves data preprocessing, structure definition, parameter estimation (MLE), and inference using user input.

## 📁 Repository Contents

- `heart_disease.csv`: Cleaned dataset  
- `main.py`: Script for building the model and running inference  
- `requirements.txt`: Python dependencies  
- `bayesian_network.png`: Visualization of the learned Bayesian Network  
- `inference_output.txt`: Output showing inferred probability of heart disease  
- `.gitignore`: Ignores virtual environment and other unnecessary files  
- `README.md`: This documentation

## 🛠️ Setup Instructions

1. Clone the repo:  
   git clone https://github.com/23241a6749/heart-disease-bayes.git

2. Navigate into the project:  
   cd heart-disease-bayes

3. Create virtual environment:  
   python -m venv venv

4. Activate the environment:  
   - On Windows: venv\Scripts\activate  
   - On Unix/Mac: source venv/bin/activate

5. Install dependencies:  
   pip install -r requirements.txt

## 🚀 Run the Project

To start the Bayesian model and get predictions:  
Run:  
python main.py  
It will prompt you for inputs like age, sex, chest pain type, etc. Based on your inputs, it computes and displays the probability of heart disease and saves the result in `inference_output.txt`.

## 📊 Visualizations

The file `bayesian_network.png` shows the learned Bayesian Network structure, connecting features like age, cholesterol, restecg, etc. You can visually interpret how these attributes influence the `target` variable (presence of heart disease).

## ✅ Sample Output

Enter Age: 56  
Enter Sex (0 = female, 1 = male): 1  
Enter Chest Pain Type (0–3): 2  
...  
Predicted Probability of Heart Disease: 0.76  
(Also saved in `inference_output.txt`)

## 🧠 Libraries Used

- pandas  
- networkx  
- matplotlib  
- pgmpy  

## 👤 Author

GitHub: [23241a6749](https://github.com/23241a6749)

## 📝 License

This project is licensed under the MIT License.
