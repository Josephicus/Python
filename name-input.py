


name = input('Podaj swoje imię ')
lname=name.lower()


if lname==('maria'):
    print(lname)
    print('Cfane, ale możesz by i kobietą i mężczyzną')
elif lname==(''):
    print('Musisz podac jakąs wartosc')
elif lname.endswith('a'):
    print(lname)
    print('jestes kobieta')
else:
    print(lname)
    print('Jestes mężczyzną')

blank=input()
