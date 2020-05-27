def solution(total_sp, skills):
    sorted_skills = sorted(skills)
    top_skill = sorted(skills)[0][0]
    tree = {}

    key = top_skill
    value_list = []

    for i in range(len(skills)):
        if sorted_skills[i][0] == key:
            value_list.append(sorted_skills[i][1])
        tree[key] = value_list

    for value in tree[key]:
        key = value
        value_list = []
        for i in range(len(skills)):
            if sorted_skills[i][0] == key:
                value_list.append(sorted_skills[i][1])

        if len(value_list) == 0:
            continue
        else:
            tree[key] = value_list

    count = 0

    a = []
    for value in tree[top_skill]:
        if value not in tree:
            count += 1

        elif value in tree:
            count += len(tree[value])

    # 가장 마지막단 노드의 개수
    for values in tree.values():
        for value in values:
            if value not in tree:
                count += 1
                a.append(1)
            elif value in tree:
                count += len(tree[value])
                a.append(len(tree[value]))

    x = total_sp // count  # 문제의 해
    b = []
    b.append((a[0]+a[1])*x)
    for i in range(len(a)):
        b.append(a[i]*x)

    return b


total_sp = 121
# 길이 : 스킬 개수 n -1
skills = [[1,2], [1,3], [3,6], [3,4], [3,5]]
# -> {1: [2, 3], 3: [4, 5, 6]}


b = solution(total_sp, skills)
print(b)


