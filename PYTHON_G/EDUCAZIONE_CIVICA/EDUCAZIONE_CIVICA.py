import matplotlib as mpl
mpl.use('TKAgg')
import matplotlib.pyplot as plt
import csv

mesi_n = []
temperatura = []
giorni_scuola = []
giorni_giacca = []
giorni_videogiochi = []

data_file = open("dati.csv")
data_reader = csv.reader(data_file, delimiter = ',')
next(data_reader)


for row in data_reader:
    print(row)
    mesi_n.append(float(row[1]))
    temperatura.append(float(row[2]))
    giorni_giacca.append(float(row[3]))
    giorni_scuola.append(float(row[4]))
    giorni_videogiochi.append(float(row[5]))

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
fig.suptitle('Grafici di educazione civica')

ax1.plot(mesi_n, temperatura, 'o-g')
ax1.set_xlabel('Mese')
ax1.set_ylabel('Temperatura')

ax2.plot(mesi_n, giorni_scuola, 'o-r')
ax2.set_xlabel('Mese')
ax2.set_ylabel('Scuola')

ax3.plot(mesi_n, giorni_giacca, 'o-b')
ax3.set_xlabel('Mese')
ax3.set_ylabel('Giacca')

ax4.plot(mesi_n, giorni_videogiochi, 'o-y')
ax4.set_xlabel('Mese')
ax4.set_ylabel('Videogiochi')

plt.show()