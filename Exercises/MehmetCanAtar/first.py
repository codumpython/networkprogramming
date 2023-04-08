from optparse import OptionParser
import socket
import sys

parser = OptionParser()
parser.add_option("-i", "--ipadres", dest="ipadres", help="ip adresini giriniz.")
parser.add_option("-p", "--port", dest="port", help="port numarasini giriniz.")

(ui, arguments) = parser.parse_args()

ipadresi = ui.ipadres
port = int(ui.port)

try: 
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # tuple tipinde data alma
    socket.connect((ip_adresi, port))
    mesaj = input("iletilecek mesajinizi giriniz :")
    socket.send(mesaj.encode(encoding="UTF-8"))

except KeyboardInterrupt:
    print("ctrl + c basildi")
    sys.exit()

except Exception as E:
    print(E)
    sys.exit()    