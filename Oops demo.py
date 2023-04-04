class Calculator:  #class name declaration
    num = 100
    def __init__(self):   # creating a constuctor
        print("I am called automatically when object is called") # no need to call ouside the class seperately


    def GetData(self): #method/function
        print("Starting the project")

    def Summation(self):  #value should come from the run time while object creation
                            # the arguments we give to the class when craeting object should be mentioned in the constructor

#GetData()  #we can not directly call the method outside the class, we need to create a object first

obj = Calculator()  # creating the object for the class
obj.GetData() # calling the method inside the class
print(obj.num) # calling the variable