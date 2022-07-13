# print name
name = "Brendan"
print(name)

# calculate fav number squared
fav_number = 3
fav_squared = fav_number**2

# count up to fav number squared while printing
counter = 1
while counter <= fav_squared:
    print(counter)
    counter += 1

class Engineer:

    def __init__(self,name,type,years_experience):
        self.skill = "problem solver"
        self.name = name
        self.type = type
        self.years_experience = years_experience
    def getName(self):
        print("Engineers Name: " + self.name)
    def getSkill(self):
        print("Skill: " + self.skill)
    def getType(self):
        print("Discipline: " + self.type)
    def getExperience(self):
        print("Years of experience: " + self.years_experience)


Bob = Engineer("Bob", "Electrical", "12")
Fredrick = Engineer("Fredrick", "Civil", "8")

print(" ") # blank line
Bob.getName()
Bob.getType()
Bob.getSkill()
Bob.getExperience()
print(" ") # blank line
Fredrick.getName()
Fredrick.getType()
Fredrick.getSkill()
Fredrick.getExperience()

Backwards = name[6] + name[5] + name[4] + name[3] + name[2] + name[1] + name[0]
print(Backwards)