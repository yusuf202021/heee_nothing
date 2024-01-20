import lief, sys, hashlib

if len(sys.argv) < 2:
    quit(f"{sys.executable} {sys.argv[1]} [pe.(exe/dll)]")

fp = open(sys.argv[1], "rb")

pe = lief.parse(fp)

sizeof_headers = pe.sizeof_headers

fp.seek(0)
data = fp.read(sizeof_headers)
fp.close()
print(hashlib.sha256(data).digest().hex().upper())