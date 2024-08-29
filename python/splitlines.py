v= b'+ timeout 240 perf/sanity.sh\nfdisk: cannot open /dev/nvme*n*: No such file or directory\n+ timeout 240'
print (v.splitlines())
a=v.splitlines()
print (*a, sep ="\n")
