import random


def get_unique_list_numbers(start=-10, end=10, len_=15) -> list[int]:
    list_ = []
    while len(list_) < len_:
        digit_ = random.randint(start, end)
        if digit_ not in list_:
            list_.append(digit_)

    return list_


ne_kak_y_drygih = get_unique_list_numbers()
print(ne_kak_y_drygih)
print(len(ne_kak_y_drygih) == len(set(ne_kak_y_drygih)))
print(len(ne_kak_y_drygih))
print(len(set(ne_kak_y_drygih)))
