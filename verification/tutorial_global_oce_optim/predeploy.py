import os
import shutil

# aim: put a clean set of files in clean/, assuming that mitgcmuv_ad and
# optim.x have been built already
#
# similar to what is described in the README, but we hard-copy the files
# symlinked by prepare_run into clean_data/, and adjust prepare_run accordingly

shutil.copytree("input_oad/", "clean/")
shutil.copy2("build/mitgcmuv_ad", "clean/")
shutil.copy2("../../../optim_m1qn3/src/optim.x", "clean/")
shutil.copy2("./run_optim.py", "clean/")

lines = open("clean/prepare_run").read().splitlines()
lines[4] = 'fromDir="../clean_data"'  # change line 5, python numbering
open("clean/prepare_run", "w").write('\n'.join(lines))

os.mkdir("clean_data")

for fil in os.listdir("../tutorial_global_oce_latlon/input"):
    if fil.endswith(".bin"):
        shutil.copy2("../tutorial_global_oce_latlon/input/" + fil, "clean_data/")
