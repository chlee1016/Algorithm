def solution(s):
    # s = list(s[1:-1])
    # s = ''.join(s)
    # s = s.split(',')
    # arr_list = []
    # for i in range(len(s)):
    #     arr = []
    #     if '{' in s[i] and '}' in s[i]:
    #         temp = s[i]
    #         arr.append(int(temp[1:-1]))
    #         arr_list.append(arr)
    #
    #     elif '{' in s[i]:
    #         temp = s[i]
    #         arr.append(int(temp[1:]))
    #         for j in range(1,len(s)+1):
    #             if '}' in s[i+j]:
    #                 temp = s[i+j]
    #                 arr.append(int(temp[:-1]))
    #                 arr_list.append(arr)
    #                 break
    #             else:
    #                 arr.append(int(s[i+j]))
    # 입력 : "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    # 출력 : [[2],[2,1],[2,1,3],[2,1,3,4]]

    s = s[2:-2].split("},{")
    arr_list = []
    for i in s:
        arr = i.split(',')
        arr_list.append(list(map(int, arr)))
    # 입력 : "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    # 출력 : [[2],[2,1],[2,1,3],[2,1,3,4]]

    # 길이 순서대로 정렬
    arr_list.sort(key=lambda x: len(x))
    answer = []
    answer.append(arr_list[0][0])
    for arr in arr_list:
        for ele in arr:
            if ele in answer:
                continue
            else:
                answer.append(ele)

    return answer


# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s = "{{20,111},{111}}"
answer = solution(s)
# print(answer)

