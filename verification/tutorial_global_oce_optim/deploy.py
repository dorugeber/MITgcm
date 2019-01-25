import os
import shutil
import subprocess

# aim: copy from clean/ to folders run_7 through run_52/, running prepare_run
# in each folder, and adjusting run_optim accordingly


for ii in range(7, 53):
    print(ii)
    folname = "run_" + str(ii) + "/"
    shutil.copytree("clean/", folname)

    os.chdir(folname)
    subprocess.call("./prepare_run", shell=True)

    lines = open("run_optim.py").read().splitlines()
    # change rpeprec to ii
    for lineno, line in enumerate(lines):
        if "rpeprec=53" in line:
           line = line.replace("rpeprec=53", "rpeprec=" + str(ii))
           lines[lineno] = line
    open("run_optim.py", "w").write('\n'.join(lines))

    os.chdir("..")
