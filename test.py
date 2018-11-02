import seciqlib
import numpy as np

window = 0.08

# 3DES region
data = seciqlib.getData("./3DES/3des-6.cfile")
#seciqlib.plotSpectrogram(data, 0.53, window, '3des.1')
#seciqlib.plotFFT(data, 0.53, window, '3des.1')
#seciqlib.plotPSD(data, 0.53, window, '3des-psd')
#seciqlib.plotWaveform(data, 0.53, window, '3des-wave')
#seciqlib.plotScatter(data, 0.53, window, '3des-scatter')
#fftdata = seciqlib.getFFTVector(data, 0.53, window)
fftVector = seciqlib.getNormalizedFFTVector(data, 0.53, window)
print(len(fftVector))
print(type(fftVector))
print(min(fftVector))
print(max(fftVector))
print("fftVector=", fftVector)


"""
# Saving FFT vectors to *.npy files
# =================================
data = seciqlib.getData("./3DES/3des-6.cfile")
fftdata = seciqlib.getFFTVector(data, 0.53, window)
# save an FFT vector to a *.npy file and load it back
print("fftdata=", fftdata)
print("len(fftdata)=", len(fftdata))
print("max(fftdata)=", max(fftdata))
np.save("fft-segment", fftdata)
print("\n Loading...\n")
fftloaded = np.load("fft-segment.npy")
print("fftloaded=", fftloaded)
print("len(fftloaded)=", len(fftloaded))
print("max(fftloaded)=", max(fftloaded))
"""


###############################################################################
# AES region
data = seciqlib.getData("./AES/aes-2.cfile")
#seciqlib.plotSpectrogram(data, 7.40, window, 'aes.1')
#seciqlib.plotFFT(data, 7.40, window, 'aes.1')
#seciqlib.plotPSD(data, 7.40, window, 'aes-psd')
#seciqlib.plotWaveform(data, 7.40, window, 'aes-wave')
#seciqlib.plotScatter(data, 7.40, window, 'aes-scatter')
#fftdata = seciqlib.getFFTVector(data, 7.40, window)
fftVector = seciqlib.getNormalizedFFTVector(data, 7.40, window)
print(len(fftVector))
print(type(fftVector))
print(min(fftVector))
print(max(fftVector))
print("fftVector=", fftVector)

