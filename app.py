from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Initialize the video capture object
# 0 is typically the default webcam. Change if you have multiple cameras.
video_capture = cv2.VideoCapture(3)

def generate_frames():
    while True:
        # Capture frame-by-frame
        success, frame = video_capture.read()
        if not success:
            break
        else:
            # Encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue
            # Convert the image to bytes
            frame = buffer.tobytes()
            # Yield the output frame in byte format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    # Render the HTML template
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    # Return the response generated along with the specific media type (mime type)
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    try:
        # Run the Flask app
        app.run(host='0.0.0.0', port=5000, debug=False)
    finally:
        # Release the video capture when the app stops
        video_capture.release()
