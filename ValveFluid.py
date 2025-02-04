import pandas as pd 
import numpy as np
import math
# Load the data
def main():
    print("Valve Sizing Calculator")
    print("\n Enter the following data to calculate the valve size")

    df=pd.read_csv('Density Property.csv',delimiter=';')
    df['Density']=df['Density'].str.replace(',','.').astype(float)
    # Get the data from the user

    Fluid_type=str(input("\n Enter the fluid type: "))

    Fluids=df.loc[df['Fluid']==Fluid_type]
    Density_value=Fluids['Density'].values[0]


    flow_rate = float(input("\n Enter the flow rate in m3/hr: "))

    pressure_drop = float(input("\n Enter the pressure drop in bar: "))



    def cv(flow_rate, pressure_drop, density_value):
        cv=flow_rate * math.sqrt(((density_value/1000)*10e5) / (pressure_drop*10e5))
        return cv

    print("\n The Cv value is: ", round(cv(flow_rate, pressure_drop, Density_value),2))
    print(" \n The following medium data is used: ")
    print("\n Fluid type: ", Fluid_type)
    print(" \n Density: ", Density_value, "kg/m3")
    print(" \n Flow rate: ", flow_rate, "m3/hr")
    print(" \n Pressure Drop: ", pressure_drop, "bar")
    print("\n")
