from collections import deque
prices=[1,2,3,2,3]

def solution(prices):
    answer=[]
    que_prices = deque(prices)

    while que_prices:
        index = que_prices.popleft()
        count = 0
        for n in que_prices:
            count +=1
            if index > n:
                break;
        answer.append(count)
    return answer

print(solution(prices))

