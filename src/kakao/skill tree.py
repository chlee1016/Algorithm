def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_list = list(skill)

        # 한 문자씩 검사
        for s in skill_tree:
            # skill_tree의 문자들을 하나씩 꺼내어서,
            if s in skill and s != skill_list.pop(0):
                break

            # 이것과 무엇이 다른지 몰라서 어려웠던 문제
            # if s in skill and s != skill_list[0]:
            #     skill_list.pop(0)
            #     break

        # break문에 안걸리면 answer 증가
        else:
            answer += 1

    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

# print(solution(skill, skill_trees))
# solution(skill, skill_trees)
print(list(skill).pop(0))
print(list(skill)[0])