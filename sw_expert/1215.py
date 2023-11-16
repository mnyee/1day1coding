def a():
    global answer,N
    for n in range(8):
        for m in range(8):
            new_arr = arr[n][m:N + m]
            re_arr = list(reversed(new_arr))
            if new_arr == re_arr and len(new_arr) == N:
                answer += 1


def b():
    global answer,N
    arr_90 = list(map(list,zip(*arr)))
    for n in range(8):
        for m in range(8):
            new_arr = arr_90[n][m:N + m]
            re_arr = list(reversed(new_arr)) #그냥 new_arr.reverse()하면 None나옴
            if new_arr == re_arr and len(new_arr) == N:
                answer += 1

for i in range(10):
    answer = 0
    N = int(input())
    arr = []
    for _ in range(8): #'CBBCBAAB' -> ['C','B',...]으로 받기
        li = input()
        arr.append(list(li))
    a()
    b()

    print(f'#{i+1} {answer}')

