# Youtube Downloader Program

try:
    from pytube import YouTube
except ImportError:
    import os
    if os.name == 'nt':
        os.system('pip install pytube')
        os.system('cls')
    else:
        os.system('pip3 install pytube')
        os.system('clear')
    from pytube import YouTube

# English
def en():
    # Watermark
    print('-'*20)
    print('Youtube Downloader Program')
    print('This Program Was Created Using Python3')
    print('Created By Arkan')
    print('Github : Arkan237')
    print('-'*20)
    # Link Input
    while True:
        try:
            link = input('Enter the link : ')
            yt = YouTube(link)
            break
        except:
            print('Video not found. Try another video')
    # Video Information
    print('-'*5,'Video Information','-'*5)
    # Title Of Video
    print('Title :',yt.title)
    # Number Of Views Of The Video
    print('Views :',yt.views)
    print('Duration :',yt.length,'seconds')
    # Rating
    print('Ratings :',yt.rating)
    # Highest Resolution Or Custom Resolution
    res = input('Do you want to download highest resolution (Y/N)? ')
    if res == 'y' or res == 'Y':
        ys = yt.streams.get_highest_resolution()
    else:
        print(yt.streams)
        sel = input('Choose one (insert the itag) : ')
        ys = yt.streams.get_by_itag(sel)
    # Starting download
    print("Downloading...")
    ys.download()
    print("Download completed!!")

# Indonesian
def idn():
    # Watermark
    print('-'*20)
    print('Youtube Downloader Program')
    print('Program Ini Dibuat Menggunakan Python3')
    print('Dibuat Oleh Arkan')
    print('Github : Arkan237')
    print('-'*20)
    # Link Input
    while True:
        try:
            link = input('Masukan link : ')
            yt = YouTube(link)
            break
        except:
            print('Video tidak ditemukan. Coba video lain')
    # Informasi Video
    print('-'*5,'Informasi Video','-'*5)
    # Judul Video
    print('Judul :',yt.title)
    # Jumlah Views Video
    print('Views :',yt.views)
    print('Durasi :',yt.length,'detik')
    # Rating
    print('Ratings :',yt.rating)
    # Resolusi Tertinggi Atau Resolusi Khusus
    res = input('Apakah kamu mau mendownload resolusi tertinggi (Y/N)? ')
    if res == 'y' or res == 'Y':
        ys = yt.streams.get_highest_resolution()
    else:
        print(yt.streams)
        sel = input('Pilih salah satu (masukan itag) : ')
        ys = yt.streams.get_by_itag(sel)
    # Memulai download
    print("Mendownload...")
    ys.download()
    print("Download selesai!!")

print('Choose Language/Pilih Bahasa')
print('1. English\n2. Indonesia')
setlang = input('')
if setlang == '1':
    en()
elif setlang == '2':
    idn()
else:
    exit()