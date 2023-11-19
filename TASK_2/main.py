import numpy as np
import matplotlib.pyplot as pyplot
from scipy.fft import fft, ifft

Amplitude_of_carrier = 1
Frequency_of_carrier = 32
Frequency_of_meandr = 4
T = 1

t = np.linspace(0, 1, 1000)
meandr = np.where(np.sin(2 * np.pi * Frequency_of_meandr * t) > 0, 1, 0)


def modulation(i):
    if i == 0:
        return Amplitude_of_carrier * meandr * np.sin(2 * np.pi * Frequency_of_carrier * t)
    elif i == 1:
        return Amplitude_of_carrier * np.sin(2 * np.pi * Frequency_of_carrier * t + 2 * np.pi * Frequency_of_meandr *
                                             np.cumsum(meandr) * (1 / 100))
    elif i == 2:
        return np.sin(4 * np.square(np.pi) * Frequency_of_meandr * t + meandr * np.pi / 2)


def support_modulation(n):
    names_of_modulation = ['Амплитудная модуляция', 'Частотная модуляция', 'Фазовая модуляция']
    pyplot.title(names_of_modulation[n])
    pyplot.xlabel('Время')
    pyplot.ylabel('Амплитуда')


def spectrum(l):
    list_of_names = ['Спектр амплитудно-модулированног сигнала', 'Спектр частотно-модулированного сигнала', 'Спектр '
                                                                                                            'фазово-модулированного сигнала']
    spectr = fft(modulation(l))
    frequency_of_spectrum = np.fft.fftfreq(len(t), t[1] - t[0])
    pyplot.plot(frequency_of_spectrum, np.abs(spectr))
    pyplot.title(list_of_names[l])
    pyplot.xlabel('Частота')
    pyplot.ylabel('Амплитуда')
    pyplot.xlim(0, 100)


def filther(sign):
    pyplot.subplot(3, 1, 3)
    sign = np.where(sign > 0, 1, 0)
    pyplot.plot(t, sign)
    pyplot.title('Результат фильтрации синтезированного сигнала')
    pyplot.xlabel('Время')
    pyplot.ylabel('Амплитуда')
    pyplot.tight_layout()
    pyplot.show()


def synthesis():
    signal = modulation(0)
    spectr = fft(signal)
    freq = np.fft.fftfreq(len(t), t[1] - t[0])
    cut = 5
    fft_result = np.where(np.abs(freq) <= cut, spectr, 0)
    pyplot.plot(freq, np.abs(fft_result))
    pyplot.title('Обрезанный сигнал')
    pyplot.xlabel('Частота')
    pyplot.ylabel('Амплитуда')
    pyplot.xlim(0, 50)
    y_synthes = ifft(fft_result)
    pyplot.subplot(3, 1, 2)
    pyplot.plot(t, y_synthes.real)
    pyplot.title('Синтезированный сигнал')
    pyplot.xlabel('Время')
    pyplot.ylabel('Амплитуда')
    pyplot.tight_layout()
    filther(y_synthes)


pyplot.figure(figsize=(12, 8))
pyplot.subplot(3, 1, 1)
pyplot.plot(t, modulation(0))
support_modulation(0)
pyplot.subplot(3, 1, 2)
pyplot.plot(t, modulation(1))
support_modulation(1)
pyplot.subplot(3, 1, 3)
pyplot.plot(t, modulation(2))
support_modulation(2)
pyplot.tight_layout()
pyplot.show()

pyplot.figure(figsize=(12, 8))
pyplot.subplot(3, 1, 1)
spectrum(0)
pyplot.subplot(3, 1, 2)
spectrum(1)
pyplot.subplot(3, 1, 3)
spectrum(2)
pyplot.tight_layout()
pyplot.show()

pyplot.figure(figsize=(12, 8))
pyplot.subplot(3, 1, 1)
synthesis()
pyplot.tight_layout()
pyplot.show()
