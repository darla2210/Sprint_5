import random

def generate_email():
    names = ["ivan", "anna", "sergey", "olga"]
    surnames = ["ivanov", "petrova", "sidorov", "smirnova"]
    cohort = "1999"  # можно заменить на свой номер
    random_digits = str(random.randint(100, 999))
    domain = "@yandex.ru"

    email = f"{random.choice(names)}_{random.choice(surnames)}_{cohort}_{random_digits}{domain}"
    return email


import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    print(generate_email())
    print(generate_password())



# email для входа
def get_existing_email():
    return "di.music96@yandex.ru"

# пароль для входа
def get_existing_password():
    return "testtest"

if __name__ == "__main__":
    print(generate_email())
    print(generate_password())