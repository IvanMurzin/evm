from math import floor
s2i = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12,
       "d": 13, "e": 14, "f": 15}


def convert_float(s, base):
    ret = 0
    if "." not in s:
        bef = s
    else:
        bef, aft = s.split(".")
    for i in enumerate(reversed(bef)):
        integer = s2i[i[1]]
        if integer >= base:
            raise ValueError
        ret += base**i[0] * integer
    if "." not in s:
        return ret
    for i in enumerate(aft):
        integer = s2i[i[1]]
        if integer >= base:
            raise ValueError
        ret += base**-(i[0] + 1) * integer
    return ret


x = input("Введите число: ")
base_x = int(input("Введите основание числа: "))
base_ans = int(input("Введите основание ответа: "))
lg_x = input(f"Логарифм {base_x}: ")
lg_ans = input(f"Логарифм {base_ans}: ")
if "." in x:
    n1 = len(x.split('.')[1])
else:
    n1 = 0
print(f"Количество знаков после запятой в начальном числе: {n1}")
number_count = floor(n1 * float(lg_x)/float(lg_ans)) + 1
print(f"Количество знаков после запятой по формуле: {number_count}")
answer_dec = convert_float(x, base_x)
answer_dec_bef, answer_dec_aft = str(answer_dec).split(".")
answer_dec_bef = int(answer_dec_bef)
answer_dec_aft = float(answer_dec_aft)/10**(len(answer_dec_aft))
answer_bef = ""
answer_aft = ""
while answer_dec_bef != 0:
    answer_bef = str(answer_dec_bef % base_ans) + answer_bef
    answer_dec_bef //= base_ans


while len(answer_aft) != number_count+1:
    answer_dec_aft *= base_ans
    answer_aft += str(int(answer_dec_aft))
    answer_dec_aft -= int(answer_dec_aft)

print(f"Ответ в {base_ans}-ной системе: {answer_bef}.{answer_aft}")
print("Не забудьте округлить по последней цифре!")
