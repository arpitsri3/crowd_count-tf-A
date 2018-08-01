import numpy as np
import cv2
import argparse

font = cv2.FONT_HERSHEY_SIMPLEX
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Crowd Counting')
    parser.add_argument(
        'InputVideo',
        type=str,
        help='Path to Model. Model should be on the same path.'
    )
    parser.add_argument(
        'OutputVideo',
        type=str,
        help='Directory of Model checkpoint folder. Checkpoint should be on the same directory.'
    )
parser.add_argument(
    'countFile',
    type=str,
    help='Path to the test feed. Video file should be on the same path.'
)
args = parser.parse_args()

vid_path = args.InputVideo
out_path = args.OutputVideo
countFile = args.countFile

feed_vid = cv2.VideoCapture(vid_path)
success = True

if success:
    success, im = feed_vid.read()
    print("success-", success)

    fps = feed_vid.get(cv2.CAP_PROP_FPS)

    fps = np.int32(fps)
    print("Frames Per Second:",fps,"\n")

    counter = 0
    tm = 1
    if success:
        video = cv2.VideoWriter(out_path, -1, 1, (im.shape[1], im.shape[0]))

    out = open(countFile, "r")

    while success:
        counter +=1
        img = np.copy(im)
        txt = out.readline(tm)
        if counter <= fps:
            cv2.putText(img, txt, (0, 0), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(img, txt, (0, 0), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            counter = 0
            tm += 1
        video.write(img)
        success, im = feed_vid.read()

out.close()
video.release()
feed_vid.release()
cv2.destroyAllWindows()
