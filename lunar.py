import cv2
import numpy as np

# Load the global mosaic image (LRO WAC)
global_mosaic = cv2.imread('luna.webp', 0)  # 0 for grayscale

# Load the input crater image (Chandrayaan-2 TMC)
crater_template = cv2.imread('luna.webp', 0)  # 0 for grayscale

# Perform template matching
result = cv2.matchTemplate(global_mosaic, crater_template, cv2.TM_CCOEFF_NORMED)

# Get the best match location
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Extract coordinates of the best match
top_left = max_loc
h, w = crater_template.shape
bottom_right = (top_left[0] + w, top_left[1] + h)

# Draw a rectangle around the matched region
matched_image = global_mosaic.copy()
cv2.rectangle(matched_image, top_left, bottom_right, 255, 2)

# Display the result
cv2.imshow('Matched Crater', matched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Extract latitude and longitude (you need a function to convert pixel coordinates to lat/long)
latitude, longitude = convert_pixel_to_latlong(top_left[0], top_left[1])
print(f'Crater found at Latitude: {latitude}, Longitude: {longitude}')