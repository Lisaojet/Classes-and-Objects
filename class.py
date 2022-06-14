

class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)

    def change_name(self, changename):
        self.name = changename
        print("My name is", changename)

    def change_age(self, changeage):
        self.change_age = changeage
        print("My age is", changeage)

    def add_track(self, newtrack):
        self.add_track = newtrack
        print("My new track is", newtrack)

    def get_score(self):
        self.get_score = self.score
        print("My new score is", self.score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

