#猜数字
#两人可玩
import random
import getpass

s = '''
    猜数字游戏
1、可选择单人或两人游戏；
2、单人游戏由电脑随机出一个0～100范围的数字，
玩家最多可以猜6次;
3、两人游戏，首先由一方出题，给另一方猜，最多
猜6次;
4、一局结束后选择退出或重新开始
'''
print(s)

def guess(target):
    for i in range(6):
        gnum = eval(input('请输入一个整数：'))
        if gnum == target:
            if i < 3:
                print('{}次就猜对了！你是天才吧～～'.format(i + 1))
            else:
                print('太棒了，猜对咯～～')
            break
        elif gnum > target:
            if i < 4:
                print('你猜的数有点大咯！你还有{}次机会。'.format(5 - i))
            elif i == 4:
                print('你猜的数有点大，你只剩最后一次机会咯。')
            else:
                print('最后一次机会没能把握好，你猜的数偏大呢！')
        elif gnum < target:
            if i < 4:
                print('你猜的数有点小咯！你还有{}次机会。'.format(5 - i))
            elif i ==  4:
                print('你猜的数有点小呢！你只剩最后一次机会咯。')
            else:
                print('最后一次机会没把握好，你猜的数偏小呢！')

#单人游戏
def singleGame(n=100):
    print('电脑已出题，请猜出一个0~{}以内的整数'.format(n))
    return random.randint(0, n)

#双人游戏
def doubleGame():
    tnum = getpass.getpass("请(ha)出(ha)题(不要让对方知道哦):")
    return eval(tnum)

#主要逻辑
def main():
    start = input('开始游戏?(y/n)')
    while start == 'y' or start == 'Y':
        game = input('单人(s)游戏还是双人(d)游戏？(s/d)')
        if game == 's' or game == 'S':
            rnum = singleGame()
            guess(rnum)
            start = input('是否再来一次?(y/n)')
        elif game == 'd' or game == 'D':
            tnum = doubleGame()
            guess(tnum)
            start = input('是否再来一次?(y/n)')
        else:
            print('输入有误，请重新输入')


if __name__ == "__main__":
    main()
