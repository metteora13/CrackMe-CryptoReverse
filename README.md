<div align="center">
  <img src="https://img.shields.io/github/languages/count/metteora13/CrackMe-CryptoReverse?style=flat-square&color=blueviolet" alt="Language Count">
  <img src="https://img.shields.io/github/languages/top/metteora13/CrackMe-CryptoReverse?style=flat-square&color=1e90ff" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/metteora13/CrackMe-CryptoReverse?style=flat-square&color=ff69b4" alt="Last Commit">
  <img src="https://img.shields.io/github/license/metteora13/CrackMe-CryptoReverse?style=flat-square&color=yellow" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions">
</div>

# CrackMe-CryptoReverse
*CrackMe-CryptoReverse*

*Bu proje, temel bir "CrackMe" uygulaması olarak tasarlanmıştır ve kullanıcıdan bir şifre talep eder. Şifre, program içinde XOR kriptografik tekniği kullanılarak gizlenmiştir. Projenin amacı, tersine mühendislik (reverse engineering) becerilerini sınamak ve siber güvenlik alanında eğitimsel bir örnek sunmaktır. Kullanıcılar, binary dosyasını analiz ederek doğru şifreyi bulmaya çalışır, bu süreçte temel kriptografik yöntemlerin nasıl çalıştığını ve tersine mühendislik tekniklerini öğrenir.*

*This project is designed as a basic "CrackMe" application that prompts the user for a password. The password is hidden within the program using the XOR cryptographic technique. The goal is to test reverse engineering skills and provide an educational example in the field of cybersecurity. Users attempt to uncover the correct password by analyzing the binary, learning about basic cryptographic methods and reverse engineering techniques in the process.*

---

## Features / *Özellikler*

**Feature 1**: XOR Encryption
The password is concealed using an XOR operation, requiring users to understand XOR logic to decipher it.

**Özellik 1**: XOR Şifreleme
Şifre, XOR işlemiyle gizlenmiş olup, kullanıcıların bu kriptografik yöntemi analiz ederek şifreyi ortaya çıkarmasını sağlar.

**Feature 2**: Reverse Engineering Focused
The application encourages users to analyze the binary file to find the password, offering an opportunity to learn the use of reverse engineering tools.

**Özellik 2**: Tersine Mühendislik Odaklı
Kullanıcılar, disassembler veya debugger gibi araçlarla binary'yi inceleyerek şifre çözme pratiği yapabilir.

**Feature 3**: Educational Design
CrackMe provides a simple and clear platform for learning fundamental concepts in cybersecurity and cryptography.

**Özellik 3**: Eğitimsel Amaçlı Tasarım
Yeni başlayanlar için uygun, öğretici bir deneyim sunar ve karmaşık kavramları sade bir şekilde açıklar.

**Feature 4**: Flexible Analysis Support
The application supports various reverse engineering approaches (static and dynamic analysis), allowing users to experiment with different methods.

**Özellik 4**: Esnek Analiz Desteği
Kullanıcılar, statik kod analizi veya çalışma zamanı hata ayıklaması gibi farklı tekniklerle şifreyi çözmeyi keşfedebilir.

More features will be added as development progresses.
Geliştikçe daha fazla özellik eklenecektir.

---

## Team / *Ekip*

- **2320191004** - İlke Meryem EYBERCİOĞLU: *Project Managment*  
  *İlke Meryem Eybercioğlu: Proje Yönetimi*


## Roadmap / *Yol Haritası*

See our plans in [ROADMAP.md](ROADMAP.md).  
*Yolculuğu görmek için [ROADMAP.md](ROADMAP.md) dosyasına göz atın.*

---

## Research / *Araştırmalar*

| Topic / *Başlık*        | Link                                    | Description / *Açıklama*                        |
|-------------------------|-----------------------------------------|------------------------------------------------|
| Aircrack Deep Dive      | [researchs/aircrack.md](researchs/aircrack.md) | In-depth analysis of Aircrack-ng suite. / *Aircrack-ng paketinin derinlemesine analizi.* |
| Example Research Topic  | [researchs/your-research-file.md](researchs/your-research-file.md) | Brief overview of this research. / *Bu araştırmanın kısa bir özeti.* |
| Add More Research       | *Link to your other research files*     | *Description of the research*                  |

---

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

## Usage / *Kullanım*

Run the project:  
*Projeyi çalıştırın:*

```bash
python main.py --input your_file.pcap --output results.txt
```

**Steps**:  
1. Prepare input data (*explain data needed*).  
2. Run the script with arguments (*explain key arguments*).  
3. Check output (*explain where to find results*).  

*Adımlar*:  
1. Giriş verilerini hazırlayın (*ne tür verilere ihtiyaç duyulduğunu açıklayın*).  
2. Betiği argümanlarla çalıştırın (*önemli argümanları açıklayın*).  
3. Çıktıyı kontrol edin (*sonuçları nerede bulacağınızı açıklayın*).

---

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
