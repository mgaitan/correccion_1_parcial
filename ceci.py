from pathlib import Path
from moviepy.editor import *

def imagen_clip(directorio, duracion, audio=None, tamaño=(500, 500)):
	directorio = Path(directorio)
	clips = []
	for archivo in directorio.iterdir():
		if archivo.is_file() and archivo.name.endswith(('.jpg','.jpeg', '.png')):
			 
			archivo=str(archivo) 
			clip = ImageClip(archivo, duration=duracion).resize(tamaño)
			clips.append(clip)

	final = concatenate_videoclips(clips*3)
	
	final.write_videofile(f'{directorio}.mp4', fps=15)
