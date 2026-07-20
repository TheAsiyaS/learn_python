#here we understand when year incease , age , location change 
# with class , obj (instants , init)

class userdata :
   
    def __init__ (self, name , age , place): 
        self.name= name
        self.age = age
        self.place = place
        
    def display(self):
        print('name : '+ self.name)
        print('age : '+ str (self.age))
        print('location : '+ self.place)

    def agechange (self):
        self.age = self.age+1
    def locationchange (self, location):
        self.place = location

x = userdata('asi',20,"kollam")
y = userdata('abc',8,"kochi")
x.display