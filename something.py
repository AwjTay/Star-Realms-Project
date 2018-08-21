class Dog:
    def bark(self):
        print("bark")

    def is_small(self):
        print("I don't know! I am just a generic dog.")


class Shitzu(Dog):
    def is_small(self):
        print("I am small")


class Retriever(Dog):
    def is_small(self):
        print("Hell no")


dog = Dog()
dog.is_small()

missy = Shitzu()
missy.bark()
missy.is_small()
