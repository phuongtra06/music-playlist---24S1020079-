songs = []

def main():
    while True:
        print("\n--- MUSIC PLAYLIST MANAGER ---")
        print("1. Thêm bài hát")
        print("2. Xem danh sách phát")
        print("3. Tìm bài hát theo ca sĩ")
        print("4. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
def add_song():
    title = input("Nhập tên bài hát: ")
    artist = input("Nhập tên ca sĩ: ")
    duration = int(input("Nhập thời lượng (giây): "))

    song = {
        'title': title,
        'artist': artist,
        'duration': duration
    }
    songs.append(song)
    print("Đã thêm bài hát vào playlist.")    