from flask import Flask,render_template,Response
import cv2

app=Flask(__name__)
camera=cv2.VideoCapture(0)

def zoom(img, zoom_factor=2):
    return cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor)

def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        	
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #print(grayFrame[0])
        #cropped = grayFrame[700:1200, 600:1000]
        cropped = grayFrame[425:1400, 800:1100]
        zoomed = zoom(grayFrame, 3)
        grayFrame = zoom(cropped, 1)
        #grayFrame = zoom_at(grayFrame, 1.5, coord=(264.5, 275))
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

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(port=8000, debug=True)

