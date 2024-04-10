import matplotlib.pyplot as plt
from scipy import stats
x=[10,20,30,40,50]
y=[5,6,4,2,9]

slope,intercept,r,p,std_err=stats.linregress(x,y)
def func(x):
    return slope*x+intercept

mymodel=list(map(func,x))
plt.scatter(x,y)
plt.plot(x,mymodel)
plt.show()
