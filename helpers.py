import random

from datetime import date, timedelta


# Генерируем словарь для формы заказа
def generate_order_info():
    metro_stations = ["Черкизовская", "Сокольники", "Охотный ряд",
                      "Кропоткинская", "Спортивная", "Фрунзенская",
                      "Аэропорт", "Динамо", "Белорусская"]
    colors = ['black', 'grey']
    rental_durations = ['сутки', 'двое суток', 'трое суток', 'четверо суток',
                        'пятеро суток', 'шестеро суток', 'семеро суток']

    return {
        'name': random.choice(['Иван', 'Ольга', 'Сергей', 'Анна']),
        'surname': random.choice(['Петросян', 'Акинфеев', 'Игнашевич', 'Дубовицкая']),
        'address': random.choice(['Москва, Степной', 'Ленинград, д. 100',
                                  'У чёрта на куличках', 'Промышленная, дом 7']),
        'metro': random.choice(metro_stations),
        'phone': random.randint(10000000000, 99999999999),
        'date': (date.today() + timedelta(
            days=random.randint(1, 7))).strftime('%d.%m.%Y'),
        'duration': random.choice(rental_durations),
        'color': random.choice(colors),
        'comment': random.choice(['', 'позвонить заранее', 'вход со двора',
                                  'код на двери 779'])
    }
