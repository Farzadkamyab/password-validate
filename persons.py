import pickle

class Person:
    def __init__(self, name, age, address) -> None:
        self.name = name
        self.age = age
        self.address = address

    def __str__(self) -> str:
        return f"name: {self.name}, age:{self.age}, address:{self.address}"
    
    def save_person(person, filename):
        with open(filename, 'wb') as file:
            pickle.dump(person, file)


persons ={
    Person('farzad', 21, 'Tehran'),
    Person('nima', 20, 'Mashhad')
}

Person.save_person(persons, "Persons.pkl")