## Introduction

This is a simple program i created to download any videos from YouTube. You can use this program for any purpose.

## How To Use It?
**ATTENTION!**
<br>
>You must install [`python 3.x`](https://www.python.org) or this program will not work.

Follow this step to run and use this program

1. Clone this repository
```sh
git clone https://github.com/Arkan237/youtube-downloader-cli
```
2. Copy command on below then paste it on terminal or CMD to run it
<details>
<summary>Linux</summary>

   ```sh
   cd youtube-downloader-cli &&
   chmod 755 yt-downloader.sh &&
   ./yt-downloader.sh
   ```
</details>
<details>
  <summary>Windows</summary>
   
  ```sh
  cd youtube-downloader-cli &&
  python .main.py
  ```
</details>
<details>
  <summary>Mac OS</summary>
   
  ```sh
  cd youtube-downloader-cli &&
  python3 .main.py
  ```
</details>

3. Choose Language
> For now, there are only 2 languages are available (English and Indonesian). You can add other languages by editing the `.main.py` file

4. Enter the link of the video you want to download
5. Select `download highest resolution` or `custom resolution` (by typing y or n)
>I recommend you to choose `download highest resolution` because to download custom resolution will be a bit difficult.

<details>
   <summary>How To Choose Custom Resolution</summary>
   <br>
   When you choose to download a custom resolution, a list of downloadable resolutions will appear. But it's a bit difficult to read the list. To select a     resolution, enter the itag based on the resolution you want to download.
   
   <br>
   
   >If you're a Linux user, I recommend you to use the `find` feature to make it easier for you to search for itag based on the resolution you choose.
   
   <br>
   
   <p align="center"><a href="find-feature-in-konsole-terminal"><img src="https://i.imgur.com/i5Kt0yn.png" alt="find-feature"/></a></p>
   
   <br>
   
   For example I want to download video from YouTube. I choose custom resolution because I want to download 720p60 resolution. There are 4 option for 720p resolution (720p 30 fps video format = mp4, 720p 30 fps video format = webm, 720p 60 fps video format = mp4, 720p 60 fps video format = webm). I want to download 720p 60 fps and the video format is mp4. Itag for 720p 60 fps video format = mp4 is 398. So i type 398 in terminal then i press enter to start download.
   
</details>

6. The video will start downloading. Wait until the video is finished to download.
