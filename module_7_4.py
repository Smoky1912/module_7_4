from module_7_3 import *

# Входные данные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

# определение рез-ов соревнования
if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

# Использование %
# Пример итоговой строки: "В команде Мастера кода участников: 5 !"
team1_str = "В команде Мастера кода участников: %d !" % team1_num
print(team1_str)

# Пример итоговой строки: "Итого сегодня в командах участников: 5 и 6 !"
teams_str = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(teams_str)

# Использование format()
# Пример итоговой строки: "Команда Волшебники данных решила задач: 42 !"
team2_score_str = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(team2_score_str)

# Пример итоговой строки: "Волшебники данных решили задачи за 18015.2 с !"
team2_time_str = "Волшебники данных решили задачи за {} с !".format(team2_time)
print(team2_time_str)

# Использование f-строк
# Пример итоговой строки: "Команды решили 40 и 42 задач."
teams_tasks_str = f"Команды решили {score_1} и {score_2} задач."
print(teams_tasks_str)

# Пример итоговой строки: "Результат битвы: победа команды Мастера кода!"
challenge_result_str = f"Результат битвы: {challenge_result}"
print(challenge_result_str)

# Пример итоговой строки: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."
tasks_avg_str = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."
print(tasks_avg_str)