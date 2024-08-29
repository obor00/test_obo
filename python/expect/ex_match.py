import pexpect
import re

def find_matched_pattern(command: str, pattern: str):
    try:
        child = pexpect.spawn(command)

        # Attendez que le motif soit trouvé
        index = child.expect([pattern, 'toto'])

        # Si le motif est trouvé, affichez la partie du texte qui a fait correspondance avec le motif
        if index == 0:
            match = re.search(pattern, child.after.decode())  # Recherche dans ce qui suit la correspondance
            if match:
                matched_text = match.group(0)
                print(f"Motif correspondant trouvé : {matched_text}")

    except pexpect.ExceptionPexpect as e:
        print(f"Erreur : {str(e)}")

# Exemple d'utilisation
command = "ls -l"
pattern = r'file\d+\.txt'
find_matched_pattern(command, pattern)
