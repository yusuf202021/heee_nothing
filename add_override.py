import os, hashlib, sys, json

if len(sys.argv) < 4: # script, save name, original, modified
    quit(f"{sys.argv[0]} [save name] [original] [modified]")

malware_databas = os.path.join(os.environ["USERPROFILE"])
overrides = os.path.join(malware_databas, "overrides")

if not os.path.exists(overrides):
    os.path.makedirs(overrides, exist_ok=True)

