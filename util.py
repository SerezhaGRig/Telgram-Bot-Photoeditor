import config,photorej
import requests as req
modcucak={"/norm":0,"/mecatr":1,}#modifikaciai hamar 2 ev 3 choktagorces eti zbaxvaca harceri hamar kara sra tex list lini
hrcucak={
"qfur tur":"xujan lakot et inch es asum",
"/start":"Baroves ekel.\nHramannerin canotanalu hamar sexmir  '  /  '  nshann.",
"/krasotka":1,
"/photoredakt":"Filtrner:\n1:/negative \n2:/grey",
'/negative':3,
'/grey':3,
}# 3n ogtagorcvuma vorpes photoredaktori rejim
filtrcuc={'/negative':2,'/grey':3}#photorejimneri identificatornern

#ete tiva uremn hramani patasxann text chi
harccuc=["/harctur","/brightness"]#kar vapshe bararan chlini
cmd=2
mod=1
harc=3
nocmd=0
def normrej(js):
            chat_id=js["message"]["from"]["id"]
            config.stug[chat_id]=0
            nrej=nrejvorosh(js)
            if nrej==cmd:
               cmdkat(js)





            if nrej==mod:
               modif(js)




            if nrej==harc:
                harcverc(js)#kuxarkes knopka kdnes harci rej
                ## stug petqa te che stug[iid]=harc_index

            if nrej==nocmd:
               js["message"]["text"]="Chgitem inch patasxanem bayc du sharunaki grel..."
               krkni(js)




def krkni(jeson):#anunn karas poxes

   chat_id=jeson["message"]["from"]["id"]
   mess=jeson["message"]["text"]
   ans={"chat_id": chat_id,"text":mess}
   req.post(config.URL+config.tmethods[0],json=ans)




def harcrej(jeson):
     pat=jeson['callback_query']["data"]
     chat_id=jeson['callback_query']["message"]['chat']["id"]
     config.stug[chat_id]=0#harci rejimi hanum hari stug initializ
     pater={"/harctur0":"du debil es","/harctur1":"du gites"}
     erkpat=2
     ereqpat=3
     if config.harcientaqan[chat_id]==ereqpat:#voroshvaca harcvercum
         pass
     if config.harcientaqan[chat_id]==erkpat:
        if pater[pat]!=None:
           pat=pater[pat]
           ans={"chat_id": chat_id,"text":pat}
           req.post(config.URL+config.tmethods[0],json=ans)

def nrejvorosh(js):

    tex=js["message"].get('text',config.default)
    if tex in harccuc:
       return harc
    if tex in modcucak:
       return mod
    if tex in hrcucak:
        return cmd
    return nocmd
def donothing(text):
    return text

def uppertext(text):
    return text.upper()
def cmdkat(jeson,func=donothing):
     chat_id=jeson["message"]["from"]["id"]
     mess=jeson["message"].get('text',config.default)
     #entah skizb
     if hrcucak[mess]==1:
          file_id="AgADAgADDqsxG3I8OEv1Nv39wv-NQLm8UQ8ABCiUqCFHTyS08ZwDAAEC"
          ans={"chat_id":chat_id,"photo":file_id}
          req.post(config.URL+config.tmethods[1],json=ans)
          return 0
          
     if hrcucak[mess]==3:#filtri voroshum
        config.stug[chat_id]=3#filtri rej
        photorej.pentar[chat_id]=photorej.filtrcuc[mess]
        req.post(config.URL+config.tmethods[0],json={"chat_id":chat_id,"text":"prej miacvec uxarkeq photo"})
        return 0



     mess=hrcucak[mess]
      # entah verj
     mess=func(mess)

     ans={"chat_id":chat_id,"text":mess}
     req.post(config.URL+config.tmethods[0],json=ans)





def modif(jeson):
     chat_id=jeson["message"]["from"]["id"]
     message=jeson["message"].get('text',config.default)
     ans={"chat_id": chat_id,"text":"mod miacav"}#kara lini orinak modif miacav
     req.post(config.URL+config.tmethods[0],json=ans)
     config.stug[chat_id]=modcucak[message]

     return 0
def harcverc(jeson):
     chat_id=jeson["message"]["from"]["id"]
     mess=jeson["message"].get('text',config.default)
     config.stug[chat_id]=2
     erkupat={"/harctur":1}
     hingpat={"/brightness":1}

     if  mess in erkupat:
        config.harcientaqan[chat_id]=2
        if erkupat[mess]==1:
            reply_markup={"inline_keyboard":[[{"text":"pat 6","callback_data":"/harctur1"}],[{"text":"pat 8","callback_data":"/harctur0"}]]}
            ans={"chat_id": chat_id,"text":"patasxaneq harcn stanaluc anmijapes heto sexmelov kochakn."}
            req.post(config.URL+config.tmethods[0],json=ans)
            ans["reply_markup"]=reply_markup
            ans["text"]="2+2*2=?"
            req.post(config.URL+config.tmethods[0],json=ans)
            return 0
        


                        #erku knopka
     if  mess in hingpat:
        if hingpat[mess]==1:
            reply_markup={"inline_keyboard":[[{"text":"20","callback_data":"20"}],[{"text":"40","callback_data":"40"}],
            [{"text":"60","callback_data":"60"}],
            [{"text":"80","callback_data":"80"}],[{"text":"100","callback_data":"100"}]]}
            ans={"chat_id":chat_id,"reply_markup":reply_markup,"text":"choose intensivity"}
            config.stug[chat_id]=3
            photorej.pentar[chat_id]=photorej.filtrcuc[mess]
            req.post(config.URL+config.tmethods[0],json=ans)
def mecatrej(js):
   chat_id=js["message"]["from"]["id"]
   tex=js["message"].get('text',config.default)
   if tex in harccuc:
      harcverc(js)
      return 0
   if tex in hrcucak:
      cmdkat(js,func=uppertext)


      return 0
   if tex in modcucak:
      config.stug[chat_id]=modcucak[tex]
      return 0
   js["message"]["text"]="CHGITEM INCH PATASXANEM BAYC DU SHARUNAKI GREL..."
   krkni(js)
def jsonistug(js):
   if "message" in js or 'callback_query' in js:
           if "message" in js:
               if "text" in js["message"] or "photo" in js["message"]  or "document" in js["message"] :
                 config.chat_id=js["message"]["from"]["id"]
               else:return 0
           elif  "message" in js['callback_query']:
                 config.chat_id=js['callback_query']["message"]['chat']["id"]
           else: return 0
   else:return 0
   return 1