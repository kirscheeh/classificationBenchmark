with open('help', 'r') as f:
    lines=f.readlines()
    seq=""
    for line in lines:
        seq+=line
new_seq=seq.replace(" ", "")
seq=new_seq.replace("\n", "")
print(len(seq))
print(seq[866:1367] ,len(seq[866:1367]))