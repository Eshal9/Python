class Robot:
    age = 10
    name = "Ronald"
    donthave = "feelings"

    def introduction(self):
        print("Hi I am a Robot")

    def details(self):
        print("My name is", self.name)
        print("I was invented in", self.age , "years")
        print("I am freindly but i dont have", self.donthave)

ob = Robot()
ob.introduction()
ob.details()