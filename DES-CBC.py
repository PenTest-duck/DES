#DES-CBC

print("Data Encryption Standard - DES")

pc1_table = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
ls_scheme = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
pc2_table = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
ip_table = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
e_table = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
p_table = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
ip_inv_table = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

s_boxes = [[[14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9, 0,  7],
            [ 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5, 3,  8],
            [ 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10, 5,  0],
            [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0, 6, 13]],

           [[15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12, 0,  5, 10],
            [ 3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6, 9, 11,  5],
            [ 0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9, 3,  2, 15],
            [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0, 5, 14,  9]],

           [[10,  0,  9, 14, 6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8],
            [13,  7,  0,  9, 3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1],
            [13,  6,  4,  9, 8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7],
            [ 1, 10, 13,  0, 6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]],

           [[ 7, 13, 14, 3,  0,  6,  9, 10,  1, 2, 8,  5, 11, 12,  4, 15],
            [13,  8, 11, 5,  6, 15,  0,  3,  4, 7, 2, 12,  1, 10, 14,  9],
            [10,  6,  9, 0, 12, 11,  7, 13, 15, 1, 3, 14,  5,  2,  8,  4],
            [ 3, 15,  0, 6, 10,  1, 13,  8,  9, 4, 5, 11, 12,  7,  2, 14]],

           [[ 2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13, 0, 14,  9],
            [14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3, 9,  8,  6],
            [ 4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6, 3,  0, 14],
            [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10, 4,  5,  3]],

           [[12,  1, 10, 15, 9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11],
            [10, 15,  4,  2, 7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8],
            [ 9, 14, 15,  5, 2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6],
            [ 4,  3,  2, 12, 9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]],

           [[ 4, 11,  2, 14, 15, 0,  8, 13,  3, 12, 9,  7,  5, 10, 6,  1],
            [13,  0, 11,  7,  4, 9,  1, 10, 14,  3, 5, 12,  2, 15, 8,  6],
            [ 1,  4, 11, 13, 12, 3,  7, 14, 10, 15, 6,  8,  0,  5, 9,  2],
            [ 6, 11, 13,  8,  1, 4, 10,  7,  9,  5, 0, 15, 14,  2, 3, 12]],

           [[13,  2,  8, 4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7],
            [ 1, 15, 13, 8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2],
            [ 7, 11,  4, 1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8],
            [ 2,  1, 14, 7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]]]

def ascii2bin(string):
    binary = ''
    for char in string:
        bin_char = bin(ord(char))[2:]
        while len(bin_char) < 8:
            bin_char = "0" + bin_char
        binary += bin_char
            
    out = []
    for bit in binary:
        out.append(bit)
    return out

def bin2ascii(binary):
    out = ""
    for i in range(int(len(binary) / 8)):
        byte = binary[i * 8:i * 8 + 8]
        out += chr(int(bin2dec(byte)))
    return out

def list2string(input_list):
    out = ""
    for i in input_list:
        out += i
    return out

def string2list(string):
    out = []
    for char in string:
        out.append(char)
    return out

def hex2bin(hexa):
    out = ""
    for digit in hexa:
        out += bin(int(digit, 16))[2:].zfill(4)
    return string2list(out)

def bin2hex(binary):
    out = ""
    for nibble in range(int(len(binary) / 4)):
        out += hex(int(binary[nibble * 4: nibble * 4 + 4], 2))[2:]
    return out 

def bin2dec(binary):
    return str(int(binary, 2))

def dec2bin(dec):
    return bin(dec)[2:].zfill(4)

def XOR(arg1, arg2):
    out = []
    for pos in range(len(arg1)):
        if arg1[pos] == arg2[pos]:
            out.append('0')
        else:
            out.append('1')
    return out

def permute(inp, table):
    output = []
    for pos in table:
        output.append(inp[pos - 1])
    return output

def substitute(inp, s_box):
    out = []
    for i in range(8):
        row = bin2dec(inp[i][0] + inp[i][5])
        col = bin2dec(list2string(inp[i][1:5]))
        cell = s_box[i][int(row)][int(col)]
        out += string2list(dec2bin(cell))
    return out

def left_shift(inp, num):
    for i in range(num):
        inp.append(inp.pop(0))
    return inp

