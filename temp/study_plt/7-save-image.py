import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from PIL import Image

im = Image.open("marvin.jpg")

# 对比原始图片重建图片
fig = plt.figure(figsize=(2, 2))
gs = gridspec.GridSpec(2, 2)
gs.update(wspace=0.05, hspace=0.05)
for i in range(4):
    ax = plt.subplot(gs[i])
    plt.axis('off')
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_aspect('equal')
    plt.imshow(im)

plt.savefig("save-image.jpg", bbox_inches='tight')