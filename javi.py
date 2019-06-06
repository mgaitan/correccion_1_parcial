"""back_gif
Usage:
  back_gif.py --duracion=<duracion> [--tamaño=<tamaño>]

Options:
  -h --help          Show this screen.
  --tamaño=<tamaño>  Tamaño del video  [default=128,128]
"""
from docopt import docopt
from moviepy.editor import *

def back_gif(duracion, tamaño=(128,128)):
    backB = ColorClip(tamaño, color=(0, 0, 0), duration=duracion)
    backW = ColorClip(tamaño, color=(255, 255, 255), duration=duracion)
    vfinal= concatenate_videoclips([backW, backB]*3)
    vfinal.write_videofile('back.mp4', fps=15)

if __name__ == '__main__':
    argumentos = docopt(__doc__)
    #print(argumentos)
    duracion = int(argumentos['--duracion'])
    tamaño = (argumentos['--tamaño'])
    if tamaño:
        tamaño = [int(v) for v in tamaño.split(',')]
    back_gif(duracion, tamaño)
