import hashlib
import json

import os
import typing

with open("legal-builds.txt", "w+") as f:
    curr = [l.strip().split("\t") for l in f.readlines()]


def hash_entry(hash) -> typing.Optional[list[str]]:
    for l in curr:
        if l[1] == hash:
            return l
    return None


for path, folder, file in os.walk("legal-mods"):
    if len(file) == 0: continue
    assert len(file) == 1
    file = file[0]
    if file.endswith(".json"):
        with open(os.path.join(path, file), "r") as f:
            data = json.load(f)
        file = data["link"][data["link"].rfind("/") + 1:]
        hash = data["hash"]
    else:
        with open(os.path.join(path, file), "rb") as f:
            hash = hashlib.sha512(f.read()).hexdigest()
    curr_entry = hash_entry(hash)
    if curr_entry is not None and curr_entry[0] != file:
        print(f"changing filename from {curr_entry[0]} to {file}")
        curr_entry[0] = file
    else:
        curr.append([file, hash])

with open("legal-builds.txt", "w") as f:
    f.writelines(f"{file}\t{hash}\n" for file, hash in curr)
