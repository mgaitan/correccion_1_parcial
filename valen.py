"""parcial_practica
Usage:
    parcial_practica.py <directorio> [--duracion=<duracion>] [--tamaño=<tamaño>]
Options:
  -h --help                 Show this screen.
  --duracion=<duracion>     Duracion por imagen [default: 3].
  --tamaño=<tamaño>         Tamaño del video  [default=500, 600]
"""

from docopt import docopt    
from pathlib import Path                                           
from moviepy.editor import *                                       

def imagen_clip(directorio, duracion,tamaño=(500, 600)):
	directorio = Path(directorio)
	background = ColorClip(tamaño, color=(0, 0, 0), duration=duracion)
	clips = []                                                        

	for archivo in directorio.iterdir(): 
		if archivo.is_file() and archivo.name.endswith(('.jpg','.png', '.jpeg')): 
			archivo = str(archivo) 
			clip = ImageClip(archivo, duration=duracion) 
			clips.append(clips)                                                                    

	final = concatenate_videoclips(clips)
	print ('generando video')                             
	final.write_videofile("mivideo.mp4", fps=5)

if __name__ == '__main__':
	from docopt import docopt 
	argumentos= docopt (__doc__)
	imagen_clip(argumentos['<directorio>'])
	duracion = float (argumentos['--duracion'])

