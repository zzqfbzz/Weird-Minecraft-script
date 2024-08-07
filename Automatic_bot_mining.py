# -*- coding:utf-8 -*-
# @FileName :Automatic_bot_mining.py
# @Author   :zz
# @Versions :1.0.0

import pyautogui
import pyperclip
import time

# 0:序列命名: 从按顺序开始召唤bot[优点,召唤过的bot,秒加载,缺点,不能多点同时进行]
# 1:坐标命名: 根据坐标命名bot[优点,可以多点同时进行,缺点,没召唤过的bot 需要重新加载]
bot_name_type = 0

# 前缀
Prefix = "bot_"
# 后缀
Suffix = ""


def rsleep(seconds):
    for i in range(seconds, 0, -1):
        print(f'倒计时: {i} 秒')

        # 最后三秒在游戏里面倒计时
        if i <= 3:
            pyautogui.press('enter')

            pyautogui.press('/')

            pyautogui.press('backspace')

            pyautogui.typewrite(str(i))

            pyautogui.press('enter')

        time.sleep(1)


def main():
    print('最小坐标坐标应该是面向北方,左上角的格子')
    print('最大坐标坐标应该是面向北方,右下角的格子')
    x_min = input('x最小坐标:')
    z_min = input('z最小坐标:')
    x_max = input('x最大坐标:')
    z_max = input('z最大坐标:')
    y = input('y高度:')
    print('请确保已经离开需要召唤bot的区域')
    print('请在按下回车后，点击自己的游戏窗口')
    input('按回车键继续')

    # 等待 6 秒以便切换到需要操作的窗口
    rsleep(6)

    attack_list = []

    name_num = 0
    for x in range(int(x_min), int(x_max) + 1):
        for z in range(int(z_min), int(z_max) + 1):
            name_num += 1

            if bot_name_type:
                t_name = str(x) + str(z)
            else:
                t_name = str(name_num)

            t_name = Prefix + t_name + Suffix

            attack_list.append(t_name)

            text_to_paste = f'player {t_name} spawn at {x} {y} {z}'
            print(f'{name_num}:{t_name} at {x} {y} {z}')

            pyperclip.copy(text_to_paste)
            time.sleep(0.3)
            pyautogui.press('/')

            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')

    print(f'本次召唤bot{len(attack_list)}个')
    input('请在所有bot加载完成后按下回车键')

    # 等待 6 秒以便切换到需要操作的窗口
    rsleep(6)

    pyautogui.press('enter')
    for t_name in attack_list:
        pyautogui.press('/')

        pyperclip.copy(f'player {t_name} look down')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

        pyautogui.press('/')
        pyperclip.copy(f'player {t_name} attack continuous')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')


if __name__ == '__main__':
    main()
