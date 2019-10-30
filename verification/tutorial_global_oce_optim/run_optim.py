import os
import shutil
import random
import time

mypid = os.getpid()
childdir = "/dev/shm/mitgcm-" + str(mypid) + "/"
print("OAD checkpoints being saved in", childdir)
os.mkdir(childdir)

randdelay = random.randrange(10, 120)
print("Sleeping for", randdelay, "seconds...")
time.sleep(randdelay)

for ii in range(15):
    lines = open("data.optim").read().splitlines()
    lines[5] = " optimcycle=" + str(ii) + ","
    lines[8] = "#dfminFrac=0.4,"
    open("data.optim", "w").write('\n'.join(lines))
    os.system("oadcachedir=" + childdir + " rpeprec=53 ./mitgcmuv_ad > aaatemp.txt")
    os.rename("aaatemp.txt", "aaa" + str(ii) + ".txt")

    lines = open("data.optim").read().splitlines()
    lines[8] = " dfminFrac=0.4,"
    open("data.optim", "w").write('\n'.join(lines))
    os.system("./optim.x > aabtemp.txt")
    os.rename("aabtemp.txt", "aab" + str(ii) + ".txt")

print("Deleting checkpoint directory", childdir)
shutil.rmtree(childdir)