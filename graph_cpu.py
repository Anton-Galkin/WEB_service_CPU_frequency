import keyboard
import matplotlib.pyplot as plt
from psutil import cpu_percent
from time import sleep


def freq_cpu_array(sec=1):
    print(f'Для остановки программы нажмите "ПРОБЕЛ"')
    freq_array = []
    while True:
        frequency = cpu_percent(interval=None)
        print(f'Частота процессора: {frequency}%')
        freq_array.append(frequency)

        if keyboard.is_pressed(hotkey='space'):
            break

        sleep(sec)

    return freq_array


print(freq_cpu_array())


def graph_cpu():
    fig, ax = plt.subplots()
    ax.set_title('График загрузки процессора')
    ax.set_xlabel('Время, с')
    ax.set_ylabel('Частота, %')
    # ax.set_xlim((0, 100))
    ax.set_ylim((0, 100))
    ax.grid()

    freq = freq_cpu_array()[1:]
    # print(len(freq))
    x = range(0, len(freq))
    y = freq
    # print(y, type(y))

    ax.plot(x, y)
    plt.show()


graph_cpu()
