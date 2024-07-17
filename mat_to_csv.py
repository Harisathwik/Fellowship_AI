import scipy.io
import os

# load the .mat file
mat = scipy.io.loadmat(os.path.join('D:\Sathwik\Fellowship.AI\Zip files','imagelabels.mat'))['labels'][0]
print(mat, len(mat))
print(len(os.listdir('D:/Sathwik/Fellowship.AI/102flowers/jpg')))

# save the data as txt file.
with open('labels.txt', 'w') as f:
    for each in mat:
        print(each)
        f.write(str(each)+"\n")
