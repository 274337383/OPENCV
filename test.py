# -*- codeing = utf-8 -*-
# @Time : 2021/8/5 15:33
# @Author : 张涛
# @File : test.py
# @software : PyCharm

import random

num = random.randint(0, 10)
end = 0
print('------------------猜数字------------------')

temp = input("猜数字(1~10之间):")
guess = int(temp)

if guess == num:
    print("你猜对了!")

else:
    print("猜错了!")
    if guess > num:
        print("太大了")
        end = guess - num
        print("超过了%i" % end)
    else:
        print("太小了")
        end = num - guess
        print("低了%i" % end)

print("你输入的数字:%i" % guess)
print("正确的数字:%i" % num)

print("Game over")
