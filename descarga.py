from __future__ import unicode_literals
import youtube_dl
import win32clipboard

win32clipboard.OpenClipboard()
video = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video])

# get clipboard data
 
