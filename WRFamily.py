# -*- coding: utf-8 -*- 
import LINEPY
from LINEPY import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
import youtube_dl

kingbii = LineClient(authToken='')
kingbii.log("Auth Token : " + str(kingbii.authToken))
channel = LineChannel(kingbii)
kingbii.log("Channel Access Token : " + str(channel.channelAccessToken))

assist = LineClient(authToken='')
assist.log("Auth Token : " + str(assist.authToken))
channel1 = LineChannel(assist)
assist.log("Channel Access Token : " + str(channel1.channelAccessToken))

assist1 = LineClient(authToken='')
assist1.log("Auth Token : " + str(assist1.authToken))
channel2 = LineChannel(assist1)
assist1.log("Channel Access Token : " + str(channel2.channelAccessToken))

assist2 = LineClient(authToken='')
assist2.log("Auth Token : " + str(assist2.authToken))
channel3 = LineChannel(assist2)
assist2.log("Channel Access Token : " + str(channel3.channelAccessToken))

ghost = LineClient(authToken='')
ghost.log("Auth Token : " + str(ghost.authToken))
channel11 = LineChannel(ghost)
ghost.log("Channel Access Token : " + str(channel11.channelAccessToken))

poll = LinePoll(kingbii)
call = LineCall(kingbii)
creator = ["u02aea92a3d7e44f587e7a91141e78b59"]
owner = ["u02aea92a3d7e44f587e7a91141e78b59"]
admin = ["ucf97e89bfc77943c7d11c52c9c46b2b9"]
staff = ["ucf97e89bfc77943c7d11c52c9c46b2b9"]
mid = kingbii.getProfile().mid
Amid = assist.getProfile().mid
Bmid = assist1.getProfile().mid
Cmid = assist2.getProfile().mid
Zmid = ghost.getProfile().mid
KAC = [kingbii,assist,assist1,assist2]
ABC = [assist,assist1,assist2]
Bots = [mid,Amid,Bmid,Cmid,Zmid]
WRFamily = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
welcome = []

responsename = kingbii.getProfile().displayName
responsename1 = assist.getProfile().displayName
responsename2 = assist1.getProfile().displayName
responsename3 = assist2.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "mention":"Jangan Suka Ngintip ah",
    "Respontag":"┏━━━━━━━━━━━━\n┃⇒ Jangan suka tag orang ntar kualat\n⇒ Tag aku sekali lagi bayar yah :v\n┗━━━━━━━━━━━━",
    "welcome":"Selamat datang cek note yah biar anu",
    "comment":"┏━━━━━━━━━━━━\n┃• Edited : 🔰 WRFamily\n┃• Support :\n┃🔰 RAFamily\n┃🔰 Sains Bot\n┃🔰 WRFamily\n┗━━━━━━━━━━━━",
    "message":"┏━━━━━━━「 WRFamily 」━━━━━━━\n┃• Open Order :\n┃• Selfbot Only\n┃• Selfbot + 3 Assist + 1 Ghost\n┃• Selfbot + 5 Assist + 1 Ghost\n┃• VPS Gcloud\n┃• Bot Official\n┃• Bot Protection\n┃• Sirichan\n┃• Pembuatan Script Bot\n┗━━━━━━━",
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "「 Mention Unser {} 」\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(kingbii.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        kingbii.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kingbii.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Cieee ketahuan ngintip ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(kingbii.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        kingbii.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kingbii.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Selamat Datang  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = kingbii.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nGroup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(kingbii.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        kingbii.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kingbii.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = kingbii.getAllContactIds()
        gid = kingbii.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"\n• Pada Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" WIB\n• Group Anda : "+str(len(gid))+"\n• Teman : "+str(len(teman))+"\n• Masa Aktif : In "+hari+"\n• Edited :🔰 WRFamily\n• Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n• Runtime : \n • "+bot
        kingbii.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kingbii.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "🔰 WRFamily Selfbot\n\n" + \
                  "• menu\n" + \
                  "• self\n" + \
                  "• bot\n" + \
                  "• group\n" + \
                  "• media\n" + \
                  "\nGunakan Selfbot Dengan Bijak Edited :\n 🔰 WRFamily\n Support :\n🔰 RAFamily\n🔰 Sains bot\n"
    return helpMessage

def self():
    key = Setmain["keyCommand"]
    key = key.title()
    selfMessage = "🔰 WRFamily\n| Command For Self |\n\n" + \
                  "• me\n" + \
                  "• myid\n" + \
                  "• gid\n" + \
                  "• ginfo\n" + \
                  "• gcreator\n" + \
                  "• mid 「Mention」\n" + \
                  "• info 「Mention」\n" + \
                  "• ikick 「Mention」\n" + \
                  "• imkick 「Mention」\n" + \
                  "• status\n" + \
                  "• informasi\n" + \
                  "• runtime\n" + \
                  "• restart\n" + \
                  "• mygroup\n" + \
                  "• infogroup \n" + \
                  "• infomember \n" + \
                  "• leavegroup \n" + \
                  "• mention\n" + \
                  "• assist in\n" + \
                  "• assist out\n" + \
                  "• ghost in\n" + \
                  "• ghost out\n" + \
                  "\nGunakan Huruf Besar Dari Awal Example : Me\n"
    return seflMessage

