class Parent:
    def my_method(self):
        print("Parent method")


class Child(Parent):
    def my_method(self):
        print("Child method")


obj = Child()
obj.my_method()  # Prints: "Child method"
