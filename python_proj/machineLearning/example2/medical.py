import SimpleITK as sitk
import matplotlib.pyplot as plt

# Load a medical image (replace with your actual image path)
image_path = 'path_to_your_medical_image.nii.gz'
image = sitk.ReadImage(image_path)

# Apply Otsu thresholding for segmentation
otsu_filter = sitk.OtsuThresholdImageFilter()
segmented_image = otsu_filter.Execute(image)

# Convert SimpleITK image to numpy array for visualization
image_array = sitk.GetArrayFromImage(image)
segmented_array = sitk.GetArrayFromImage(segmented_image)

# Plot original and segmented images using matplotlib
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image_array[0, :, :], cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(segmented_array[0, :, :], cmap='gray')
plt.title('Segmented Image')

plt.tight_layout()
plt.show()
