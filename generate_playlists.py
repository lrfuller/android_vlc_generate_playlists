#!/usr/bin/env python3
"""
VLC Android Playlist Generator
Generates one M3U playlist per subfolder in the current directory.

Usage:
    1. Move this script into your music folder (the one containing your playlist folders)
    2. Run: python3 generate_playlists.py
"""

import os

AUDIO_EXTENSIONS = {".mp3", ".m4a", ".opus", ".flac", ".wav", ".ogg", ".aac"}


def generate_playlist(folder_path: str, folder_name: str) -> int:
    """Scan a folder for audio files and write an M3U playlist. Returns file count."""
    audio_files = sorted(
        f for f in os.listdir(folder_path)
        if os.path.splitext(f)[1].lower() in AUDIO_EXTENSIONS
    )

    if not audio_files:
        print(f"  [skip] '{folder_name}' — no audio files found")
        return 0

    playlist_path = os.path.join(folder_path, f"{folder_name}.m3u")

    with open(playlist_path, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for filename in audio_files:
            filepath = os.path.join(folder_path, filename)
            f.write(f"#EXTINF:-1,{os.path.splitext(filename)[0]}\n")
            f.write(f"{filepath}\n")

    print(f"  [ok]   '{folder_name}.m3u' — {len(audio_files)} tracks")
    return len(audio_files)


def main():
    music_root = os.getcwd()

    print("=" * 50)
    print("VLC Playlist Generator")
    print("=" * 50)
    print(f"\nCurrent directory:\n  {music_root}\n")
    print("Does this directory contain the folders that should become playlists?")
    print("If not, type 'exit', move this script to the correct folder, and re-run.\n")

    response = input("Press Enter to continue, or type 'exit' to quit: ").strip().lower()
    if response == "exit":
        print("\nExiting. Move the script to your music folder and run it again.")
        return

    print(f"\nScanning: {music_root}\n")

    subfolders = sorted(
        entry.name for entry in os.scandir(music_root)
        if entry.is_dir()
    )

    if not subfolders:
        print("No subfolders found.")
        return

    total_playlists = 0
    total_tracks = 0

    for folder_name in subfolders:
        folder_path = os.path.join(music_root, folder_name)
        count = generate_playlist(folder_path, folder_name)
        if count > 0:
            total_playlists += 1
            total_tracks += count

    print(f"\nDone! Created {total_playlists} playlist(s) with {total_tracks} total tracks.")


if __name__ == "__main__":
    main()
