import subprocess
import paramiko

pack = 'bash'
cmd2 = f"""
    echo hello
    [ true ] && echo "true"
    bash -c 'apt-get source --download-only {pack} | sed -n \
    "/dsc/ s/^Get.* \([^ ]*\) (dsc) .*$/\1/p;s/^Skipping already downloaded file .bash_\(.*\).dsc.$/\1/p" \
    | xargs -I PKGVERSION echo "DSC=/home/vagrant/fsut/bash/src/bash_PKGVERSION.dsc; echo $DSC; test -r $DSC" | sh'
 """

ret = subprocess.run(cmd2,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

#print(ret)
print(ret.stdout)
print(ret.stderr)

assert False, f"{cmd2}"

