import cv2
import time

# Video path
video_path = "C:\\Users\\CAGLA\\Desktop\\OpenCV\\OpenCv_image_processing\\2_opening_video\\MOT17-04-DPM.mp4"

# Capture video
cap = cv2.VideoCapture(video_name)  # cap is frames to come from the video

print("Width: ", cap.get(3))
print("Height: ", cap.get(4))

if cap.isOpened() == False:
    print("Failed to capture")

while True:  # Frame is actually an image, we have to loop it so that it can be played as a video
    ret, frame = cap.read()  # We transfer each frame to the frame and whether the frame has come successfully or not to the ret

    if ret == True:  # If reading is successful
        time.sleep(0.01)  # If we don't use it, video will flow too fast
        cv2.imshow("Video", frame)
    else:  # Break if all frames are shown / video is finished (ret == False)
        break

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()  # Stop capture
cv2.destroyAllWindows()  # Close windows
