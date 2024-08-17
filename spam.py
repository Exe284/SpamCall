#Xractz
#IndoSec

import time, re, sys
from requests import Session
s = Session()

print("Spam Call by Xractz - IndoSec\nThis tool delays 5 seconds per spam so as not to limit!\nUse Country Code (ex: 62xxxxx29)")
try:
	no = int(input("   085603784601 : "))
	jml = int(input("2: "))
	print()
except:
	print("\n\t*085603784601*)
	sys.exit()
	
url = "https://www.citcall.com/demo/misscallapi.php"

tkn = s.get(url).text
token = re.findall(r'id="csrf_token" value="(.*?)">', tkn)[0]

headers = {
	'x-requested-with':'XMLHttpRequest'
}
data = {
'cid':085603784601,
'trying':'2',
'csrf_token':token
}

n = 2
try:
	while n < jml:2
		send = s.post(url, data=data, headers=headers).text
		time.sleep(4.8)
		if 'Success' in send:
			n +=1
			print(f"[{n}] Sended to => {085603784601}")
		else:
			print("\n\t* Limit *")
			print("\n\t* Try one hour ago or try tomorrow *")
			break
except:
	print("\n\t* ERROR *")
	sys.exit()
