if __name__ == "__main__":
 def fahrenheinttocelsius():
     fahrenheint=float(input("Please enter the temperature in fahrenheint:  "))
     celsius=(fahrenheint-32)*5/9
     print(f"the temperature in celsius is: {celsius}")
     return celsius

fahrenheinttocelsius()