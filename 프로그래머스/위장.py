test = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]


def solution(clothes):
    
    diction = {}
    for cloth in clothes:
        if cloth[1] in diction:
            diction[cloth[1]] +=1
        else:
            diction[cloth[1]] = 1

    answer = 1
    for index in diction.values():
        answer = answer*(index+1)
    return answer -1

print(solution(test))

