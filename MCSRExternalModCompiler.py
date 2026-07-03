"""
MCSR External Mod Compiler script made by DuncanRuns
This script takes data from a modrinth project to create link files for legal-mods

License Below

MIT License

Copyright (c) 2022 MCSR Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import json
import os
import re
import shutil
from modrinth import Projects as ModrinthProjects
from modrinth import Versions as ModrinthVersions
from datetime import datetime, timezone

MC_VERSION_PATTERN = r"[mM][cC] ?1\.\d\d?(?:\.\d\d?)?"
GENERAL_VERSION_PATTERN = r"\d+\.\d+(?:\.\d+(?:\.\d+)?)?"


def version_to_int(version_string: str) -> int:
    all_numbers = [int(i) for i in re.findall(r"\d+", version_string)]
    while len(all_numbers) < 4:
        all_numbers.append(0)
    total = 0
    for i in range(4):
        total *= 10000
        total += all_numbers[i]
    return total

def iso_to_int(iso_str: str) -> int:
    return int(datetime.fromisoformat(iso_str.replace("Z","+00:00")).timestamp())

def compile_folder_for_modrinth_mod(project_name: str, modid: str = None, release_only: bool = False):
    if modid is None:
        modid = project_name

    print(f"Compiling for {project_name}")
    project = ModrinthProjects.ModrinthProject(project_name)

    all_files_per_mc_version = {}

    # https://discord.com/channels/734077874708938864/734077874708938867/1319083641955029084
    print("Getting versions...")
    versions: list[ModrinthVersions.ModrinthVersion] = []
    for project_id in project.versions:
        try:
            versions.append(ModrinthVersions.ModrinthVersion(project, project_id))
        except json.JSONDecodeError:
            pass

    print("Checking versions...")
    for v in versions:
        if "fabric" not in v.loaders or (release_only and v.versionType != "release"):
            continue

        url = v.files[0]["url"]
        hash = v.files[0]["hashes"]["sha512"]
        vdata = {
            "link": url,
            "hash": hash,
            "filename": v.files[0]["filename"],
            "compatible_versions": v.gameVersions,
            "date_published": iso_to_int(v.datePublished)
        }
        for game_version in v.gameVersions:
            # Exclude snapshots
            # Using general pattern because mc pattern requires "mc" prefix
            if re.match(GENERAL_VERSION_PATTERN, game_version) is None:
                continue
            all_files_per_mc_version[game_version] = all_files_per_mc_version.get(
                game_version, [])
            all_files_per_mc_version[game_version].append(vdata)

    best_file_per_mc_version = {}

    for mc_version, all_files in all_files_per_mc_version.items():
        best_file_per_mc_version[mc_version] = max(
            all_files, key=lambda x: x["date_published"])

    mc_version_ranges = sorted(
        best_file_per_mc_version.keys(), key=lambda x: version_to_int(x))
    i = 0
    while i < len(mc_version_ranges)-1:
        current_version = mc_version_ranges[i].split('-')[0]
        if best_file_per_mc_version[current_version] == best_file_per_mc_version[mc_version_ranges[i+1]]:
            mc_version_ranges[i] = current_version+"-"+mc_version_ranges[i+1]
            mc_version_ranges.pop(i+1)
        else:
            i += 1

    best_file_per_mc_version_range = {mc_version_range: best_file_per_mc_version[mc_version_range.split(
        '-')[0]] for mc_version_range in mc_version_ranges}

    if (os.path.exists(modid)):
        shutil.copytree(modid, modid +
                        "-old-"+str(int(os.path.getctime(modid))))
        shutil.rmtree(modid)
    os.mkdir(modid)
    for mc_version, file in best_file_per_mc_version_range.items():
        verp = os.path.join(modid, mc_version)
        os.mkdir(verp)
        linkfilename = file["filename"].removesuffix(".jar")+".json"
        with open(os.path.join(verp, linkfilename), "w+") as f:
            json.dump(
                {"link": file["link"], "hash": file["hash"]}, f, indent=2)


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        project_name = input(
            "Enter modrinth project name (example \"fabricproxy-lite\"): ")
    else:
        project_name = sys.argv[1]
    modid = None
    if len(sys.argv) >= 3:
        modid = sys.argv[2]
    release_only = False
    if len(sys.argv) >= 4 and (sys.argv[3] == "--release-only" or sys.argv[3] == "-r"):
        release_only = True
    compile_folder_for_modrinth_mod(project_name, modid, release_only)
