import random
import time


class TestUser:
    first_name = 'first_name_user'
    last_name = 'last_name_user'
    email = f'{time.time()}@gmail.com'
    username = f'username{random.choice(list(range(1, 100000)))}'
    password = 'natediaz'