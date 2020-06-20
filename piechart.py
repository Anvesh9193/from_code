""" import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
import xlrd
import xlsxwriter
from matplotlib import pyplot as plt
from pandas import DataFrame
x= ["niranjan","Anvesh","Sudheer","aalen","Rostock"]
y= [10,20,21,43,5]
popout=[0,0,0,0,0.005]
plt.plot(x,y)
plt.title("sample")
plt.xlabel("serial_numbers")
plt.ylabel("values")
plt.legend(['this is y'])
plt.show()
plt.pie(y,labels=x, autopct="%.1f%%", explode=popout)
plt.show()  """
""" data = pd.read_excel(r'C:\Users\User\Desktop\Book1.xlsx')
print(data)
df = pd.DataFrame(data,columns=['values','val','names'])
print(df)

print(data.columns.ravel())    # printing headings in list
a = data['names'].tolist()
print(a)
b = data['val'].tolist()
print(b)
popout = [0,0,0.5,0,0]
piechart = plt.pie(b,labels = a, explode = popout,autopct="%.1f%%")
popout = [0,0,0.5,0,0]
plt.show()
 """
