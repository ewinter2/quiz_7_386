def sequence_length(n, memo):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n % 2 == 0:
        length = 1 + sequence_length(n // 2, memo)
    else:
        length = 1 + sequence_length(3 * n + 1, memo)
    memo[n] = length
    return memo[n]

def longest_sequence(limit):
    memo = {}
    max_length = 0
    starting_num = 0
    for i in range(1, limit):
        length = sequence_length(i, memo)
        if length > max_length:
            max_length = length
            starting_num = i
    return starting_num, max_length

def collatz(n, d):
    og = n 
    if d.get(n, False):
        return n, d[n]
    c = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if d.get(n, False):
            d[og] = d[n] + c
            return n, d[og] + c
        c += 1
    return n, c


limit = 1000000
dict = {}
result, length = collatz(limit, dict)
print('The starting number under', limit, 'that produces the longest sequence is:', result)
print('The length of the sequence is:', length)

