from sklearn import datasets
from sklearn.svm import SVC
from scipy import misc
from resizeimage import resizeimage



# The digits dataset
digits = datasets.load_digits()


features = digits.data 
labels = digits.target


print "Shape Of Dataset :- ",features.shape
# Create a classifier: a support vector classifier
clf = SVC(gamma = 0.001)


# We learn the digits 
clf.fit(features, labels)



# Load Image
img = misc.imread("/home/rupesh/Desktop/Handwriting_ Digit_Recognition/tkInter_Canvas_Test/image.png")


img = misc.imresize(img, (8,8))
img = img.astype(digits.images.dtype)
img = misc.bytescale(img, high=16, low=0)


x_test = []

for eachRow in img:
	for eachPixel in eachRow:
		x_test.append(sum(eachPixel)/3.0)


print "Predicted Digit is := "
print (clf.predict([x_test]))




