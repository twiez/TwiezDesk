import os
import shutil
import time

# Beyaz renk için ANSI escape kodu
WHITE = "\033[97m"
RESET = "\033[0m"  # Rengi sıfırlamak için

# Kullanıcının masaüstü yolu
DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop")

# Dosya kategorileri
CATEGORIES = {
    "Resimler": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico", ".tiff"],
    "Videolar": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"],
    "Müzikler": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"],
    "Belgeler": [".txt", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".odt"],
    "Kod Dosyaları": {
        "Python": [".py"],
        "Java": [".java"],
        "C": [".c"],
        "C++": [".cpp"],
        "C#": [".cs"],
        "JavaScript": [".js"],
        "HTML_CSS": [".html", ".css"],
        "PHP": [".php"],
        "Ruby": [".rb"],
        "Go": [".go"],
        "Rust": [".rs"],
        "Shell": [".sh"]
    },
    "Arşivler": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"],
    "Yürütülebilir Dosyalar": [".exe", ".msi", ".bat", ".sh", ".app"],
    "Disk İmajları": [".iso", ".img", ".dmg"],
    "3D Modeller": [".obj", ".stl", ".step", ".dwg", ".dxf", ".fbx", ".blend"],
    "Diğer": []  # Tanımlanamayan dosyalar buraya gidecek
}

# Başlık değiştirme
os.system('title TwiezDesk v1.0')  # Burada istediğiniz başlığı yazabilirsiniz

# ASCII art başlık
def display_banner():
    # Terminali temizle
    os.system('cls' if os.name == 'nt' else 'clear')
    
    banner = WHITE + r"""
▄▄▄█████▓ █     █░ ██▓▓█████ ▒███████▒   ▓█████▄ ▓█████   ██████  ██ ▄█▀
▓  ██▒ ▓▒▓█░ █ ░█░▓██▒▓█   ▀ ▒ ▒ ▒ ▄▀░   ▒██▀ ██▌▓█   ▀ ▒██    ▒  ██▄█▒ 
▒ ▓██░ ▒░▒█░ █ ░█ ▒██▒▒███   ░ ▒ ▄▀▒░    ░██   █▌▒███   ░ ▓██▄   ▓███▄░ 
░ ▓██▓ ░ ░█░ █ ░█ ░██░▒▓█  ▄   ▄▀▒   ░   ░▓█▄   ▌▒▓█  ▄   ▒   ██▒▓██ █▄ 
  ▒██▒ ░ ░░██▒██▓ ░██░░▒████▒▒███████▒   ░▒████▓ ░▒████▒▒██████▒▒▒██▒ █▄
  ▒ ░░   ░ ▓░▒ ▒  ░▓  ░░ ▒░ ░░▒▒ ▓░▒░▒    ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒
    ░      ▒ ░ ░   ▒ ░ ░ ░  ░░░▒ ▒ ░ ░    ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░░ ░▒ ▒░
  ░        ░   ░   ▒ ░   ░   ░ ░ ░ ░ ░    ░ ░  ░    ░   ░  ░  ░  ░ ░░ ░ 
             ░     ░     ░  ░  ░ ░          ░       ░  ░      ░  ░  ░   
                             ░            ░                              
""" + RESET
    print(banner)
    time.sleep(2)  # Kullanıcıya Loading ekranı için süre tanıma

# Masaüstünü düzenleme işlevi
def organize_desktop():
    # Masaüstündeki dosyaları al
    files = [f for f in os.listdir(DESKTOP_PATH) if os.path.isfile(os.path.join(DESKTOP_PATH, f))]
    
    for file in files:
        file_ext = os.path.splitext(file)[1].lower()
        moved = False
        
        # Kod dosyalarını özel alt klasörlere ayır
        if file_ext in [ext for sublist in CATEGORIES["Kod Dosyaları"].values() for ext in sublist]:
            for subcategory, extensions in CATEGORIES["Kod Dosyaları"].items():
                if file_ext in extensions:
                    move_file(file, os.path.join("Kod Dosyaları", subcategory))
                    moved = True
                    break
        
        # Diğer kategorileri kontrol et
        if not moved:
            for category, extensions in CATEGORIES.items():
                if isinstance(extensions, list) and file_ext in extensions:
                    move_file(file, category)
                    moved = True
                    break
        
        # Hiçbir kategoriye uymuyorsa "Diğer" klasörüne taşı
        if not moved:
            move_file(file, "Diğer")

def move_file(file, category):
    category_path = os.path.join(DESKTOP_PATH, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)
    shutil.move(os.path.join(DESKTOP_PATH, file), os.path.join(category_path, file))
    print(WHITE + f"{file} -> {category}/" + RESET)

# Menü
def menu():
    while True:
        print(WHITE + "\n[ + ] github.com/twiez")
        print(WHITE + "\n[ 1 ] Masaüstünü Düzenle")
        print("[ 2 ] Çıkış")
        choice = input("\nSeçiminizi yapın: ")

        if choice == "1":
            organize_desktop()
            print("\nMasaüstü düzenleme işlemi tamamlandı!")
        elif choice == "2":
            print("Programdan çıkılıyor. Hoşça kal!")
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

# Program başlangıcı
if __name__ == "__main__":
    display_banner()  # Banner'ı ekrana bas
    menu()
