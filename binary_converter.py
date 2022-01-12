# File for binary conversion

def binary_to_base10(binary):
    """converts binary to a base 10 number"""
    new_number = 0
    str_binary = str(binary)
    count = len(str_binary) - 1
    for i in str_binary:
        if i == '0':
            pass
        elif i == '1':
            new_number += 2**count
        count -= 1
    return new_number

if __name__ =='__main__':
    print(binary_to_base10(10))
    print(binary_to_base10(100))
    print(binary_to_base10(1001))
    print(binary_to_base10(11000))
    print(binary_to_base10(110100))
    print(binary_to_base10(111000))
