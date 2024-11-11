import numpy as np
#Ask the parameters
y0=float(input("Tell me the height\n> "))
g=float(input("Tell me the gravity\n> "))
#Define the initial velocity
v0=0
#Ask the maximum time and how many moments want to study
tmax=int(input("Tell me the maximum time\n> "))
el=int(input("How many moments do you want to study\n> "))
#Create an interval of the time
t=np.linspace(0,tmax,el)
#Create the variable where you will save the values
values=np.array([])
#Calculate the position for each time 
for index in range(len(t)):
    y=y0-(1/2)*g*t[index]**2
    values=np.append(values,y)
#Calculate the difference between times
difference=np.diff(values)
difference=np.absolute(difference)
print(difference)
#Calculate the mean of the difference
print(np.mean(difference))
