# ИСПОЛЬЗОВАТЬ: оформление кода согласно PEP 8 — в качестве образца можно использовать код из репозитория _scripts

a = int(input())
b = int(input())
if a % b == 0:
    # ИСПРАВИТЬ: этот способ форматирования строк устарел ещё четырнадцать лет назад, именно поэтому я вам его не показывал — стоило хотя бы задать мне вопрос о нём — используйте f-строки, они на порядок более производительны и удобны
    print("%d делится на %d нацело" % (a, b))
    # ИСПРАВИТЬ: слишком много вызовов print() — учитесь обходиться минимумом
    print("частное: %d" % (a // b))
else:
    print("%d не делится на %d" % (a, b))
    print("неполное частное: %d" % (a // b))
    # ИСПРАВИТЬ: вы уже вычисляли остаток, а здесь повторно выполняете ту же операцию — оптимизируйте
    print("остаток: %d" % (a % b))

# СДЕЛАТЬ: лучше выстроить код так, чтобы не прописывать генерацию очень похожего литерала второй раз, не использовать блок else, а функцию print() вызывать только один раз — подумайте, как это можно сделать


# ДОБАВИТЬ: результат выполнения программы с собственными данными


# ИТОГ: хорошо, но можно лучше — 2/3


# КОММЕНТАРИЙ: PEP 8 — сборник рекомендаций по стилистическому оформлению Python кода — их стоит использовать для большего удобства чтения своего и чужого кода: https://peps.python.org/pep-0008/
