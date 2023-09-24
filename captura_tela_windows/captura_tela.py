import cv2
from windowcapture import WindowCapture

# Escreva o nome da Janela
#wincap = WindowCapture("Nome da Janela")

# Escreve um tamanho de tela e a origem
wincap = WindowCapture(size=(800,600), origin=(40,40))

while True:
    #captura tela
    img = wincap.get_screenshot()

    # desenha tela
    cv2.imshow("img", img)

    # aperta q para sair
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()
print("desligando")