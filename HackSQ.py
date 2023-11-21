# pip install colorama
# pip install mcstatus
# pip install re
# pip install requests

import mcstatus
import minecraft
import json
import random
import requests
import os
import re
import __future__
import requests.exceptions
import time
import socket

from urllib.error import URLError
from urllib.parse import urlsplit
import urllib.request
from urllib.request import urlopen
from colorama import *
from mcstatus import *
from minecraft.networking.connection import Connection
from minecraft.networking.packets import Packet, clientbound, serverbound
from minecraft.compat import input

init()


os.system("cls")


def info_update(message):
    print(f' {message}\r', end='')


def help():
	print (f"""
    {Fore.WHITE}╔══════════════════════════════════╗
    {Fore.WHITE}║ {Fore.MAGENTA}help      {Fore.WHITE}- {Fore.MAGENTA}Show this menu.      {Fore.WHITE}║
    {Fore.WHITE}║ {Fore.MAGENTA}scanning  {Fore.WHITE}- {Fore.MAGENTA}Show scanning menu.  {Fore.WHITE}║
    {Fore.WHITE}║ {Fore.MAGENTA}minecraft {Fore.WHITE}- {Fore.MAGENTA}Show Minecraft menu. {Fore.WHITE}║
    {Fore.WHITE}║ {Fore.MAGENTA}ipt       {Fore.WHITE}- {Fore.MAGENTA}Show IP tools menu.  {Fore.WHITE}║
    {Fore.WHITE}║ {Fore.MAGENTA}clear     {Fore.WHITE}- {Fore.MAGENTA}Clear the screen.    {Fore.WHITE}║
    {Fore.WHITE}╚══════════════════════════════════╝
		""")
def minecraft():
	print (f"""
    {Fore.WHITE}╔════════════════════════════════════════════════════════════════════════════╗
    {Fore.WHITE}║ {Fore.MAGENTA}connect [ip] [port] [nick] {Fore.WHITE}- {Fore.MAGENTA}Connect to a Minecraft server (Offline Mode). {Fore.WHITE}║
    {Fore.WHITE}║ {Fore.MAGENTA}server [ip]                {Fore.WHITE}- {Fore.MAGENTA}Lookup Minecraft servers.                     {Fore.WHITE}║
    {Fore.WHITE}║ {Fore.MAGENTA}player [nick/uuid]         {Fore.WHITE}- {Fore.MAGENTA}Lookup Minecraft players.                     {Fore.WHITE}║
    {Fore.WHITE}╚════════════════════════════════════════════════════════════════════════════╝
		""")

def scanning():
	print (f"""
    {Fore.WHITE}╔══════════════════════════════════════╗
    {Fore.WHITE}║ {Fore.MAGENTA}subds [domain] {Fore.WHITE}- {Fore.MAGENTA}Subdomains scanner. {Fore.WHITE}║
    {Fore.WHITE}╚══════════════════════════════════════╝
		""")

def ipt():
	print (f"""
    {Fore.WHITE}╔═══════════════════════════════════════════════════════════════════════════╗
    {Fore.WHITE}║ {Fore.MAGENTA}locate [ip]                     {Fore.WHITE}- {Fore.MAGENTA}Geolocate IPv4.                         {Fore.WHITE}║
    {Fore.WHITE}║ {Fore.MAGENTA}dbs [nick]                      {Fore.WHITE}- {Fore.MAGENTA}Find Minecraft players IP. (230K IP DB) {Fore.WHITE}║
    {Fore.WHITE}║ {Fore.MAGENTA}dbs-c [nick] [path to db]       {Fore.WHITE}- {Fore.MAGENTA}Find Minecraft players IP. (Custom DB)  {Fore.WHITE}║
    {Fore.WHITE}║ {Fore.MAGENTA}scrape-p [http/sock4/sock5/all] {Fore.WHITE}- {Fore.MAGENTA}Scrape Proxies.                         {Fore.WHITE}║
    {Fore.WHITE}╚═══════════════════════════════════════════════════════════════════════════╝
		""")

