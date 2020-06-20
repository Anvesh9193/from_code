import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
data = pd.read_excel(r'C:\Users\User\Desktop\Workbook.xlsx')
data1 = pd.read_excel(r'C:\Users\User\Downloads\TODAY REPORT COVID 19 (10).xlsx')
df = pd.DataFrame(data, columns= ['locations','profit','employees','revenue'])
print(df) = data1['State']
print(a)

a= data['profit']
b= data['locations']
print(b)
c= [0,0,0,0.5]
print(type(b))
pie = plt.pie(a,labels=b, autopct="%.1f%%", explode= c, shadow=True)
plt.show()
bar = a.plot.bar[x="locations",y='employees',rot=0]
plt.show()
x=1
print(x<<2)
