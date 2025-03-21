"""
Create a FamousPerson class with:
Attributes: name, birth_year, country_of_birth
Method: introduce()
Example format: [name] was born in [birth_year] in [country_of_birth]
Create subclasses:
Scientist (adds field, notable_discovery)
Politician (adds position, years_in_office)
NOTE: you will need a new introduce() for each subclass so the printed statement will include the additional information for each.
Create instances for Albert Einstein,  Lebron James, and Abraham Lincoln, then call introduce() for each of them. 
Remember to use the correct class or subclass when you create these famouse people.
"""
## Parent class
class FamousPerson:
    def __init__(self, name, birth_year, country_of_birth):
        self.name = name
        self.birth_year = birth_year
        self.country_of_birth = country_of_birth

    def introduce(self):
        return f"{self.name} was born in {self.birth_year} in {self.country_of_birth}."
    
#Child Class
class Scientist(FamousPerson):
    def __init__(self, name, birth_year, country_of_birth, field, notable_discovery):
        super().__init__(name, birth_year, country_of_birth)
        self.field = field
        self.notable_discovery = notable_discovery
    
    def introduce(self):
        return (f"{self.name} was born in {self.birth_year} in {self.country_of_birth}.\n"
                f"They studied {self.field} and are known for their discovery of {self.notable_discovery}.")

class Politician(FamousPerson):
    def __init__(self, name, birth_year, country_of_birth, position, years_in_office):
        super().__init__(name, birth_year, country_of_birth)
        self.position = position
        self.years_in_office = years_in_office
    
    def introduce(self):
        return (f"{self.name} was born in {self.birth_year} in {self.country_of_birth}.\n"
                f"They served as {self.position} for {self.years_in_office} years.")
    
#People
print("###############################################################")
print("Famous People Introductions: \n")
LeBron = FamousPerson("LeBron James", 1984, "United States")
print(LeBron.introduce())
print()
Einstein = Scientist("Albert Einstein", 1879, "Germany", "Physics", "Theory of Relativity")
print(Einstein.introduce())
print()
Lincoln = Politician("Abraham Lincoln", 1809, "United States", "President", 4)
print(Lincoln.introduce())
print("###############################################################")

