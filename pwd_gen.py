import random

a = int(input())
pas = ''
for x in range(a):  # Количество символов
    pas = pas + random.choice(list(
        '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))  # Символы, из которых будет составлен пароль
print('your password is: ', pas)
