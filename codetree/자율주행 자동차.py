#1.현재 방향을 기준으로 왼쪽 방향으로 한 번도 간 적이 없다면 좌회전해서 해당 방향으로 1 칸 전진합니다.
#2.왼쪽 방향이 인도거나 이미 방문한 경우 또 좌회전하고 1번 과정 시도
#3.4방향 모두 확인했으나 전진하지 못한 경우 바라보는 방향 유지한채 한칸 후진 후 다시 1번과정 수행
#4.3번 과정 시도하려했으나 뒷 공간이 인도여서 후진조차 못한다면 작동 멈춤

n,m = map(int,input().split()) #도로의 세로,가로 크기

x,y,d = map(int,input().split()) #자동차의 초기위치, 바라보는 방향 d : 0~3,북동남서

road = [list(map(int,input().split())) for _ in range(n)] #도로의 상태

cnt = 0 #자동차 방문 총 면적

#d : 0~3,북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#자동차의 현재 위치에서 왼쪽 방향이 진행 가능할 경우 좌회전으로 방향 바꾼 후 전진
#만약 왼쪽 방향이 인도거나 방문한 도로인 경우 좌회전하고 전진
def car_move(x,y,d): #왼쪽 방향부터 돌기
    global cnt
    #현재 위치가 0인 경우
    if road[x][y] == 0:
        cnt +=1
        road[x][y] = -1
    #왼쪽 방향이 진행 가능한 경우
    if road[x][y-1] == 0:
        cnt += 1
        road[x][y-1] = -1
    else:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and road[nx][ny] == 0:
                road[nx][ny] = -1
                cnt += 1
                car_move(nx,ny,i)

    return False

if car_move(x,y,d):
    x += 1
    if 0 <= x < n and road[x][y] != 1:
        car_move(x, y, d)  # 전진하지 못한 경우 방향 유지한 채 한칸 후진 후 1번 과정 수행

    else:
        print(cnt)
# 5 5
# 1 1 0
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 1 0 1
# 1 0 0 0 1
# 1 1 1 1 1
