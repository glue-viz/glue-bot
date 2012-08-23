import glob
import os

files = {}

for filename in glob.glob(os.path.join('builds','*.dmg')):
    files[filename] = os.path.getmtime(filename)

times = sorted(files.values())

if len(times) > 5:
    limit = times[-5]

    for filename in files:
        if files[filename] < limit:
            print "Removing %s" % filename
            os.remove(filename)
            os.remove(filename.replace('.dmg', '.log').replace('Glue_', ''))