def group():
    key = Setmain["keyCommand"]
    key = key.title()
    groupMessage = "🔰 WRFamily\n| Command For Group |\n\n" + \
                   "• buka qr\n" + \
                   "• tutup qr\n" + \
                   "• qr group\n" + \
                   "• broadcast:「Text」\n" + \
                   "• lurking「On Or On」\n" + \
                   "• lurkers\n" + \
                   "• sider「On Or On」\n" + \
                   "• welcomemessage「On Or On」\n" + \
                   "• autorespon「On Or On」\n" + \
                   "• sticker「On Or On」\n" + \
                   "• autojoin「On Or On」\n" + \
                   "• autoleave「On Or On」\n" + \
                   "• autoadd「On Or On」\n" + \
                   "• cekcontact「On Or On」\n" + \
                   "• protect 「On Or On」\n" + \
                   "• protectcancel 「On Or On」\n" + \
                   "• protectjoin 「On Or On」\n" + \
                   "• protectqr 「On Or On」\n" + \
                   "• wrprotect 「On Or On」\n" + \
                   "• removechat\n" + \
                   "• groupprotect\n" + \
                   "\nGunakan Huruf Besar Dari Awal Example : Me\n"
    return groupMessage

def bot():
    key = Setmain["keyCommand"]
    key = key.title()
    botMessage = "🔰 WRFamily\n| Command For Bot |\n\n" + \
                 "• changeprofile\n" + \
                 "• changegg\n" + \
                 "• addbot 「Mention」\n" + \
                 "• dellbot 「Mention」\n" + \
                 "• listbot\n" + \
                 "• contact banned\n" + \
                 "• daftar banned\n" + \
                 "• addbannd \n" + \
                 "• dellbanned \n" + \
                 "• addtalkban \n" + \
                 "• delltalkban \n" + \
                 "• listtalkban\n" + \
                 "• hapus banned\n" + \
                 "• .p respon\n" + \
                 "• .p sider\n" + \
                 "• .p welcomemessage\n" + \
                 "• .p pesan\n" + \
                 "• .p spam\n" + \
                 "• .g respon:「Text」\n" + \
                 "• .g sider:「Text」\n" + \
                 "• .g welcomemessage:「Text」\n" + \
                 "• .g pesan:「Text」\n" + \
                 "• .g spam:「Text」\n" + \
                 "• .g name:「Text」\n" + \
                 "• .g assist-2:「Text」\n" + \
                 "• .g iamge-2\n" + \
                 "\nGunakan Huruf Besar Dari Awal Example : Me\n"
    return botMessage


def media():
    key = Setmain["keyCommand"]
    key = key.title()
    mediaMessage = "🔰 WRFamily\n| Command For Media |\n\n" + \
                   "• ID line:「Id Line nya」\n" + \
                   "• sholat:「Location」\n" + \
                   "• cuaca:「Location」\n" + \
                   "• lokasi:「Location」\n" + \
                   "• music:「Judul」\n" + \
                   "• lirik:「Judul」\n" + \
                   "• ytmp3:「Judul」\n" + \
                   "• ytmp4:「Judul」\n" + \
                   "• profileig:「Nama IG」\n" + \
                   "• cekdate:「tgl-bln-thn」\n" + \
                   "• jumlah:「angka」\n" + \
                   "• spamtag「Mention」\n" + \
                   "• spamcall:「jumlahnya」\n" + \
                   "• spamcall\n" + \
                   "\nGunakan Huruf Besar Dari Awal Example : Me\n"
    return mediaMessage


