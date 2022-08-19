# Scraping website
from sys import platform
import time, os, sys, threading, itertools

sys.setrecursionlimit(5000)
sys.getrecursionlimit()

Cyan='\033[0;36m'
reset='\033[0m'

os.system("clear||cls")

done = False

def animate():
    print(Cyan + " ")
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rMohon Menunggu, Sedang mengecek versi Python ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
        if not sys.version_info.major==3 and sys.version_info.minor >= 6:
            print("Harap gunakan python versi 3.6 keatas")
            os.system("xdg-open xdg-open https://python.org/download")
            sys.exit(1)
        sys.stdout.write('\rSelesai, Silahkan Pilih Menu')
    os.system("clear||cls")
    print(reset + " ")

t=threading.Thread(target=animate)
t.start()
time.sleep(5)
done = True

try:
    import requests
    from bs4 import BeautifulSoup
    from html2image import Html2Image
except (ImportError, ModuleNotFoundError):
    if platform == "linux" or platform == "linux2":
        os.system('pip3 install requests beautifulsoup4 html2image')
    elif platform == "darwin":
        os.system('pip install requests beautifulsoup4 html2image')
    elif platform == "win32":
        os.system('pip install requests beautifulsoup4 html2image')
    else:
        print("Unknown platform")
        exit(1)

user = os.getlogin()

try:
    file = open("url.txt", "r", encoding="utf-8")
    file2 = file.readlines()
except (FileNotFoundError):
    try:
        url = "https://cekgangguan.id/"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        for tbody in soup.find_all('tbody'):
            for index, tr in enumerate(tbody.find_all('tr'),1):
                file = open('url.txt','a')
                print("{}".format(tr.find('a').get('href')),end="\n", file=file)
    except (ConnectionError):
        print("nyalakan Koneksi Internet")
        exit(1)


__author__ = "Xnuvers007"
__version__ = "1.0"
__copyright__ = "Copyright (c) 2022 Xnuvers007 and CekGangguan.\nAll Rights Reserved."
__license__ = "MIT"

localtime = time.asctime(time.localtime(time.time()))

hti = Html2Image(output_path='Gambar')

def menu():
    print("Selamat datang {}".format(user))
    print("Created by Xnuvers007\nInstagram: @indradwi.25")
    print("Author : {}".format(__author__))
    print("Copyright : {}".format(__copyright__))
    print("Version: {}".format(__version__))
    print("Dicari sejak : {}".format(localtime))
    print("==========================================================")
    url = "https://cekgangguan.id/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    print(soup.find('h1', class_='mt-3 mb-3').text)
    print("==========================================================")
    for scope in soup.find_all('th', {'scope': 'col'}):
        for i in range(len(scope.text)):
            print(scope.text[i], end="")
            time.sleep(0.05)
        print(end="\t\t")
    print("\n")
    for tbody in soup.find_all('tbody'):
        for index, tr in enumerate(tbody.find_all('tr'),1):
            print("{}. {}".format(index, tr.text),end="\n")
            # print("{}".format(tr.find('a').get('href')),end="\n")
            # for td in tr.find_all('td'):
            #     print(td.text, end="  |  ")
            # print(end="\n")
    #     for tr in tbody.find_all('tr'):
    #         print("\t")
            # for td in tr.find_all('td'):
            #    print(td.text, end="\t     | ")
            #     # for i in range(len(td.text)):
            #     #     print(td.text[i], end="")
            #     # print("\n")
#            file = open('url.txt','a')
#            print("{}".format(tr.find('a').get('href')),end="\n", file=file)
                
