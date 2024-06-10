# mouseclick
---
Plays the sound of mouse clicks when the mouse keys are pressed

Воспроизводит звук щелчков мыши при нажатии клавиш мыши

---
## Compilation
Requires: pygame, pynput, pyinstaller

Требуется: pygame, pynput, pyinstaller

pyinstaller --onefile --add-data "mouse1.mp3;." --add-data "mouse2.mp3;." --add-data "mouse3.mp3;." --icon=icon.ico --noconsole mouseclick.py
