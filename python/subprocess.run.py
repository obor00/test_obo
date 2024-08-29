 ret = subprocess.run("vagrant up" , cwd = self._vm_path, shell=True, timeout=240, universal_newlines = True)
