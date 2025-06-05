<div align="center">
  <img src="https://img.shields.io/github/languages/count/metteora13/CrackMe-CryptoReverse?style=flat-square&color=blueviolet" alt="Language Count">
  <img src="https://img.shields.io/github/languages/top/metteora13/CrackMe-CryptoReverse?style=flat-square&color=1e90ff" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/metteora13/CrackMe-CryptoReverse?style=flat-square&color=ff69b4" alt="Last Commit">
  <img src="https://img.shields.io/github/license/metteora13/CrackMe-CryptoReverse?style=flat-square&color=yellow" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions">
</div>

## 🕵️‍♂️ **CRACKME-CRYPTOREVERSE: Şifre Avı Başlasın! / Embark on the Cipher Hunt!**

*"CrackMe" uygulaması, siber güvenlik ve tersine mühendislik dünyasına adım atmak isteyenler için tasarlanmış heyecan verici bir meydan okuma sunuyor. Karşınıza, kullanıcı dostu Python Tkinter tabanlı şık bir grafik arayüz çıkacak ve göreviniz basit: "Doğru şifreyi girin!" Ancak sakın aldanmayın; şifre, uygulamanın derinliklerinde ustaca gizlenmiş durumda
İşte tam da bu noktada tersine mühendislik yetenekleriniz devreye giriyor. Kod akışını incelemeniz ve nihayetinde gizli anahtarı ortaya çıkarmanız gerekecek. strings, Ghidra, IDA Free, x64dbg gibi popüler tersine mühendislik araçlarını kullanarak dijital dedektiflik becerilerinizi konuşturmaya hazır olun!*

*This "CrackMe" application presents an exhilarating challenge designed for anyone eager to step into the world of cybersecurity and reverse engineering. You'll be greeted by a sleek, user-friendly Python Tkinter-based graphical interface with a deceptively simple task: "Enter the correct password!" But don't be fooled; the password is masterfully concealed deep within the application, and it's certainly not stored as plain text within the software itself!

This is precisely where your reverse engineering prowess comes into play. Your mission: meticulously scrutinize the program's binary file, trace its intricate code flow, and ultimately unearth the hidden key. Get ready to unleash your digital detective skills and master tools like strings, Ghidra, IDA Free, and x64dbg to crack the code!*

---

## ✨ **Features / Özellikler**
Sizi hem eğlendirecek hem de öğretecek dikkat çekici özellikler:

🔒 **Çok Seviyeli Kripto Gizemleri (Multi-Level Crypto Puzzles)**: Basitten karmaşığa doğru ilerleyen 6 farklı şifreleme algoritmasıyla karşılaşın. Her seviye, farklı bir kriptografik bulmacayı çözmenizi gerektirecek. (Ters Çevirme, XOR, Sezar Şifrelemesi, MD5 Hash, Matematiksel Hesaplama, Karmaşık Kontrol Akışı gibi!)

🧠 **Tersine Mühendislik Laboratuvarı (Reverse Engineering Sandbox)**: Bu uygulama, strings, disassembler'lar (Ghidra, IDA Free) ve debugger'lar (x64dbg) gibi araçların nasıl kullanılacağını pratik bir şekilde öğrenmek için mükemmel bir ortam sunar. Kodun iç yüzünü keşfetmeye odaklanın!

🎓 **Eğitimsel ve Öğretici Tasarım (Educational & Instructive Design)**: CrackMe, siber güvenlik ve kriptografi alanındaki temel kavramları yeni başlayanlar için anlaşılır ve ilgi çekici bir platformda sunar. Karmaşık algoritmaların ardındaki mantığı çözerek hem bilgi hem de beceri kazanın.

🔄 **Esnek Analiz Desteği (Flexible Analysis Support)**: Statik kod analizi (kodun kaynak dosyasına veya ikili dosya yapısına bakma) veya dinamik analiz (programı çalıştırırken hata ayıklama ve bellek durumunu izleme) gibi çeşitli tersine mühendislik yaklaşımlarını deneme özgürlüğüne sahipsiniz. Size uygun yöntemi seçin!

🚀 **İlerlemeyi Kaydetme (Progress Saving)**: Çözdüğünüz seviyeler otomatik olarak kaydedilir, böylece kaldığınız yerden devam edebilirsiniz. Her seferinde baştan başlamak zorunda kalmazsınız.

---

## Team / *Ekip*

- **2320191004** - İlke Meryem EYBERCİOĞLU: *Project Managment*  
  *İlke Meryem Eybercioğlu: Proje Yönetimi*


## Roadmap / *Yol Haritası*

See our plans in [ROADMAP.md](ROADMAP.md).  
*Yolculuğu görmek için [ROADMAP.md](ROADMAP.md) dosyasına göz atın.*

---

## Research / *Araştırmalar*

