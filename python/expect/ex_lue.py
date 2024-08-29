import pexpect

def find_pattern_output(command: str, pattern: str):
    try:
        child = pexpect.spawn(command)
        
        # Attendez que le motif soit trouvé
        index = child.expect(pattern)
        
        # Si le motif est trouvé, affichez la partie de la sortie lue avant la correspondance
        if index == 0:
            print("Motif trouvé :")
            print(child.before.decode())  # Cela affiche la sortie lue jusqu'à la correspondance
        
    except pexpect.ExceptionPexpect as e:
        print(f"Erreur : {str(e)}")

# Exemple d'utilisation
command = "ls -l"
pattern = r'file\d+\.txt'
find_pattern_output(command, pattern)

