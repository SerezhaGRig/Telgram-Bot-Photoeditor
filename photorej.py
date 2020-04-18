import config,wget,os,requests,json
from PIL import Image
filtrcuc={'/negative':2,'/grey':3,'/brightness':4}#photorejimneri identificatornern
pentar={}#@st identifikatori filtri durs berum
sfname="send.jpg"
fname="saved.jpg"
intens={}
def photorej(js):
    chat_id=config.chat_id
    intens[chat_id]=40
    if 'callback_query' in js:
           string=js["callback_query"]["data"]
           text=[int(s) for s in string.split() if s.isdigit()]
           if text[0]!=None:
               intens[chat_id]=text[0]%101
               requests.post(config.URL+config.tmethods[0],json={"chat_id":chat_id,"text":"uxarkeq nkar"})
    else:
       if "photo" in js["message"]:
           file_id=js["message"]["photo"][0]["file_id"]
       if "document" in js["message"]:
           if 'image/jpeg'  in js["message"]["document"]["mime_type"]:
                file_id=js["message"]["document"]["file_id"]
           else: return 0
       res=requests.get(config.URL+config.tmethods[3],json={"file_id":file_id})
       re=res.json()
       print(re)
       file_path=re["result"]["file_path"]
       fname=file_path
       fname = fname.split('/')[1]
       try:
           wget.download('https://api.telegram.org/file/bot{}/{}'.format(config.TOKEN,file_path))
       except: 
          return 0
       else: 
           if pentar[chat_id]==2:#filtri voroshum
               negative(fname,sfname)
             
           if pentar[chat_id]==3:
               gray_scale(fname,sfname)
           if pentar[chat_id]==4:
               bright(fname,sfname,(intens[chat_id]/50))#brightness khetazotes
           sendImage(chat_id)
           os.remove(fname)
           os.remove(sfname)
def sendImage(id):
    files = {'photo': open(sfname, 'rb')}
    data = {'chat_id' : id}
    r= requests.post(config.URL+config.tmethods[1], files=files, data=data)
    print(r.status_code, r.reason, r.content)











def negative(source_name, result_name):
    source = Image.open(source_name)
    result = Image.new('RGB', source.size)
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))
            result.putpixel((x, y), (255 - r, 255 - g, 255 - b))
    result.save(result_name, "JPEG")    
def gray_scale(source_name, result_name):
    source = Image.open(source_name)
    result = Image.new('RGB', source.size)
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))
            gray = int(r * 0.2126 + g * 0.7152 + b * 0.0722)
            result.putpixel((x, y), (gray, gray, gray))
    result.save(result_name, "JPEG")
def bright(source_name, result_name, brightness):
    source = Image.open(source_name)
    result = Image.new('RGB', source.size)
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))

            red = int(r * brightness)
            red = min(255, max(0, red))

            green = int(g * brightness)
            green = min(255, max(0, green))

            blue = int(b * brightness)
            blue = min(255, max(0, blue))

            result.putpixel((x, y), (red, green, blue))
    result.save(result_name, "JPEG")