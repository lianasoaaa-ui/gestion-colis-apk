[app]

title = Gestion Colis Madagascar

package.name = gestioncolis
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,mp3,json

version = 1.0

requirements = python3==3.11.9,kivy==2.3.0,reportlab==4.0.8

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21
android.ndk = 25b

android.accept_sdk_license = True

presplash.color = #FFFFFF

[buildozer]

log_level = 2
warn_on_root = 1
