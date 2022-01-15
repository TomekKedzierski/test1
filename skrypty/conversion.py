import pandas as pd
filepath_in = "C:\\Users\\tomek\\Desktop\\zadania\\test2.csv"
filepath_out = "C:\\Users\\tomek\\Desktop\\zadania\\wynik2.xlsx"
pd.read_csv(filepath_in, delimiter=";").to_excel(filepath_out,index=False)
