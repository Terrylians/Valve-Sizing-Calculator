def main():
    import pandas as pd 
    import numpy as np
    import math
    # Load the data

    print("Valve Sizing Calculator")
    print("\n Enter the following data to calculate the valve size")

    df=pd.read_csv('Gas Density.csv',delimiter=';')
    df['Density']=df['Density'].str.replace(',','.').astype(float)
    # Get the data from the user

    Gas_type=str(input("\n Enter the Gas type: "))

    Gas=df.loc[df['Gas']==Gas_type]
    Gas_value=Gas['Gas'].values[0]
    Density_value=Gas['Density'].values[0]
    
    print(Gas_value, Density_value)

    flow_rate = float(input("\n Enter the flow rate in m3/hr: "))

    pressure_in=float(input("\n Enter the entry pressure in bar: "))

    pressure_drop = float(input("\n Enter the pressure drop in bar: "))

    temperature_value = float(input("\n Enter the temperature in Celsius: "))

    temperature_value=temperature_value+273.15
    p2=pressure_in-pressure_drop
    norm_flow_rate=flow_rate*pressure_in*273.15/(temperature_value*1.01325)
    norm_density=Density_value*temperature_value*1.01325/(pressure_in*273.15)

    def cv1(norm_flow_rate, pressure_drop, norm_density,temperature_value):
        cv1=(norm_flow_rate/514)*math.sqrt(norm_density*temperature_value/(pressure_drop*p2))
        return cv1

    def cv2(norm_flow_rate, pressure_in,norm_density,temperature_value):
        cv2=(norm_flow_rate/(257*pressure_in))*math.sqrt(norm_density*temperature_value)
        return cv2

    if p2/pressure_in>=0.5:
        output= cv1(norm_flow_rate, pressure_drop, norm_density, temperature_value)
    else:
        output= cv2(norm_flow_rate,pressure_in, norm_density, temperature_value)


    print("\n The Cv value is: ", output, "m3/hr")
    print(" \n The following medium data is used: ")
    print("\n Gas type: ", Gas_value)
    print(" \n Norm Density: ", norm_density, "kg/m3")
    print(" \n Norm Flow rate: ", norm_flow_rate, "nm3/hr")
    print("\n Entry Pressure: ", pressure_in, "bar")
    print(" \n Pressure Drop: ", pressure_drop, "bar")
    print(" \nTemperature: ", temperature_value, "K")

