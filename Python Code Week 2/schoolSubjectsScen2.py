#============== INHERITANCE SCHOOL SUBJECTS =====================

# generic info about school subjects
# Base class
class Subject:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"Studying {self.name}")


# adds specific info about difficulty ability to solve problems
class Math(Subject):
    def __init__(self, name, difficulty_level):

        # super calls the  name from constructor in parent/base class
        super().__init__(name)
        self.difficulty_level = difficulty_level

    # called to state how hard studies are
    def solve_problem(self):
        print(f"Solving a {self.difficulty_level} math problem")


# info on language subject, on language type and ability to practise language
class Language(Subject):
    def __init__(self, name, language_type):

        super().__init__(name)
        self.language_type = language_type

    # embedded def - states what one is currently learning
    def practice_language(self):
        print(f"Practicing {self.language_type} language")


# Hospo class
class Hospitality(Subject):
    # attribites
    def __init__(self, name, cooking_skill):
        super().__init__(name)
        self.cooking_skill = cooking_skill

        # method recounting what one likes to cook
    def cooking(self):
        print(f"I love to cook {self.cooking_skill}")


# Instances
# instance for subject
subject = Subject("Biology")
subject.study()


# math instance
math = Math("Mr Nerd", "Statistics")
math.solve_problem()


#language instance
language = Language("Risa","Japanese")
language.practice_language()


#hospo instance
hospo = Hospitality("Chef", "Self Saucing Choc Pudding.. nom nom nom")
hospo.cooking()
