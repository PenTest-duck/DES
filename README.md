# DES Encryption/Decryption Tool

This tool "manually" performs each of the steps in the DES key generation process and encryption/decryption process.
This tool also supports both ECB and CBC.


# Key Generation
1. Permute using the PC-1 table to shrink the key size from 64 bits to 56 bits.
2. Split the key in half (left = c0, right = d0).
3. Left shift c0 and d0 according to the LS scheme, to obtain 32 half-keys; c1 to c16 and d1 to d16.
4. Permute cNdN using the PC-2 table to shrink the key size from 56 bits to 48 bits.
The resulting 16 subkeys (k1 to k16) will be used in each of the 16 rounds in the encryption/decryption process.


# Encryption process
1. Pad the last block (in this tool, with PKCS#5/#7) so the block size is 64 bits.
2. Concatenate all of the block output to form the final ciphertext.

For each block:
1. Perform initial permutation using the IP table.
2. Split the text in half (left = l0, right = r0).
3. Perform 16 rounds.
4. After 16 rounds, switch the order of l16 and r16, and concatenate them.
5. Inverse permute r16l16 using the IP-1 table.

In each round:
1. Permute rN using the E table, to expand the size from 32 bits to 48 bits.
2. XOR the round key kN with the expanded rN.
3. Substitute the XOR-ed rN using S-boxes S1 to S8 to shrink the size from 48 bits to 32 bits, by splitting rN    into 		8 groups of 6 bits, then taking the first and last bit as the row and the middle 4 bits as the column, then finding 	 the matching entry in Sg, where g is the group number. 
4. Permute the substituted rN using the P table.
5. XOR l(n-1) with the permuted rN.


# Decryption Process
The Decryption process is the exact same as the Encryption process, with some differences:
1. The round keys are applied in reverse order (i.e. from k16 to k1)
2. Padding is removed at the end of the Decryption process, to return the final plaintext.

# Counter Block Chaining (CBC)
CBC involves a 64-bit Initialisation Vector (IV), which is used in both the Encryption and Decryption processes.

Encryption:
1. The first block of plaintext is XORed with the IV.
2. DES-ECB encryption is applied to the block.
3. The resulting ciphertext of the block is used as the IV of the next block, and this process continues until all                          
   blocks have been encrypted.

Decryption (last block decrypted first):
1. DES-ECB decryption is applied to the block.
2. The resulting output is XORed with the previous block's ciphertext, to return the plaintext.
3. This process continues until all blocks have been decrypted, with the first block's output being XORed with the IV.
