import os

import cv2
import matplotlib.pyplot as plt

import alg1_plaka_tespiti
import alg2_plaka_tanima

veriler: list[str] = os.listdir("veriseti")

isim = veriler[1]
for isim in veriler:
    print("resim:", "veriseti/" + isim)
    img = cv2.imread("veriseti/" + isim)
    img = cv2.resize(img, (500, 500))

    plaka = alg1_plaka_tespiti.plaka_konum_don(img)
    plakaImg, plakaKarakter = alg2_plaka_tanima.plakaTani(img, plaka)
    print("resimdeki plaka:", plakaKarakter)
    plt.imshow(plakaImg)
    plt.show()
