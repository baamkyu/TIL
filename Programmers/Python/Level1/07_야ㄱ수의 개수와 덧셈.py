def solution(left, right):
    answer = 0
    n = 0 # 약수의 개수
    # 왼쪽 ~ 오른쪽 수
    for now in range(left, right+1):
      # 약수의 개수 count -> n
      for i in range(1, now+1):
        if now % i == 0:
          n += 1

      # 약수의 개수가 홀수일 때    
      if n % 2 == 1:
          answer -= now
          n = 0

      # 약수의 개수가 짝수일 때
      elif n % 2 == 0:
        answer += now
        n = 0
    return answer