def hi():
    print('Hi there')
    print ('How are you')

name = 'Hannah'


def hello(name):
    print(name)
    if name == 'Hannah':
        print ('Hi Hannah')
    elif name == 'Sonja':
        print ('Hi Sonja!')
    else:
        print ('Hi anonymous!')

    hi()
hello(f'{name} Smith')


class Dog:
    def __init__(self, age, name, favourite_hobby):
        self.age=age
        self.name=name
        self.favourite_hobby=favourite_hobby
    
    def get_name (self):
        print(f'my name is {self.name}')

dog_1 = Dog(3, 'Buffy', 'barking')
dog_1.get_name()

def hallo(name):
    print('Hi'+ name +'!')


girls =['Rachel', 'Monika', 'Phoebe', 'Ola', 'Hannah']
for name in girls:
    print('Hi'+ ' ' + name + '!')
girls =['Rachel', 'Monika', 'Phoebe', 'Ola', 'Hannah']
for name in girls:
    hallo(name)
    print('Next girl')


for i in range (1,6):
    print(i)
