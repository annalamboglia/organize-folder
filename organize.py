import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS" :['.pdf', '.rtf', '.txt','.odt','.docx','.doc','.pptx'],
    "AUDIO" : ['.m4a', '.m4b', '.mp3','.wav','.aac', '.MP3'],
    "VIDEOS" : ['.mov', '.avi', '.mp4'],
    "IMAGES" : ['.jpg', '.jpeg', '.png','.svg','.gif','.jfif'],
    "EBOOKS" : ['.epub', '.azw3'],
    "ZIP" : ['.zip'],
    "PHOTHOSHOP" : ['.psd'],
    "EXE" : ['.exe'],
    "HTML" : ['.html'],
    "JSON" : ['.JSON', 'json'],
    "PYTHON" : ['.py', '.ipynb'],
    "EXCEL" : ['.xlx', '.csv', '.xls','.xlsx']
}

def pickDirectiory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'

def organizeDirectory():
    for item in os.scandir():
        #print(item)
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDirectiory(filetype)
        #print("directory: ", directory)
        directoryPath = Path(directory)
        #print("directoryPath: ", directoryPath)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))


organizeDirectory()