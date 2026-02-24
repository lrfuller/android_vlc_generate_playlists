# VLC Playlist Generator — Setup Guide

Generates an M3U playlist for each subfolder in your music directory,
so they show up properly in VLC Android's Playlist tab.

---

## Requirements

### 1. Install Termux
Download and install **Termux** from F-Droid (recommended) or the Play Store.
- F-Droid (preferred): https://f-droid.org/packages/com.termux/
- The Play Store version may be outdated.

### 2. Install Python
Open Termux and run:
```
pkg install python
```

### 3. Grant Storage Permissions
Still in Termux, run:
```
termux-setup-storage
```
When prompted, tap **Allow**. This lets Termux access your device storage (e.g. /sdcard).

### 4. Move the Script to Your Music Folder
Move `generate_playlists.py` into the folder that **contains** your playlist folders.

Example structure:
```
/sdcard/Music/              ← put the script HERE
    Rock/
        song1.mp3
        song2.mp3
    Jazz/
        track1.m4a
    Podcasts/
        episode1.opus
```

You can move it using a file manager app, or via Termux:
```
mv /sdcard/Download/generate_playlists.py /sdcard/Music/
```

---

## Running the Script

Navigate to the folder in Termux:
```
cd /sdcard/Music
```

Then run:
```
python3 generate_playlists.py
```

The script will show your current directory and ask you to confirm before doing anything.
Each subfolder will get its own `.m3u` playlist file saved inside it.

---

## Re-running
If you add new songs later, just run the script again — it will overwrite the old playlists with updated ones.
