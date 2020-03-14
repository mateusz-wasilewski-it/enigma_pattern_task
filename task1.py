import pandas as pd
from datetime import  datetime

test = pd.read_csv("test.csv")

print("ilosc osob urodzonych po 1999-12-31", test[pd.to_datetime(test.data_urodzenia) > datetime(1999, 12, 31)].shape[0])

print("imiona zenskie:",test['imie'][test.imie.str.endswith("a")].unique())
