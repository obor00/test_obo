import pexpect

child = pexpect.spawn('ls -l')
index = child.expect(['file1', 'file2', pexpect.EOF])
if index == 0:
    print("Motif 'pattern1' trouvé.")
elif index == 1:
    print("Motif 'pattern2' trouvé.")
elif index == 2:
    print("Fin de la sortie.")
else:
    print("Aucun motif trouvé ou timeout atteint.")

