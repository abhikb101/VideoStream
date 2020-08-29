from flask import Flask, render_template, Response,send_file,redirect,render_template, request,jsonify
from camera import VideoCamera


# App Globals (do not edit)
app = Flask(__name__)
video_camera = VideoCamera(flip=False) # creates a camera object, flip vertically


video_camera = VideoCamera(flip=False)

def gen(camera):
    while True:
        camera.rotation = 180
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def pen(camera):
    camera.rotation = 180
    frame = camera.get_frame()
    yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/imageclick')
def imageclick():
   return Response(pen(video_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_feed')
def video_feed():

    return Response(gen(video_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def home():
   app.run(host='0.0.0.0', debug=False, threaded=True)

