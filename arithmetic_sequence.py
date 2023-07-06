# for-loop
# a_0 = a_0 + 0*d
# a_1 = a_0 + 1*d
# a_n = a_0 + n*d

def arithmetic_sequence(a_0=1, d=1, N=10):
    arith_seq = [a_0 + index * d for index in range(N + 1)]
    return arith_seq

if __name__ == '__main__':
    sequence = arithmetic_sequence(a_0=1, d=5, N=100)
    print(sequence)
