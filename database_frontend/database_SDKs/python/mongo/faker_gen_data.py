from random import randint
import faker
from datetime import datetime as dt
fake = faker.Faker(locale='pt_BR')


def gen_client():
    return {
        'name': fake.name(),
        'birthdate': dt.strftime(fake.date_of_birth(), "%Y-%m-%d"),
        'cpf': fake.cpf(),
        'salary': float(fake.pydecimal(left_digits=5, right_digits=2, positive=True)),
        'phone_numbers': [fake.phone_number() for i in range(0, randint(1, 3))],
        'job': fake.job()
    }


for i in range(10):
    print((gen_client()))