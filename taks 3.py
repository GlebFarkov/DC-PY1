import random as r

def get_unique_list_numbers() -> set[int]:
    list_nums = [r.randint(-10, 10) for i in range(15)]
    list_unique_nums = set(list_nums)
    return list_unique_nums


if __name__ == '__main__':
    list_unique_numbers = get_unique_list_numbers()
    print(list_unique_numbers)
    print(len(list_unique_numbers) == len(set(list_unique_numbers)))
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
