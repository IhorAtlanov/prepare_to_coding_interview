from numpy import linalg
import numpy as np
import matplotlib.pyplot as plt

PhotoPath = 'C:\\Users\\IhorAtlanov\\Desktop\\Coding\\prepare_to_coding_interview\\SVD\\horse.jpg'
img = plt.imread(PhotoPath)  # Read image and transform it into a NumPy array.

print("img.shape:", img.shape)
print("img:", img)

img_rescaled = img / 255

print("img_rescaled.shape:", img_rescaled.shape)

img_array_transposed = np.transpose(img_rescaled, (2, 0, 1))
U, s, Vt = linalg.svd(img_array_transposed)

print("img_array_transposed.shape:", img_array_transposed.shape)
print("U.shape:", U.shape)
print("s.shape:", s.shape)
print("Vt.shape:", Vt.shape)

Sigma = np.zeros((3, 408, 612))

print("Sigma.shape:", Sigma.shape)

for j in range(3):
    np.fill_diagonal(Sigma[j, :, :], s[j, :])

print("Sigma:", Sigma)

reconstructed = U @ Sigma @ Vt

print("Reconstructed1 shape:", reconstructed.shape)

reconstructed = np.clip(reconstructed, 0, 1)

print("Reconstructed2 shape:", reconstructed.shape)

k = 50
approx_img = U @ Sigma[..., :k] @ Vt[..., :k, :]

print("Approx_img shape:", approx_img)

plt.imshow(np.transpose(approx_img, (1, 2, 0)))

if __name__ == '__main__':
    print(approx_img.shape)
    plt.show()

