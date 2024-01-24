[app]
# (str) Title of your application
title = YourApp

# (str) Package name
package.name = yourapp

# (str) Package domain (needed for android/ios packaging)
package.domain = com.your.package.name

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas

source.dir=src
version=1.0.0

[buildozer]
# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pygame_sdl2

# (str) Path to the application source code
source.include_exts = py,png,jpg,kv,atlas
