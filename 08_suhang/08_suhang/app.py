from flask import Flask, render_template
# import RPi.GPIO as GPIO
# import picamera
import os
import math
iscontinue = 0
path = "./static/album"
cupath = ""
# camera = picamera.PiCamera()
# camera.resolution = (640,480)
# camera.start_preview()
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/gallery/<num>")
def gallery(num):
    data = []
    length = 0
    maxnum = 0
    num = int(num)
    for x in range(0x8):
        if os.path.isdir("%s/" % (path)+str((8*(num-1))+x)) == True:
            data.append("%s/"% (path[8:])+str((8*(num-1))+x))
            length += 1
        else:
            break
    for x in range(0xff):
        if os.path.isdir("%s/" % (path)+str(x)) == True:
            continue
        else:
            maxnum = x
            break
    return render_template("gallery.html",data=data,length=length,num=int(num),maxnum=math.ceil(maxnum/8))

@app.route("/gallery/static/album/<num>")
def gallery_detail(num):
    data = []
    length = 0
    for x in range(1,5):
            if os.path.isfile("%s/" % path+str(num)+"/"+str(x)+".jpg") == True:
                data.append("%s/" % path[8:]+str(num)+"/"+str(x)+".jpg")
                length += 1
            else:
                break
    return render_template("gallery_detail.html",data=data,length=length)

@app.route("/camera")
def camera():
    global cupath,path,iscontinue
    if iscontinue == 0:
        for x in range(0xff):
            if os.path.isdir('%s/' % path+str(x))==True:
                continue
            else:
                os.makedirs('%s/' % path+str(x))
                cupath = '%s/' % path+str(x)

                iscontinue = 1
                break
        return render_template("camera.html")
    else:
        data = []
        for x in range(1,5):
            if os.path.isfile("%s/" % cupath+str(x)+".jpg") == True:
                data.append("%s/"% cupath[8:]+str(x)+".jpg" )
            else:
                data.append("/temp.jpg")
        return render_template("camera.html",data=data)






@app.route("/camera/<num>")
def take_photo(num):
    global iscontinue
    if num == '1':
        camera.capture("%s/1.jpg"% cupath)
        return render_template("camera.html")
    elif num == '2':
        camera.capture("%s/2.jpg"% cupath)
        return render_template("camera.html")
    elif num == '3':
        camera.capture("%s/3.jpg"% cupath)
        return render_template("camera.html")
    elif num == '4':
        camera.capture("%s/4.jpg"% cupath)
        return render_template("camera.html")
    elif num == '5':
        iscontinue =0
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")


