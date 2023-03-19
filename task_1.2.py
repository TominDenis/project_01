# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]


sum_sound_time_a = 0
sum_sound_time_a += my_favorite_songs[4][1]
sum_sound_time_a += my_favorite_songs[6][1]
sum_sound_time_a += my_favorite_songs[3][1]

print('Пункт А: Три песни звучат', round(sum_sound_time_a), 'минут')


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}



sum_sound_time_b = 0
sum_sound_time_b += my_favorite_songs_dict['Staying\' Alive']
sum_sound_time_b += my_favorite_songs_dict['Out of Touch']
sum_sound_time_b += my_favorite_songs_dict['Waste a Moment']

print('Пункт В: Три песни звучат', round(sum_sound_time_b), 'минут')


# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

import random

ran_song = random.sample(my_favorite_songs, 3)
print('Пункт С/А: Три случайные песни:', ran_song)

ran_song_d = random.sample(list(my_favorite_songs_dict), 3)
print('Пункт С/В: Три случайные песни', ran_song_d)



# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 



