
# without constructor
class A:
    name=''
    age=''
    def getdetails():
     print(A.name)
     print(A.age)
a=A
a.name="Niraj Singh"
a.age=20
a.getdetails()
# with constructor
class Person():
    def __init__(self,name,branch,dob):
        self.name=name
        self.branch=branch
        self.dob=dob
    def getdetails(self):
        print("Name:--->",self.name)
        print("Branch:--->",self.branch)
        print("dob:--->",self.dob)
Person("Niraj singh","Mechanical","09-12-2002").getdetails()
