import os
import math
import random

def create_data(circle_path:str,points_path:str):

    def generate_data():

        with open(points_path, "w") as file:
            for _ in range(100):
                file.write(f"{random.uniform(-10**38, 10**38)} {random.uniform(-10**38, 10**38)}\n")


        with open(circle_path, "w") as file:
            for _ in range(100):
                center_x = round(random.uniform(-10**38, 10**38), 2)
                center_y = round(random.uniform(-10**38, 10**38), 2)
                radius = round(random.uniform(-10**38, 10**38), 2)
                file.write(f"{center_x} {center_y}\n{radius}\n")

    generate_data()

def get_circle_data(path:str) -> list:
    circle_data = []
    with open(path, "r") as f:
        i = 0
        for line in f:
            if len(line.split()) == 1:
                circle_data[i].append(float(line))
                i += 1
            else:
                circle_data.append(list(map(float, line.split())))
    return circle_data        


def get_points_data(path:str) -> list:
    points_data = [] 
    with open(path, "r") as f:
         for line in f:
            points_data.append(list(map(float, line.split())))

    return points_data



def calculate_distance(center_x, center_y, R, point_x, point_y):
    d = math.sqrt((point_x - center_x)**2 + (point_y - center_y)**2)

    if d < R:
        return 1
    elif d == R:
        return 0
    return 2


def process_data(path_circle, path_points):
    circle_data = get_circle_data(path_circle)
    points_data = get_points_data(path_points)

    # вывод массивов 
    # print("-"*100)
    # print(f"circle_data:\t{circle_data}")
    # print()
    # print(f"circle_data:\t{points_data}\n")
    # print("-"*100)



    if (len(points_data) == len(circle_data)):
        N = len(points_data)
        for i in range(N):
            center_x, center_y, r = circle_data[i]
            point_x, point_y = points_data[i] 
            
            # вывод данных, которые учавствуюут в вычислениях
            # print(f"centerX: {center_x}\ncenterY: {center_y}\nr: {r}\npointX: {point_x}\npointY:{point_y}")
            print(f"--------result №{i+1}:\t{calculate_distance(center_x, center_y, r, point_x, point_y)}\n")
    else:
        
        for i in range(len(circle_data)):
            center_x, center_y, r = circle_data[i]
            for j in range(len(points_data)):
                point_x, point_y = points_data[j] 
                
                # вывод данных, которые учавствуюут в вычислениях
                # print(f"centerX: {center_x}\ncenterY: {center_y}\nr: {r}\npointX: {point_x}\npointY:{point_y}")
                print(f"--------result №{i+1}:\t{calculate_distance(center_x, center_y, r, point_x, point_y)}\n")


def main():
    

    path_circle = "task2/circle_data.txt"
    path_points ="task2/points_data.txt"


    # данные из тз
    # path_circle = "task2/tests_data/circle_data.txt"
    # path_points ="task2/tests_data/points_data.txt"

    if not (os.path.exists(path_circle) or os.path.exists(path_points)):
        create_data(path_circle, path_points)
    process_data(path_circle, path_points)


main()
