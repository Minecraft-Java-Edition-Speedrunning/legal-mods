import csv
import hashlib
import json
import os
import subprocess
import typing

with open("legal-builds.csv", "r") as f:
    reader = csv.reader(f)
    fields = next(reader)
    curr = list(reader)


def hash_entry(modid, hash) -> typing.Optional[list[str]]:
    for l in curr:
        if l[0] == modid and l[4] == hash:
            return l
    return None


for path, _, file in os.walk("legal-mods"):
    if len(file) == 0:
        continue
    assert len(file) == 1 and path.count(os.path.sep) == 2
    file = file[0]
    if file.endswith(".json"):
        with open(os.path.join(path, file), "r") as f:
            data = json.load(f)
        file = data["link"][data["link"].rfind("/") + 1:]
        hash = data["hash"]
    else:
        with open(os.path.join(path, file), "rb") as f:
            hash = hashlib.sha512(f.read()).hexdigest()

    modid = path[path.index(os.path.sep) + 1: path.rindex(os.path.sep)]
    curr_entry = hash_entry(modid, hash)
    if curr_entry is not None:
        if curr_entry[1] != file:
            print(f"changing filename from {curr_entry[0]} to {file}")
            curr_entry[1] = file
        else:
            # print(f"keeping {file}")
            pass
    else:
        print(f"adding {file}")
        time = subprocess.check_output(["git", "log", "--max-count=1", "--format=%cd", "--date=unix"]).decode().strip()
        date = subprocess.check_output(["git", "log", "--max-count=1", "--format=%cd", "--date=format:%Y-%m-%d"]).decode().strip()
        curr.append([modid, file, time, date, hash])

with open("legal-builds.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerows(curr)
