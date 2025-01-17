from random import shuffle
import time

def main():
    while True:
        try:
            user_choice = int(input('Сколько пуль вставить (от 1 до 6): '))
            if user_choice < 1 or user_choice > 6:
                print("Пожалуйста, введите число от 1 до 6.")
                continue
        except ValueError:
            print("Пожалуйста, введите корректное число.")
            continue

        a = [0] * user_choice + [1] * (6 - user_choice)
        shuffle(a)

        while True:
            q = input('Вращать барабан? (Да/Нет): ')
            if q.lower() == 'да':
                time.sleep(0.8)
                shuffle(a)
                action = input('1. Вращать барабан 2. Стрелять: ')
                
                if action == '1':
                    shuffle(a)
                elif action == '2':
                    if a[0] == 0:
                        print('Вы проиграли!', a)
                    else:
                        print('Вы выиграли!', a)
                    break
                else:
                    print('Нет такой команды!')
                    break
            elif q.lower() == 'нет':
                print("Игра окончена.")
                return
            else:
                print('Пожалуйста, введите "Да" или "Нет".')

if __name__ == "__main__":
    main()
