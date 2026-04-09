import main

class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        pass
        # print('config of this com is',self.cpu,self.ram)

comp1 = Computer('i7',32)
comp2 = Computer("Ryzon5",16)

comp1.config()
comp2.config()


def recPract(num):
    if num <= 0:
        pass
        # print('this is Zeerooo') 
    else:
        pass
        # print(f"this is {num}")
        recPract(num-1)
recPract(4)

# 1. Default Constructor using default values
class ComputerDefault:
    def __init__(self, cpu="i3", ram=8):  # default values
        self.cpu = cpu
        self.ram = ram

    def config(self):
        pass
        # print("Default Config:", self.cpu, self.ram)

comp_default = ComputerDefault()  # no arguments passed
comp_default.config()


# 2. Parameterized Constructor (already used in your original code)
# Just showing another example
comp_param = ComputerDefault("i9", 64)
comp_param.config()


# 3. Using class method as alternative constructor
class ComputerAlt:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    @classmethod
    def from_string(cls, config_str):
        # Example input: "i5-16"
        cpu, ram = config_str.split("-")
        return cls(cpu, int(ram))

    def config(self):
        pass
        # print("Alt Constructor Config:", self.cpu, self.ram)

comp_alt = ComputerAlt.from_string("i5-16")
comp_alt.config()


# 4. Constructor with validation logic
class ComputerValidated:
    def __init__(self, cpu, ram):
        if ram <= 0:
            raise ValueError("RAM must be positive")
        self.cpu = cpu
        self.ram = ram

    def config(self):
        pass
        # print("Validated Config:", self.cpu, self.ram)

comp_valid = ComputerValidated("i7", 16)
comp_valid.config()


# 5. Using __str__ method with constructor (for better print output)
class ComputerStr:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def __str__(self):
        return f"Computer(cpu={self.cpu}, ram={self.ram}GB)"

comp_str = ComputerStr("Ryzen7", 32)
# print(comp_str)  # automatically calls __str__


# 6. Copy constructor-like behavior (not built-in, but manual)
class ComputerCopy:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    @classmethod
    def copy(cls, other_obj):
        return cls(other_obj.cpu, other_obj.ram)

    def config(self):
        pass
        # print("Copied Config:", self.cpu, self.ram)

original = ComputerCopy("i5", 8)
copy_obj = ComputerCopy.copy(original)

copy_obj.config()


# 7. Destructor example (__del__)
class ComputerDestructor:
    def __init__(self, cpu):
        self.cpu = cpu
        pass
        # print(f"{self.cpu} Computer Created")

    def __del__(self):
        pass
        # print(f"{self.cpu} Computer Destroyed")

comp_des = ComputerDestructor("i3")
del comp_des  # manually deleting object


# 8. Constructor with dynamic attributes
class ComputerDynamic:
    def __init__(self, **kwargs):
        # allows flexible attributes
        for key, value in kwargs.items():
            setattr(self, key, value)

    def config(self):
        pass
        # print("Dynamic Config:", self.__dict__)

comp_dyn = ComputerDynamic(cpu="i9", ram=64, gpu="RTX 4090")
comp_dyn.config()






students = [
    {
        "id": 1,
        "name": "Alice",
        "age": 16,
        "grade": "10th",
        "marks": 88
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 15,
        "grade": "9th",
        "marks": 92
    },
    {
        "id": 3,
        "name": "Charlie",
        "age": 17,
        "grade": "11th",
        "marks": 81
    }
]


#@app.put("/UpdStudent/id")


# async def updateStudent(id:int,name:str):
def updateStudent(id=1,name= "this sis the name"):
    index = main.getStudentIndex(id)
    std = students[index] 
    print(std)
    print('students typeeeee',type(students))
    if std["id"]== id:
        std["name"] = name 
    print('updated std>>>>', std)
    return std
updateStudent()