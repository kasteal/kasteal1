import random as rand
import matplotlib.pyplot as plt

STUDENTS_AMOUNT = 30
MAX_GENERATION = 40
P_CROSS = 0.8
P_MUTATION = 0.1
RAND_SEED = 4
rand.seed(RAND_SEED)

zachet = (60, 60, 40, 40)


def death(s):
    # кол-во заваленных предеметов
    c = 0
    for i in range(4):
        if s[i] < zachet[i]:
            f = peresdacha(s[i], zachet[i])
            if not f:
                c += 1
    return c


# рассчитывает успешно ли пересдал, учитывая количество затраченных часов
def peresdacha(s_points, minimum):
    return rand.choices([1, 0], weights=[s_points, 10+minimum-s_points])[0]


def generate_group(n):
    students = []
    for i in range(n):
        points = 300
        s = [0]*5

        while points > 0:
            x = rand.randint(0, points)
            s[rand.randint(0, 4)] += x
            points -= x
        students.append(s)
    return students


def tournament(group, res_ses, students_amount):
    elita = []
    for i in range(students_amount):
        i1 = i2 = 0
        while i1 == i2:
            i1, i2 = rand.randint(0, students_amount-1), rand.randint(0, students_amount-1)
        if res_ses[i1] < res_ses[i2]:
            i1 = i2
        elita.append(group[i1])

    return elita


def crossing(s1, s2):
    ind = rand.randint(0, 4)
    dif = s1[ind] - s2[ind]
    s1[ind], s2[ind] = s2[ind], s1[ind]
    ind = rand.randint(0, 4)
    if dif > 0:
        s2 = del_extra_points(s2, dif)
        s1[ind] += dif
    else:
        s1 = del_extra_points(s1, abs(dif))
        s2[ind] += abs(dif)
    return s1, s2


def del_extra_points(s, extra_points):
    for i in range(5):
        k = min(extra_points, s[i])
        s[i] -= k
        extra_points -= k
    return s


def mutation(lab_rat):
    for i in range(5):
        ind = rand.randint(0, 4)
        ind2 = rand.randint(0, 4)
        while lab_rat[ind2] < 5:
            ind2 = rand.randint(0, 4)
        lab_rat[ind] += 5
        lab_rat[ind2] -= 5

    return lab_rat


group = generate_group(STUDENTS_AMOUNT)
group_res = []
res = [0]*STUDENTS_AMOUNT
mission_complete = 0
gen_counter = 0

while not mission_complete and gen_counter < MAX_GENERATION:
    for i in range(STUDENTS_AMOUNT):
        res[i] = death(group[i])
    gen_counter += 1
    group_res.append(sum(res))

    if min(res) == 4:
        mission_complete = 1
        print('В {} году всех студентов отчислили, поэтому '
              'в вузе никто не учился и его закрыли'.format(gen_counter+2022))
        print('Вот как распределяло наше поколение чудес 300 часов для подготовки к сессии:')
        for i in range(STUDENTS_AMOUNT):
            print('Студент {}: математика {}, физика {}, гуманитаризм {}, '
                  'физра {} и главное - раздолбайство {}'.format(i+1, group[i][0],
                        group[i][1], group[i][2], group[i][3], group[i][4]))
        break

    group = tournament(group, res, STUDENTS_AMOUNT)

    for role_model in range(0, STUDENTS_AMOUNT, 2):
        for role_model2 in range(1, STUDENTS_AMOUNT, 2):
            if rand.random() < P_CROSS:
                group[role_model], group[role_model2] = crossing(group[role_model], group[role_model2])

    for i in range(STUDENTS_AMOUNT):
        if rand.random() < P_MUTATION:
            group[i] = mutation(group[i])

gen_num = [i for i in range(gen_counter)]

plt.bar(gen_num, group_res)

plt.show()
