from itertools import permutations


def isMatchId(ban_id, user_id):
    # 여기서 banned_id와 candidate_users는 id 한 개를 의미
    # 문자열 길이 만큼 반복

    for i in range(len(ban_id)):
        if ban_id[i] == '*': continue
        elif ban_id[i] != user_id[i]:
            return False

    # 이 리턴을 엄한데 indent 해놓아서 풀이에 오래 걸렸다.
    return True


def check(banned_ids, candidate_users):
    for i in range(len(banned_ids)):
        # candidate_users와 문자 길이가 다르면 False 리턴
        if len(banned_ids[i]) != len(candidate_users[i]):
            return False
        # 이제 각 문자 일치 여부 비교
        if isMatchId(banned_ids[i], candidate_users[i]) is False:
            return False
    return True


def solution(user_ids, banned_ids):
    # banned_id에서 하나씩 꺼내 온다.
    # user_id에서 해당하는 id를 매칭한다. 매칭되는 총 list를 구한다.
    # 그 리스트들로 banned_id와 매칭한다.
    ans = []

    for candidate_users in permutations(user_ids, len(banned_ids)):
        if check(banned_ids, candidate_users) is True:
            candidate_users = set(candidate_users)
            if candidate_users not in ans:
                ans.append(candidate_users)

    return len(ans)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "abc1**"]
banned_id = ["*rodo", "*rodo", "******"]
print(solution(user_id, banned_id))
