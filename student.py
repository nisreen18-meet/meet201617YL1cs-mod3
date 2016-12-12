class student:
    def __init__(self,name,hometown,age,height,favicecreamflavor):

        self.name=name
        self.hometown=hometown
        self.age=age
        self.height=height
        self.favicecreamflavor=favicecreamflavor

    def print_summary(self):

        print("My name is" +str(self.name)+"."+ "I live in" +str(self.hometown)+"."+ "I am"+ str(self.age)+"."+ "I am" +str(self.height)+"."+ "My favorite ice ream flavor is" +str(self.favicecreamflavor)+".")

    def get_giraffe_gap(self):
        return (str(500-int(self.height)))