def banner():
	os.system("title ♥ HackSQ Private Tool ♥")

	print (f"""{Style.NORMAL}
    {Fore.WHITE} 
    {Fore.WHITE}----------------------------------------------------{Fore.CYAN}

     ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀  ██████   █████  
    ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▒██    ▒ ▒██▓  ██▒
    ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ░ ▓██▄   ▒██▒  ██░
    ░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄   ▒   ██▒░██  █▀ ░
    ░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄▒██████▒▒░▒███▒█▄ 
     ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ 
     ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░░ ░▒  ░ ░ ░ ▒░  ░ 
     ░  ░░ ░  ░   ▒   ░        ░ ░░ ░ ░  ░  ░     ░   ░ 
     ░  ░  ░      ░  ░░ ░      ░  ░         ░      ░    
                  ░                                 
    {Fore.WHITE}╔══════════════════════════════════════════════════╗
    {Fore.WHITE}║ {Fore.MAGENTA}Telegram {Fore.WHITE}- {Fore.MAGENTA}t.me/squadhackers                     {Fore.WHITE}║
    {Fore.WHITE}║ {Fore.MAGENTA}Discord  {Fore.WHITE}- {Fore.MAGENTA}discord.gg/2gvrG8c                    {Fore.WHITE}║
    {Fore.WHITE}║ {Fore.MAGENTA}Author   {Fore.WHITE}- {Fore.MAGENTA}iTsToastZ (iTsToastZ#2870)            {Fore.WHITE}║
    {Fore.WHITE}╚══════════════════════════════════════════════════╝

    		""")
