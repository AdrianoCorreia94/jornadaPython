# importar matplotlib
#%%
import matplotlib.image as img 
import matplotlib.pyplot as plt

imagem = img.imread('teste.jpeg')

#%%
print(imagem.shape)
print(imagem.size)
plt.imshow(imagem)


# %%
plt.show()
# %%
