import os

for ii in range(10):
    os.system("rpeprec=53 ./mitgcmuv_ad > aaatemp.txt")
    os.rename("aaatemp.txt", "aaa" + str(ii) + ".txt")
    os.system("./optim.x > aabtemp.txt")
    os.rename("aabtemp.txt", "aab" + str(ii) + ".txt")

    lines = open("data.optim").read().splitlines()
    lines[5] = " optimcycle=" + str(ii+1) + ","
    open("data.optim", "w").write('\n'.join(lines))
