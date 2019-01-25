import re

userPrompt = input('Введите ваше предложение')

re.sub(' +', ' ', userPrompt)

temp = re.sub(' +', ' ', userPrompt)
temp = temp.lower()

print(temp.title())