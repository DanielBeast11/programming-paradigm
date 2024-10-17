import random

def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield random.randint(begin, end)

# random_number = gen_random(5, 1, 3)
# for i in random_number:
#     print(i)
