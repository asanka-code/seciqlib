import seciqlib

window = 0.08

# 3DES region
data = seciqlib.getData("./3DES/3des-6.cfile")
#seciqlib.plotSpectrogram(data, 0.53, window, '3des.1')
#seciqlib.plotFFT(data, 0.53, window, '3des.1')
#seciqlib.plotPSD(data, 0.53, window, '3des-psd')
#seciqlib.plotWaveform(data, 0.53, window, '3des-wave')
#seciqlib.plotScatter(data, 0.53, window, '3des-scatter')
fftdata = seciqlib.getFFTVector(data, 0.53, window)


# AES region
#data = seciqlib.getData("./AES/aes-2.cfile")
#seciqlib.plotSpectrogram(data, 7.40, window, 'aes.1')
#seciqlib.plotFFT(data, 7.40, window, 'aes.1')
#seciqlib.plotPSD(data, 7.40, window, 'aes-psd')
#seciqlib.plotWaveform(data, 7.40, window, 'aes-wave')
#seciqlib.plotScatter(data, 7.40, window, 'aes-scatter')
fftdata = seciqlib.getFFTVector(data, 7.40, window)

