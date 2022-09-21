import numpy as np

k = int(input("Введите K:"))
print("~" * 24)

m3 = [[0, 0, 1, 1, 1],
      [1, 1, 0, 1, 0],
      [1, 0, 0, 1, 1],
      [1, 1, 1, 0, 0],
      [0, 1, 1, 0, 1]]  # Матрица связи для n=5 и k=3

m2 = [[1, 1, 0, 0],
      [1, 0, 1, 0],
      [0, 1, 0, 1],
      [0, 0, 1, 1]]  # Матрица связи для n=4 и k=2

log3 = [lambda z, x, y: (not z or not x) and y,
        lambda z, x, y: z and x and y,
        lambda z, x, y: z == x == y,
        lambda z, x, y: z != x != y,
        lambda z, x, y: z or x or y]  # Логическое выражения для n=5 k = 3

log2 = [lambda z, x: not z or x,
        lambda z, x: z and x,
        lambda z, x: z == x,
        lambda z, x: z != x,
        lambda z, x: z or x]  # Логическое выражения для n=4 k = 2


def step_for_kauf2(inp_v, connection_matrix):  # функция для аттракторов
    res_v = []  # Матрица для атракторов
    for log_id, line in enumerate(connection_matrix):
        if k == 2:
            index1, index2 = [i for i, z in enumerate(line) if z == 1]
            z = inp_v[index1]
            x = inp_v[index2]
            res_v.append(int(log2[log_id](z, x)))  # добавляем получившуюся строку в матрицу
    return res_v

def step_for_kauf3(inp_v, connection_matrix):  # функция для аттракторов
    res_v = []  # Матрица для аттракторов
    for log_id, line in enumerate(connection_matrix):
        if k == 3:
            index1, index2, index3 = [i for i, z in enumerate(line) if z == 1]
            z = inp_v[index1]
            x = inp_v[index2]
            y = inp_v[index3]
            res_v.append(int(log3[log_id](z, x, y)))  # добавляем получившуюся строку в матрицу
    return res_v

if k == 2:
    attrs_len = []
    all_atts = []
    for i in range(16):
        trig = True
        vector = list(map(int, '{0:04b}'.format(i)))
        attractors = []
        state_id = 0
        while vector not in attractors:
            print(state_id, "Состояние", *vector)
            attractors.append(vector)
            vector = step_for_kauf2(vector, m2)
            state_id += 1

            if vector in all_atts:
                trig = False

        if trig == True:
            if vector not in all_atts:
                all_atts.append(vector)

        attrs_len.append(len(attractors) - attractors.index(vector))

        print(state_id, "Состояние", *vector)
        print("Длинна аттрактора:", len(attractors) - attractors.index(vector))
        print("~" * 24)

    print('Mean attractors:', np.mean(attrs_len))
    print('Different attractors:', len(all_atts))

if k == 3:
    attrs_len = []
    all_atts = []
    for i in range(32):
        trig = True
        vec = list(map(int, '{0:05b}'.format(i)))
        attractors = []
        state_id = 0
        while vec not in attractors:
            print(state_id, "Состояние", *vec)
            attractors.append(vec)
            vec = step_for_kauf3(vec, m3)
            state_id += 1

            if vec in all_atts:
                trig = False

        if trig == True:
            if vec not in all_atts:
                all_atts.append(vec)

        attrs_len.append(len(attractors) - attractors.index(vec))

        print(state_id, "Состояние", *vec)
        print("Длинна аттрактора:", len(attractors) - attractors.index(vec))
        print("~" * 24)

    print('Mean attractors:', np.mean(attrs_len))
    print('Different attractors:', len(all_atts))
