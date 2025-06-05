# ROADMAP.md: CrackMe-CryptoReverse Uygulamasının Gelişim Yolculuğu

## GİRİŞ
Bu yol haritası, CrackMe-CryptoReverse uygulamasının mevcut durumunu ve gelecekteki gelişim aşamalarını detaylandırır. Proje, kullanıcıların çeşitli kriptografik bulmacaları ve kod gizleme tekniklerini, tersine mühendislik araçlarını kullanarak çözme becerilerini geliştirmeyi amaçlamaktadır. Her yeni seviye, siber güvenlik meraklılarına daha derinlemesine bir meydan okuma sunacak ve farklı analiz yöntemlerini keşfetme fırsatı tanıyacaktır.

 **Önemli Uyarı: Bu bilgiler yalnızca eğitim ve araştırma amaçlıdır. Yetkisiz kullanımı yasa dışı ve etik dışıdır. Herhangi bir ağda veya sistemde test yapmadan önce açık izin almanız zorunludur.**

 
## 🎯  PROJE VİZYONU / Project Vision
CrackMe-CryptoReverse'in nihai hedefi, tersine mühendislik ve kriptografi alanında yeni başlayanlardan ileri seviye kullanıcılara kadar herkes için kapsamlı, etkileşimli ve ilham verici bir öğrenme platformu olmaktır. Uygulamanın temel amacı, kullanıcıları problem çözme, analitik düşünme ve siber güvenlik araçlarını etkin kullanma konularında teşvik etmektir.

## ÖN KOŞULLAR

**Python 3.x**: Uygulamanın temel geliştirme dili.

**KÜTÜPHANELER**:
**tkinter**: Grafik kullanıcı arayüzü (GUI) için.

**hashlib**: Şifreleme algoritmaları için (örneğin MD5).
Diğer standart Python kütüphaneleri.

**BİLGİ GEREKSİNİMLERİ (Kullanıcılar İçin)**:
Python programlama temelleri (opsiyonel, ancak kod analizi için faydalı).
Temel kriptografi (Sezar, XOR, Hashing) bilgisi.
Tersine mühendislik kavramlarına aşinalık (statik/dinamik analiz).
Önerilen Araçlar (Şifre Çözmek İçin):
strings (komut satırı aracı)
Ghidra (disassembler/decompiler)
IDA Free (disassembler)
x64dbg (debugger)
Online kriptografi çözücüler (örneğin XOR, Sezar)
Hex editörler


## ✅  MEVCUT SEVİYELER VE HEDEFLER (v1.0) / Current Levels & Objectives
Uygulamanın mevcut sürümünde (v1.0) bulunan seviyeler ve her birindeki temel tersine mühendislik hedefleri:

**Seviye 1**: Ters Çevirme (Reverse String)
**Hedef**: Basit string manipülasyonunu tanıma ve Python kodundaki string operasyonlarını fark etme.

**Seviye 2**: XOR Şifrelemesi (XOR Encryption)
**Hedef**: XOR işleminin temel kriptografik kullanımını anlama. İkili dosyada anahtarı veya XOR'lanmış değeri bulma ve manuel olarak çözme.

**Seviye 3**: Sezar Şifrelemesi (Caesar Cipher)
**Hedef**: Klasik şifreleme algoritmalarından birini çözme. Sabit kaydırma miktarını (shift) tespit etme ve metni deşifre etme.

**Seviye 4**: MD5 Hash Kısmi Parçası (Partial MD5 Hash)
**Hedef**: Hashing algoritmalarının tek yönlü doğasını anlama. Belirli bir hash parçasını karşılayacak orijinal metni bulmak için deneme-yanılma veya bilinen stringlerin hash'ini kontrol etme.

**Seviye 5**: Matematiksel Hesaplama (Mathematical Calculation)
Hedef: Programın içerisinde basit matematiksel işlemlerin nasıl saklandığını veya yürütüldüğünü tespit etme ve sonucu hesaplama.

**Seviye 6**: Karmaşık Kontrol Akışı (Obfuscated Control Flow)
**Hedef**: Kod gizleme tekniklerine ilk bakış. Uygulamanın mantığını takip ederek veya hata ayıklayıcı kullanarak doğru değeri dinamik olarak bulma.


