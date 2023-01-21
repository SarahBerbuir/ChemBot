# This file contains Python code to setup the webserver which displays the image data of a webcam
from flask import Flask,render_template,Response
import cv2

app=Flask(__name__)
# Get image data of the USB webcam
camera=cv2.VideoCapture(0)

def zoom(img, zoom_factor=2):
    return cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor)

def generate_frames():
    while True:
            
        ## Read the camera frame
        success,frame=camera.read()
        # Transform the image data in grey tones to save memory	
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cropped = grayFrame[425:1400, 800:1100]
        # Optional zooming
        zoomed = zoom(grayFrame, 3)
        grayFrame = zoom(cropped, 1)
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',grayFrame)
            grayFrame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + grayFrame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

# Generate frames to display images 
@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

# Start webserver on local side
if __name__=="__main__":
    app.run(port=8000, debug=True)

