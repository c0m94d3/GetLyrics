from p import *
import requests
base_url = 'https://api.lyrics.ovh/v1/'
BLUE = '\u001b[34;1m'
YEllow = '\u001b[33;1m'
BWhite = '\u001b[37;1m'
ENDC = '\033[m'
MAgenta = '\u001b[35;1m'
header = {'header':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:66.0) Gecko/20100101 Firefox/66.0'}
def get_lyric():
	print(BLUE + logo + ENDC)
	print(YEllow + "Welcome to GetLyric program".center(80,'_'))
	print("\nThis program can print lyrics for any song\n" + ENDC)
	track = str(input(MAgenta + "Enter the name of song\n--->>> "))
	artist = str(input('\nOK, Now Enter the name of the Artist\n--->>> '))
	resp = requests.get(base_url+artist+'/'+track)
	print(BWhite + '\n')
	resp_json = resp.json()
	return resp_json['lyrics'];
print(get_lyric())
