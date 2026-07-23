
#----------MRO-------------------- multiple level inheritance
class HabitPrayer :  # parent 1 {class-A}
    def habits (self):
        print("Habit is prayer")

class HabitRead :  # parent 2 {class-B}
    def habits (self):
        print("Habit is Reading")

    def pages (self) :
        print("100 pages")


class HabitJournel (HabitPrayer, HabitRead) : # output varies accoding to class(parent) inherit 
# if we want to call habits(method) from Class - B without changing order (in subclass-calling)
    def habit_read_only (self):
        HabitRead.habits(self)

    pass


x = HabitJournel() # obj create 
x.habit_read_only() # forcefully calling for desired output (parent 2 method)
x.habits() # call method from child to parent class , since 2 of them have same named method left one works first 
x.pages() # call 2nd parent method 

