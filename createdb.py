# Import OpenCV module
import cv2
import sys

# Get the camera
camera = cv2.VideoCapture(0)

# Create the classifier
detector = cv2.CascadeClassifier("data/third/haarcascade_frontalface_default.xml")

record = False
person = sys.argv[1]
filled = (0, 255, 0)
sample = 0

# Show camera until exit signal
while(True):

    # Capture frame-by-frame
    ret, frame = camera.read()

    # Convert camera frame to grayscale
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = detector.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        # Record frames
        if(record):
            sample = sample + 1
            cv2.imwrite(
                "data/photos/" + str(person) + "_" + str(sample) + ".jpg",
                gray[y:y + h, x:x + h])

        cv2.rectangle(frame, (x, y), (x + w, y + h), filled, 2)

    # Display the modified frame
    cv2.imshow('Mirror, Mirror on the Wall...', frame)

    # Record when press 'r' key
    if cv2.waitKey(1) & 0xFF == ord('r'):
        if(record):
            record = False
            sample = 0
            filled = (0, 255, 0)
            print("Stop recording...")
        else:
            record = True
            filled = (255, 0, 0)
            print("It's recording...")

    # Exit when press 'q' key
    elif cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the camera
camera.release()
cv2.destroyAllWindows()
