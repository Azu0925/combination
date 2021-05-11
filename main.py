import itertools

def initial(check_list):
    for i in range(0, 50):
        check_list.append(False)
    return check_list

def visit(planet_number, check_list, relation_list):
    for i_index, i_item in enumerate(relation_list):
        if planet_number == int(relation_list[i_index][0]):
            check_list[int(relation_list[i_index][0])] = True
            check_list[int(relation_list[i_index][1])] = True
        if planet_number == int(relation_list[i_index][1]):
            check_list[int(relation_list[i_index][0])] = True
            check_list[int(relation_list[i_index][1])] = True

    return check_list

def combination():
    return list(itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], 3))

def counter(check_list):
    count = 0
    for i in check_list:
        if i == True:
            count += 1
    return count

def main():
    f = open('param.txt')
    relation_list = []
    line = f.readline()
    relation_list.append(line.split())
    
    while line:
        line = f.readline()
        if line == '':
            break
        relation_list.append(line.split())
    f.close()

    pattern = combination()
    max_planet_list = {
        'number': [],
        'langs': 0
    }
    for i in pattern:
        check_list = initial(check_list = [])
        check_list = visit(i[0], check_list, relation_list)
        check_list = visit(i[1], check_list, relation_list)
        check_list = visit(i[2], check_list, relation_list)
        if max_planet_list['langs'] < counter(check_list):
            max_planet_list = {
                'number': [i[0], i[1], i[2]],
                'langs': counter(check_list)
            }
        if counter(check_list) > 35:
            print('訪問惑星番号：' + str(i[0]) + ', ' + str(i[1]) + ', ' + str(i[2]) + '\n')
            print('合計会得言語数：' + str(counter(check_list)))
            print('----------------------------------------------------------------------------------------------------------')
    print('\n')
    print('============================================================================')
    print(max_planet_list)
    print('総パターン数：' + str(len(combination())))

main()
