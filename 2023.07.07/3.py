# ПЕРЕИМЕНОВАТЬ: переменным требуется давать имена по смыслу, так чтобы код можно было удобнее и быстрее читать — имена n, h, m очень мало говорят о том, какие значения ассоциированы с данными переменными — вместо них стоило назвать переменные minutes_total, hours, minutes
n = int(input())
# УДАЛИТЬ: эти переменные используются каждая только единожды: с учётом простоты вычисляемых выражений, объявление данных переменных избыточно
h = n // 60
m = n % 60
# ИСПРАВИТЬ: в этой задаче требуется использовать возможности f-строк
# ИСПРАВИТЬ: вывод не соответствует требуемому формату (см. тест)
print(n, " мин - это ", h, " час ", m, "минут.")


# ДОБАВИТЬ: результат выполнения программы с собственными данными, например:
# 291
# 291  мин - это  4  час  51 минут.
# КОММЕНТАРИЙ: а должно быть:
# 291 мин - это 4 час 51 мин

# КОММЕНТАРИЙ: в случае, если вы будете генерировать строку не для чтения человеком, а для другой функции/класса/программы — неверный формат может стоить вам неработающего приложения


# ИТОГ: доработать — 1/3
