'''
Created on Mar 10, 2018
32 bit hash implmentation using xor and circular left shift.
'''
import glob, os

class FileHasher:

    CONSTANT_NUM_OF_SHIFTS = 4
    CONSTANT_HASH_KEY_LEN = 32
      
    def __init__(self, srcfile):
        self.srcfile = srcfile
        self.hash_seed = 0
#         self.databytes = bytearray(srcfile.read(),'ascii')
#         

    def hash(self):
#         print('Hashing..')
        hash_curr =  self.hash_seed

        while True: #Is this condition correct?

            #Circular shift hash
#             print('Current hash: %08x' % hash_curr)
            hash_curr_rs = (hash_curr >> self.CONSTANT_NUM_OF_SHIFTS)
            hash_curr_ls = ((hash_curr & 0x0000000F) << (self.CONSTANT_HASH_KEY_LEN \
              - self.CONSTANT_NUM_OF_SHIFTS))
            hash_curr = hash_curr_ls|hash_curr_rs
#             print('Shifted hash: %08x' % hash_curr)

            #Read byte
            msg_byte = self.srcfile.read(1)
            if not msg_byte:
                break
            
            msg_dec = ord(msg_byte)
#             print("Msg byte: %02x" %msg_dec)

            #Message exor hash
            hash_curr = hash_curr ^ msg_dec
            
        return hash_curr

out_file_hdl = open("./output_files/hash.txt", 'w')
for input_file in os.listdir("./input_files"):
    
    #Hash of input file
    file_abs_path="./input_files/" + input_file
    file_hdl = open(file_abs_path,'rb')
    file_hasher = FileHasher(file_hdl)
#     file_hdl.seek(-1, os.SEEK_END)
#     file_hdl.truncate()
    hashval = file_hasher.hash()

    #Write hsh to output file
    print("File:%s hash:%08x" %(input_file, hashval))
    out_file_hdl.write("File:%s hash:%08x\n" %(input_file, hashval))
    file_hdl.close()

#Close output file
out_file_hdl.close()
