# YouTube ve Resim Formatı Dönüştürücü

Bu proje, YouTube videolarını MP3 veya MP4 formatlarına dönüştürmek ve farklı resim formatları arasında (PNG, JPG, WebP) dönüşüm yapabilen basit bir web uygulamasıdır. Flask ve Python kullanarak geliştirilmiştir.

## Özellikler

- **YouTube Video Dönüştürme:** YouTube linklerini MP3 veya MP4 formatına dönüştürme.
- **Resim Formatı Dönüştürme:** PNG, JPG ve WebP arasında dönüşüm yapabilme.
- **Kullanıcı Dostu Arayüz:** Kolay kullanımlı, modern tasarıma sahip web arayüzü.
- **Ücretsiz ve Açık Kaynak:** Herkes tarafından kullanılabilir, geliştirilebilir ve katkıda bulunulabilir.

## Gereksinimler

- Python 3.x
- Flask
- yt-dlp (YouTube video dönüştürme)
- Pillow (Resim dönüştürme)

## Kurulum

1. Projeyi bilgisayarınıza klonlayın:
    ```bash
    git clone https://github.com/Ensorchia/convert-app.git
    ```

2. Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

3. `app.py` dosyasını çalıştırın:
    ```bash
    python app.py
    ```

4. Uygulama, `http://127.0.0.1:5000` adresinde çalışacaktır.

## Kullanım

### YouTube Video Dönüştürme

1. YouTube video linkinizi girin.
2. MP3 veya MP4 formatını seçin.
3. "Dönüştür" butonuna tıklayın ve dosyanın indirilmesini bekleyin.

### Resim Formatı Dönüştürme

1. Dönüştürmek istediğiniz resmi seçin.
2. Hedef formatı seçin (JPG, PNG, WebP).
3. "Dönüştür" butonuna tıklayın ve dönüştürülmüş resmi indirin.

## Katkı

Bu proje herkese açık ücretsiz bir öğretici projedir. Herkes dilediği gibi kullanabilir ve katkıda bulunabilir.

## Not

Projede yer alan templates ve requirements.txt dosyalarını türkçeleştirmeye çalışmayın. utf-8 olayından dolayı hatalar alırsınız. Türkçe yapmakta ısrarcılık yaparsanız sadece app.py dosyasının adını düzenleyip kullanabilirsiniz.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakabilirsiniz.

