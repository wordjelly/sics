import numpy as np
import cv2
import imutils

def gray_image( image ) :

	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)	

def sharpen( image ):
	
	#Create the identity filter, but with the 1 shifted to the right!
	kernel = np.zeros( (9,9), np.float32)
	kernel[4,4] = 2.0   #Identity, times two! 

	#Create a box filter:
	boxFilter = np.ones( (9,9), np.float32) / 81.0

	#Subtract the two:
	kernel = kernel - boxFilter

	#Note that we are subject to overflow and underflow here...but I believe that
	# filter2D clips top and bottom ranges on the output, plus you'd need a
	# very bright or very dark pixel surrounded by the opposite type.
	image = cv2.filter2D(image, -1, kernel)
	cv2.imshow("sharpen",image)
	return image


def erode_image( image ):


	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))	
	image = cv2.dilate(image,kernel,iterations = 1)
	image =  cv2.GaussianBlur(image, (5, 5), 0)
	#cv2.imshow("eroded",image)
	#cv2.imwrite("eroded.jpg",image)
	return image



def thresh ( image ):
	th3 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
	#cv2.imshow("threshold",th3)
	return th3


def smooth ( image ):
	kernel = np.ones((5,5),np.float32)/25
	dst = cv2.filter2D(image,-1,kernel)
	return dst

def find_relevant_contours ( image ):

	##take each contour
	##find how well it corresponds to an arc.
	##find 

	return


# load the image and compute the ratio of the old height
# to the new height, clone it, and resize it
image = cv2.imread("sicst.jpg")
ratio = image.shape[0] / 500.0
image = imutils.resize(image, height = 500)
res_im = image.copy()
image = gray_image(image)
image = thresh(image)
image = erode_image(image)
edged = cv2.Canny(image, 75, 200)


im2, contours, hierarchy = cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(res_im, contours, -1, (0,0,0), 1)
cv2.imwrite("baba.jpg",res_im)
#cv2.imshow("Contoured", res_im)
cv2.waitKey(0)
cv2.destroyAllWindows()


