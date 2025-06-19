import tkinter as tk
from tkinter import messagebox
import hashlib
import sys
import os

class CrackMeApp:
    def __init__(self, master):
        self.master = master
        master.title("R.E.M.I.X. - Şifre Çözme Laboratuvarı")
        master.geometry("750x550")
        master.resizable(False, False)
        
        master.configure(bg="#0A0A0A")
        text_color = "#00FF00"
        font_style_normal = ("Consolas", 12)
        font_style_bold = ("Consolas", 14, "bold")
        entry_font_style = ("Consolas", 14)
        info_color = "#00FFFF"
        encoded_color = "#FFD700"
        solution_guide_color = "#FFFFFF"

        self.max_level = 6
        self.level = self.get_current_level()
        
        # Arayüz öğeleri
        self.title_label = tk.Label(master, text="┌─[ R.E.M.I.X. Challenge ]─┐", fg=text_color, bg="#0A0A0A", font=("Consolas", 22, "bold"))
        self.title_label.pack(pady=10)

        self.level_info_label = tk.Label(master, text=f"Seviye {self.level} / {self.max_level}", fg=text_color, bg="#0A0A0A", font=("Consolas", 16, "bold"))
        self.level_info_label.pack(pady=5)

        self.algo_label = tk.Label(master, text="Algoritma: ", fg=info_color, bg="#0A0A0A", font=font_style_bold, wraplength=700, justify="left")
        self.algo_label.pack(pady=5, anchor="w", padx=20)

        self.encoded_text_label = tk.Label(master, text="Çözülmesi Gereken: ", fg=encoded_color, bg="#0A0A0A", font=font_style_bold, wraplength=700, justify="left")
        self.encoded_text_label.pack(pady=5, anchor="w", padx=20)
        
        self.solution_guide_label = tk.Label(master, text="Nasıl Çözülür: ", fg=solution_guide_color, bg="#0A0A0A", font=font_style_normal, wraplength=700, justify="left")
        self.solution_guide_label.pack(pady=10, anchor="w", padx=20)

        self.prompt_label = tk.Label(master, text="Çözülmüş Şifreyi Girin:", fg=text_color, bg="#0A0A0A", font=font_style_normal)
        self.prompt_label.pack(pady=10)

        self.password_entry = tk.Entry(master, width=40, show="*", bg="#1A1A1A", fg=text_color, insertbackground=text_color, font=entry_font_style, bd=2, relief="solid")
        self.password_entry.pack(pady=10)
        self.password_entry.bind("<Return>", self.check_password)

        self.check_button = tk.Button(master, text="[ ÇÖZÜMÜ KONTROL ET ]", command=self.check_password, bg="#008000", fg="#FFFFFF", font=("Consolas", 12, "bold"), activebackground="#00A000", activeforeground="#FFFFFF", bd=0, relief="flat", padx=20, pady=10)
        self.check_button.pack(pady=15)

        self.reset_button = tk.Button(master, text="[ BAŞTAN BAŞLAT ]", command=self.reset_game, bg="#800000", fg="#FFFFFF", font=("Consolas", 10, "bold"), activebackground="#A00000", activeforeground="#FFFFFF", bd=0, relief="flat", padx=10, pady=5)
        self.reset_button.pack(pady=5)

        self.status_label = tk.Label(master, text="Bekleniyor...", fg="#FFD700", bg="#0A0A0A", font=("Consolas", 10, "italic"))
        self.status_label.pack(pady=5)
        
        self.update_level_display()

    def get_current_level(self):
        try:
            with open("level.dat", "r") as f:
                level = int(f.read().strip())
                if level < 1 or level > self.max_level:
                    return 1
                return level
        except (FileNotFoundError, ValueError):
            return 1

    def save_current_level(self):
        try:
            with open("level.dat", "w") as f:
                f.write(str(self.level))
        except IOError:
            messagebox.showerror("Hata", "Seviye kaydedilemedi. Disk erişim hatası olabilir.")

    def reset_game(self):
        if messagebox.askyesno("Oyunu Baştan Başlat", "Tüm ilerlemeniz silinecek ve oyun 1. seviyeden başlayacak. Emin misiniz?"):
            try:
                if os.path.exists("level.dat"):
                    os.remove("level.dat")
                messagebox.showinfo("Yeniden Başlatıldı", "Oyun 1. seviyeden başlatıldı. Uygulama kendini güncelleyecek.")
                
                self.level = 1 
                self.update_level_display()
                self.status_label.config(text="Oyun baştan başlatıldı.", fg="#00FF00")

            except Exception as e:
                messagebox.showerror("Hata", f"Oyunu yeniden başlatırken bir hata oluştu: {e}")

    def check_password(self, event=None):
        # **DÜZELTME 1: Girilen şifrenin başındaki ve sonundaki boşlukları temizle**
        entered_password = self.password_entry.get().strip() 
        
        correct_hidden_value = self._get_correct_password_for_level(self.level)

        if self._verify_password(self.level, entered_password, correct_hidden_value):
            messagebox.showinfo("BAŞARILI!", f"√ GİRİŞ KABUL EDİLDİ! SEVİYE {self.level} TAMAMLANDI!")
            self.level += 1
            if self.level > self.max_level:
                messagebox.showinfo("GÖREV TAMAMLANDI!", "TEBRİKLER, TÜM SEVİYELERİ ÇÖZDÜNÜZ! R.E.M.I.X. GÖREVİNİZ BİTTİ.")
                self.save_current_level()
                self.master.destroy()
                sys.exit(0)
            else:
                self.save_current_level()
                self.update_level_display()
                self.status_label.config(text=f"Seviye {self.level-1} başarıyla geçildi! Yeni seviye: {self.level}", fg="#00FF00")
        else:
            self.status_label.config(text="!!! ÇÖZÜM HATALI. TEKRAR DENE !!!", fg="#FF4500")
            self.password_entry.delete(0, tk.END)

    def update_level_display(self):
        self.level_info_label.config(text=f"Seviye {self.level} / {self.max_level}")
        self.password_entry.delete(0, tk.END)
        self.status_label.config(text="Bekleniyor...", fg="#FFD700")
        
        algo_text, encoded_text, guide_text = self._get_level_info_for_display(self.level)
        self.algo_label.config(text=f"Algoritma: {algo_text}")
        self.encoded_text_label.config(text=f"Çözülmesi Gereken: {encoded_text}")
        self.solution_guide_label.config(text=f"Nasıl Çözülür: {guide_text}")

    def _get_level_info_for_display(self, level):
        if level == 1:
            return (
                "Ters Çevirme (Reverse String)",
                "terces",
                "Size verilen metin, aslında bilinen bir kelimenin tersten yazılmış hali. Bu metni düzden okuyarak orijinal kelimeyi bulun."
            )
        elif level == 2:
            password_bytes = "xorpass".encode()
            key = 0x5a
            encrypted_bytes = bytes([b ^ key for b in password_bytes])
            return (
                f"XOR Şifrelemesi (Anahtar: {hex(key)})",
                f"Hex Kodu: {encrypted_bytes.hex()}",
                f"Verilen hexadecimal değeri ({encrypted_bytes.hex()}), belirtilen XOR anahtarı ({hex(key)} veya onluk tabanda {key}) ile XOR işlemini uygulayarak orijinal metni ortaya çıkarın. Bunun için online XOR araçlarını veya basit bir kodlama betiğini kullanabilirsiniz."
            )
        elif level == 3:
            return (
                "Sezar Şifrelemesi (Caesar Cipher)",
                "fdhvdu",
                "Bu metin, her harfin alfabede belirli bir sayıda (burada 3 birim) kaydırılmasıyla elde edilmiş bir şifredir. Harfleri 3 birim geri (sol) kaydırarak orijinal kelimeyi bulun."
            )
        elif level == 4:
            correct_pass_full = "hashedpw"
            hash_part = hashlib.md5(correct_pass_full.encode()).hexdigest()[:8]
            return (
                "MD5 Hash Kısmi Parçası",
                f"MD5 Hash Başlangıcı: {hash_part}",
                f"Verilen 8 karakterlik hash parçasının, tam bir MD5 hash'inin başlangıcı olduğunu unutmayın. Orijinal kelimenin MD5 hash'lerini deneyerek veya bilinen 'hashedpw' gibi metinlerin hash'ini manuel olarak hesaplayarak şifreyi bulun."
            )
        elif level == 5:
            return (
                "Matematiksel Hesaplama",
                "(10 * 5) - 20 + 3",
                "Verilen matematiksel ifadeyi doğru işlem sırasına göre hesaplayın. Çıkan sonuç şifreniz olacaktır."
            )
        elif level == 6:
            return (
                "Karmaşık Kontrol Akışı (Obfuscated Control Flow)",
                "Gösterilen Metin: 'obfuscated' (Bu sembolik bir isimdir.)",
                "Bu seviyede asıl hedef, gördüğünüz 'obfuscated' metnini doğrudan çözmek değildir. Programın iç çalışma mantığını (kontrol akışını) anlayın. Şifre, bu karmaşık akışın sonunda doğrulanması gereken değeri temsil ediyor. Dinamik veya statik analiz araçları kullanmanız gerekebilir."
            )
        return "Bilinmeyen Algoritma", "", ""

    def _get_correct_password_for_level(self, level):
        if level == 1:
            return "terces"
        elif level == 2:
            password_bytes = "xorpass".encode()
            key = 0x5a
            encrypted_bytes = bytes([b ^ key for b in password_bytes])
            return encrypted_bytes
        elif level == 3:
            return "fdhvdu"
        elif level == 4:
            correct_pass_full = "hashedpw"
            return hashlib.md5(correct_pass_full.encode()).hexdigest()[:8]
        elif level == 5:
            return str((10 * 5) - 20 + 3)
        elif level == 6:
            return "obfuscated" 
        return "" 

    def _verify_password(self, level, entered, correct_hidden_value):
        if level == 1:
            return entered == correct_hidden_value[::-1]
        elif level == 2:
            key = 0x5a
            entered_bytes = entered.encode()
            return bytes([b ^ key for b in entered_bytes]) == correct_hidden_value
        elif level == 3:
            # Kullanıcının girdiği metin (entered) doğrudan beklenen düz metin "caesar" olmalı.
            # Büyük/küçük harf duyarlılığını ortadan kaldırmak için ikisini de küçük harfe çevir.
            return entered.lower() == "caesar".lower() # BURASI KESİN DÜZELTME

        elif level == 4:
            return hashlib.md5(entered.encode()).hexdigest()[:8] == correct_hidden_value
        elif level == 5:
            try:
                return int(entered) == int(correct_hidden_value)
            except ValueError:
                return False
        elif level == 6:
            return entered == correct_hidden_value 
        return False 

if __name__ == "__main__":
    root = tk.Tk()
    app = CrackMeApp(root)
    root.mainloop()