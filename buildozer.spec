[app]
title = Gestion Colis Madagascar
package.name = gestioncolis
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,mp3

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21

# 🔥 IMPORTANT FIX
android.ndk = 25b
