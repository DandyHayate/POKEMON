# -*- coding: utf-8 -*-
from linepy import *
from akad.ttypes import *
from multiprocessing import Pool
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast
_session = requests.session()
translateen = []
#line = LINE()
line = LINE("ExQ6YuqVEg3zjMWlbvvb.Sp/s6yipA4kI8lGDz1Jc/W.0+6RGQEyRULTA9pbpJxcbf5IPIXqp5EKihUS7/I/J0w=")
line.log("Auth Token : " + str(line.authToken))
channelToken = line.getChannelResult()
settingsOpen = codecs.open("prankBots.json","r","utf-8")
settings = json.load(settingsOpen)
oepoll = OEPoll(line)
lineProfile = line.getProfile()
lineSettings = line.getSettings()
lineMID = line.profile.mid
def backupData():
    try:
        backup = settings
        f = codecs.open('prankBots.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    time.sleep(5)
    python = sys.executable
    os.execl(python, python, *sys.argv)
def logError(text):
    line.log("[ ERROR ] " + str(text))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("prankBots.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            prankbot = pesan.replace(settings["keyCommand"],"")
        else:
            prankbot = "Undefined command"
    else:
        prankbot = text.lower()
    return prankbot
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 5:
            line.findAndAddContactsByMid(op.param1)
            line.sendMessage(op.param1, "Thanks for You\n\nspecial from me:")
            line.sendContact(op.param1, 'u07abdfb9d1644326c65c13f9727b10d7')
        if op.type == 13:
            try:
                group = line.getGroup(op.param1)
                contact = line.getContact(op.param2)
                line.acceptGroupInvitation(op.param1)
            except Exception as error:
                logError(error)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False:
                 setKey = ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        prankbot = command(text)
                        if 'phie' in msg.text:
                            kontak = line.getContact(msg._from)
                            response = ("ada apa kau memanggilku ","ya aku disini ","apakah kamu merindukanku ","ya aku selalu ada untukmu ","kenapa sih berisik lu ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "keluar" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("ok gw keluar ya ","ok siap ","yaudah kalo gitu bye bye ","yasudahlah bye ","rese lu ","yakin ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                            line.leaveGroup(msg.to)
                        if "makan" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("silahkan makan ","ok,enakin aja ","mau makan apa ","sepertinya aku tidak lapar ","oh tentu saja,sepertinya kau lapar ","iya duluan aja aku belum lapar ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "siapa" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("selingkuhanmu mungkin ","sepertinya mantanmu ","ohh.. aku tidak tau ","sepertinya tikunganmu ","itu kan bojomu kok masih nanya siapa ","siapa sih ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "apa" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("aku tidak tau ","apanya yang kau mksud,yg jelas dong ","entahlah aku tak tau ","apa apa bae dah ","apa apa nya dong ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "mana" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("di kuburan sana ","di lubang buaya saja kalo begitu ","maaf aku tak tau arah harus kemana ","cari aja sendiri ","berisik mending pulang aja kamu ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "sayang" in text.lower() or "yank" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("beraninya kau panggil sayank ","apa kau kesepian ya ","yank yank yank aus,yank lapar ","palalu peang ","iya sayank ada apa ","what coba ulangi sekali lagi ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "mbuh" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("mbuh jare ","semprul kau ","jangan gitu ","tak colok ndasmu ","helehh knapa sih ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "kapan" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("kapan kapan aja dah ","emang mau ngapain ","nanti aja yaa ","ntah kapan gw gak tau ","kapan aja boleh ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "bot" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("paan lu manggil manggil ","oy hadir gan ","sekali lagi bilang bot gua cipok lu ","bot bot bot gundulmu lah ","bot mah bebas ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "gila" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("gila mah bebas ","lu yg gila ","gila drmna nya ","lah lu juga edan ","siapa yg gila ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "baper" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("puskun gih sana ","makan aja biar kenyang ","kapok sukurin ","baper gw kick nih ","gak usah baper deh minum larutan dulu sana biar adem ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "asem" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("asem jare ","ketek lu yg asem ","manis rasanya ","asem opone lho ","lu yg asem ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "sue" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("lu sue gw mah kagak ","lambemu sing sue ","anumu sue ","bahhhh ngomongnya kok gitu ","eh siapa yg sue, mulutnya ga dipajak in ya ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "kamvret" in text.lower() or "kampret" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("astagfirullah jangan bilang gitu ","kasar banget lu njir ","lu yg kampret ","paan lu mprett. ","biasa aja kalee ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "gw" in text.lower() or "aku" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("iya tau ","ada apa sih ","aku apa kamu ","aku juga dong ya ","hooh aku juga tau kok ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "kuy" in text.lower() or "ayo" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("kuuyyyy ahh gapake lama ","ayoo kmmana lah kita ","gw gak di ajak njir ","ayolah kalo bgitu ","udah lama gk ayo nih ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "kikil" in text.lower() or "kick" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("dasar kikil ","bah kikil ","njirr ada kikil ","situ kikil ","si kikil mana si kikil ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "assalamualaikum" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("waalaikumsalam wr.wb kemana aja baru keliatan","waalaikumsalam,aihh kirain siapa yg salam ternyata kamu ","waalaikumsalam,silahkan masuk ","waalaikumsalam,silahkan duduk ","waalaikumsalam,dari mana aja kok baru nongol ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "mojok" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("ayok mojok ","mau mojok kapan ","kalo mojok ajak2 dong ","mojok sama siapa ","mojok aja sana ditempat gelap ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "join" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("join kemana ","join juga dicuekin kan ","klo udah join trs gimna ","dih join join mulu ","join apa ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "emoh" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("kok emoh sih ","mau dong ","jgn emoh gtu ","klo emoh paksa juga nih ","klo emoh yaudah deh gpp kok ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "itu" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("itu apaan ","itu yg mna ","oh itu ","itu apa ini ","itu kan aku juga tau ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "naik" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("naik kemana ","iya naik aj dulu ","ga asik naik enak di naikin ","bentar aku juga naik kok ","naikin terus ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "udah" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("udah apaan ","iya udah kok ","klo udah cebok gih ","ciee yg udahan ","udah udah udah ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "sider" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("sider bintitan ya ","yg sider semoga tenang ya ","yg sider mudah2an selamat ya ","siapa yg sider ","sider nya kaget ya ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "kojom" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("kojom aja sendirian sana ","klo kojom ngapain aja ","kojom sana bertiga sama sayton ","kojom kok koar koar ","klo mau kojom itu diem diem aja ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "pekok" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("pekok e joget pekok e joget ya ","siapa yg pekok ","lu yg pekok ","dih kasar bgt ","pekok pekok lambe lucak lu ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "kepo" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("siapa yg kepo ","gua mah gk kepo ","kepo apa kero ","kepo kepo malam ya ","kepo dengkulmu ambles ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "pagi" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("oh udah pagi ya ","pagi juga ,mandi sana bau jigong ","eh udah bangun ya ","pagi juga ,semlm mimpi apa ","siang oy jgn pagi terus ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "hadir" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("nah hadir juga demit nya ","dih hadir apaan lu ","hadir dan hoyok ","gak di harepin kok malah hadir ","ngapain hadir diundang aja kagak lu ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "tikel" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("aku mau tikel dong ","tikel yg 1000 an mau gk ","buat apa tikel ","tikel ku cuma dikit ","tikel yg jelek kyak lu kan ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "ngantuk" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("tidur lah ","sama aku juga ngantuk ","ydh tdur aja sana ","berak dulu biar gak ngantuk ","klo ngantuk ga usah cerewet ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "mandi" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("buruan mndi nya mau di shalatin ","mndi dimana ","jgn lama2 mndi nya kasian jamaah nungguin jenazah ya ","abis mndi di kafanin ","klo mndi ya mndi aja ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "kangen" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("aku juga kangen kamu ","kangen siapa ","kangen apa nya ","kok bisa kangen ","kalo kangen temuin lah ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
    except Exception as error:
        logError(error)
        
        if op.type == 59:
            print (op)
        
#===========================POKEMON SCRIPT===================#
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          oepoll.setRevision(op.revision)
        
    except Exception as e:
        line.log("[SINGLE_TRACE] ERROR : " + str(e))
