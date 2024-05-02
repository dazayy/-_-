import os
import json

def update_values(test_item, values_data):
    test_id = test_item["id"]
    for value_item in values_data["values"]:
        if value_item["id"] == test_id:
            test_item["value"] = value_item["value"]
            break

    if "values" in test_item:
        for nested_item in test_item["values"]:
            update_values(nested_item, values_data)


def read_file(path:str):
    with open(path, "r") as file:
        data = json.load(file)

    return data


def task3(values_path:str, tests_path:str, report_path:str):

    tests_data = read_file(tests_path)
    values_data = read_file(values_path)


    updated_tests_data = tests_data.copy()  
    for test_item in updated_tests_data["tests"]:
        update_values(test_item, values_data)

    with open(report_path, "w") as report_file:
        json.dump(updated_tests_data, report_file, indent=2)


def main():
    
    # tests_path = "task3/tests.json"
    # values_path = "task3/values.json"
    # report_path = "task3/report.json"


    tests_path = input("Введиет путь до структуры данных: ")
    values_path = input("Введите путь до фала со значениями: ")
    report_path = input("Введите путь до отчета: ")

    if not(os.path.exists(tests_path) or os.path.exists(values_path)):
        print("Неверно указаны пути.")
    else:
        task3(values_path, tests_path, report_path)
        print("Отчет создан")


main()