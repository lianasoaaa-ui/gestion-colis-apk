[app]
title = Gestion Colis Madagascar
package.name = gestioncolis
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,mp3

version = 1.0

requirements = python3,kivy,reportlab

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
