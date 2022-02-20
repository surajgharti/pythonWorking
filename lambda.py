people = [
    {"name": "Suraj", "house": "Nayagaun"},
    {"name": "Sarmila", "house": "Pokhara"},
    {"name": "Sukripa", "house": "Nepal"}
]
#def f(person):
#    return person["house"]

#people.sort(key=f)

people.sort(key=lambda person: person["house"])
print(people)