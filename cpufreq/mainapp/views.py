import threading
from statistics import mean
from time import sleep
from django.http import HttpResponseNotFound
from django.shortcuts import render
from matplotlib import pyplot as plt
from psutil import cpu_percent
from mainapp.models import FrequencyCPU

# Create your views here.


header_menu = ['Гавная страница', 'Графики загрузки процессора']


def freq_cpu(sec=5):
    while True:
        freq = cpu_percent(interval=None)
        new_f_cpu = FrequencyCPU(frequency=freq)
        new_f_cpu.save()
        sleep(sec)


th = threading.Thread(target=freq_cpu).start()


# Представления

def index(request):
    return render(request, 'mainapp/index.html', {'menu': header_menu, 'title': 'Главная страница'})


def graph(request):
    freq = freq_lst()
    graph_cpu(freq, param='5_second', unit='c x 5')
    # print(list(freq_lst_minute(freq)))
    lst_freq = list(freq_lst_minute(freq))
    average_for_minute = [round(mean(i), 1) for i in lst_freq]
    graph_cpu(average_for_minute, '1_minute', unit='мин')
    return render(request, 'mainapp/graph.html', {'menu': header_menu, 'title': 'Графики'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# Вспомогательные функции

def freq_lst(): # Получение из БД 720 записей (5 х 170 = 3600 - записи за последний)
    freq = FrequencyCPU.objects.all().order_by('-id')[:720]
    freq_lst = [i.frequency for i in freq]
    freq_lst.reverse()
    return freq_lst


def freq_lst_minute(freq):
    for i in range(0, len(freq), 12):
        yield freq[i: i + 12]


def graph_cpu(freq, param, unit):
    fig, ax = plt.subplots()
    ax.set_title('График загрузки процессора')
    ax.set_xlabel(f'Время, {unit}')
    ax.set_ylabel('Частота, %')
    # ax.set_xlim((0, 100))
    ax.set_ylim((-10, 110))
    ax.grid()

    # freq = freq_lst()
    # print(len(freq))
    x = range(0, len(freq))
    y = freq
    # print(y, type(y))

    ax.plot(x, y)
    # plt.show()
    plt.savefig(f'static/graph_{param}.png')
