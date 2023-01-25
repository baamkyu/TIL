def solution(price, money, count):
    use_money = 0
    for i in range(1, count+1):
        use_money += i*price
    if use_money <= money:
        return 0
    elif use_money > money:
        return use_money - money