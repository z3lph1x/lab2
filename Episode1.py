
from PIL import Image
import numpy as np

file_path = input()
new_file_path = input()
img = Image.open(file_path)
data = np.array(img)

A = data.min()
Z = data.max()

updated_data = float(255)*(data - A)/(Z-A)
# запись картинки после обработки
res_img = Image.fromarray(updated_data.astype(np.uint8))
res_img.save(new_file_path)

