
def add_binary_string(binary_string_a, binary_string_b):
    answer = int(binary_string_a, 2) + int(binary_string_b, base=2) # 換成十進位
    answer = bin(answer)[2:]  # 0bxxxx -> xxxx 
    return answer

if __name__ == '__main__':
    a = '1011'
    b = '1101'
    answer = add_binary_string(a, b)
    print(answer)