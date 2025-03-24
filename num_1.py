
def is_palendrome(str_num):
    return str_num == str_num[::-1]

def largest_palendrome():
    largest = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            product = i * j
            if product < largest:
                break
            if is_palendrome(str(product)) and product > largest:
                largest = product
    return largest  

result = largest_palendrome()
print('The largest 3 digit product palendrome is:', result)

