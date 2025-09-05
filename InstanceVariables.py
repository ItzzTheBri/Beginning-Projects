class Character:
    def __init__(self, name, charclass):
        self.name = name
        self.charclass = charclass

        #starting numbers
        self.level = 5
        self.strength = 5
        self.dexterity = 5
        self.smarts = 5
        self.social_skills = 5 #ask why this line has '_' and if order matters

    #Methods
    def increase_level(self): self.level += 1
    def decrease_level(self): self.level -= 1
    def increase_strength(self): self.strength += 1
    def decrease_strength(self): self.strength -= 1
    def increase_smarts(self): self.smarts += 1
    def decrease_smarts(self): self.smarts -= 1
    def increase_social_skills(self): self.social_skills += 1
    def decrease_social_skills(self): self.social_skills -= 1

#Creating object #1 Alice
char1 = Character('Alice', 'liar')
char1.level = 12
char1.strength = 8
char1.dexterity = 15
char1.smarts = 13
char1.social_skills = 18

#Creating object #2 Bob
char2 = Character('Bob', 'brawler')
char2.level = 8
char2.strength = 18
char2.dexterity = 7
char2.smarts = 4
char2.social_skills = 3

#Creating object #3 Clara
char3 = Character('Clara', 'caregiver')
char3.level = 4
char3.strength = 12
char3.dexterity = 12
char3.smarts = 18
char3.social_skills = 18

print(char1.name, char1.charclass, char1.level, char1.strength, char1.dexterity, char1.smarts, char1.social_skills)
print(char2.name, char2.charclass, char2.level, char2.strength, char2.dexterity, char2.smarts, char2.social_skills)
print(char3.name, char3.charclass, char3.level, char3.strength, char3.dexterity, char3.smarts, char3.social_skills)