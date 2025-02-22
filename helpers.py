
import random
from datetime import datetime, timedelta
from data import rent_days, scooter_colour


info_client = {
    'name': random.choice(['Инджрих', 'Николай', 'Кори']),
    'last_name': random.choice(['Скалицкий', 'Бутусов', 'Тейлор']),
    'address': random.choice(['ул. Мира', 'улица Богов Войны']) +' '+ str(random.randint(1,99)),
    'metro': random.choice(['Улица Академика Янгеля' ,'Лихоборы']),
    'phone': f'+7{random.randint(100000000, 999999999)}'
}

about_scooter_rent = {
    'rent_day': random.choice(rent_days),
    'colour': random.choice(scooter_colour)
}

def generate_date_rent():
    current_date = datetime.now()
    next_date = current_date + timedelta(days=1)
    return next_date.strftime("%d.%m.%Y")