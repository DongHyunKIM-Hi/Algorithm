n = int(input())


def check_able(now_col, current_result):
    now_row = len(current_result)
    for index in range(now_row):
        if current_result[index] == now_col or abs(current_result[index] - now_col) == now_row - index:
            return False
        
    return True

def DFS(n,current_result,now_row, final_location):
    if n == now_row:
        final_location.append(current_result[:])
        return 

    for now_col in range(n):
        if check_able(now_col, current_result):
            current_result.append(now_col)
            DFS(n,current_result,now_row+1,final_location)
            current_result.pop()





def solve_location(n):
    final_location = []
    DFS(n,[],0, final_location)
    return final_location

print(len(solve_location(n)))