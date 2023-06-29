# 캠핑장을 연속하는 P일 중, L일동안만 사용할 수 있다.
# 강산이는 이제 막 V일짜리 휴가를 시작했다. 강산이가 캠핑장을 최대 며칠동안 사용할 수 있을까?

i = 0
while True:
  L, P, V = map(int, input().split())
  i += 1
  if L == 0 and P == 0 and V == 0:
     break
  else:
    cycle = V // P      # 8일 중 5일만 사용하고 있다면, 8일 싸이클
    not_cycle = V % P   # 싸이클을 제외한 일수
    ans = cycle * L     # 8일 싸이클을 두번 돌 수 있기 때문에 2(=싸이클 수) * 5(=싸이클 중 사용가능 일)

    if not_cycle <= L:
        ans += not_cycle
    else:
        ans += L
    print(f'Case {i}: {ans}')