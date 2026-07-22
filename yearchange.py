#here we understand when year incease , age , location change 
# with class , obj (instants , init)
#learning --- class & instance variable |22-7-26|
class userdata :
    yearClassVariable = 2026
    def __init__ (self, name , age , place): 
        self.name= name
        self.age = age
        self.place = place
        # above 3 are instance variable
    def display(self):
        print('name : '+ self.name)
        print('age : '+ str (self.age))
        print('location : '+ self.place)
        print("year right now : "+ str(self.yearClassVariable))
    def agechange (self):
        self.age = self.age + 1
        self.yearClassVariable = self.yearClassVariable + 1
        print("-------------age change -------------")
        print('name : '+ self.name)
        print('age : '+ str (self.age))
        print('location : '+ self.place)
        print("year right now : "+ str(self.yearClassVariable))

    def locationchange (self, location):
        self.place = location
        print("-------------location change -------------")
        print('name : '+ self.name)
        print('age : '+ str (self.age))
        print('location : '+ self.place)
        print("year right now : "+ str(self.yearClassVariable))

x = userdata('asi',20,"kollam")
y = userdata('abc',8,"kochi")
x.display()
x.agechange()
x.locationchange("Tvm")