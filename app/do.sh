#!/bin/bash

rm -r build dist
python setup.py py2app --no-chdir
cd dist
macdeployqt Glue.app -dmg
cd ..
