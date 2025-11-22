# The Vimsical — Music Player

<img width="1227" height="700" alt="Screenshot (4)" src="https://github.com/user-attachments/assets/24e513df-685f-4af0-85a5-9bc228ad3767" />


A whimsical, mood-centric desktop music player built with **Tkinter**, **Pygame**, and **Pillow**.  
Inspired by *whimsical*, tuned by *musical*, and signed with the creator’s “V”.

---

## 🎧 Overview

**The Vimsical** is a custom Python-based music player featuring categorized playlists, live album-art display, search functionality, queue management, and a clean dark-themed UI.  
Everything is packed into one project folder for easy setup and portability.

---

## 🌟 Features

- 🎵 **Play / Pause / Resume / Stop**  
- 🎼 **Five curated playlists**:  
  **Night**, **Dance**, **Energize**, **Favourites**, **K-Pop**
- 🎤 **Search music by Artist or Song Name**
- 📌 **Queue system** (add, play next, remove)
- 🖼️ **Dynamic album art loading**
- 🎨 **Custom themed UI with icons and background frames**
- 🔁 **Automatic next-song playback when queue is active**

---

## 📁 Project Structure

Ensure your folder looks like this:

```graph
Vimsical-Music_Player/
│
├─ the_vimsical.py
│
├─ Musics/
│  ├─ Night/
│  ├─ Dance/
│  ├─ Energize/
│  ├─ Favourites/
│  └─ K-pop/
│
├─ Images/
│  ├─ Night/
│  ├─ Dance/
│  ├─ Energize/
│  ├─ Favourites/
│  └─ K-Pop/
│
└─ Assets/
   ├─ play.png
   ├─ pause img.png
   ├─ stop.png
   ├─ resume new.png
   ├─ search.png
   ├─ search_button.png
   ├─ queue.png
   ├─ remove.png
   ├─ frame.png
   └─ icon.png
```

> **Note:** Song images must match mp3 names exactly (e.g., `Perfect.mp3` → `Perfect.jpg`)

---

## 🛠 Requirements

Install required packages:

```bash
pip install pygame pillow
```

---

## ▶️ Running the App

From inside the project folder, run:

```bash
python the_vimsical.py
```

---

## 🔍 Functionalities

### 🎼 Playlist Loading  
Loads songs from the selected category.

### 🖼 Album Art  
Displays artwork from matching JPG files.

### 🔎 Search  
Search by:
- Artist  
- Song name  

### 🧾 Queue  
Add, view, remove, play next.

### ⏯ Playback  
Play, pause, resume, stop (fadeout).

### ⏱ Auto-Play  
Automatically plays next queued track.

---

## ⚠️ Notes

- This script uses **absolute paths** — update them according to your machine.  
- Missing assets, images, or mp3 files will cause UI errors.  
- Required images must exist in their respective folders.

---

## 🚀 Future Enhancements

- Volume slider  
- Progress bar  
- Dynamic playlists  
- JSON song metadata  
- Modern UI themes  

---

## 💝 Creator

Developed by **Vishesh** — creator of *The Vimsical*, where music meets mood.