def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if kingbii.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            kingbii.reissueGroupTicket(op.param1)
                            X = kingbii.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            kingbii.updateGroup(X)
                            kingbii.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if assist.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                assist.reissueGroupTicket(op.param1)
                                X = assist.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                assist.updateGroup(X)
                                kingbii.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if assist1.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    assist1.reissueGroupTicket(op.param1)
                                    X = assist1.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    assist1.updateGroup(X)
                                    kingbii.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if assist2.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        assist2.reissueGroupTicket(op.param1)
                                        X = assist2.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        assist2.updateGroup(X)
                                        kingbii.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if kingbii.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            kingbii.reissueGroupTicket(op.param1)
                                            X = kingbii.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            kingbii.updateGroup(X)
                                            kingbii.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if assist.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                assist.reissueGroupTicket(op.param1)
                                                X = assist.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                assist.updateGroup(X)
                                                kingbii.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kingbii.acceptGroupInvitation(op.param1)
                        ginfo = kingbii.getGroup(op.param1)
                        kingbii.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kingbii.leaveGroup(op.param1)
                    else:
                        kingbii.acceptGroupInvitation(op.param1)
                        ginfo = kingbii.getGroup(op.param1)
                        kingbii.sendMessage(op.param1,"Ngapain invite saya ke group " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kingbii.acceptGroupInvitation(op.param1)
                        ginfo = kingbii.getGroup(op.param1)
                        kingbii.sendMessage(op.param1,"Ngapain invite saya ke group " +str(ginfo.name))
                    else:
                        kingbii.acceptGroupInvitation(op.param1)
                        ginfo = kingbii.getGroup(op.param1)
                        kingbii.sendMessage(op.param1,"Ngapain invite saya ke group " + str(ginfo.name))
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        assist.acceptGroupInvitation(op.param1)
                        ginfo = assist.getGroup(op.param1)
                        assist.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        assist.leaveGroup(op.param1)
                    else:
                        assist.acceptGroupInvitation(op.param1)
                        ginfo = assist.getGroup(op.param1)
                        assist.sendMessage(op.param1,"Ngapain invite saya ke group " + str(ginfo.name))
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        assist1.acceptGroupInvitation(op.param1)
                        ginfo = assist1.getGroup(op.param1)
                        assist1.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        assist1.leaveGroup(op.param1)
                    else:
                        assist1.acceptGroupInvitation(op.param1)
                        ginfo = assist1.getGroup(op.param1)
                        assist1.sendMessage(op.param1,"Ngapain invite saya ke group " + str(ginfo.name))
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        assist2.acceptGroupInvitation(op.param1)
                        ginfo = assist2.getGroup(op.param1)
                        assist2.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        assist2.leaveGroup(op.param1)
                    else:
                        assist2.acceptGroupInvitation(op.param1)
                        ginfo = assist2.getGroup(op.param1)
                        assist2.sendMessage(op.param1,"Ngapain invite saya ke group " + str(ginfo.name))

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = kingbii.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            kingbii.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = assist.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                assist.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = assist1.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    assist1.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = assist2.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        assist2.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    pass

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = kingbii.getGroup(op.param1)
                contact = kingbii.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                kingbii.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	assist2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                assist.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    assist1.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        kingbii.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        kingbii.sendText(op.param1, wait["message"])

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            assist.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                assist1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    assist2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        assist.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            assist1.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                kingbii.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        assist.kickoutFromGroup(op.param1,[op.param2])
                        assist.inviteIntoGroup(op.param1,[op.param3])
                        kingbii.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            assist1.kickoutFromGroup(op.param1,[op.param2])
                            assist1.inviteIntoGroup(op.param1,[op.param3])
                            kingbii.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                assist2.kickoutFromGroup(op.param1,[op.param2])
                                assist2.inviteIntoGroup(op.param1,[op.param3])
                                kingbii.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = assist.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    assist.kickoutFromGroup(op.param1,[op.param2])
                                    assist.updateGroup(G)
                                    Ticket = assist.reissueGroupTicket(op.param1)
                                    kingbii.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    assist.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    assist1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    assist2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = assist.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    assist.updateGroup(G)
                                    Ticket = assist.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        assist.kickoutFromGroup(op.param1,[op.param2])
                                        assist.inviteIntoGroup(op.param1,[op.param3])
                                        kingbii.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            assist1.kickoutFromGroup(op.param1,[op.param2])
                                            assist1.inviteIntoGroup(op.param1,[op.param3])
                                            kingbii.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        assist1.kickoutFromGroup(op.param1,[op.param2])
                        assist1.inviteIntoGroup(op.param1,[op.param3])
                        assist.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            assist2.kickoutFromGroup(op.param1,[op.param2])
                            assist2.inviteIntoGroup(op.param1,[op.param3])
                            assist.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kingbii.kickoutFromGroup(op.param1,[op.param2])
                                kingbii.inviteIntoGroup(op.param1,[op.param3])
                                assist.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = assist1.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    assist1.kickoutFromGroup(op.param1,[op.param2])
                                    assist.updateGroup(G)
                                    Ticket = assist1.reissueGroupTicket(op.param1)
                                    kingbii.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    assist.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    assist1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    assist.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = assist1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    assist.updateGroup(G)
                                    Ticket = assist1.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        assist1.kickoutFromGroup(op.param1,[op.param2])
                                        assist1.inviteIntoGroup(op.param1,[op.param3])
                                        assist.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            assist2.kickoutFromGroup(op.param1,[op.param2])
                                            assist2.inviteIntoGroup(op.param1,[op.param3])
                                            assist.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        assist2.kickoutFromGroup(op.param1,[op.param2])
                        assist2.inviteIntoGroup(op.param1,[op.param3])
                        assist1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kingbii.kickoutFromGroup(op.param1,[op.param2])
                            kingbii.inviteIntoGroup(op.param1,[op.param3])
                            assist1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                assist.kickoutFromGroup(op.param1,[op.param2])
                                assist.inviteIntoGroup(op.param1,[op.param3])
                                assist1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = assist2.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    assist2.kickoutFromGroup(op.param1,[op.param2])
                                    assist2.updateGroup(G)
                                    Ticket = assist2.reissueGroupTicket(op.param1)
                                    kingbii.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    assist.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    assist1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    assist2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = assist2.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    assist2.updateGroup(G)
                                    Ticket = assist2.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        assist.kickoutFromGroup(op.param1,[op.param2])
                                        assist.inviteIntoGroup(op.param1,[op.param3])
                                        assist2.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            assist2.kickoutFromGroup(op.param1,[op.param2])
                                            assist2.inviteIntoGroup(op.param1,[op.param3])
                                            assist1.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kingbii.kickoutFromGroup(op.param1,[op.param2])
                        kingbii.inviteIntoGroup(op.param1,[op.param3])
                        assist2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            assist.kickoutFromGroup(op.param1,[op.param2])
                            assist.inviteIntoGroup(op.param1,[op.param3])
                            assist2.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                assist1.kickoutFromGroup(op.param1,[op.param2])
                                assist1.inviteIntoGroup(op.param1,[op.param3])
                                assist2.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kingbii.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kingbii.kickoutFromGroup(op.param1,[op.param2])
                                    kingbii.updateGroup(G)
                                    Ticket = kingbii.reissueGroupTicket(op.param1)
                                    kingbii.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    assist.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    assist1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    assist2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kingbii.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kingbii.updateGroup(G)
                                    Ticket = kingbii.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kingbii.kickoutFromGroup(op.param1,[op.param2])
                                        kingbii.inviteIntoGroup(op.param1,[op.param3])
                                        assist2.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            assist.kickoutFromGroup(op.param1,[op.param2])
                                            assist.inviteIntoGroup(op.param1,[op.param3])
                                            assist2.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kingbii.kickoutFromGroup(op.param1,[op.param2])
                        kingbii.findAndAddContactsByMid(op.param1,admin)
                        kingbii.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            assist.kickoutFromGroup(op.param1,[op.param2])
                            assist.findAndAddContactsByMid(op.param1,admin)
                            assist.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                assist1.kickoutFromGroup(op.param1,[op.param2])
                                assist1.findAndAddContactsByMid(op.param1,admin)
                                assist1.inviteIntoGroup(op.param1,admin)
                            except:
                                pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        assist.kickoutFromGroup(op.param1,[op.param2])
                        assist.findAndAddContactsByMid(op.param1,staff)
                        assist.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            assist1.kickoutFromGroup(op.param1,[op.param2])
                            assist1.findAndAddContactsByMid(op.param1,staff)
                            assist1.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                assist2.kickoutFromGroup(op.param1,[op.param2])
                                assist2.findAndAddContactsByMid(op.param1,staff)
                                assist2.inviteIntoGroup(op.param1,staff)
                            except:
                                pass

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["RAreadPoint"]:
                   if op.param2 in Setmain["RAreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["RAreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = kingbii.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           kingbii.sendMessage(msg.to, wait["Respontag"])
                           kingbii.sendMessage(msg.to, None, contentMetadata={"STKID":"7839705","STKPKGID":"1192862","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           kingbii.mentiontag(msg.to,[msg._from])
                           kingbii.sendMessage(msg.to, "Jangan tag saya....")
                           kingbii.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    kingbii.sendMessage(msg.to,"「Cek ID Sticker」\n🔰 STKID : " + msg.contentMetadata["STKID"] + "\n🔰 STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n🔰 STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    kingbii.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = kingbii.getContact(msg.contentMetadata["mid"])
                        path = kingbii.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        kingbii.sendMessage(msg.to,"• Pemain : " + msg.contentMetadata["displayName"] + "\n• UID : " + msg.contentMetadata["mid"] + "\n• Status : " + contact.statusMessage + "\n• Foto linknya : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        kingbii.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    kingbii.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    kingbii.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = kingbii.getContact(msg.contentMetadata["mid"])
                        path = kingbii.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        kingbii.sendMessage(msg.to,"🔰 Nama : " + msg.contentMetadata["displayName"] + "\n🔰 MID : " + msg.contentMetadata["mid"] + "\n🔰 Status Msg : " + contact.statusMessage + "\n🔰 Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        kingbii.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        kingbii.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        kingbii.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        kingbii.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        kingbii.sendMessage(msg.to,"Contact itu bukan anggota bot saints")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        kingbii.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        kingbii.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        kingbii.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        kingbii.sendMessage(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        kingbii.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        kingbii.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        kingbii.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        kingbii.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        kingbii.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        kingbii.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        kingbii.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        kingbii.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        kingbii.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        kingbii.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        kingbii.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        kingbii.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = kingbii.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            kingbii.sendText(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = kingbii.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     kingbii.updateGroupPicture(msg.to, path)
                     kingbii.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["RAfoto"]:
                            path = kingbii.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][mid]
                            kingbii.updateProfilePicture(path)
                            kingbii.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["RAfoto"]:
                            path = assist.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Amid]
                            assist.updateProfilePicture(path)
                            assist.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["RAfoto"]:
                            path = assist1.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Bmid]
                            assist1.updateProfilePicture(path)
                            assist1.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["RAfoto"]:
                            path = assist2.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Cmid]
                            assist2.updateProfilePicture(path)
                            assist2.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Zmid in Setmain["RAfoto"]:
                            path = ghost.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Zmid]
                            ghost.updateProfilePicture(path)
                            ghost.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = assist.downloadObjectMsg(msg_id)
                     path2 = assist1.downloadObjectMsg(msg_id)
                     path3 = assist2.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     assist.updateProfilePicture(path1)
                     assist.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     assist1.updateProfilePicture(path2)
                     assist1.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     assist2.updateProfilePicture(path3)
                     assist2.sendMessage(msg.to, "Berhasil mengubah foto profile bot")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        kingbii.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               kingbii.sendMessage(msg.to,"Masih Percobaan",{'AGENT_ICON':'http://dl.profile.line-cdn.net','AGENT_LINK':'line.me/ti/p/~whiterascals1'}) str(helpMessage))
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                kingbii.sendText(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                kingbii.sendText(msg.to, "Selfbot dinonaktifkan")

                        elif cmd == "self":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               selfMessage = self()
                               kingbii.sendMessage(msg.to,"Masih Percobaan",{'AGENT_ICON':'http://dl.profile.line-cdn.net','AGENT_LINK':'line.me/ti/p/~whiterascals1'}) str(selfMessage))
                                            
                        elif cmd == "group":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               groupMessage = group()
                               kingbii.sendMessage(msg.to,"Masih Percobaan",{'AGENT_ICON':'http://dl.profile.line-cdn.net','AGENT_LINK':'line.me/ti/p/~whiterascals1'}) str(groupMessage))

                        elif cmd == "media":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               mediaMessage = media()
                               kingbii.sendMessage(msg.to,"Masih Percobaan",{'AGENT_ICON':'http://dl.profile.line-cdn.net','AGENT_LINK':'line.me/ti/p/~whiterascals1'}) str(mediaMessage))

                        elif cmd == "bot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               botMessage = bot()
                               kingbii.sendMessage(msg.to,"Masih Percobaan",{'AGENT_ICON':'http://dl.profile.line-cdn.net','AGENT_LINK':'line.me/ti/p/~whiterascals1'}) str(botMessage))

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                md = "┏━━━━━━━「 SETTING RASCALS 」━━━━━━━\n\n"
                                if wait["sticker"] == True: md+="┃≛ Cek Sticker ID ✔\n"
                                else: md+="┃≛ Cek Sticker ID ✖\n"
                                if wait["contact"] == True: md+="┃≛ Cek Contact ✔\n"
                                else: md+="┃≛ Cek Contact ✖\n"
                                if wait["talkban"] == True: md+="┃≛ Talkban ✔\n"
                                else: md+="┃≛ Talkban ✖\n"
                                if wait["Mentionkick"] == True: md+="┃≛ Detect Mention Kick ✔\n"
                                else: md+="┃≛ Detect Mention Kick ✖\n"
                                if wait["detectMention"] == True: md+="┃≛ Detect Mention  ✔\n"
                                else: md+="┃≛ Detect Mention  ✖\n"
                                if wait["autoJoin"] == True: md+="┃≛ Auto Join ✔\n"
                                else: md+="┃≛ Auto Join ✖\n"
                                if wait["autoAdd"] == True: md+="┃≛ Auto Add ✔\n"
                                else: md+="┃≛ Auto Add ✖\n"
                                if msg.to in welcome: md+="┃≛ Welcomemessage ✔\n"
                                else: md+="┃≛ Welcomemessage ✖\n"
                                if wait["autoLeave"] == True: md+="┃≛ Auto Leave ✔\n"
                                else: md+="┃≛ Auto Leave ✖\n"
                                if msg.to in protectqr: md+="┃≛ Protect QR ✔\n"
                                else: md+="┃≛ Protect QR ✖\n"
                                if msg.to in protectjoin: md+="┃≛ Protect JOIN ✔\n"
                                else: md+="┃≛ Protect JOIN ✖\n"
                                if msg.to in protectkick: md+="┃≛ Protect ✔\n"
                                else: md+="┃≛ Protect ✖\n"
                                if msg.to in protectcancel: md+="┃≛ Protect CANCEL ✔\n"
                                else: md+="┃≛ Protect CANCEL ✖\n┗━━━━━━━"
                                kingbii.sendMessage(msg.to, md)

                        elif cmd == "edited" or text.lower() == 'edited':
                            if msg._from in admin:
                                kingbii.sendText(msg.to,"Edited :\n🔰 WRFamily\n\nSupport :\n🔰 RAFamily\n🔰 Sainst Bot ") 
                                ma = ""
                                for i in creator:
                                    ma = kingbii.getContact(i)
                                    kingbii.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "🔰 WRSelfbot Version 1\n")
                               kingbii.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               kingbii.sendMessage1(msg)

                        elif text.lower() == "mid":
                               kingbii.sendMessage(msg.to,"Masih Percobaan",{'AGENT_ICON':'http://dl.profile.line-cdn.net','AGENT_LINK':'line.me/ti/p/~whiterascals1'}) msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = kingbii.getContact(key1)
                               kingbii.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               kingbii.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = kingbii.getContact(key1)
                               kingbii.sendMessage(msg.to, " Nama : "+str(mi.displayName)+"\n UID : " +key1+"\n Status "+str(mi.statusMessage))
                               kingbii.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   kingbii.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   kingbii.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               kingbii.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               kingbii.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               kingbii.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               kingbii.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Zmid}
                               kingbii.sendMessage1(msg)

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   kingbii.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   assist.removeAllMessages(op.param2)
                                   assist1.removeAllMessages(op.param2)
                                   assist2.removeAllMessages(op.param2)
                                   kingbii.sendText(msg.to,"Chat dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = kingbii.getGroupIdsJoined()
                               for group in saya:
                                   kingbii.sendMessage(group,"[ Broadcast ]\n" + str(pesan))

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "Tunggu sebentar...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               kingbii.sendMessage(msg.to, "Silahkan gunakan seperti semula...")
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               kingbii.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = kingbii.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                kingbii.sendMessage(msg.to, "🔰 WRFamily Info Group\n\n• Group Name : {}".format(G.name)+ "\n• GID : {}".format(G.id)+ "\n• Pembuat : {}".format(G.creator.displayName)+ "\n• Waktu Dibuat : {}".format(str(timeCreated))+ "\n• Jumlah Member : {}".format(str(len(G.members)))+ "\n• Jumlah Pending : {}".format(gPending)+ "\n• Group Qr : {}".format(gQr)+ "\n• Group Ticket : {}".format(gTicket))
                                kingbii.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                kingbii.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                kingbii.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogroup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = kingbii.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = kingbii.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "🔰 WRFamily Info Group\n"
                                ret_ += "\n• Nama Group : {}".format(G.name)
                                ret_ += "\n• ID Group : {}".format(G.id)
                                ret_ += "\n• Pembuat : {}".format(gCreator)
                                ret_ += "\n• Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n• Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n• Jumlah Pending : {}".format(gPending)
                                ret_ += "\n• Group Qr : {}".format(gQr)
                                ret_ += "\n• Group Ticket : {}".format(gTicket)
                                ret_ += "\nEdited : 🔰 WRFamily\nSupport : 🔰 RAFamily"
                                kingbii.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = kingbii.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = kingbii.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "↦ "+ str(no) + ". " + mem.displayName
                                kingbii.sendMessage(to,"Info Member Di Group :  " + str(G.name) + " \n\nNama Anggota :\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = kingbii.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = kingbii.getGroup(i)
                                if ginfo == group:
                                    assist.leaveGroup(i)
                                    assist1.leaveGroup(i)
                                    assist2.leaveGroup(i)
                                    assist3.leaveGroup(i)
                                    assist4.leaveGroup(i)
                                    assist5.leaveGroup(i)
                                    assist6.leaveGroup(i)
                                    assist7.leaveGroup(i)
                                    assist8.leaveGroup(i)
                                    assist9.leaveGroup(i)
                                    kingbii.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kingbii.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.displayName+ "\n"
                               kingbii.sendMessage(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kingbii.getGroupIdsJoined()
                               for i in gid:
                                   G = kingbii.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "» " + str(a) + ". " +G.name+ "\n"
                               kingbii.sendMessage(msg.to,"Group anda\n\n"+ma+"\n Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "buka qr":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = kingbii.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   kingbii.updateGroup(X)
                                   kingbii.sendMessage(msg.to, "Qr Group Telah Di Buka")

                        elif cmd == "tutup qr":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = kingbii.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   kingbii.updateGroup(X)
                                   kingbii.sendMessage(msg.to, "Url Closed")

                        elif cmd == "qr group":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = kingbii.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      kingbii.updateGroup(x)
                                   gurl = kingbii.reissueGroupTicket(msg.to)
                                   kingbii.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "changegg":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                kingbii.sendText(msg.to,"Send Image")
                                
                        elif cmd == ".g image":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAfoto"][mid] = True
                                kingbii.sendText(msg.to,"Send Image")
                                
                        elif cmd == ".g image1":
                            if msg._from in admin:
                                Setmain["RAfoto"][Amid] = True
                                assist.sendText(msg.to,"Send Image")
                                
                        elif cmd == ".g image2":
                            if msg._from in admin:
                                Setmain["RAfoto"][Bmid] = True
                                assist1.sendText(msg.to,"Send Image")
                                
                        elif cmd == ".g image3":
                            if msg._from in admin:
                                Setmain["RAfoto"][Cmid] = True
                                assist2.sendText(msg.to,"Send Image")
                                
                        elif cmd == "ghostimage":
                            if msg._from in admin:
                                Setmain["RAfoto"][Zmid] = True
                                ghost.sendText(msg.to,"Send Image")

                        elif cmd.startswith(".g name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kingbii.getProfile()
                                profile.displayName = string
                                kingbii.updateProfile(profile)
                                kingbii.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith(".g assist: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = assist.getProfile()
                                profile.displayName = string
                                assist.updateProfile(profile)
                                assist.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith(".g assist1: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = assist1.getProfile()
                                profile.displayName = string
                                assist1.updateProfile(profile)
                                assist1.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith(".g assist2: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = assist2.getProfile()
                                profile.displayName = string
                                assist2.updateProfile(profile)
                                assist2.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith(".g ghost: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ghost.getProfile()
                                profile.displayName = string
                                ghost.updateProfile(profile)
                                ghost.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "mention" or text.lower() == '😆':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                               if jml <= 100:
                                   mentionMembers(msg.to, nama)
                               if jml > 100 and jml < 200:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (100, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 200 and jml < 300:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (100, 199):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (200, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 300 and jml < 400:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (100, 199):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (200, 299):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (300, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 400 and jml < 500:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (100, 199):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (200, 299):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (300, 399):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (400, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +kingbii.getContact(m_id).displayName + "\n"
                                kingbii.sendMessage(msg.to,"🔰 WRFamily List Bot\n\n"+ma+"\nTotal「%s」Family Bots" %(str(len(Bots))))

                        elif cmd == "protectlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +kingbii.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +kingbii.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +kingbii.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                kingbii.sendMessage(msg.to,"🔰 WRFamily Protect Group\n\n🔰 PROTECT URL :\n"+ma+"\n🔰 PROTECT KICK :\n"+mb+"\n🔰 PROTECT JOIN :\n"+md+"\n🔰 PROTECT CANCEL:\n"+mc+"\nTotal「%s」Grup yg dijaga" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel))))

                        elif cmd == "absen":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                kingbii.sendMessage(msg.to,responsename)
                                assist.sendMessage(msg.to,responsename1)
                                assist1.sendMessage(msg.to,responsename2)
                                assist2.sendMessage(msg.to,responsename3)

                        elif cmd == "invitebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Bmid,Cmid,Amid]
                                    kingbii.inviteIntoGroup(msg.to, anggota)
                                    assist1.acceptGroupInvitation(msg.to)
                                    assist2.acceptGroupInvitation(msg.to)
                                    assist.acceptGroupInvitation(msg.to)
                                except:
                                    pass

                        elif cmd == "assist in":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = kingbii.getGroup(msg.to)
                                ginfo = kingbii.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kingbii.updateGroup(G)
                                invsend = 0
                                Ticket = kingbii.reissueGroupTicket(msg.to)
                                assist.acceptGroupInvitationByTicket(msg.to,Ticket)
                                assist1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                assist2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = assist2.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                assist2.updateGroup(G)

                        elif cmd == "assist out":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = kingbii.getGroup(msg.to)
                                assist.sendText(msg.to, "Maaf saya keluar dulu dari group "+str(G.name))
                                assist.leaveGroup(msg.to)
                                assist1.sendText(msg.to, "Maaf saya keluar dulu dari group "+str(G.name))
                                assist1.leaveGroup(msg.to)
                                assist2.sendText(msg.to, "Maaf saya keluar dulu dari group "+str(G.name))
                                assist2.leaveGroup(msg.to)
                                
                        elif cmd == "inti bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendText(msg.to, "Bye bye fams "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = kingbii.getGroupIdsJoined()
                                for i in gid:
                                    h = kingbii.getGroup(i).name
                                    if h == ng:
                                        assist.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                                        assist.leaveGroup(i)
                                        assist1.leaveGroup(i)
                                        assist2.leaveGroup(i)
                                        kingbii.sendMessage(to,"Berhasil keluar dari grup " +h)

                        elif cmd == "assist":
                            if msg._from in admin:
                                G = kingbii.getGroup(msg.to)
                                ginfo = kingbii.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kingbii.updateGroup(G)
                                invsend = 0
                                Ticket = kingbii.reissueGroupTicket(msg.to)
                                assist.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = assist.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                assist.updateGroup(G)

                        elif cmd == "assist1":
                            if msg._from in admin:
                                G = kingbii.getGroup(msg.to)
                                ginfo = kingbii.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kingbii.updateGroup(G)
                                invsend = 0
                                Ticket = kingbii.reissueGroupTicket(msg.to)
                                assist1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = assist1.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                assist1.updateGroup(G)

                        elif cmd == "assist2":
                            if msg._from in admin:
                                G = kingbii.getGroup(msg.to)
                                ginfo = kingbii.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kingbii.updateGroup(G)
                                invsend = 0
                                Ticket = kingbii.reissueGroupTicket(msg.to)
                                assist2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = assist2.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                assist2.updateGroup(G)

                        elif cmd == "ghost in":
                            if msg._from in admin:
                                G = kingbii.getGroup(msg.to)
                                ginfo = kingbii.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kingbii.updateGroup(G)
                                invsend = 0
                                Ticket = kingbii.reissueGroupTicket(msg.to)
                                ghost.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ghost.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ghost.updateGroup(G)

                        elif cmd == "ghost out":
                            if msg._from in admin:
                                G = kingbii.getGroup(msg.to)
                                ghost.leaveGroup(msg.to)

                        elif cmd == "stime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "🔰 |SB| Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "time" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               cl.sendMessage(msg.to, "Tunggu Sebentar")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['RAreadPoint'][msg.to] = msg_id
                                 Setmain['RAreadMember'][msg.to] = {}
                                 cl.sendText(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['RAreadPoint'][msg.to]
                                 del Setmain['RAreadMember'][msg.to]
                                 cl.sendText(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['RAreadPoint']:
                                if Setmain['RAreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['RAreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['RAreadPoint'][msg.to]
                                        del Setmain['RAreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['RAreadPoint'][msg.to] = msg.id
                                    Setmain['RAreadMember'][msg.to] = {}
                                else:
                                    cl.sendText(msg.to, "User kosong...")
                            else:
                                cl.sendText(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  cl.sendMessage(msg.to, "Sudak tidak aktif")

#===========Hiburan============#
                        elif cmd.startswith("sholat: "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「Jadwal Sholat」"
                                         ret_ += "\n🔰 Lokasi : " + data[0]
                                         ret_ += "\n🔰 " + data[1]
                                         ret_ += "\n🔰 " + data[2]
                                         ret_ += "\n🔰 " + data[3]
                                         ret_ += "\n🔰 " + data[4]
                                         ret_ += "\n🔰 " + data[5]
                                         ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("cuaca: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "「Status Cuaca」"
                                    ret_ += "\n🔰 Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n🔰 Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n🔰 Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n🔰 Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n🔰 Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("lokasi: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "「Info Lokasi」"
                                    ret_ += "\n🔰 Location : " + data[0]
                                    ret_ += "\n🔰 Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                cl.sendMessage(msg.to,str(ret_))

                        elif cmd.startswith("lirik: "):
                           if msg._from in admin:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                   try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          songs = song[5]
                                          lyric = songs.replace('ti:','Title - ')
                                          lyric = lyric.replace('ar:','Artist - ')
                                          lyric = lyric.replace('al:','Album - ')
                                          removeString = "[1234567890.:]"
                                          for char in removeString:
                                              lyric = lyric.replace(char,'')
                                          ret_ = "╔══[ Lyric ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Finish ]\n\nLirik nya :\n{}".format(str(lyric))
                                          cl.sendText(msg.to, str(ret_))
                                   except:
                                       cl.sendText(to, "Lirik tidak ditemukan")
                            
                        elif cmd.startswith("music: "):
                           if msg._from in admin:
                              sep = msg.text.split(" ")
                              search = msg.text.replace(sep[0] + " ","")
                              params = {'songname': search}
                              with requests.session() as web:
                                  web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                  r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                  try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          ret_ = "╔══[ Music ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Waiting Audio ]"
                                      cl.sendText(msg.to, str(ret_))
                                      cl.sendText(msg.to, "Mohon bersabar musicnya lagi di upload")
                                      cl.sendAudioWithURL(msg.to, song[3])
                                  except:
                                      cl.sendText(to, "Musik tidak ditemukan")

                        elif cmd.startswith("gimage: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "https://api.xeonwz.ga/api/image/google?q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["data"] != []:
                                    start = timeit.timeit()
                                    items = data["data"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendText(msg.to,"「Google Image」\nType : Search Image\nTime taken : %seconds" % (start))
                                    cl.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("ytmp4: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n🔰 Author : ' + str(vid.author)
                                    durasi = '\n🔰 Duration : ' + str(vid.duration)
                                    suka = '\n🔰 Likes : ' + str(vid.likes)
                                    rating = '\n🔰 Rating : ' + str(vid.rating)
                                    deskripsi = '\n🔰 Deskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))

                        elif cmd.startswith("ytmp3: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n🔰 Author : ' + str(vid.author)
                                    durasi = '\n🔰 Duration : ' + str(vid.duration)
                                    suka = '\n🔰 Likes : ' + str(vid.likes)
                                    rating = '\n🔰 Rating : ' + str(vid.rating)
                                    deskripsi = '\n🔰 Deskripsi : ' + str(vid.description)
                                cl.sendImageWithURL(msg.to, me)
                                cl.sendAudioWithURL(msg.to, shi)
                                cl.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))

                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['user']['full_name'])
                                bioIG = str(data['user']['biography'])
                                mediaIG = str(data['user']['media']['count'])
                                verifIG = str(data['user']['is_verified'])
                                usernameIG = str(data['user']['username'])
                                followerIG = str(data['user']['followed_by']['count'])
                                profileIG = data['user']['profile_pic_url_hd']
                                privateIG = str(data['user']['is_private'])
                                followIG = str(data['user']['follows']['count'])
                                link = "🔰 Link : " + "https://www.instagram.com/" + instagram
                                text = "🔰 Name : "+namaIG+"\n🔰 Username : "+usernameIG+"\n🔰 Biography : "+bioIG+"\n🔰 Follower : "+followerIG+"\n🔰 Following : "+followIG+"\n🔰 Post : "+mediaIG+"\n🔰 Verified : "+verifIG+"\n🔰 Private : "+privateIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"🔰 I N F O R M A S I 🔰\n\n"+"🔰 Date Of Birth : "+lahir+"\n🔰 Age : "+usia+"\n🔰 Ultah : "+ultah+"\n🔰 Zodiak : "+zodiak)

                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["RAlimit"] = num
                                cl.sendText(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendText(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["RAlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        cl.sendText(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendText(msg.to,str(e))
                                else:
                                    cl.sendText(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kc.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      ki.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      kk.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      kc.sendMessage(midd, str(Setmain["RAmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Semua pro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Semua pro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

#===========KICKOUT============#
                        elif ("Nk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass

                        elif ("Kick1 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendText(msg.to,"Berhasil di Refresh...")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                cl.sendText(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                cl.sendText(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                cl.sendText(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendText(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                cl.sendText(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                cl.sendText(msg.to,"Auto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendText(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendText(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                cl.sendText(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendText(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendText(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendText(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                cl.sendText(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                cl.sendText(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                cl.sendText(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                cl.sendText(msg.to,"Notag dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"🔰 |SB| Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"🔰 |SB| Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"Sukses membersihkan " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["RAmessage1"] = spl
                                  cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["RAmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group2 = kk.findGroupByTicket(ticket_id)
                                     kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kk.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group3 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kc.sendMessage(msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
