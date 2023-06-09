# 혜아의 머릿속에는 long int는 4바이트 정수, long long int는 8바이트 정수, long long long int는 12바이트까지 저장할 수 있는 정수 자료형이다.
# 혜아가 $N$바이트 정수까지 저장할 수 있다고 생각하는 정수 자료형의 이름을 출력하여라.

N = int(input())
long_num = N // 4
print(long_num * 'long ' + 'int')