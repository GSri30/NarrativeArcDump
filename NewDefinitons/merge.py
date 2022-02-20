import pandas as pd

csv1 = pd.read_csv("../Dataset/trial_definition.csv")
csv2 = pd.read_csv("./Definition_Intent.csv")

merged = pd.concat([csv1 , csv2])
# print(merged.tail())

merged.to_csv('./definitions.csv')