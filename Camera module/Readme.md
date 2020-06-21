# Pi camera libray 
## Instalation

```
sudo apt-get update
sudo apt-get install python3-picamera
```
## Usage
### Importing library
```
import picamera
camera=picamera.PiCamera() #creating a object
```

### Camera fuctions :Take a picture
``` 
camera.capture("pic.jpg")
```
### View Video on screen
```
camera.start_preview()
camera.stop_preview()
```
## Video Capture
```
import time
camera.start_recoding("vid.h264)
time.sleep(10)
camera.stop_recording()
```
