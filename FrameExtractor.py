import cv2
import numpy as np

def main():

	video_name = "C:\\Users\\AlbusPeter\\Desktop\\Github\\Projects\\FrameExtractor\\test.mp4"
	print "Read Video\n"
	capture = cv2.VideoCapture(video_name)
	
	# length = int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
	# width  = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
	# height = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
	# fps    = cap.get(cv2.cv.CV_CAP_PROP_FPS)
	
	#check if video successfully opened
	if not capture.isOpened():
		print "The video can not open!\n"
		return 0
	
	print "Extract frames...\n"
	skip_num = 30
	count_num = 0
	while(capture.isOpened()):
		ret,frame = capture.read()
		if count_num%skip_num == 0:
			frame_num = count_num/skip_num
			if ret == True:
				frame_name = video_name.split(".")[0] + "_frame" + str(frame_num) + ".jpg"
				cv2.imwrite(frame_name,frame)
			else:
				break
		
		count_num = count_num + 1
	
	capture.release()
	print "Video Capture Done!"

if __name__ == '__main__':
    main()