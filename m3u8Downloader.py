from m3u import m3u
import requests
import math
import json
import os

"""
baseURL = sometimes the links in a m3u8 file need a prefix e.g. https://www.funny.com/
which will result in the new download link: baseURL+link_from_m3u8_file
saveName = name of the downloaded movie without extension
fileName = name of your m3u8 file that contains the playlists...
the highest video quality file is picked automatically
"""
baseURL="https://www.lmao.lol"
saveName="myMovie"
fileName="hls.m3u8"

def query(url,headers=None,params=None,verbose=True):
    response = requests.get(url,params=params,headers=headers)

    if verbose:
        print("Status Code: "+str(response.status_code)+" Length: "+str(response.headers['content-length']+" Request to: "+url))

    return response

def parse(str):
	parser=m3u(str)
	parser.parse()
	
	return parser.json
	
def main():
	with open(fileName) as f:
		m3ustr=f.read()
		
	jsonstr=parse(m3ustr)
	tag=max(jsonstr["tags"], key=lambda tag: int(tag["attribs"]["BANDWIDTH"]) if "BANDWIDTH" in tag["attribs"] else -math.inf)
	bandwidth=int(tag["attribs"]["BANDWIDTH"])
	print("Best Qualiy Bitrate: %d" % bandwidth)
	URL=tag["link"]
	res=query(baseURL+URL)
	res=res.content.decode('utf-8') #byte array to string
	jsonstr=parse(res)
	list=[]
	for tag in jsonstr["tags"]:
		if("link" in tag):
			list.append(tag["link"])
		
	print("Starting download. Found %d files" % len(list))
	
	dir = os.path.dirname(os.path.realpath(__file__))
	save_path=os.path.join(dir,"parts")
	if not os.path.isdir(save_path):
		os.mkdir(save_path)

	for i, link in enumerate(list):
		file=os.path.join(save_path,str(i+1)+".ts")
		with open(file, "wb") as f:
			print("Downloading segment %d/%d.................................." 
			% (i+1,len(list)),end="\r")
			data=query(baseURL+link)
			f.write(data.content)
			
	print("Download finished. Merging files...")
	
	l=[]
	files=os.listdir(save_path)
	for file in files:
		filePath=os.path.join(save_path,file)
		if os.path.isfile(filePath):
			 t=os.path.splitext(file)
			 if t[1] == ".ts" and t[0].isdigit():
				 tup=filePath,t[0]
				 l.append(tup)

	l.sort(key=lambda tup: int(tup[1]))
	
	all=os.path.join(dir,saveName+".ts")
	with open(all,"ab") as f:
		for file in l:
			with open(file[0],"rb") as f2:
				f.write(f2.read())
			os.remove(file[0])

	os.rmdir(save_path)
	
	print("Ready!")
	
if __name__ == "__main__":
	main()
		
