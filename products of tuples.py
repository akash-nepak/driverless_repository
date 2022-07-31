def mul_list(series):
    mu1 = 1
    for element in series:
        mu1 = mu1 * element
    return mu1

    nums= [1, 2, 3 ,4 ,5 ,6]
    print(mul_list(nums))