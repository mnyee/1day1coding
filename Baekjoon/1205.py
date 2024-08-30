import sys
input = sys.stdin.readline
N, new, P= map(int,input().split())
answer = 1

if N != 0:
    h = list(map(int,input().split()))
    h_min = h[N-1]
    #꽉찬 경우
    if N == P:
        for i in range(N):
            # 새로운 정수가 안에 최솟값보다 같거나 작으면 -1
            if new <= h_min:
                print(-1)
                break
            #새로운 점수가 안에 최솟값보다 크면 넣기
            else:
                if h[i] > new:
                    answer += 1
                else:
                    print(answer)
                    break
    #꽉차 있지않은 경우
    else:
        if h_min > new:
            print(N+1)
        else:
            for i in range(N):
                if h[i] > new:
                    answer += 1
                #순위가 다 동일한 경우
                #10 1 11
                #1 1 1 1 1 1 1 1 1 1
                elif h[i] == new:
                    print(answer)
                    break
                elif h[i] < new:
                    print(answer)
                    break
else:
    print(1)
