import lief, sys, hashlib

fp = open(sys.argv[1], "rb")

pe = lief.parse(fp)
if not pe: quit()
fp.seek(0)
print(hashlib.sha256(fp.read(pe.sizeof_headers)).digest().hex().upper())