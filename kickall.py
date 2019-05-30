#!/usr/bin/python3
from lxml import html
import requests
import subprocess
import re
import datetime

with open('config') as config:

child = subprocess.Popen(["ddos -b"],stdout=subprocess.PIPE, shell=True)
msg,err = child.communicate()

now = datetime.datetime.now()
raw = msg.decode()
pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
ips = []

for(ip) in re.findall(pattern, raw):
	ips.append(ip)

page = requests.get('http://' + data['ip'] + '/admin/listclients.xsl?mount=/live', auth=('admin', data['password']))
tree = html.fromstring(page.content)
clients = tree.xpath('/html/body/div/div[1]/div[2]/table[2]/tbody/tr/td[1]/text()')
kicks = tree.xpath('/html/body/div/div[1]/div[2]/table[2]/tbody/tr/td[5]/a/@href')

for(i,client) in enumerate(clients):
	if client in ips:
		url = ""
		url =  "http://" + data['ip'] + "/admin/" + kicks[i]
		res = requests.get(url, auth=('admin', data['ip']))
		print("["+ now.strftime("%d/%m/%Y %H:%M") +"]Kicked an IP: " + client)

