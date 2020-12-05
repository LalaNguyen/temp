#!/usr/bin/python3
import socket
import numpy
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.15.18.69",5555))
cur_loc = 0
cnt = 0;
while True:
    raw_bytes=s.recv(1024)
    data = str(raw_bytes, encoding='latin-1')
    clean_data = data.splitlines()
    # The first time starts, len is 1
    if(len(clean_data)==1):
        print(data)
        continue
    print(data)
    lines=[]
    s_idx=0
    for i in range(0,len(raw_bytes)):
        if(raw_bytes[i] == 10): # \n byte is 10 in decimal
            lines.append(raw_bytes[s_idx:i])
            s_idx=i+1
        if(raw_bytes[i] ==94): # ^ is 94
            cur_loc = i-166
    # Print all lines here
    print("cnt: ",cnt)
    print(" 1:  ", lines[0])
    print(" 2:  ", lines[1])
    print(" 3:  ", lines[2])
    print(" 4:  ", lines[3])
    print(" 5:  ", lines[4])
    print(" 6:  ", lines[5])
    print(" 7:  ", lines[6])
    print(" 8:  ", lines[7])
    print(" 9:  ", lines[8])
    print(">10: ", lines[9])
    print(" 11: ", lines[10])
    print("cursor (%s) is at loc: x=%s"%(chr(lines[10][cur_loc]),cur_loc))
    zero_loc = 0
    for i in range(0,len(lines[3])):
        #print(lines[3][i])
        if(lines[9][i]==48):
            zero_loc = i
    #print("zero_loc is at loc: x=", zero_loc)
    if(zero_loc == cur_loc):
        print("zero is approaching, move right")
        s.send("XC".encode())
    if(cnt<10000):
        cnt+=1
    if(cnt==10000):
        break
