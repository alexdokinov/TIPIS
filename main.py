# Необходимо получить графики гармонического и цифрового (однополярный меандр)  сигнала с частотами 1,2,4,8 герц.
#
# Для каждого сигнала необходимо получить спектр
#
# Результат необходимо представить в виде картинки и в виде архива проекта/приложения(с исходными текстами).
import numpy as np
import matplotlib.pyplot as pyplot


def support_GUI():
    pyplot.xlabel('Время в секундах')
    pyplot.ylabel('Амплитуда')
    pyplot.legend()
    pyplot.grid()
    pyplot.show()


def spectrum(signal, freq, type_of_signal):
    pyplot.figure(figsize=(10, 6))
    if type_of_signal:
        pyplot.title('Спектр гармонического сигнала')
    else:
        pyplot.title('Спектр цифрового сигнала')

    spectr = np.fft.fft(signal)
    frequency_axis = np.fft.fftfreq(len(spectr), 1 / 1000)

    for a in freq:
        pyplot.plot(frequency_axis, np.abs(spectr), label=f'Частота {a} Гц')

    pyplot.xlabel('Частота (Гц)')
    pyplot.ylabel('Амплитуда спектра')
    pyplot.legend()
    pyplot.grid()
    pyplot.show()


def harmonic_signal(freq, time):
    pyplot.figure(figsize=(10, 6))
    for a in freq:
        signal = np.sin(2 * np.pi * a * time)
        pyplot.plot(t, signal, label=f'Частота {a} Гц')
    pyplot.title('Гармонический сигнал')
    support_GUI()
    spectrum(signal, freq, 1)


def digital_signal(freq, time):
    pyplot.figure(figsize=(10, 6))
    for a in freq:
        signal = np.where(np.sin(2 * np.pi * a * time) >= 0, 1, -1)
        pyplot.plot(t, signal, label=f'Частота {a} Гц')
    pyplot.title('Цифровой сигнал')
    support_GUI()
    spectrum(signal, freq, 0)


t = np.linspace(0, 1, 1000)
frequency = [1, 2, 4, 8]

digital_signal(frequency, t)
harmonic_signal(frequency, t)
