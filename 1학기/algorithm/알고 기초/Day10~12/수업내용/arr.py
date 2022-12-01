def powerset(idx):

    check[idx] = 0
    powerset(idx+1)

    check[idx] = 1
    powerset(idx+1)