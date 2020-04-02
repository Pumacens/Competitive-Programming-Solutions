def cyclops (n):
    n_bin = bin(n)[2:]
    n_len = len(n_bin)
    return n_bin.count('0') == 1 and n_bin[n_len//2] == '0' and n_len%2



# def cyclops(n):
#     n = bin(n)[2:]
#     return n.count("0") == 1 and n == n[::-1]

