''' Lab 03 - Excercise 03 '''

def count_tul(tul):
    cnt = 0
    for x in tul:
        cnt += 1
    return cnt

def index_tul(tul, item):
    for x in range(0, count_tul(tul)):
        if tul[x] == item:
            return x

tul = (9, 3, 0, -4, 8, 7, 10, -1, 5)
item = 9

print(f"The number of items in the tuple is {count_tul(tul)}")
print(f"The first index of {item} is {index_tul(tul, item)}")
