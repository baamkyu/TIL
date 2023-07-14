# 현재의 날짜, 캠프의 종료일이 주어지고 현재 기준으로 종료까지 며칠 남았는지 출력하라.

today = list(map(int, input().split()))
end = list(map(int, input().split()))

dday = 0
if end[0] - today[0] > 1000 or (end[0] - today[0] == 1000 and ((end[1] == today[1] and end[2] >= today[2]) or end[1] > today[1])):
    print('gg')
else:
  for y in range(today[0], end[0]):
      pass