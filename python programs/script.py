# polynomial regression | price of S&P 500 ($) vs. time (days)

'''

import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import pandas

user = input("Enter Days Since Start: ")

actualPrices = pandas.read_csv('actualPrices.csv')
df = pandas.read_csv('s&p500_data.csv')
print(df)

x = df['Day']
y = df['Close']

mymodel = numpy.poly1d(numpy.polyfit(x, y, 11)) 
myline = numpy.linspace(0, int(user), 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

print("Calculating...")

def getAveragePercentError(i):
  global totalPercent
  global currentError
  global maxError
  global minError

  totalPercent = 0
  currentError = 0
  maxError = 0
  minError = 1000

  while i < 23816:
    currentError = abs(1-mymodel(i)/actualPrices.iloc[23816-i, 0])

    if currentError > maxError:
      maxError = currentError

    elif currentError < minError:
      minError = currentError

    totalPercent += (1-mymodel(i)/actualPrices.iloc[23816-i, 0])
    i+=1

  return totalPercent/i

rScore = str(round(r2_score(y, mymodel(x)),3))
averageError = str(round(getAveragePercentError(0)*100,3))
maxError = str(round(maxError*100,3))
minError = str(round(minError*100,3))
predictedPrice = str(mymodel(int(user)))

print('\n'+"Predicted price at "+user+" days: "+predictedPrice+'\n\n'+"Model's Stats"+'\n'+"R^2: "+rScore+'\n'+"Average Error: "+averageError+"%"+'\n'+"Maximum Error: "+maxError+"%"+'\n'+"Minimum Error: "+minError+"%"+'\n')

'''

# linear regression | price of S&P 500 ($) vs. time (days)

'''

import pandas
from scipy import stats
import matplotlib.pyplot as plt

user = input("Enter Days Since Start: ")

df = pandas.read_csv('s&p500_data.csv')
print(df)

x = df['Day']
y = df['Close']

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

price = myfunc(int(user))
print(r*r)
print(price)

'''

# multiple regression | price of S&P 500 ($) vs. time (days)

'''

import pandas
from sklearn import linear_model

df = pandas.read_csv('fulls&p500data.csv')
print(df)

X = df[["Open","High","Low"]]
y = df['Close']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedPrice = regr.predict([[3700, 4000, 3647.42]])

print(predictedPrice)

'''