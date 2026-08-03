[app]
title = Persian Cars
package.name = persiancars
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 1.0.0
requirements = python3,kivy,requests,android,plyer

orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.1.0
fullscreen = 0

# android permittions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.gradle_dependencies = 'com.android.support:support-annotations:28.0.0'

[buildozer]
log_level = 2
warn_on_root = 1
