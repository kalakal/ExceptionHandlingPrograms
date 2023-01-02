# exception class
class VotingPerson(Exception):
    #   Raised when the input age is less than 18
    def _inti_(self, name, age):
        self.name = name
        self.age = age

    # try taking details of the users,
    # if the age is inappropriate, throw an exception


try:
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    if age < 18:
        raise VotingPerson
    vote1 = VotingPerson(name, age)
    print("You are eligible for voting")
except VotingPerson:
    print("You not eligible for voting")