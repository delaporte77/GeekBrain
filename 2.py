link = input('Введите вашу ссылку')

templink = ''
temp = ''

if 'www' in link:
    link.replace('www.', '')
    temp = 'www.'
elif 'http' in link:
    link.replace('http://', '')
    temp = 'http://'
elif 'https' in link:
    link.replace('https://', '')
    temp = 'https://'

if '@' in link:
    for i in link:
        if i != '.' and i != '@':
            i = '*'
            templink += i
        else:
            templink += i
else:

    for i in link:
        if i != '.':
            i = '*'
            templink += i
        else:
            templink += i


print(temp + templink)