import random
import time
import sys
import os

traits = [
    # --- TỘC (Origins) ---
    "Noxus",
    "Demacia",
    "Zaun",
    "Hư không",
    "Bilgewater",
    "Đảo bóng đêm",
    "Ionia",
    "Ixtal",
    "Piltower",
    "Darkin",
    "Freljord",
    "Shurima",
    "Yordle",
    "Targon",
    
    # --- HỆ (Classes) ---
    "Pháp sư",
    "Đấu sĩ",
    "Vệ quân",
    "Xạ thủ",
    "Thuật sư",
    "Đồ tể",
    "Nhiễu loạn",
    "Dũng sĩ",
    "Cực tốc",
    "Chinh phạt",
    "Viễn kích",
    "Cảnh vệ"
    ]

def clear_screen():
    # Lệnh xóa màn hình cho sạch
    os.system('cls' if os.name == 'nt' else 'clear')

def spin_trait():
    clear_screen()
    print("\n" + "="*40)
    print(" Đang xoay tộc/hệ định mệnh...")
    print("="*40)

    # Hiệu ứng chạy chữ
    for i in range(15):
        sys.stdout.write(f"\r {random.choice(traits)}               ")
        sys.stdout.flush()
        time.sleep(0.08)

    sys.stdout.write("\r" + " "*50 + "\r")
    
    final_trait = random.choice(traits)
    print(f"\n\n    KẾT QUẢ: {final_trait.upper()}  ")
    print("="*40)

if __name__ == "__main__":
    while True:
        spin_trait()
        key = input("\n[Enter] Quay lại | [Q] Nghỉ game: ")
        if key.lower() == 'q':
            break