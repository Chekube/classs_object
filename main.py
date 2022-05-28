class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    print("Details of new student:")


    def change_name(self, change_name):
          self.name = change_name
          change_name = input("Enter new name: ")
          print(change_name, "; Name changed succerssfully,")

    def change_age(self, change_age):
          self.age = change_age
          change_age = input("Enter new age: ")
          print(change_age, "; Age changed succerssfully,")

    def add_tracks(self, add_tracks):
          self.tracks = add_tracks
          add_tracks = input("Add new track: ")
          print(add_tracks, "; Track added succerssfully,")

    def get_score(self):
          print("Score: ",self.score)                



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_tracks("UI/UX")
Bob.get_score()

