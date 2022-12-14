from matplotlib import pyplot as pl
from sklearn import linear_model
import pandas as pd

ar = [[2, -1], [3, 1], [4, 2]]

DataFrame = pd.DataFrame(ar, columns=['x', 'y'])
LinearRegression = linear_model.LinearRegression()
LinearRegression.fit(DataFrame[['x']], DataFrame.y)

print('X=5', LinearRegression.predict([[5]]))
pl.ylabel('y')
pl.xlabel('x')
pl.scatter(DataFrame.x, DataFrame.y)
pl.plot(DataFrame.x, LinearRegression.predict(DataFrame[['x']]))
pl.show()

arra = [[2, -1], [3, 1]]
DataFrame = pd.DataFrame(arra, columns=['x', 'y'])
LinearRegression = linear_model.LinearRegression()
LinearRegression.fit(DataFrame[['x']], DataFrame.y)
print('X=4', LinearRegression.predict([[4]]))
pl.ylabel('y')
pl.xlabel('x')
pl.scatter(DataFrame.x, DataFrame.y)
pl.plot(DataFrame.x, LinearRegression.predict(DataFrame[['x']]))
pl.show()