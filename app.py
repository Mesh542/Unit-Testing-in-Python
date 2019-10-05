class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def allowed_in_the_club(self):
        if self.age >= 18:
            return True
        return False

    def __repr__(self):
        return f'''
        Name:\t\t{self.name}
        Surname:\t{self.surname}
        Age:\t\t{self.age}
        '''            

print('Enter Person(s) Details and enter "exit" to stop\n\n')
flag = True
count = 1
people = []

while flag:
    print(f"person {count}'s details")
    try:
        name = input('Name:\t\t')
        surname = input('Surname:\t')
        age = int(input('Age:\t\t'))
        
        person = Human(name, surname, age)
        people.append(person)

        print('\n')
        answer = input('continue? (type exit to stop)\t')
        print('\n\n')

        if answer.lower() == 'exit':
            flag = False
            continue
        count += 1

    except ValueError as e:
        print(e)
if count > 1:
    print(f'These are the {count} people going to the club')
elif count == 0:
    print('There are not people going to the club')
else:
    print('Error')        
for person in people:
    print(person.__repr__()+f'Allowed in:\t{person.allowed_in_the_club()}\n\n')


