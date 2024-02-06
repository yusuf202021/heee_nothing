import os, hashlib, sys, json, shutil
from itertools import cycle
if len(sys.argv) < 4: # script, save name, original, modified
    quit(f"{sys.argv[0]} [save name] [original] [modified]")

arguments = cycle(sys.argv[1:])

save_name = next(arguments)
original  = next(arguments)
modified  = next(arguments)

malware_database = os.path.join(os.environ["USERPROFILE"], "malware_database")
overrides = os.path.join(malware_database, "overrides")

if not os.path.exists(overrides):
    os.makedirs(overrides, exist_ok=True)

with open(os.path.join(malware_database, "file_patches.json"), encoding="utf8") as fp:
    file_patches = json.load(fp)

if not save_name in file_patches:
    file_patches[save_name] = {}

with open(original, "rb") as fp:
    original_content = fp.read()
    with open(modified, "rb") as fp:
        modified_content = fp.read()

file_patches[save_name][hashlib.sha256(original_content).digest().hex().upper()] = hashlib.sha256(modified_content).digest().hex().upper()

shutil.copy(modified, os.path.join(overrides, hashlib.sha256(modified_content).digest().hex().upper()))

with open(os.path.join(malware_database, "file_patches.json"), "w", encoding="utf8") as fp:
    json.dump(file_patches, fp, indent=4, ensure_ascii=False)