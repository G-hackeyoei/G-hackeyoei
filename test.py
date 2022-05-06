import random
while True:
    choice = input('【【口算】开平方根/立方根训练器】\n输入后会立刻开始计时，请小心使用\n训练开平方根输入2，训练开立方根输入3\n输入：')
    if choice == '2':
        num = random.randint(10, 99)
        print('√' + str(num ** 2) + '=', end=' ')
        res = int(input())
        if res == num:
            print('挑战成功！')
        else:
            print('挑战失败！答案：' + str(num))
    if choice == '3':
        num = random.randint(10, 99)
        print('3√' + str(num ** 3) + '=', end=' ')
        res = int(input())
        if res == num:
            print('挑战成功！')
        else:
            print('挑战失败！答案：' + str(num))