def pilih():
    pilihan = int(input("Masukan Pilihan : "))
    print("\n")
    print("====="*4)
    if(pilihan==1):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        #hti.screenshot(url="https://cekgangguan.id/agea",save_as=tanya)
        hti.screenshot(url=file2[0].rstrip(), save_as=tanya)
        try:
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==2):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        #hti.screenshot(url="https://cekgangguan.id/airasia",save_as=tanya)
        hti.screenshot(url=file2[1].rstrip(), save_as=tanya)
        try:
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==3):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        #hti.screenshot(url="https://cekgangguan.id/akulaku",save_as=tanya)
        hti.screenshot(url=file2[2].rstrip(), save_as=tanya)
        try:
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==4):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        #hti.screenshot(url="https://cekgangguan.id/alodokter",save_as=tanya)
        hti.screenshot(url=file2[3].rstrip(), save_as=tanya)
        try:
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==5):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        #hti.screenshot(url="https://cekgangguan.id/antv",save_as=tanya)
        hti.screenshot(url=file2[4].rstrip(), save_as=tanya)
        try:
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==6):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        #hti.screenshot(url="https://cekgangguan.id/apkpure",save_as=tanya)
        hti.screenshot(url=file2[5].rstrip(), save_as=tanya)
        try:
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==7):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        #hti.screenshot(url="https://cekgangguan.id/app-world",save_as=tanya)
        hti.screenshot(url=file2[6].rstrip(), save_as=tanya)
        try:
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==8):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        #hti.screenshot(url="https://cekgangguan.id/astinet",save_as=tanya)
        hti.screenshot(url=file2[7].rstrip(), save_as=tanya)
        try:
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==9):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        #hti.screenshot(url="https://cekgangguan.id/atm-amar-bank",save_as=tanya)
        hti.screenshot(url=file2[8].rstrip(), save_as=tanya)
        try:
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==10):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        #hti.screenshot(url="https://cekgangguan.id/atm-anz",save_as=tanya)
        #print(file2[9].rstrip())
        hti.screenshot(url=file2[9].rstrip(), save_as=tanya)
        try:
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==11):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[10].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==12):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[11].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==13):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[12].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==14):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[13].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==15):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[14].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==16):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[15].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==17):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[16].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==18):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[17].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==19):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[18].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==20):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[19].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==21):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[20].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==22):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[21].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==23):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[22].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==24):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[23].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==25):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[24].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==26):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[25].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==27):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[26].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==28):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[27].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==29):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[28].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==30):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[29].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==31):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[30].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==32):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[31].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==33):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[32].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==34):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[33].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==35):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[34].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==36):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[35].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==37):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[36].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==38):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[37].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==39):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[38].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==40):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[39].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==41):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[40].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==42):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[41].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==43):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[42].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==44):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[43].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==45):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[44].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==46):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[45].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==47):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[46].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==48):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[47].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==49):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[48].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==50):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[49].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==51):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[50].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==52):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[51].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==53):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[52].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==54):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[53].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==55):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[54].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==56):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[55].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==57):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[56].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==58):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[57].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==59):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[58].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==60):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[59].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==61):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[60].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==62):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[61].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==63):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[62].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==64):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[63].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==65):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[64].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==66):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[65].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==67):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[66].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==68):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[67].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==69):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[68].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==70):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[69].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==71):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[70].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==72):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[71].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==73):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[72].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==74):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[73].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==75):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[74].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==76):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[75].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==77):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[76].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==78):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[77].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==79):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[78].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==80):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[79].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==81):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[80].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==82):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[81].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==83):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[82].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==84):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[83].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==85):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[84].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==86):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[85].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==87):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[86].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==88):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[87].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==89):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[88].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==90):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[89].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==91):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[90].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==92):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[91].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==93):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[92].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==94):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[93].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==95):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[94].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==96):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[95].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==97):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[96].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==98):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[97].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==99):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[98].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==100):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[99].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==101):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[100].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==102):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[101].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==103):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[102].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==104):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[103].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==105):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[104].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==106):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[105].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==107):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[106].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==108):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[107].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==109):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[108].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==110):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[109].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==111):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[110].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==112):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[111].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==113):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[112].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==114):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[113].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==115):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[114].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==116):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[115].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==117):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[116].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==118):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[117].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==119):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[118].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==120):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[119].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==121):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[120].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==122):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[121].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==123):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[122].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==124):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[123].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==125):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[124].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==126):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[125].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==127):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[126].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==128):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[127].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==129):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[128].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==130):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[129].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==131):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[130].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==132):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[131].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==133):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[132].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==134):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[133].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==135):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[134].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==136):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[135].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==137):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[136].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==138):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[137].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==139):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[138].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==140):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[139].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==141):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[140].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==142):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[141].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==143):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[142].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==144):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[143].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==145):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[144].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==146):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[145].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==147):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[146].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==148):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[147].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==149):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[148].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==150):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[149].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==151):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[150].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==152):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[151].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==153):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[152].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==154):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[153].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==155):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[154].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==156):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[155].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==157):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[156].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==158):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[157].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==159):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[158].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==160):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[159].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==161):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[160].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==162):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[161].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==163):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[162].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==164):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[163].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==165):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[164].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==166):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[165].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==167):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[166].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==168):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[167].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==169):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[168].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==170):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[169].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==171):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[170].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==172):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[171].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==173):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[172].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==174):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[173].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==175):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[174].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==176):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[175].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==177):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[176].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==178):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[177].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==179):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[178].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==180):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[179].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==181):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[180].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==182):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[181].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==183):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[182].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==184):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[183].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==185):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[184].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==186):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[185].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==187):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[186].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==188):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[187].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==189):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[188].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==190):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[189].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==191):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[190].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==192):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[191].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==193):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[192].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==194):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[193].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==195):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[194].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==196):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[195].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==197):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[196].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==198):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[197].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==199):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[198].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==200):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[199].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==201):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[200].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==202):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[201].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==203):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[202].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==204):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[203].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==205):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[204].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==206):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[205].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==207):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[206].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==208):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[207].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==209):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[208].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==210):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[209].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==211):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[210].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==212):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[211].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==213):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[212].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==214):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[213].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==215):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[214].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==216):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[215].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==217):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[216].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==218):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[217].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==219):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[218].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==220):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[219].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==221):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[220].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==222):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[221].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==223):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[222].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==224):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[223].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==225):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[224].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==226):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[225].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==227):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[226].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==228):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[227].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==229):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[228].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==230):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[229].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==231):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[230].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==232):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[231].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==233):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[232].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==234):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[233].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==235):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[234].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==236):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[235].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==237):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[236].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==238):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[237].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==239):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[238].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==240):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[239].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==241):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[240].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==242):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[241].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==243):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[242].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==244):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[243].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==245):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[244].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==246):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[245].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==247):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[246].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==248):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[247].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==249):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[248].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==250):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[249].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==251):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[250].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==252):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[251].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==253):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[252].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==254):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[253].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==255):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[254].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==256):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[255].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==257):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[256].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==258):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[257].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==259):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[258].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==260):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[259].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==261):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[260].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==262):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[261].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==263):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[262].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==264):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[263].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==265):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[264].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==266):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[265].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==267):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[266].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==268):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[267].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==269):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[268].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==270):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[269].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==271):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[270].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==272):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[271].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==273):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[272].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==274):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[273].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==275):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[274].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==276):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[275].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==277):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[276].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==278):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[277].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==279):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[278].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==280):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[279].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==281):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[280].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==282):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[281].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==283):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[282].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==284):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[283].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==285):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[284].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==286):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[285].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==287):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[286].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==288):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[287].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==289):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[288].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==290):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[289].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==291):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[290].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==292):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[291].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==293):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[292].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==294):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[293].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==295):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[294].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==296):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[295].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==297):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[296].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==298):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[297].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==299):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[298].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==300):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[299].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==301):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[300].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==302):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[301].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==303):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[302].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==304):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[303].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==305):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[304].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==306):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[305].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==307):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[306].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==308):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[307].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==309):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[308].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==310):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[309].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==311):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[310].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==312):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[311].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==313):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[312].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==314):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[313].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==315):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[314].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==316):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[315].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==317):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[316].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==318):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[317].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==319):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[318].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==320):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[319].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==321):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[320].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==322):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[321].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==323):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[322].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==324):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[323].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==325):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[324].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==326):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[325].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==327):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[326].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==328):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[327].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==329):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[328].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==330):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[329].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==331):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[330].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==332):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[331].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==333):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[332].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==334):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[333].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==335):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[334].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==336):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[335].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==337):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[336].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==338):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[337].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==339):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[338].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==340):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[339].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==341):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[340].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==342):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[341].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==343):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[342].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==344):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[343].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==345):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[344].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==346):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[345].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==347):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[346].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==348):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[347].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==349):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[348].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==350):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[349].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==351):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[350].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==352):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[351].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==353):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[352].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==354):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[353].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==355):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[354].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==356):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[355].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==357):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[356].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==358):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[357].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==359):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[358].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==360):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[359].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==361):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[360].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==362):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[361].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==363):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[362].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==364):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[363].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==365):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[364].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==366):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[365].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==367):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[366].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==368):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[367].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==369):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[368].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==370):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[369].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==371):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[370].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==372):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[371].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==373):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[372].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==374):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[373].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==375):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[374].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==376):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[375].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==377):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[376].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==378):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[377].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==379):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[378].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==380):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[379].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==381):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[380].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==382):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[381].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==383):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[382].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==384):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[383].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==385):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[384].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==386):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[385].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==387):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[386].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==388):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[387].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==389):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[388].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==390):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[389].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==391):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[390].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==392):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[391].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==393):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[392].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==394):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[393].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==395):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[394].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==396):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[395].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==397):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[396].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==398):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[397].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==399):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[398].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==400):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[399].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==401):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[400].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==402):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[401].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==403):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[402].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==404):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[403].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==405):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[404].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==406):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[405].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==407):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[406].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==408):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[407].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==409):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[408].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==410):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[409].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==411):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[410].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==412):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[411].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==413):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[412].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==414):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[413].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==415):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[414].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==416):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[415].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==417):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[416].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==418):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[417].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==419):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[418].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==420):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[419].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==421):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[420].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==422):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[421].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==423):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[422].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==424):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[423].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==425):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[424].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==426):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[425].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==427):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[426].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==428):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[427].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==429):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[428].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==430):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[429].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==431):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[430].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==432):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[431].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==433):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[432].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==434):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[433].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==435):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[434].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==436):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[435].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==437):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[436].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==438):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[437].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==439):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[438].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==440):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[439].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==441):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[440].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==442):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[441].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==443):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[442].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==444):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[443].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==445):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[444].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==446):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[445].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==447):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[446].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==448):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[447].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==449):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[448].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==450):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[449].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==451):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[450].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==452):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[451].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==453):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[452].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==454):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[453].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==455):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[454].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==456):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[455].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==457):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[456].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==458):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[457].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==459):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[458].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==460):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[459].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==461):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[460].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==462):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[461].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==463):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[462].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==464):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[463].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==465):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[464].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==466):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[465].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==467):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[466].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==468):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[467].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==469):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[468].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==470):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[469].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==471):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[470].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==472):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[471].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==473):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[472].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==474):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[473].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==475):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[474].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==476):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[475].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==477):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[476].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==478):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[477].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==479):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[478].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==480):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[479].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==481):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[480].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==482):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[481].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==483):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[482].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==484):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[483].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")
    elif(pilihan==485):
        print("Masukan Nama File seperti = gambar.png atau gambar.jpg")
        print("Gunakan Akhiran png/jpg\n")
        tanya = str(input("Masukan Nama File : "))
        print("\n")
        hti.screenshot(url=file2[484].rstrip(), save_as=tanya)
        try:
            print("\n")
            print("ukuran file tersebut ", os.stat('Gambar/{}'.format(tanya)).st_size, "byte")
        except (FileNotFoundError):
            pass
        print("Sudah tersimpan pada folder Gambar")        

    else:
        print("Tidak ada pilihan")

file.close()

try:
    menu()
    pilih()

except (ConnectionError):
    print("Periksa Internet Nyala atau belum")
    exit(code=None)
