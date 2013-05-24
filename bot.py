import sys
import os
import subprocess
import shutil

os.chdir('glue')

# Find latest remote hash
p = subprocess.Popen("/usr/local/git/bin/git ls-remote http://github.com/glue-viz/glue.git HEAD".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.wait()
hash_remote = p.stdout.read().split()[0]

# Find latest local hash
p = subprocess.Popen("/usr/local/git/bin/git rev-parse HEAD".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.wait()
hash_local = p.stdout.read().strip()

if hash_local != hash_remote or '--force' in sys.argv:

    p = subprocess.Popen("rm -r /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/glue", shell=True)
    p.wait()

    p = subprocess.Popen("rm /Library/Frameworks/Python.framework/Versions/2.7/bin/{glue,glueqt,glueconfig,runtests.py}", shell=True)
    p.wait()

    p = subprocess.Popen("/usr/local/git/bin/git pull origin master".split())
    p.wait()

    p = subprocess.Popen("/Library/Frameworks/Python.framework/Versions/2.7/bin/python setup.py build".split())
    p.wait()

    p = subprocess.Popen("/Library/Frameworks/Python.framework/Versions/2.7/bin/python setup.py install".split())
    p.wait()

    shutil.copy('scripts/glue', '../app/Glue.py')

    shutil.rmtree('build')

    os.chdir('../app/')

    import datetime
    n = datetime.datetime.now()
    stamp = "%04i%02i%02i%02i%02i%02i_%08s" % (n.year, n.month, n.day, n.hour, n.minute, n.second, hash_remote[:8])

    os.system('source do.sh > ../builds/%s.log' % stamp)

    shutil.copy2('dist/Glue.dmg', '../builds/Glue_%s.dmg' % stamp)
    shutil.copy2('dist/Glue.dmg', '../builds/Glue_latest.dmg')

    shutil.rmtree('dist')

else:

    os.chdir('..')


