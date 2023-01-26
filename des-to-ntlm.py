'''
USAGE

C:\> set DES_KEY_1=<秘密鍵1>
C:\> set DES_KEY_2=<秘密鍵2>
C:\> set NTLM_END=<NTLMハッシュの末尾2Bytes>
C:\> python des-to-ntlm.py
'''

import os

def f_des_split(des_key):
    des_key_part_1 = des_key[0:2]
    des_key_part_2 = des_key[2:4]
    des_key_part_3 = des_key[4:6]
    des_key_part_4 = des_key[6:8]
    des_key_part_5 = des_key[8:10]
    des_key_part_6 = des_key[10:12]
    des_key_part_7 = des_key[12:14]
    des_key_part_8 = des_key[14:16]
    return [des_key_part_1, des_key_part_2, des_key_part_3, des_key_part_4, des_key_part_5, des_key_part_6, des_key_part_7, des_key_part_8]

def f_des_to_ntlm(des_key_split):
    des_key_bin_1 = format(int(des_key_split[0], 16), '08b')[0:7]
    des_key_bin_2 = format(int(des_key_split[1], 16), '08b')[0:7]
    des_key_bin_3 = format(int(des_key_split[2], 16), '08b')[0:7]
    des_key_bin_4 = format(int(des_key_split[3], 16), '08b')[0:7]
    des_key_bin_5 = format(int(des_key_split[4], 16), '08b')[0:7]
    des_key_bin_6 = format(int(des_key_split[5], 16), '08b')[0:7]
    des_key_bin_7 = format(int(des_key_split[6], 16), '08b')[0:7]
    des_key_bin_8 = format(int(des_key_split[7], 16), '08b')[0:7]
    des_key_bin = des_key_bin_1 + des_key_bin_2 + des_key_bin_3 + des_key_bin_4 + des_key_bin_5 + des_key_bin_6 + des_key_bin_7 + des_key_bin_8
    ntlm = format(int(des_key_bin, 2), 'x')
    return ntlm

des_key_1 = os.environ.get('DES_KEY_1')
des_key_2 = os.environ.get('DES_KEY_2')
ntlm_end = os.environ.get('NTLM_END')

if not des_key_1 or not des_key_2 or not ntlm_end:
    print('[-]環境変数が見つかりません')
    exit(1)

if len(des_key_1) != 16 or len(des_key_2) != 16 or len(ntlm_end) != 4:
    print('[-]環境変数の長さに誤りがあります')
    exit(2)

des_key_split_1 = f_des_split(des_key_1)
des_key_split_2 = f_des_split(des_key_2)
ntlm_1 = f_des_to_ntlm(des_key_split_1)
ntlm_2 = f_des_to_ntlm(des_key_split_2)
ntlm_result = ntlm_1 + ntlm_2 + ntlm_end
print("[+]NTLM = " + ntlm_result)
