
correct_code = input("Proszę ustawić kod zamka szyfrowego: ")

def check_code ():
    code = input("Proszę wpisać kod do zamka szyfrowego: ")
    if (code == correct_code):
        print("Uzyskano dostęp")
    else:
            print("Nie uzyskano dostępu")
            check_code()

check_code()
