import sys
import re
from handler import handle
import helper

# compile regex to match imports
imports = re.compile(r"(\w+)(?: ?[,и]\W|$)", re.M | re.U)

# create global state dictionary
global_state = helper.GlobalData()

# try to get filename from command line argument
try:
    filename = sys.argv[1]
# if no argument given, print message and exit
except IndexError:
    print("Oni-chan! You don't have a penis!")
    exit(1)

# open file and read lines into list
with open(filename, "r", encoding="utf-8") as f:
    commands = f.read().splitlines()

# loop through lines
for line in commands:
    # search for matches to imports regex
    if line.lower().startswith("undress"):
        # save index of matched line
        pointer = commands.index(line)
        # update global dict with matches
        global_state.modules = re.findall(imports, line.lower())
        # break out of loop if match found
        break
# if no match after full loop, print message and exit
else:
    print("Oni-chan! I'm still dressed!")
    exit(1)


while True:
    pointer += 1
    try:
        global_state = handle(global_state, *commands[pointer].split())
        if global_state.is_done:
            break
    except IndexError:
        print("Oni-chan! You didn't cum!")
        exit(1)
    except Exception as e:
        print("\n".join(e.args))
        exit(1)

if global_state.output_end:
    print("I'm cuming! I'm cuming!")
