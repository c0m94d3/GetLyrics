from p import *
import requests
import os
import timeit
base_url = 'https://api.lyrics.ovh/v1/'
BLUE = '\u001b[34;1m'
YEllow = '\u001b[33;1m'
BWhite = '\u001b[37;1m'
ENDC = '\033[m'
MAgenta = '\u001b[35;1m'
Red = '\u001b[31;1m'
success = '\u001b[32m'
header = {'header':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:66.0) Gecko/20100101 Firefox/66.0'}
def get_lyric():
	print(BLUE + logo + ENDC)
	print(YEllow + "Welcome to GetLyric program".center(80,'_'))
	print("\nThis program can print lyrics for any song\n" + ENDC)
	track = str(input(MAgenta + "Enter the name of song\n--->>> " + ENDC))
	artist = str(input(MAgenta + '\nOK, Now Enter the name of the Artist\n--->>> ' + ENDC))
	resp = requests.get(base_url+artist+'/'+track)
	print(BWhite + '\n')
	resp_json = resp.json()
	if resp_json['lyrics'] == '':
		return Red + '[!]Lyrics not found :(\n[!]This doesn\'t happen often' + ENDC
	else:
		print(success + "Lyrics found\n")
		save_file = input("Do you want to save it to a file? [y/N]  ")
		print("\n\n")
		if save_file == 'y':
			filename = str('lyrics_' + track + '.txt')
			fi = open(filename, "w")
			fi.write(resp_json['lyrics'])
			fi.close()
			print("Saved to file \'{0}\' in the directory \'{1}\'\n\n".format(filename, os.getcwd()))
	return resp_json['lyrics']
print(get_lyric())
