import ValveFluid as VF
import ValveGas as VG

print("Choose the type of valve you want to simulate: (1) Fluid Valve, (2) Gas Valve")
valve_type = input("Enter 1 or 2: ")

while valve_type != "1" and valve_type != "2":
    print("Invalid input. Please enter 1 or 2.")
    valve_type = input("Enter 1 or 2: ")

if valve_type == "1":
    print("You have chosen to simulate a fluid valve.")
    VF.main()
elif valve_type == "2":
    print("You have chosen to simulate a gas valve.")
    VG.main()

print("Simulation complete.")
