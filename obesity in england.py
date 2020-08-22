import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.ExcelFile("obes-phys-acti-diet-eng-2014-tab.xls")
print(data.sheet_names)
#Read second section by age
data_age=data.parse(sheet_name="7.2",skiprows=4,skipfooter=14)
print(data_age)
#Rename unamed to year
data_age.rename(columns={'Unnamed: 0':'Year'},inplace=True)
#Drop empties
data_age.dropna(inplace=True)
data_age.set_index("Year",inplace=True)
print("Cleaned data \n", data_age)

#Plotting graphs
#data_age.plot()
#plt.show()
data_age_minus_total=data_age.drop("Total",axis=1) #drop the columns
data_age_minus_total.plot()
#plt.show()

#Are children getting fatter?
data_age["Under 16"].plot(label="Under 16")
data_age["35-44"].plot(label="35-44")
plt.legend(loc="upper right")
#plt.show()

#What about future
#Curve fitting, Polynomial Interpolation
kids_values=data_age["Under 16"].values
x_axis=range(len(kids_values))
poly_degree=5
curve_fit=np.polyfit(x_axis,kids_values,poly_degree)
poly_interp=np.poly1d(curve_fit)

poly_fit_values=[]

for i in range(len(x_axis)):
    poly_fit_values.append(poly_interp(i))

fig, ax = plt.subplots()
ax.plot(x_axis, poly_fit_values, "-r", label = "Fitted")
ax.plot(x_axis, kids_values, "-b", label = "Orig")

ax.legend(loc="upper right")
plt.show()

