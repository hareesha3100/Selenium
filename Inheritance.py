from Variables import Calculator # importing the class--> from the file variables importing the class Calculator
#from <file_name>  import <parent class_name>

class ChildImp(Calculator):  #inheriting the parent class calculator to child class
    num2=200
    def __init__(self):  #in the child constructor we need to mandatorily call parent constructor if parent constructor is not default
        Calculator.__init__(self,2,3)
    def GetComData(self):
        return self.num2+self.num1+self.Summation()

obj3 = ChildImp()
print(obj3.GetComData())
#we need to invoke the parent class constructor from the child class



