import datetime
import cv2
import os
from windowcapture import WindowCapture
import keyboard  # pip install keyboard
#import bird_transform as bt

# show_bird = True
#show_bird = False

video_delay_default = 1000
video_delay = video_delay_default

size = (640, 480)
offset = (8, 30)
wincap = WindowCapture(size=size, origin=offset)

# configura os diretorios
game_name = "projeto_1/"
path = "./imagens/" + game_name + "train/"
path_videos = "./videos/" + game_name

if not os.path.exists(path):
    os.makedirs(path)

if not os.path.exists(path_videos):
    os.makedirs(path_videos)

count = len([name for name in os.listdir(path) if os.path.isfile(path + name)])
print("count", count)

count_videos = len([name for name in os.listdir(path_videos) if os.path.isfile(path_videos + name)])
print("count_videos", count)

data = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")

img = None

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
videoWriter = None


def capturar_uma_imagem():
    global count, path, img, last_image
    #if keyboard.is_pressed('shift'):
    # take a picture
    if not (last_image == img).all():
        name = path + "frame_" + data + "_%s.jpg" % str(count).zfill(6)
        print("saving", name)
        count += 1
        cv2.imwrite(name, img)
        last_image = img.copy()
    else:
        print("Nao Gravou porque a Imagem é repetida!")


def sair():
    global capturar
    capturar = False


def salvar_imagens_automatico():
    global gravar_imagens
    gravar_imagens = not gravar_imagens
    print("Salvar imagens automatico esta", gravar_imagens)


def inicia_grava_video():
    global gravar_video, videoWriter
    # if keyboard.is_pressed('shift'):
    gravar_video = not gravar_video
    if gravar_video:
        videoWriter = cv2.VideoWriter(path_videos + 'video_' + data + "_" + str(count_videos) + '.avi', fourcc, 30.0,
                                      (640, 480))
    else:
        videoWriter.release()

    print("Gravando video esta", gravar_video)


def do_action():
    sair()


capturar = True
gravar_imagens = False
primeira = False
gravar_video = False
last_image = []

# definir comandos
try:  # used try so that if user pressed other than the given key error will not be shown
    keyboard.add_hotkey('shift+r', capturar_uma_imagem)  # if key 'q' is pressed
    # keyboard.on_press_key('q', sair, True)
    keyboard.add_hotkey('shift+t', salvar_imagens_automatico)
    keyboard.add_hotkey('shift+v', inicia_grava_video)
    keyboard.add_hotkey('shift+q', sair)
except Exception as e:
    print("erro keyboard", e)

while capturar:
    img = wincap.get_screenshot()

    cv2.imshow("img", img)

    #if show_bird:
    #    bt.bird_transform(img)

    if not primeira:
        primeira = True
        print("Primeira")
        last_image = img.copy()

    if gravar_imagens:
        print("recording", count)
        capturar_uma_imagem()
        video_delay = video_delay_default
    else:
        video_delay = 1

    if gravar_video:
        videoWriter.write(img)

    k = cv2.waitKey(video_delay)

if videoWriter:
    videoWriter.release()
cv2.destroyAllWindows()
print("desligando")
