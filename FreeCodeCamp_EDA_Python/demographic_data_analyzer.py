import numpy as np
import pandas as pd


path = r"C:\Users\Hugo\Documents\MEGA\PROYECTOS\Personal proyects\FreeCodeCamp_EDA_Python\utils\archive\diabetes_prediction_dataset.csv"
df = pd.read_csv(path)

print(df.head)

print("How mani people with hypertension info: \n", df['smoking_history'].value_counts())
print("What is the average age of men?: \n", df['age'].loc[(df['gender'] == 'Male')].mean())
print("What is the percentage of people who have smoking history data?",df)
