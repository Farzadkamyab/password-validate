import pickle
from persons import Person

def load_from_file(path):
    with open(path, 'rb') as file:
        persons_list = pickle.load(file)
    return persons_list

people = load_from_file("/home/farzadkb/farzad/pass/Persons.pkl")

for person in people:
    print(person)