def pkcs5_pad(inp):
    last_block = inp[len(inp) // 64 * 64:]
    pad_length = int((64 - len(last_block)) / 8)
    pad_bits = ""
    for i in range(pad_length):
        pad_bits += "0000" + dec2bin(pad_length)
    last_block += string2list(pad_bits)
    out = inp[0:len(inp) // 64 * 64] + last_block
    return out

def pkcs5_unpad(inp):
    last_byte = int(bin2dec(list2string(inp[len(inp) - 7:])))
    if 1 <= last_byte <= 7:
        out = inp[:-8 * last_byte]
        return out
    elif last_byte == 8:
        return ""
    else:
        return inp

def blockify(inp, block_length):
    out = []
    for i in range(len(inp) // block_length + 1):
        if len(inp) % block_length == 0 and i == len(inp) // block_length:
            break
        out.append(inp[i * block_length: i * block_length + block_length])
    return out

def subkey_gen(c0, d0):
    global subkeys
    c = []
    d = []
    prev_c = c0
    prev_d = d0
    
    #1. Left shift c0 and d0 according to the LS Scheme to obtain c1 to c16 and d1 to d16
    for i in range(16):
        shifted = left_shift(prev_c, ls_scheme[i])
        c.append(shifted[:]) 
        
    for i in range(16):
        shifted = left_shift(prev_d, ls_scheme[i])
        d.append(shifted[:])

    #2. Permute cNdN using PC-2 Table to obtain 16 subkeys:
    #14    17   11    24     1    5
    # 3    28   15     6    21   10
    #23    19   12     4    26    8
    #16     7   27    20    13    2
    #41    52   31    37    47   55
    #30    40   51    45    33   48
    #44    49   39    56    34   53
    #46    42   50    36    29   32
    subkeys = []
    for i in range(1, 17):
        cd = c[i-1] + d[i-1]
        subkeys.append(permute(cd, pc2_table))

def keygen(key):
    #1. Permute using PC-1 Table:
    #57   49    41   33    25    17    9
    #1    58    50   42    34    26   18
    #10    2    59   51    43    35   27
    #19   11     3   60    52    44   36
    #63   55    47   39    31    23   15
    #7    62    54   46    38    30   22
    #14    6    61   53    45    37   29
    #21   13     5   28    20    12    4 
    pc1_key = permute(key, pc1_table)

    #2. Split key in half
    c0 = pc1_key[0:28]
    d0 = pc1_key[28:56]

    #3. Generate 16 subkeys
    subkey_gen(c0, d0)

def DES_Round(l, r, n):
    #1. Expansion using E Table:
    #32     1    2     3     4    5
    # 4     5    6     7     8    9
    # 8     9   10    11    12   13
    #12    13   14    15    16   17
    #16    17   18    19    20   21
    #20    21   22    23    24   25
    #24    25   26    27    28   29
    #28    29   30    31    32    1
    expanded_r = permute(r, e_table)
    
    #2. XOR round key with expanded right half-block
    xor_r = XOR(subkeys[n], expanded_r)

    #3. Substitute XORed right half-block with S-boxes S1 to S8
    pre_sub = []
    for i in range(8):
        pre_sub.append(xor_r[i * 6: i * 6 + 6])
    sub_r = substitute(pre_sub, s_boxes)

    #4. Permute substituted right half-block using P Table:
    #16   7  20  21
    #29  12  28  17
    # 1  15  23  26
    # 5  18  31  10
    # 2   8  24  14
    #32  27   3   9
    #19  13  30   6
    #22  11   4  25
    permuted_r = permute(sub_r, p_table)

    #5. XOR L(n-1) with permuted right half-block
    ln = r
    rn = XOR(l, permuted_r)
    prev_lr["prev_l"] = ln
    prev_lr["prev_r"] = rn
    round_out = ln + rn

    return round_out

def DES_Block(text):
    #1. Initial permutation using IP Table:
    #58    50   42    34    26   18    10    2
    #60    52   44    36    28   20    12    4
    #62    54   46    38    30   22    14    6
    #64    56   48    40    32   24    16    8
    #57    49   41    33    25   17     9    1
    #59    51   43    35    27   19    11    3
    #61    53   45    37    29   21    13    5
    #63    55   47    39    31   23    15    7
    permuted_text = permute(text, ip_table)

    #2. Split text in half
    l0 = permuted_text[0:32]
    r0 = permuted_text[32:64]

    #3. Perform 16 rounds
    global prev_lr
    prev_lr = {"prev_l" : l0, "prev_r" : r0}
    if method == "e":
        for n in range(16):
            final_block = DES_Round(prev_lr["prev_l"], prev_lr["prev_r"], n)
    elif method == "d":
        for n in range(15, -1, -1):
            final_block = DES_Round(prev_lr["prev_l"], prev_lr["prev_r"], n)

    #4. Switch the left and right half-blocks
    final_block = final_block[32:64] + final_block[0:32]

    #5. Inverse permute using IP-1 Table:
    #40     8   48    16    56   24    64   32
    #39     7   47    15    55   23    63   31
    #38     6   46    14    54   22    62   30
    #37     5   45    13    53   21    61   29
    #36     4   44    12    52   20    60   28
    #35     3   43    11    51   19    59   27
    #34     2   42    10    50   18    58   26
    #33     1   41     9    49   17    57   25
    block_out = permute(final_block, ip_inv_table)
    return block_out

def DES_ECB_encrypt(plaintext):
    bin_encrypted = ""
    for block in plaintext:
        if block == plaintext[-1]:
            bin_encrypted += list2string(DES_Block(pkcs5_pad(ascii2bin(block))))
        else:
            bin_encrypted += list2string(DES_Block(ascii2bin(block)))
    hex_encrypted = bin2hex(bin_encrypted)
    print("\n\nBinary: " + bin_encrypted)
    print("Hex: " + hex_encrypted)

def DES_ECB_decrypt(ciphertext):
    decrypted = ""
    for block in ciphertext:
        if block == ciphertext[-1]:
            decrypted += list2string(pkcs5_unpad(DES_Block(hex2bin(block))))
        else:
            decrypted += list2string(DES_Block(hex2bin(block)))
    print("Plaintext: " + bin2ascii(decrypted))

def DES_CBC_encrypt(plaintext, iv):
    bin_encrypted = ""
    next_iv = iv
    for block in plaintext:
        if block == plaintext[-1]:
            padded_xor_block = XOR(pkcs5_pad(ascii2bin(block)), next_iv)
            bin_encrypted += list2string(DES_Block(padded_xor_block))
        else:
            xor_block = XOR(ascii2bin(block), next_iv)
            block_out = DES_Block(xor_block)
            bin_encrypted += list2string(block_out)
            next_iv = block_out
    hex_encrypted = bin2hex(bin_encrypted)
    print("\n\nBinary: " + bin_encrypted)
    print("Hex: " + hex_encrypted)

def DES_CBC_decrypt(ciphertext, iv):
    decrypted = ""
    for block in range(len(ciphertext) - 1, -1, -1):
        block_out = DES_Block(hex2bin(ciphertext[block]))
        if block == 0:
            xor_block = XOR(block_out, iv)
            decrypted = list2string(pkcs5_unpad(xor_block)) + decrypted
        else:
            next_iv = hex2bin(ciphertext[block - 1])
            xor_block = XOR(block_out, next_iv)
            decrypted = list2string(xor_block) + decrypted
    print("Plaintext: " + bin2ascii(decrypted))

def DES_ECB():
    if method == "e":
        plaintext = blockify(input("Plaintext (PKCS#5/#7 padding will be applied): "), 8)
        DES_ECB_encrypt(plaintext)
       
    elif method == "d":
        ciphertext = blockify(input("Ciphertext (in hex): "), 16)
        DES_ECB_decrypt(ciphertext)

def DES_CBC():
    if method == "e":
        iv = string2list(input("64-bit IV (in binary; optionally leave blank for randomisation): "))
        if iv == []:
            from random import randint
            for i in range(64):
                iv.append(str(randint(0, 1)))
            print("IV: " + list2string(iv))
    elif method == "d":
        iv = input("64-bit IV (in binary): ")
            
    if method == "e":
        plaintext = blockify(input("Plaintext (PKCS#5/#7 padding will be applied): "), 8)
        DES_CBC_encrypt(plaintext, iv)

    elif method == "d":
        ciphertext = blockify(input("Ciphertext (in hex): "), 16)
        DES_CBC_decrypt(ciphertext, iv)
    
def main():
    global method
    mode = input("(e) ECB or (c) CBC: ")
    method = input("(e)ncrypt or (d)ecrypt: ")
    key = input("64-bit Key: ")
    keygen(ascii2bin(key))

    if mode == "e":
        DES_ECB()
    elif mode == "c":
        DES_CBC()

if __name__ == "__main__":
    main()
