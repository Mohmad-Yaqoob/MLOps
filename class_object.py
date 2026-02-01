class employee :
    def __init__(self):
        print(id(self))
        self.id = 123
        self.sal = 3000
        self.designation = "MLE"
        # print("data initiatiated")
        
    def travel(self, des):
        print("method called")
        print(f"Employee is now travelling to {des}")
        
yaqoob = employee()
mohmad = employee()
print(id(yaqoob))
print(id(mohmad))
yaqoob.travel("A")
# yaqoob.travel("Kargil")
# print(type(yaqoob))