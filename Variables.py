class Calculator():
    num1=900

    def __init__(self,a,b):  # the arguments we give to the class when craeting object should be mentioned in the constructor
        self.a=a  #storing the value of the arguments given when creating the object to instance variable(a and b)
        self.b=b  # a and b are instance variables , when we craete different object and give arguments the value of instance variable will change
        print("Constructor called automatically when objcet is craeted")

    def Summation(self):  #value should come from the run time while object creation
        return self.a+self.b

#obj1=Calculator(3,4)  #value of instance variable is 3 and 4 for the obj1
#print(obj1.Summation())
#obj2=Calculator(8,2)  # value of instance variable is 8 and 2 for the obj2
#print(obj2.Summation())


# instance variable keep on changing for every object creation
# class variable will be constant for every object



