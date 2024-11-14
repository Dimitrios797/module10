import time
from multiprocessing import Pool
import os

def read_info(name):
    try:
        with open(name, 'r', encoding='utf-8') as file:
            while True:
                line = file.readline()
                if not line: 
                    break

    except FileNotFoundError:
        print(f"Ошибка: Файл '{name}' не найден.")

if __name__ == '__main__':

    print("Текущая рабочая директория:", os.getcwd())


    filenames = [f'./file {number}.txt' for number in range(1, 5)]


    start_time_linear = time.time()
    for filename in filenames:
        read_info(filename)
    print(f"Линейный вызов: {time.time() - start_time_linear:.6f} секунд")


    start_time_multiprocessing = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    print(f"Многопроцессный вызов: {time.time() - start_time_multiprocessing:.6f} секунд")