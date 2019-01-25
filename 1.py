emailList = []

while True:

    email = input('Введите ваш электронный адрес')

    if email not in emailList:
        emailList.append(email)

    print(emailList)