banner()
while True:
	print (f" {Fore.WHITE}╔═[{Fore.MAGENTA}root{Fore.WHITE}@{Fore.MAGENTA}HackSQ{Fore.WHITE}]{Fore.MAGENTA}-{Fore.WHITE}[{Fore.MAGENTA}-{Fore.WHITE}]")
	print (f" {Fore.WHITE}╚══════════ $ ", end='')
	x = input().split()
	try:
		cmd = x[0].lower()
		if cmd == "help":
			help()
		elif cmd == "scrape-p":
			try:
				type = x[1].lower()

				if type == "http":
					try:
						file = open("proxies.txt", "a+")
						res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
						proxies = []
						for proxy in res.text.split('\n'):
							proxy = proxy.strip()
							if proxy:
								proxies.append(proxy)
						for p in proxies:
							file.write((p)+"\n")
						print ()
						print(f' Scraped {len(proxies)} proxies @ proxies.txt !')
						print ()
					except Exception as e:
						print(f" An error occurred while downloading proxies from ProxyScrape.com: {e}")
				elif type == "sock5":
					try:
						file = open("proxies.txt", "a+")
						res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
						proxies = []
						for proxy in res.text.split('\n'):
							proxy = proxy.strip()
							if proxy:
								proxies.append(proxy)
						for p in proxies:
							file.write((p)+"\n")
						print ()
						print(f' Scraped {len(proxies)} proxies @ proxies.txt !')
						print ()
					except Exception as e:
						print(f" An error occurred while downloading proxies from ProxyScrape.com: {e}")
				elif type == "sock4":
					try:
						file = open("proxies.txt", "a+")
						res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
						proxies = []
						for proxy in res.text.split('\n'):
							proxy = proxy.strip()
							if proxy:
								proxies.append(proxy)
						for p in proxies:
							file.write((p)+"\n")
						print ()
						print(f' Scraped {len(proxies)} proxies @ proxies.txt !')
						print ()
					except Exception as e:
						print(f" An error occurred while downloading proxies from ProxyScrape.com: {e}")
				elif type == "all":
					try:
						file = open("proxies.txt", "a+")
						res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=all&timeout=1500')
						proxies = []
						for proxy in res.text.split('\n'):
							proxy = proxy.strip()
							if proxy:
								proxies.append(proxy)
						for p in proxies:
							file.write((p)+"\n")
						print ()
						print(f' Scraped {len(proxies)} proxies @ proxies.txt !')
						print ()

					except Exception as e:
						print(f" An error occurred while downloading proxies from ProxyScrape.com: {e}")
					file.close()
				else:
					print ()
					print (f"""
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╔════════════════════════════════════════╗
    {Fore.WHITE}║ {Fore.MAGENTA}Usage: scrape-p [http/sock4/sock5/all].{Fore.WHITE}║
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╚════════════════════════════════════════╝
						""")											
			except:
				print ()
				print (f"""
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╔════════════════════════════════════════╗
    {Fore.WHITE}║ {Fore.MAGENTA}Usage: scrape-p [http/sock4/sock5/all].{Fore.WHITE}║
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╚════════════════════════════════════════╝
					""")				
		elif cmd == "minecraft":
			minecraft()
		elif cmd == "scanning":
			scanning()
		elif cmd == "ipt":
			ipt()
		elif cmd == "subds":
			try:
				target = x[1]
				f = open("subdomains.txt")
				print ()
				lines = f.readlines()
				lines = [x.strip() for x in lines]
				for line in lines:
					try:
						final = (line)+"."+(target)
						ip = socket.gethostbyname(final)
						try:
							server = MinecraftServer.lookup(ip)
							status = server.status()
							if "104." in ip:
								print (f"{Fore.WHITE} IP: "+(ip)+f" {Fore.MAGENTA}= {Fore.WHITE}"+(final)+" ("+str(status.version.name)+") ("+str(status.players.online)+"/"+str(status.players.max)+") (Cloufare)")
							else:
								print (f"{Fore.WHITE} IP: "+(ip)+f" {Fore.MAGENTA}= {Fore.WHITE}"+(final)+" ("+str(status.version.name)+") ("+str(status.players.online)+"/"+str(status.players.max)+")")
						except:
							if "104." in ip:
								print (f"{Fore.WHITE} IP: "+(ip)+f" {Fore.MAGENTA}= {Fore.WHITE}"+(final)+" (No Minecraft Detected) (Cloudfare)")
							else:
								print (f"{Fore.WHITE} IP: "+(ip)+f" {Fore.MAGENTA}= {Fore.WHITE}"+(final)+" (No Minecraft Detected)")

					except:
						pass
				print()
			except:
				print ()
				print (f"""
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╔═══════════════════════╗
    {Fore.WHITE}║ {Fore.MAGENTA}Usage: subds [domain].{Fore.WHITE}║
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╚═══════════════════════╝
					""")				

		elif cmd == "dbs-c":
			try:
				target = x[1]
				path = x[2]
				print ()
				time.sleep(2)
				try:

					with open(path) as f:

						lines = f.readlines()
						lines = [x.strip() for x in lines]
						print (" Searching, Please Wait...")
						print ()
						for line in lines:
							if target in line:
								print (" Found: "+(line))
				except:
					print ()
					print (f"""
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╔═══════════════════════════════╗
    {Fore.WHITE}║ {Fore.MAGENTA}Usage: Incorrect path to db.  {Fore.WHITE}║
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╚═══════════════════════════════╝
					""")
				print ()
			except:
				print ()
				print (f"""
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╔═══════════════════════════════════════════════════════╗
    {Fore.WHITE}║ {Fore.MAGENTA}Usage: dbs-c [nick/uuid] [path to db].                {Fore.WHITE}║
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╚═══════════════════════════════════════════════════════╝
					""")
		elif cmd == "dbs":
			try:
				target = x[1]
				print ()
				print (" Searching, Please Wait...")
				print ()
				time.sleep(2)
				try:
					with open("database.txt") as f:
						lines = f.readlines()
						lines = [x.strip() for x in lines]
						for line in lines:
							if target in line:
								print (" Found: "+(line))
				except:
					pass


				print ()
			except Exception as e:
				print ()
				print (f"""
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╔═══════════════════════════════════╗
    {Fore.WHITE}║ {Fore.MAGENTA}Usage: dbs [nick/uuid].           {Fore.WHITE}║
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╚═══════════════════════════════════╝
					""")


		elif cmd == "connect":
			try:
				server = x[1]
				port = x[2]
				nick = x[3]
				connection = Connection(server, int(port), username=nick)
				def handle_join_game(join_game_packet):
					print(" Connected !")
					print ()
					connection.register_packet_listener(handle_join_game, clientbound.play.JoinGamePacket)
				def print_chat(chat_packet):
					json_data = chat_packet.json_data
					print(f"{Fore.MAGENTA} DATA >> {Fore.WHITE}"+str(chat_packet.json_data)+f"{Fore.MAGENTA} / Position >> {Fore.CYAN}"+str(chat_packet.position))
				connection.connect()
				while True:
					# NICK TO OP
					print ()
					print (f" {Fore.WHITE}╔═[{Fore.MAGENTA}root{Fore.WHITE}@{Fore.MAGENTA}HackSQ{Fore.WHITE}]{Fore.MAGENTA}-{Fore.WHITE}[{Fore.MAGENTA}Set the command to execute{Fore.WHITE}]")
					print (f" {Fore.WHITE}╚══════════ $ ", end='')

					text = input()
					print ()
					connection.register_packet_listener(print_chat, clientbound.play.ChatMessagePacket)
					packet = serverbound.play.ChatPacket()
					packet.message = text
					connection.write_packet(packet)
			except Exception as e:
				print ()
				print (e)
				print (f"""
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╔═══════════════════════════════════╗
    {Fore.WHITE}║ {Fore.MAGENTA}Usage: connect [ip] [port] [nick].{Fore.WHITE}║
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╚═══════════════════════════════════╝
					""")
		elif cmd == "server":
			try:
				target = x[1]
				try:
					server = MinecraftServer.lookup(target)
					status = server.status()
					print ()
					print (" IP: "+(target))
					print (" Players: "+str(status.players.online)+"/"+str(status.players.max))
					print (" Version: "+str(status.version.name)+" - "+str(status.version.protocol))
					print (" Description: "+str(status.description))
					print ()
				except Exception as e:
					print ()
					print (f"""
    {Fore.MAGENTA}{Fore.WHITE}╔═══════════════════════╗
    {Fore.WHITE}║ {Fore.MAGENTA}Can't resolve server. {Fore.WHITE}║
    {Fore.MAGENTA}{Fore.WHITE}╚═══════════════════════╝
						""")
			except:
				print ()
				print (f"""
    {Fore.MAGENTA}{Fore.WHITE}╔═════════════════════╗
    {Fore.WHITE}║ {Fore.MAGENTA}Usage: server [ip].{Fore.WHITE}║
    {Fore.MAGENTA}{Fore.WHITE}╚═════════════════════╝
					""")

		elif cmd == "clear":
			os.system("cls")
			banner()
		elif cmd == "locate":
			try:
				target = x[1]
				try:
					url = ("http://ip-api.com/json/")
					response = urllib.request.urlopen(url + target)
					data = response.read()
					jso = json.loads(data)
					print (jso)
					print ()
					print (f"{Fore.WHITE} IP: "+(target))
					print (f"{Fore.WHITE} ISP: "+(jso["isp"]))
					print ()
					print (f" {Fore.MAGENTA}[{Fore.WHITE}#{Fore.MAGENTA}]{Fore.WHITE} Country: "+(jso["country"])+" - TZ: "+(jso["timezone"]))
					print (f"  {Fore.WHITE}║")
					print (f"  {Fore.WHITE}╚═{Fore.MAGENTA}[{Fore.WHITE}#{Fore.MAGENTA}]{Fore.WHITE} Region: "+(jso["regionName"])+" - "+(jso["zip"]))
					print (f"     {Fore.WHITE}║")
					print (f"     {Fore.WHITE}╚═{Fore.MAGENTA}[{Fore.WHITE}#{Fore.MAGENTA}]{Fore.WHITE} City: "+(jso["city"]))  
					print ()        	          	    
				except Exception as e:
					print (e)
					print ()
					print (f"""
    {Fore.MAGENTA}{Fore.WHITE}╔═══════════════════════╗
    {Fore.WHITE}║ {Fore.MAGENTA}Can't resolve target. {Fore.WHITE}║
    {Fore.MAGENTA}{Fore.WHITE}╚═══════════════════════╝
						""")
			except:
				print ()
				print (f"""
    {Fore.MAGENTA}{Fore.WHITE}╔═════════════════════╗
    {Fore.WHITE}║ {Fore.MAGENTA}Usage: locate [ip].{Fore.WHITE}║
    {Fore.MAGENTA}{Fore.WHITE}╚═════════════════════╝
					""")
		elif cmd == "player":
			try:
				target = x[1]
				url = "https://api.mojang.com/users/profiles/minecraft/"
				text123 = requests.get((url)+(target))

				if text123.text == "":
					print ()
					print (f"{Fore.WHITE} Nick: "+(target))
					print (f"{Fore.WHITE} UUID: *")
					print (f"{Fore.WHITE} Type: Cracked")
					print ()
				else:
					asmr = (text123.text).split('"')
					uuid = (asmr)[3]
					print ()
					print (f"{Fore.WHITE} Nick: "+(target))
					print (f"{Fore.WHITE} UUID: "+(uuid))
					print (f"{Fore.WHITE} Type: Premium")
					print ()
			except Exception as e:
				print (e)
				print ()
				print (f"""
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╔══════════════════════╗
    {Fore.WHITE}║ {Fore.MAGENTA}Usage: player [nick].{Fore.WHITE}║
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╚══════════════════════╝
					""")				
		else:
			print (f"""
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╔═════════════════════════════════════╗
    {Fore.WHITE}║ {Fore.MAGENTA}Usage: Unknow command, type 'help'. {Fore.WHITE}║
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╚═════════════════════════════════════╝
				""")		
	except:
			print (f"""
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╔═════════════════════════════════════╗
    {Fore.WHITE}║ {Fore.MAGENTA}Usage: Unknow command, type 'help'. {Fore.WHITE}║
    {Fore.MAGENTA}{Fore.WHITE}{Fore.WHITE}╚═════════════════════════════════════╝
				""")