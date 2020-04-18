from flask import Flask,request,jsonify
from flask_sslify import SSLify
import json,config,util,photorej,requests
app=Flask(__name__)
SSLify(app)


@app.route('/',methods=["POST","GET"])
def index():
   if request.method=="POST":
      try:
        r=request.get_json()
        print(r)
      except: return json({"errors":"error"})
      else:
        #jsoni mshakum karas arandzin funkcia gres
         if util.jsonistug(r):
          #verjacav jsoni mshakumn
          chat_id=config.chat_id
          if chat_id not in config.stug:
             config.stug[chat_id]=0
          if 2==config.stug[chat_id]:#harci rej
            if 'callback_query' in r:#stugumenq rejimum uxarkvac informaciai tesakn
               util.harcrej(r)
               return jsonify(r)
            else:
                config.stug[chat_id]=0
                util.normrej(r)
                return jsonify(r)

            return jsonify(r)
          
          if 3==config.stug[chat_id]:#fotored rejim
            if ('message' in r and ("photo" in r['message'] or  "document" in r['message'])) or 'callback_query' in r:#stugumenq rejimum uxarkvac informaciai tesakn
               photorej.photorej(r)
               return jsonify(r)
            else:
                requests.post(config.URL+config.tmethods[0],json={"chat_id":chat_id,"text":"prej anjatvec"})
                config.stug[chat_id]=0
                util.normrej(r)
                return jsonify(r)

            return jsonify(r)
          if 1==config.stug[chat_id]:#mecat rej
              if 'message' in r and "text" in r['message']:#stugumenq rejimum uxarkvac informaciai tesakn
                 util.mecatrej(r)
              return jsonify(r)


          if 0==config.stug[chat_id]:#norm rej
            if 'message' in r and "text" in r['message']:#stugumenq rejimum uxarkvac informaciai tesakn
                 util.normrej(r)
            return jsonify(r)



         else:
           return jsonify(r)









   return "<h1> Bots start</h1>"
if __name__ == "__main__":
    app.run()




