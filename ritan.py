# -*- coding: utf-8 -*-
# Codding By tanysyz & Ari Restu
from linepy import *
from akad.ttypes import *
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse, ffmpy, pafy, wikipedia, atexit, datetime, goslate

# For login to Bot
client = LINE("EuGL9zPQIA7mdpoD00n1.42RYi7B1FAzLHEuXpgu90q.lBe2WRsxAweV1krXRI7A0zvvGc46/va1z+bA/ql98aI=")
client.log("Auth Token : " + str(client.authToken))
channelToken = client.getChannelResult()
client.log("Channel Token : " + str(channelToken))

wait = {
    'autoJoin':True,
    }
# For about Token
tokenOpen = codecs.open("toket.json","r","utf-8")
token = json.load(tokenOpen)

# For about profile
mid = client.profile.mid
clientProfile = client.getProfile()
clientSettings = client.getSettings()
clientMID = client.profile.mid 
oepoll = OEPoll(client)
Bots = [mid]
listToken = ['desktopmac','desktopwin','iosipad','chromeos','win10','clovafriends']

# For def or class
def sendMessageWithContent(to, text, name, url, iconlink):
    contentMetadata = {
        'AGENT_NAME': name,
        'AGENT_LINK': url,
        'AGENT_ICON': iconlink
        }
    return client.sendMessage(to, text, contentMetadata, 0)

def Rie(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Ri'
        client.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        client.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMentionTan(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Meka Finee "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@i") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@i")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    client.sendMessage(to, textx, {'AGENT_NAME':'「 Helps Message 」', 'AGENT_LINK': 'line://ti/p/~{}'.format(client.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + client.getProfile().picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def sendMentionRi(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Meka Finee "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    client.sendMessage(to, textx, {'AGENT_NAME':'「 Helps Message 」', 'AGENT_LINK': 'line://ti/p/~{}'.format(client.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + client.getProfile().picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def helps():
    helpsMessage = "" + " ╔─「 List Token 」\n" + \
                  "" + " │ •" + "Desktopmac" + "\n" + \
                  "" + " │ •" + "Desktopwin" + "\n" + \
                  "" + " │ •" + "Iosipad" + "\n" + \
                  "" + " │ •" + "Chromeos" + "\n" + \
                  "" + " │ •" + "Win10" + "\n" + \
                  "" + " │ •" + "Clovafriends" + "\n" + \
                  "" + " ╠─「Ex: .token win10」" +  "\n" + \
                  "" + " │ 「Creator」" + "\n" + \
                  "" + " │ • @! " + "\n" + \
                  "" + " │ • @! " + "\n" + \
                  "" + " ╚─「Jika sudah ketik .done」"
    return helpsMessage

def sendMentionV2(receiver, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    client.sendMessage(receiver, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

# For Bot/assist
def lineBot(op):
    global token
    try:
        if op.type == 0:
            return
        if op.type == 22:
            print("「 22 」 Leave ROOM!")
            client.leaveRoom(op.param1)
        if op.type == 24:
            print("「 24 」 ROOM NGNTD!")
            client.leaveRoom(op.param1)
        if op.type == 13:
            if mid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots :
                        client.acceptGroupInvitation(op.param1)
                        ginfo = client.getGroup(op.param1)
                        client.sendMessage(op.param1,"Thanks For invite me " + str(ginfo.name))
                        #client.leaveGroup(op.param1)
                    else:
                        client.acceptGroupInvitation(op.param1)
                        ginfo = client.getGroup(op.param1)
                        client.sendMessage(op.param1,"Hy.. Thanks for invite me to " + str(ginfo.name) + "\nType help for look the command")
        if op.type == 26:
            print("「 26 」 MENERIMA MESSAGE!")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != client.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    pass
                if text.lower() == "help":
                    text = helps()
                    mids = ["udf060a89ebb2af83af77edddb767c329","ue36af223b6f57da66585e5313c653dd1"]
                    client.sendMentionRi(to, str(text), mids)
                    text = helps()

                elif text.lower().startswith(".token"):
                    separate = text.split(" ")
                    username = text.replace(separate[0] + " ","")
                    if username.lower() in listToken:
                        r = requests.get('https://api.eater.tech/{}'.format(username.upper()))
                        data = json.loads(r.text)
                        qrz = data['result'][0]['linkqr']
                        token['data'] = {
                            '{}'.format(sender): {
                                'jenisToken': '{}'.format(username.upper()),
                                'token': data['result'][0]['linktkn']
                                }
                            }
                        sendMentionV2(to, 'Hi @! Click this link!\n{}\nIf you done type (.done)'.format(qrz), [sender])
                    else:
                        sendMentionV2(to, "Ketik yang bener ngentod @! , sesuaikan sama Help kontol!\nGk bisa baca lo anjg!")

                elif text.lower() == ".done":
                    a = token['data']['{}'.format(sender)]['token']
                    req = requests.get('{}'.format(a))
                    b = req.text
                    contact = client.getContact(sender)
                    yan_ = " [ Result Token ] "
                    yan_ += "\n\nName : @!"
                    yan_ += "\nMid : {} ".format(str(contact.mid))
                    yan_ += "\nYour Token : {} ".format(str(b))
                    yan_ += "\nType Token : {} ".format(str(token['data']['{}'.format(sender)]['jenisToken']))
                    sendMentionV2(to, str(yan_), [contact.mid])

        if op.type == 25:
            print("「 25 」 SEND MESSAGE!")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != client.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    pass
                elif text.lower()== "autojoin on":
                  if wait['autoJoin'] == True:
                        client.sendMessage(msg.to,"αυтσʝσιи ѕєт тσ σи")
                      #else:
                       #client.sendMessage(msg.to,"αυтσʝσιи αℓяєα∂у σи")

                elif text.lower()== "autojoin off":
                  if wait['autoJoin'] == False:
                        client.sendMessage(msg.to,"αυтσʝσιи ѕєт тσ σff")
                    #else:
                       #client.sendMessage(msg.to,"αυтσʝσιи αℓяєα∂у σff")
    except Exception as error:
        print(error)

# For polling bot
while True:
    try:
        ops = oepoll.singleTrace(count=10)
        if ops is not None:
            for op in ops:
                threads = []
                for i in range(1):
                    thread = threading.Thread(target=lineBot(op))
                    threads.append(thread)
                    thread.start()
                    oepoll.setRevision(op.revision)
        for thread in threads:
            thread.join()
    except Exception as e:
        print(e)
