#!/bin/bash

rm -r build dist
/Library/Frameworks/Python.framework/Versions/2.7/bin/python setup.py py2app
cd dist
/usr/bin/macdeployqt Glue.app -dmg
cd ..

# Clean up (for permissions)
rm -r build
rm /Library/Frameworks/Python.framework/Versions/2.7/bin/glueqt
rm /Library/Frameworks/Python.framework/Versions/2.7/bin/glueconfig
rm /Library/Frameworks/Python.framework/Versions/2.7/bin/runtests.py
rm Glue.py
rm -r ../glue/build
