import pandas as pd
import matplotlib.pyplot as plt

Largest_Companies = [
    ["Citigroup", 108.28, 17.05, 1484.10],
    ["General Electric", 152.36, 16.59, 750.33],
    ["American Intl Group", 95.04, 10.91, 766.42],
    ["Bank of America", 65.45, 14.14, 110.46],
    ["HSBC Group", 62.97, 9.52, 1031.29],
    ["ExxonMobil", 263.99, 25.33, 195.26],
    ["Royal Dutch/Shel", 265.19, 18.54, 193.83],
    ["BP", 285.06, 15.73, 191.11],
    ["ING Group", 92.01, 8.10, 1175.16],
    ["Toyota Motor", 165.68, 11.13, 211.15]
]
DF_Larges_Companies = pd.DataFrame(Largest_Companies, columns=["Company", "x1=sales(bilions)", "x2=sales(bilions)",
                                                               "x3=sales(bilions)"])
# Selecting
print(DF_Larges_Companies.iloc[5])

# Filtering
print(DF_Larges_Companies.filter(items=["Company", "x2=sales(bilions)"]))

# Manipulating (creating a new column or a row)
DF_Larges_Companies.insert(4, "x4=sales(bilions)", 0)
print(DF_Larges_Companies)

new_row = {"Company": "Oracle", "x1=sales(bilions)": 0, "x2=sales(bilions)": 0, "x3=sales(bilions)": 0,
           "x4=sales(bilions)": 0, }
DF_Larges_Companies = DF_Larges_Companies.append(new_row, ignore_index=True)
print(DF_Larges_Companies)

# Sorting
sort = DF_Larges_Companies.sort_values("x1=sales(bilions)", axis=0, ascending=False)
print(sort)

# Grouping
gr = DF_Larges_Companies.groupby(["x2=sales(bilions)", "x3=sales(bilions)"]).size().reset_index()
print(gr)

# Rearranging

rear = pd.pivot_table(DF_Larges_Companies, index=["Company", "x2=sales(bilions)"])
print(rear)

# Ranking
rank = pd.DataFrame()
rank['default_rank'] = DF_Larges_Companies["x3=sales(bilions)"].rank()
rank['max_rank'] = DF_Larges_Companies["x2=sales(bilions)"].rank(method='first')
print(rank)

# Plotting data
DF_Larges_Companies.plot(x='Company', y=['x1=sales(bilions)','x2=sales(bilions)','x3=sales(bilions)','x4=sales(bilions)'], kind='bar')
plt.show()
