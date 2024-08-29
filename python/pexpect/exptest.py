import pexpect
import re

try:
    child = pexpect.spawn('tail -n 20 -f  mytty', timeout=300 )
except:
    pass

#mypath = [ r'\r\n\[root@buildroot', r'\r\n# ' ]
mypath = [ r'\r\n\[root@buildroot ~\]#', r'\r\n# ' ]
#child.sendline('')
#child.expect('b.*u.*i.*l.*d.*r.*o.*o.*t.*l.*o.*g.*i.*n.*:',5)
child.expect( mypath, 2)
#child.expect( '\nbuildroot',  2)

print ('found')

