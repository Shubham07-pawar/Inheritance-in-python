"""
OOPs concepts.
Inheritance:
inheritance provide code reusability to the program.
inheritance is parent(base)-child(derived) relationship.
The child class acquires the properties and can access all the data members and methods defined in parent class.
A child class also provide its own properties and functions of the parent class.
inheritance means relationship
------------------------------------------------------------------------------------------------------------------------
"""
# single inheritance:
"""
class University:
    def __init__(self):
        print("University constructor")

    def rules(self):
        print("University rules")


class College(University):
    pass


c = College()
c.rules()
------------------------------------------------------------------------------------------------------------------------



# method overriding

class University:

    def __init__(self):
        print("University constructor")

    def rules(self):
        print("University rules")


class College(University):
    # constructor and method overloading is not possible in python because they access the only recent declare method
    # but method overriding is possible in python.
    def __init__(self):
        super().__init__()
        print("college constructor")

    def rules(self):   # method override, if the method present in child and parent class with same name.
        print("college rules")
        super().rules()  # rules method is override parent class method, but you want to call child class method as well 
                         # as parent class method then use super() function. super() designed only inheritance purpose.
                         # help of super you can arrange the calling sequence of methods. 


c = College()
c.rules()
------------------------------------------------------------------------------------------------------------------------



# multilevel inheritance: [super parent-parent-child]
class Grandfather:
    def money(self):
        print("Grandfather money")


class Father(Grandfather):
    def money(self):
        super().money()  # call grandfather
        print("Father money")


class Child(Father):
    def money(self):
        super().money() # its call father
        print("child money")


m = Child()
m.money()

------------------------------------------------------------------------------------------------------------------------



# multiple inheritance : [multiple parent-one child]

class Father:
    def money(self):
        print("Father money")

    def s1(self):
        print("s1")


class Mother:
    def money(self):
        print("Mother money")
        # super().money()


class Child(Mother, Father):
    def my_money(self):
        print("child money")


c = Child()
print(Child.__mro__)
------------------------------------------------------------------------------------------------------------------------


# Hierarchical Inheritance : [one parent - multiple child]


class Parent:

    def sample(self):
        print("parent")

class Child1(Parent):
    def sample(self):
        super(C1, self).sample()
        print("Child1")

class Child2(Parent):
    def sample(self):
        super(Child2, self).sample()
        print("child2")

c = Child1()
c.sample()
s = Child2()
s.sample()
------------------------------------------------------------------------------------------------------------------------


# hybrid Inheritance [combination of multiple and hierarchical]
# hybrid is combination of hierarchical and multiple inheritance.  

------------------------------------------------------------------------------------------------------------------------
"""

# MRO : method resolution order
# method resolution oeder in which python its get hierarchy of class.



