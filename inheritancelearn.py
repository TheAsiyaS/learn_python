class person : #parent class
    def __init__(self,name ):
        self.name = name # name come from child class later 
    def display(self ): 
        print("Name of the person : "+ self.name)

class student (person) :  # child class
    def __init__(self, name , id):
        super().__init__(name) # passing name data to parent 
        self.id = id # id added to object(self , memory)

    def display(self):
         super().display() #call parent method display
         print("student id is : "+ str(self.id))


x = student("Asiya" , 1243) # object create for student 
x.display() # with that object we call sub_class