Implementation logic
====================
1. Initialize the hash to all zeros; 
2. Scan the file one byte at a time; 
3. Before a new byte is read from the file, circularly shift the bit pattern 
in the hash to the left by four positions; 
4. XOR the new byte read from the file with the least significant byte of the hash.

Files used for hashing
=====================
The files used for hashing are placed in input_files

Output files
============
The output file containing hashes is placed in output_files.

TODO
====
Proving the weakness of the algorithm through following steps:
       1. Take two random files and compute the hashes of the same.
       2. Use the hashes to determine the bytes to append in one of the files
        to make the hash same


