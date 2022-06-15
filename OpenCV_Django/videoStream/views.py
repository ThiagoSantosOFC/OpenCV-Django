from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from django.http import HttpResponse
import cv2
import threading

# Create your views here.

@gzip.gzip_page
def home(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(cam.gen(), content_type='multipart/x-mixed-replace;boundary=frame')

    except:
        pass
    return render(request, 'home.html')

# to capture the video class


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')