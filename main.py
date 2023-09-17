import cv2

# Load the images
image1 = cv2.imread("one.jpg")
image2 = cv2.imread("two.jpg")

# Define the regions to be cropped and swapped
# Format: (startY:endY, startX:endX)
target_size = (500, 500)

# Resize image2 for consistency
image2 = cv2.resize(image2, (700, 700))

# Swap the cropped regions
image1[100:300, 100:700] = image2[100:300, 100:700]
image2[300:600, 300:600] = image1[300:600, 300:600]

# Display the modified images
image1 = cv2.resize(image1, target_size)
image2 = cv2.resize(image2, target_size)

cv2.imshow('Image 1 with swapped region', image1)
cv2.imshow('Image 2 with swapped region', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
