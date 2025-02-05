
# 🚗 Plaka Tanıma Sistemi

Bu proje, **görüntü işleme ve makine öğrenimi** tekniklerini kullanarak araç plakalarını tespit edip üzerlerindeki karakterleri tanımayı amaçlayan bir sistemdir. 

📸 **OpenCV** kullanarak plaka bölgesini tespit eder, ardından **makine öğrenmesi tabanlı OCR modeli** ile plaka karakterlerini tanır.

---

## 📌 Özellikler

✔️ OpenCV ile **Plaka Tespiti**  
✔️ Karakter ayrıştırma ve OCR Modeli  
✔️ Python ile hızlı çalıştırılabilir yapı  
✔️ Eğitim ve test için veri analizi desteği  

---

## 🚀 Kurulum

Aşağıdaki komutları çalıştırarak gerekli tüm kütüphaneleri yükleyebilirsiniz:

```bash
pip install opencv-python-headless numpy scikit-learn matplotlib
```

Ayrıca, eğer GUI destekli OpenCV kullanmak istiyorsanız:

```bash
pip install opencv-python
```

---

## 📊 Kullanılan Teknolojiler

- **Python** - Projenin ana dili  
- **OpenCV** - Görüntü işleme ve plaka tespiti  
- **Scikit-learn** - Karakter tanıma modeli  
- **NumPy** - Sayısal işlemler  
- **Matplotlib** - Görselleştirme  

---

## 🔧 Kullanım

### 1️⃣ **Plaka Tespiti Çalıştırma**
Bir araç görüntüsündeki plakayı tespit etmek için:

```bash
python alg1_plaka_tespiti.py --input_image path_to_image.jpg
```

📌 **Çıktı olarak tespit edilen plaka bölgesi yeni bir dosyada kaydedilecektir.**

---

### 2️⃣ **Plaka Üzerindeki Karakterleri Tanıma**
Tespit edilen plakadaki karakterleri ayrıştırmak için:

```bash
python alg2_karakter_ayristirma.py --input_image detected_plate.jpg
```

📌 **Çıktı olarak karakterlere ayrılmış görüntüler dosyaya kaydedilecektir.**

---

### 3️⃣ **Karakter Tanıma Modeli Eğitimi**
Eğer kendi modelinizi eğitmek isterseniz:

```bash
python alg2_model_m_o.py
```

📌 **Eğitim tamamlandıktan sonra model `model.pth` dosyasına kaydedilir.**

---

### 4️⃣ **Plaka Tanıma ve Sonuçları Çalıştırma**
Tüm süreci uçtan uca çalıştırmak için:

```bash
python main_pts.py --input_image path_to_car_image.jpg
```

📌 **Bu komut, hem plaka tespitini hem de karakter tanımayı otomatik olarak çalıştıracaktır.**

---

## 📂 Proje Dosya Yapısı

```
📂 PlakaTanima
 ├── 📜 alg1_plaka_tespiti.py       # Plaka tespiti algoritması
 ├── 📜 alg2_karakter_ayristirma.py # Karakter ayrıştırma işlemi
 ├── 📜 alg2_model_m_o.py           # OCR modeli eğitimi
 ├── 📜 alg2_model_o_test.py        # Eğitilen modelin testi
 ├── 📜 alg2_plaka_tanima.py        # Plaka tanıma işlemi
 ├── 📜 main_pts.py                 # Ana çalışma dosyası
 ├── 📜 veri_seti_inceleme.py       # Veri analizi ve ön işleme
 ├── 📜 README.md                   # Proje dökümantasyonu
 └── 📂 data                         # Eğitim ve test verileri
```

---

## 📉 Model Performansı ve Sonuçlar

Eğitim tamamlandıktan sonra **plaka üzerindeki karakterlerin tahmini doğruluk oranı** grafikle gösterilebilir:

```python
import matplotlib.pyplot as plt

plt.plot(train_loss, label="Eğitim Kaybı")
plt.plot(val_loss, label="Doğrulama Kaybı")
plt.legend()
plt.show()
```

---

## 🔗 Kaynaklar
- 📌 [OpenCV Documentation](https://opencv.org/)
- 📌 [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- 📌 [NumPy Documentation](https://numpy.org/)

---

## 🤝 Katkıda Bulunma
Eğer projeye katkıda bulunmak isterseniz, aşağıdaki adımları takip edebilirsiniz:

1. 🍴 **Projeyi Fork'layın**
2. 🛠️ **Yeni Özellik veya Hata Düzeltmesi Ekleyin**
3. 🔄 **Kodunuzu Güncelleyin**
4. ✅ **Pull Request (PR) Gönderin**

---

## 📝 Lisans
📌 **MIT Lisansı** - Bu projeyi özgürce kullanabilir, değiştirebilir ve geliştirebilirsiniz.

---
```

---


4️⃣ **Profesyonel Yapı** – Açık kaynak topluluğu standartlarına uygun, temiz bir belge oluşturuldu.  

---

Bu güncellenmiş **`README.md`** dosyasını projenize ekleyerek, projenizi daha açıklayıcı ve profesyonel hale getirebilirsiniz. 🚀📸
