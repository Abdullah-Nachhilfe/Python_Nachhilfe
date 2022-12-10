import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("E:\ASOTE_Python_Nachhilfe\Folien_MUNZ\Kapitel3\meteoblue_temperatur_basel_history_export_2019-03-15T10_04_55.csv",
                   sep=';', header=10)
data.info()
data = data.rename(index=str, columns = {'Temperature  [2 m above gnd]':'Temperature'})
print(data.head())

# Zugreifen auf Daten
print('Erste Temp: %.2f°C' % data.at['0', 'Temperature'])

# Zugreifen auf einer Spalte
temp = data['Temperature']
print(temp)

# Zugreifen auf Zeilen --> Wie Slicing
print(data[1:4])
