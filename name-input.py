name = input("Podaj swoje imię ")

try:
    if name.endswith("a"):
        print(name)
        print('jestes kobieta')
    else:
        print(name)
        print('Jestes mężczyzną')
except:
    name("Maria")
    print("Cfane, ale możesz by i kobietą i mężczyzną")

blank=input()
