import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import networkx as nx
import matplotlib.pyplot as plt
import os

def main():
    # --------------------------------------------
    # STEP 1: Load and clean the dataset
    # --------------------------------------------
    df = pd.read_csv('heart_disease.csv')

    print("Initial Dataset Preview:")
    print(df.head())
    print("\nDataset Info:")
    print(df.info())

    # Remove duplicates and missing values
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # Normalize numeric columns using Min-Max scaling
    numeric_cols = df.select_dtypes(include='number').columns
    scaler = MinMaxScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    # Optional: Save cleaned dataset
    df.to_csv("cleaned_heart_disease.csv", index=False)
    print("\nCleaned dataset saved as cleaned_heart_disease.csv")

    # --------------------------------------------
    # STEP 2: Define the Bayesian Network structure
    # --------------------------------------------
    model = BayesianModel([
        ('age', 'fbs'),
        ('fbs', 'target'),
        ('target', 'chol'),
        ('target', 'thalach')
    ])

    print("\nBayesian Network Structure:")
    print("Nodes:", model.nodes())
    print("Edges:", model.edges())

    # --------------------------------------------
    # STEP 3: Train the model using MLE
    # --------------------------------------------
    model.fit(df, estimator=MaximumLikelihoodEstimator)

    print("\nLearned CPDs:")
    for cpd in model.get_cpds():
        print("CPD of {}:".format(cpd.variable))
        print(cpd)

    # --------------------------------------------
    # STEP 4: Inference using the trained model
    # --------------------------------------------
    infer = VariableElimination(model)

    # Inference 1: Probability of heart disease given age = 0.6
    result = infer.query(variables=['target'], evidence={'age': 0.6})
    print("\nP(target | age=0.6):")
    print(result)

    # Inference 2: Cholesterol distribution given target = 1
    result = infer.query(variables=['chol'], evidence={'target': 1})
    print("\nP(chol | target=1):")
    print(result)

    # Inference 3: Max heart rate distribution given target = 0
    result = infer.query(variables=['thalach'], evidence={'target': 0})
    print("\nP(thalach | target=0):")
    print(result)

    # --------------------------------------------
    # STEP 5: Visualize the Bayesian Network
    # --------------------------------------------
    print("\nGenerating Bayesian Network Graph...")

    # Ensure 'images/' directory exists
    os.makedirs("images", exist_ok=True)

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(model)
    nx.draw(model, with_labels=True, node_size=3000, node_color='lightblue', font_size=12, pos=pos)
    plt.title("Bayesian Network Structure")
    plt.tight_layout()
    plt.savefig("images/bayesian_network.png")
    plt.show()

    print("\nBayesian Network graph saved to images/bayesian_network.png")

if __name__ == "__main__":
    main()