## 🗺️  YOL HARİTASI (Gelecek Geliştirmeler) / Roadmap (Future Developments)
**Faz 1**: Kriptografik Zenginleştirme (Hedef: v1.1)
Yeni Şifreleme Algoritmaları:
**Base64/ROT13**: Daha sık karşılaşılan kodlama/basit şifreleme yöntemlerini ekleme.
**Polyalphabetic Ciphers (Vigenere gibi)**: Daha karmaşık klasik şifreleme yöntemlerini dahil etme.
**Basit Symmetric Key Crypto (AES/DES)**: Python'daki kütüphanelerle basit bir simetrik şifreleme seviyesi ekleme (anahtarın bulunması gereken).
**Daha Kapsamlı Hash Fonksiyonları**: SHA-256, SHA-3 gibi farklı hash türlerini içeren seviyeler.
Bitwise Operasyonlar: Şifrelemelerde sıkça kullanılan bitwise (AND, OR, NOT, Shift) operasyonlarını içeren seviyeler.
**Faz 2**: Tersine Mühendislik Zorlukları (Hedef: v1.2)
**Anti-Tampering Mekanizmaları**: Uygulamanın, değiştirilmeye çalışıldığında veya hata ayıklayıcıya bağlandığında davranışını değiştiren basit önlemler.
**Anti-Debugging Teknikleri**: Uygulamanın bir debugger altında çalışıp çalışmadığını algılayan ve buna göre farklı bir yol izleyen seviyeler.
**Dinamik Anahtar Üretimi**: Şifrenin veya anahtarın sabit olarak depolanmak yerine çalışma zamanında belirli koşullara göre üretildiği seviyeler.
**Farklı Dosya Biçimleri**: Sadece string aramasıyla bulunamayacak, dosya formatı analizi gerektiren (örneğin gömülü resimlerde/dosyalarda gizli veri) seviyeler.
**Faz 3**: Kullanıcı Deneyimi ve Araç Entegrasyonu (Hedef: v2.0)
**Geliştirilmiş GUI**: Kullanıcı arayüzünü daha interaktif ve bilgilendirici hale getirme.
**İlerleme Takibi**: Detaylı seviye tamamlama istatistikleri ve başarımlar.
**Hata Ayıklama İpuçları**: Takılan kullanıcılar için isteğe bağlı olarak sunulabilecek seviyeye özel ipuçları (sadece ipucu butonuyla aktifleşen).
**Test Otomasyonu**: Her seviyenin doğru çalışıp çalışmadığını kontrol etmek için otomatik testler geliştirme.
**Daha İyi Cross-Platform Uyumluluğu**: MacOS ve Linux'ta da daha sorunsuz çalışmasını sağlama.

## 📈 GELİŞTİRMELERİN TEST EDİLMESİ / Testing Developments
Her yeni seviye ve özellik eklendiğinde, aşağıdaki test adımları uygulanacaktır:

**Manuel Testler**: Uygulama, her seviye için belirlenmiş doğru şifrelerle manuel olarak test edilecektir.
**Tersine Mühendislik Testleri**:
strings ile metin arama.
Ghidra/IDA Free ile statik kod analizi yaparak fonksiyon akışlarını ve veri yapılarını inceleme.
x64dbg gibi bir debugger ile dinamik analiz yaparak çalışma zamanı davranışını izleme.
**Hata Yakalama**: Potansiyel hataları ve güvenlik açıklarını belirlemek için çeşitli yanlış girişler denenecektir.

## 🛡️  GÜVENLİK VE ETİK İLKELER / Security & Ethical Guidelines
**Eğitim Amacı**: Projenin tek amacı, siber güvenlik becerilerini etik ve yasal sınırlar içinde geliştirmektir.
**İzinli Kullanım**: Bu projede öğrenilen hiçbir teknik, yazılı izin alınmadan gerçek sistemlere veya ağlara karşı kullanılmamalıdır.
**Sorumluluk**: Kullanıcılar, bu araçları ve bilgileri kullanırken kendi eylemlerinden tamamen sorumludur.

## 🏁  SONUÇ/ Conclusion
Bu yol haritası, CrackMe-CryptoReverse'in heyecan verici gelişim potansiyelini ortaya koymaktadır. Topluluktan gelecek geri bildirimler ve katkılarla projenin daha da zenginleşeceğine inanıyoruz. Siber güvenlik dünyasında yeteneklerinizi test etmek ve geliştirmek için bize katılın!
