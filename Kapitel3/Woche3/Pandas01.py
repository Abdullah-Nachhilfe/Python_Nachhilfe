import pandas as pd
import numpy as np

# csv-Datei importieren mit ';' als Seperator. Dafault ist ','
# header = ab welche Zeile. Achtung: Wir zählen ab 0 
# parse_dates = [[0 , 1, 2]]. Elemente der Liste sind die Spalten wo ein Datum ist. Reihenfolge beachten.

data = pd.read_csv(
    "E:\ASOTE_Python_Nachhilfe\Folien_MUNZ\Kapitel3\meteoblue_sonnenschein_täglich_basel_header1_history_export_2019-03-15T10_12_15.csv",
    sep=';', header=0, parse_dates = [[0, 1  , 2]])

# information über die csv-Datei wie: Anzahl Spalten, Datentyp der Werte in Spalten, Name der Spalten usw...
data.info()

# Gibt Zurück, die ersten n-Zeilen, default ist 5
print(data.head())

# Umbenennen einer Spalte
data = data.rename(index=str, columns={"Hour":"Stunde"})

