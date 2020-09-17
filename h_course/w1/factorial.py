def factorial(n):
    if n == 0:
        return 1
    else:
    	N = 1
        for i in range(1, n+1):
            N *= i
        return(N)