| Topic / *Başlık*          | Link                                          | Description / *Açıklama*                        |
| :------------------------ | :-------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Python Binary Analizi** | [`researchs/python-binary-analysis.md`](researchs/python-binary-analysis.md) | PyInstaller ile paketlenmiş Python uygulamalarının ikili dosyalarının (`.exe`) tersine mühendislik araçlarıyla nasıl analiz edileceğine dair bir inceleme. |
| **Obfuscation Teknikleri** | [`researchs/obfuscation-techniques.md`](researchs/obfuscation-techniques.md) | Kod gizleme (obfuscation) yöntemleri ve bu tekniklerin tersine mühendislik süreçlerini nasıl zorlaştırdığı üzerine bir genel bakış. |
| **Temel Kriptografi Algoritmaları** | [`researchs/basic-crypto-algs.md`](researchs/basic-crypto-algs.md) | Sezar, XOR ve MD5 gibi uygulamada kullanılan temel kriptografik algoritmaların çalışma prensipleri ve zayıflıkları. |
| **Debugger Kullanımı (x64dbg)** | [`researchs/x64dbg-usage.md`](researchs/x64dbg-usage.md) | Dinamik analiz için x64dbg hata ayıklayıcısının temel özellikleri ve uygulamanın çalışma zamanı davranışını incelemede kullanımı. |
| **Statik Analiz Araçları (Ghidra/IDA Free)** | [`researchs/static-analysis-tools.md`](researchs/static-analysis-tools.md) | Ghidra ve IDA Free gibi statik analiz araçlarıyla ikili kodun nasıl parçalandığı, fonksiyon akışının nasıl çıkarıldığına dair bir inceleme. |



## Installation / *Kurulum*

1. **Clone the Repository / *Depoyu Klonlayın***:  
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO
   ```

2. **Set Up Virtual Environment / *Sanal Ortam Kurulumu*** (Recommended):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies / *Bağımlılıkları Yükleyin***:  
   ```bash
   pip install -r requirements.txt
   ```

---

Harika! Usage (Kullanım) bölümünü projenizin CrackMe yapısına uygun hale getirelim. Uygulamanızın argüman almadığını ve direkt olarak çalıştırıldığını düşünerek, bu bölümü daha açıklayıcı ve yönlendirici bir şekilde düzenleyelim.

İşte size özel olarak hazırlanmış, güncellenmiş "Usage" bölümü:

🎮 **Usage / Kullanım**
Hazır mısınız? Bu gizemli uygulamanın sırlarını çözmek için aşağıdaki adımları izleyin:

**Projeyi başlatın**:

**Bash**
python main.py

**Adımlar**:

**Uygulamayı Başlatın**: Terminalinizde yukarıdaki komutu çalıştırın. Kısa bir süre sonra, Python Tkinter tabanlı şık bir grafik arayüzle karşılaşacaksınız. Bu, şifre avınızın başlangıç noktası olacak!

**Gizli Şifreyi Çözün**: Uygulamanın ana ekranında "Çözülmesi Gereken" başlığı altında size verilen şifreli metni dikkatlice inceleyin. Aynı zamanda, "Algoritma" ve "Nasıl Çözülür" kısımlarındaki ipuçları ve detaylı rehber metinleri size yol gösterecek. Bu bilgiler, hangi kriptografik yöntemin kullanıldığını ve şifreyi nasıl deşifre etmeniz gerektiğini anlamanız için kritik. Gerekirse harici tersine mühendislik araçlarını kullanmaktan çekinmeyin!

**Çözümü Girin**: Şifreli metnin ardındaki gerçek kelimeyi bulduğunuzda, bunu "Çözülmüş Şifreyi Girin" kutusuna yazın. Doğrulamak için klavyenizdeki Enter tuşuna basın veya "ÇÖZÜMÜ KONTROL ET" butonuna tıklayın.

**İlerlemenizi İzleyin**: Eğer çözümünüz doğruysa, "BAŞARILI!" mesajını görecek ve bir sonraki zorlu seviyeye geçeceksiniz. Tüm 6 seviyeyi başarıyla tamamlayarak R.E.M.I.X. görevinizi bitirin ve siber güvenlik alanındaki ustalığınızı kanıtlayın!

## Contributing / *Katkıda Bulunma*

We welcome contributions! To help:  
1. Fork the repository.  
2. Clone your fork (`git clone git@github.com:YOUR_USERNAME/YOUR_REPO.git`).  
3. Create a branch (`git checkout -b feature/your-feature`).  
4. Commit changes with clear messages.  
5. Push to your fork (`git push origin feature/your-feature`).  
6. Open a Pull Request.  

Follow our coding standards (see [CONTRIBUTING.md](CONTRIBUTING.md)).  

*Topluluk katkilerini memnuniyetle karşılıyoruz! Katkıda bulunmak için yukarıdaki adımları izleyin ve kodlama standartlarımıza uyun.*

---

## License / *Lisans*

Licensed under the [MIT License](LICENSE.md).  
*MIT Lisansı altında lisanslanmıştır.*

---

## Acknowledgements / *Teşekkürler* (Optional)

Thanks to:  
- Keyvan Arasteh (keyvan.arasteh@istinye.edu.tr)
- Istinye University

*Teşekkürler: Harika kütüphaneler ve ilham kaynakları için.*

---

## Contact / *İletişim* (Optional)

Project Maintainer: [İlke Meryem Eybercioğlu/ Istinye University] - [2320191004@stu.istinye.edu.tr]  
Found a bug? Open an issue.  

*Proje Sorumlusu: [İlke Meryem Eybercioğlu/ Istinye University] - [2320191004@stu.istinye.edu.tr]. Hata bulursanız bir sorun bildirin.*

---

*Replace placeholders (e.g., YOUR_USERNAME/YOUR_REPO) with your project details.*
