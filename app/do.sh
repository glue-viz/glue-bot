#!/bin/bash

rm -r build dist
python setup.py py2app
cd dist
macdeployqt Glue.app -dmg
cd ..
