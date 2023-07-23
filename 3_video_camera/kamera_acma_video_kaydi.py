import cv2

# capture
cap = cv2.VideoCapture(0)  # 0 == default camera, cap == frames from our video camera

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width, height)

# As the frames are read and visualized on our screen, they will also be recorded on the video recorder:
writer = cv2.VideoWriter("video_record.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 20, (width, height))  # writer is a frame repo
# "video_record.mp4" --> name of the video to be recorded
# cv2.VideoWriter_fourcc(*"DIVX") --> 4-character codec used to compress frames
# 20 --> frame per second
# (width, height) --> size of the video recorder

while True:
    ret, frame = cap.read()  # We transfer each frame to the frame and whether the frame has come successfully or not to the ret.

    cv2.imshow("Video", frame)  # show the video
    writer.write(frame)  # save the video (show the video and at the same time record it)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break  # stop recording when press q

cap.release()  # Stop capture
writer.release()  # Stop writing
cv2.destroyAllWindows()  # Destroy windows
