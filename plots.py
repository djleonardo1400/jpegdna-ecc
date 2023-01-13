import matplotlib.pyplot as plt
import numpy as np

iso_line = np.array([0,1,2])

# Define the data for the first plot
x1 = [0.05, 0.15, 0.3, 0.4, 0.5, 1]
pc1 = [0, 0, 0, 0, 0.0453, 0.85]
wt1 = [0.0205, 0.0411, 0.098, 0.131, 0.183, 1.12]
dr1 = [0, 0, 0.008, 0.018, 0.055, 0.98]

# Define the data for the second plot
x2 = [3, 8, 16, 32, 64]
pc2 = [7.9, 0.051, 0, 0, 0]
wt2 = [7.86, 0.158, 0.105, 0.0913, 0.13]
dr2 = [8.18, 0.078, 0, 0, 0]

# Define the data for the third plot
pcx = [11.811, 14.663, 19.375, 28.779, 47.494]
wtx = [4.679, 5.845, 7.723, 11.455, 18.946]
drx = [3.113, 3.894, 5.154, 7.635, 12.627]

pc3 = [7.9, 0.051, 0, 0, 0]
wt3 = [7.86, 0.158, 0.105, 0.0913, 0.13]
dr3 = [8.18, 0.078, 0, 0, 0]



plt.title("nucleotide alteration vs error correction performance (fixed RS=8)")
plt.xlabel("nucleotide alteration made by random_change() (%)")
plt.ylabel("error between original and decoded file (%)")
plt.xlim(0, 1.2)
plt.ylim(0, 1.15)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
sc1, = plt.plot(x1, pc1, '-o')
sc2, = plt.plot(x1, dr1, '-o')
sc3, = plt.plot(x1, wt1, '-o')
plt.plot(iso_line,linestyle = 'dotted', color='blue')

plt.legend([sc1, sc2, sc3], ["parrots_crop.jpg", "door.jpg","water.jpg"])
plt.show()


plt.title("RS check bits number vs error correction performance (fixed nucleotide alteration=0.5%)")
plt.xlabel("check_size value for RS")
plt.ylabel("error between original and decoded file (%)")
# plt.xlim(0, 1)
# plt.ylim(0, 1.15)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
sc4, = plt.plot(x2, pc2, '-o')
sc5, = plt.plot(x2, dr2, '-o')
sc6, = plt.plot(x2, wt2, '-o')

plt.legend([sc4, sc5, sc6], ["parrots_crop.jpg", "door.jpg","water.jpg"])
plt.show()

plt.title("bit rate vs error correction performance (fixed nucleotide alteration=0.5%)")
plt.xlabel("bit rate (nts/px)")
plt.ylabel("error between original and decoded file (%)")
# plt.xlim(0, 1)
# plt.ylim(0, 1.15)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
sc7, = plt.plot(pcx, pc3, '-o')
sc8, = plt.plot(wtx, dr3, '-o')
sc9, = plt.plot(drx, wt3, '-o')

plt.legend([sc7, sc8, sc9], ["parrots_crop.jpg", "door.jpg","water.jpg"])
plt.show()