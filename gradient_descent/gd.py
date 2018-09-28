import numpy as np
import pandas as pd
#df = pd.read_csv("test_scores.csv")
#df

def gradient_descent(x,y):
    m_curr = b_curr = 0
    iteration = 10
    n = len(x)
    learning_rate = 0.08
    for i in range(iteration):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print ("m {}, b {}, cost {} iteration {}".format(m_curr,b_curr,cost, i))


df = pd.read_csv("test_scores.csv")
x = np.array(df.math)
y = np.array(df.cs)
print(x)
print(y)
gradient_descent(x,y)
