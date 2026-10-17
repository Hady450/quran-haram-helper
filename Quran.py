import json
import os

def checkHaram(kelime):
    """
    Girilen kelimeyi hem yerel örnek sözlükte hem de varsa quran_data.json 
    dosyasında arayarak dini hükmü veya ilgili ayetleri döndürür.
    """
    aranan = kelime.lower()
    
    # 1. Önce varsa quran_data.json dosyasından kapsamlı arama yapalım
    if os.path.exists("quran_data.json"):
        try:
            with open("quran_data.json", "r", encoding="utf-8") as file:
                quran_data = json.load(file)
            
            bulunan_ayetler = []
            for ayet_bilgisi in quran_data:
                # Anahtar kelimelerde veya metin içinde geçiyor mu?
                anahtar_kelimeler = [k.lower() for k in ayet_bilgisi.get("anahtar_kelimeler", [])]
                if aranan in anahtar_kelimeler or aranan in ayet_bilgisi.get("metin", "").lower():
                    bulunan_ayetler.append(ayet_bilgisi)
            
            if bulunan_ayetler:
                print(f"'{kelime}' ile ilgili Kur'an-ı Kerim'den bulunan sonuçlar:\n")
                for ayet in bulunan_ayetler:
                    print(f"[Sure {ayet.get('sure')}, Ayet {ayet.get('ayet')}]: {ayet.get('metin')}")
                return bulunan_ayetler
        except Exception as e:
            print(f"JSON okunurken bir hata oluştu: {e}")

    # 2. Eğer JSON dosyası yoksa veya dosyada eşleşme bulunamadıysa temel örnek sözlüğe bakalım
    hukumler = {
        "gambling": "Haram (Kumar dinimizde kesinlikle yasaklanmıştır.)",
        "kumar": "Haram (Kumar dinimizde kesinlikle yasaklanmıştır.)",
        "alcohol": "Haram (İçki ve sarhoş edici maddeler yasaktır.)",
        "icki": "Haram (İçki ve sarhoş edici maddeler yasaktır.)",
        "apple": "Helal (Temiz ve yenmesi caiz olan yiyeceklerdendir.)",
        "lying": "Haram (Yalan söylemek yasaklanmıştır.)"
    }
    
    if aranan in hukumler:
        sonuc = hukumler[aranan]
        print(f"Sorgulanan: {kelime} -> Sonuç: {sonuc}")
        return sonuc
    else:
        print(f"'{kelime}' terimi ile ilgili sistemde kayıtlı özel bir hüküm veya quran_data.json bulunamadı.")
        return None
