import sys
input = sys.stdin.readline
N = int(input()) #스위치 갯수
S = list(map(int,input().split())) #스위치 상태
M = int(input()) #학생 수
for _ in range(M):
    a,b = map(int,input().split())
    if a == 1:#남자
        for i in range(N):
            if (i+1)%b == 0:
                S[i] = 1 if S[i] == 0 else 0
    else: #여자 처음과 마지막은?
        cnt = 0
        B = b-1 #실제 번호 3-1 = 2
        j = 1
        while True:
            # 양쪽이 같은 경우
            if B-j >= 0 and B+j < N and S[B-j] == S[B+j] :
                cnt += 1
                j += 1
                continue
            #양쪽이 다른 경우
            else:
                j -= 1
                if j > 0:
                    S[B] = 1 if S[B] == 0 else 0
                    for k in range(1,j+1):
                        S[B-k] = 1 if S[B-k] == 0 else 0
                        S[B+k] = 1 if S[B+k] == 0 else 0
                #시작부터 양쪽이 다른 경우는 기준점만 변경
                else:
                    S[B] = 1 if S[B] == 0 else 0
                break

#20개씩 출력
for i in range(0,N,20):
    print(*S[i:i+20]) #리스트에서 대괄호 제외하고 출력하고 싶으면 * 사용
