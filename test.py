import seciqlib

# 3DES region
data = seciqlib.getData("./3DES/3des-6.cfile")
#seciqlib.plotSpectrogram(data, 0.53, '3des.1')
#seciqlib.plotFFT(data, 0.53, '3des.1')
#seciqlib.plotPSD(data, 0.53, '3des-psd')
#seciqlib.plotWaveform(data, 0.53, '3des-wave')
seciqlib.plotScatter(data, 0.53, '3des-scatter')

# AES region
data = seciqlib.getData("./AES/aes-2.cfile")
#seciqlib.plotSpectrogram(data, 7.40, 'aes.1')
#seciqlib.plotFFT(data, 7.40, 'aes.1')
#seciqlib.plotPSD(data, 7.40, 'aes-psd')
#seciqlib.plotWaveform(data, 7.40, 'aes-wave')
seciqlib.plotScatter(data, 0.53, 'aes-scatter')
