import os
import statistics

def get_min_step(arr):
    median = statistics.median(arr)    
    step = 0
    for num in arr:
        step += abs(num - median)
    return int(step)

def main():
    # path = "task4/input.txt"

    path = input("Введите путь до фалйла с данными: ")
    
    if not os.path.exists(path):
        print("Неверно указан путь.")
    else: 
        with open(path, "r") as file:
            nums = [int(line.strip()) for line in file.readlines()]
            print("Минимальное кол-во ходов:", get_min_step(nums))


main()