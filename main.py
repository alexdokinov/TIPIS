# Необходимо получить графики гармонического и цифрового (однополярный меандр)  сигнала с частотами 1,2,4,8 герц.
#
# Для каждого сигнала необходимо получить спектр
#
# Результат необходимо представить в виде картинки и в виде архива проекта/приложения(с исходными текстами).
import numpy as np
import matplotlib.pyplot as pyplot

t = np.linspace(0, 1, 1000)
frequency = [1, 2, 4, 8]


def support_GUI():
    pyplot.xlabel('Время в секундах')
    pyplot.ylabel('Амплитуда')
    pyplot.legend()
    pyplot.grid()
    pyplot.show()


def spectrum(signal, type_of_signal, index):
    if type_of_signal:
        pyplot.subplot(2, 2, 2)
        pyplot.title('Спектр гармонического сигнала')
    else:
        pyplot.subplot(2, 2, 4)
        pyplot.title('Спектр цифрового сигнала')

    spectr = np.fft.fft(signal)
    frequency_axis = np.fft.fftfreq(len(spectr), 1 / 1000)

    for a in frequency:
        pyplot.plot(frequency_axis, np.abs(spectr), label=f'Частота {frequency[index]} Гц')

    pyplot.xlabel('Частота (Гц)')
    pyplot.ylabel('Амплитуда спектра')
    pyplot.legend()
    pyplot.grid()
    pyplot.xlim(0, 50)
    pyplot.show()


def harmonic_signal(index):
    pyplot.subplot(2, 2, 3)
    signal = np.sin(2 * np.pi * frequency[index] * t)
    pyplot.plot(t, signal, label=f'Частота {frequency[index]} Гц')
    pyplot.title('Гармонический сигнал')
    support_GUI()
    spectrum(signal, 1, index)


def digital_signal(index):
    pyplot.subplot(2, 2, 1)
    signal = np.where(np.sin(2 * np.pi * frequency[index] * t) >= 0, 1, -1)
    pyplot.plot(t, signal, label=f'Частота {frequency[index]} Гц')
    pyplot.title('Цифровой сигнал')
    support_GUI()
    spectrum(signal, 0, index)


for i in range(1, 4):
    digital_signal(i)
    harmonic_signal(i)

