class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('config of this com is',self.cpu,self.ram)

comp1 = Computer('i7',32)
comp2 = Computer("Ryzon5",16)

comp1.config()
comp2.config()


def recPract(num):
    if num <= 0:
        print('this is Zeerooo') 
    else:
        print(f"this is {num}")
        recPract(num-1)
recPract(4)
