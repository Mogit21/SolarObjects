

class TestClass:
    def __init__ (self, name, first_attribute):
        self.name = name
        self.first_attribute = first_attribute
        self.second_attribute = self.first_attribute/2


class TestClassLocal:
    def __init__ (self, name, first_attribute):
        self.name = name
        self.first_attribute = first_attribute
        self.second_attribute = first_attribute/2

first_object=TestClass("Test_object", 48)
second_object=TestClassLocal("Test_object", 48)

print(first_object)
print(first_object.second_attribute)
print(second_object)
print(second_object.second_attribute)