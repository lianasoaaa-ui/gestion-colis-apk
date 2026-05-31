[app]

title = Gestion Colis Madagascar

package.name = gestioncolis
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,mp3,json

version = 1.0

# ✅ IMPORTANT: pas de version fixée
requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Android permissions (clean version)
android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b

android.accept_sdk_license = True

presplash.color = #FFFFFF

[buildozer]

log_level = 2
warn_on_root = 1
