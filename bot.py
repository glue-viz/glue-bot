import os
import subprocess
import shutil

os.chdir('glue')

# Find latest remote hash
p = subprocess.Popen("git ls-remote http://github.com/glue-viz/glue.git HEAD".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.wait()
hash_remote = p.stdout.read().split()[0]

# Find latest local hash
p = subprocess.Popen("git rev-parse HEAD".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.wait()
hash_local = p.stdout.read().strip()

if hash_local != hash_remote:

    p = subprocess.Popen("git pull".split())
    p.wait()

    shutil.copy('scripts/glueqt', '../app/Glue.py')

    os.chdir('../app/')

    import datetime
    n = datetime.datetime.now()
    stamp = "%04i%02i%02i%02i%02i%02i_%08s" % (n.year, n.month, n.day, n.hour, n.minute, n.second, hash_remote[:8])

    os.system('source do.sh > ../builds/%s.log' % stamp)

    shutil.copy2('dist/Glue.dmg', '../builds/Glue_%s.dmg' % stamp)

else:

    os.chdir('..')


