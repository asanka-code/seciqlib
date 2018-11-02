
# Reference: http://witestlab.poly.edu/~ffund/el9043/labs/lab1.html


# includes core parts of numpy, matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, fftfreq, fftshift

sampleRate=20000000

'''
# practice reading in complex values stored in a file
# Read in data that has been stored as raw I/Q interleaved 32-bit float samples
dat = np.fromfile("./data/with-aes.cfile", dtype="float32")
sampleRate=20000000

# Turn the interleaved I and Q samples into complex values
# the syntax "dat[0::2]" means "every 2nd value in 
# array dat starting from the 0th until the end"
dat = dat[0::2] + 1j*dat[1::2]

# Note: a quicker way to turn the interleaved I and Q samples  into complex values
# (courtesy of http://stackoverflow.com/a/5658446/) would be:
# dat = dat.astype(np.float32).view(np.complex64)
'''

#########################################################################

def getData(cfileName):
    """
    Given a name of a *.cfile, this function extracts the interleaved
    Inphase-Quadrature data samples and convert it into a numpy array of complex
    data elements. *.cfile format has interleaved I and Q samples where each sample
    is a float32 type. GNURadio Companion (GRC) scripts output data into a file
    though a file sink block in this format.
    Read more in SDR data types: https://github.com/miek/inspectrum
    """
    # Read the *.cfile which has each element in float32 format.
    data = np.fromfile(cfileName, dtype="float32")
    # Take each consecutive interleaved I sample and Q sample to create a single complex element.
    data = data[0::2] + 1j*data[1::2]
    # Return the complex numpy array.
    return data

def getSegment(timeOffset, window):
    """
    Given a starting time offset (seconds) and a time window (seconds), this function
    returns the starting and ending sample indexes of a complex numpy array.
    """
    # Segment starting offset (sample points)
    start = timeOffset * sampleRate
    # Segment ending offset (sample points)
    end = start + (window * sampleRate)
    #print("start=%d", int(start))
    #print("end=%d", int(end))
    #Return the starting index and ending index
    return int(start), int(end)

def plotWaveform(data, timeOffset, window, wavformFileName):
    """
    Given a data set as a complex numpy array, a time offset (seconds), a time window (seconds)
    and a file name for the graph, this function returns the waveform plot as a PDF file.
    """
    # Get the desired starting and ending index of the numpy data array
    start, end = getSegment(timeOffset, window)
    plt.figure()
    # Plot the waveform of the selected sample range of the numpy data array
    plt.plot(data[start:end])
    # Save the waveform into a PDF file
    plt.savefig('./spectrograms/' + wavformFileName +'.pdf', fotmat='pdf', bbox_inches='tight')
    return 1

def plotScatter(data, timeOffset, window, scatterFileName):
    """
    Given a data set as a complex numpy array, a time offset (seconds), a time window (seconds)
    and a file name for the graph, this function returns the scatter plot as a PDF file.
    """
    # Get the desired starting and ending index of the numpy data array
    start, end = getSegment(timeOffset, window)
    # And let's look at it on the complex plane
    # Note that showing *every* data point would be time- and processing-intensive
    # so we'll just show a few
    plt.figure()
    # plot the scatter plot of the selected sample range of the numpy data array
    plt.scatter(np.real(data[start:end]), np.imag(data[start:end]))
    plt.title("Constellation of the 'signal' loaded from file")
    # save the scatter plot into a PDF file
    plt.savefig('./spectrograms/' + scatterFileName +'.pdf', fotmat='pdf', bbox_inches='tight')
    return 1

def plotPSD(data, timeOffset, window, psdFileName):
    """
    Given a data set as a complex numpy array, a time offset (seconds), a time window (seconds)
    and a file name for the graph, this function returns the power spectral density (PSD) plot as a PDF file.
    """
    # Get the desired starting and ending index of the numpy data array
    start, end = getSegment(timeOffset, window)
    plt.figure()
    # plot the PSD of the selected sample range of the numpy data array
    plt.psd(data[start:end], NFFT=1024, Fs=sampleRate)
    # save the PSD plot into a PDF file
    plt.savefig('./spectrograms/' + psdFileName +'.png', fotmat='pdf', bbox_inches='tight')
    return 1
    
def plotFFT(data, timeOffset, window, fftFileName):
    """
    Given a data set as a complex numpy array, a time offset (seconds), a time window (seconds)
    and a file name for the graph, this function returns the FFT plot as a PDF file.
    """
    # Get the desired starting and ending index of the numpy data array
    start, end = getSegment(timeOffset, window)
    # get the length of the selected data sample range        
    N = len(data[start:end])
    # get the time interval beteween each sample
    T = 1.0 / sampleRate
    # calculate the FFT of the selected sample range. But the FFT x axis contains data
    # in the range from 0 to positive values first and at the end the negative values
    # like 0, 1, 2, 3, 4, -4, -3, -2, -1
    yf = fft(data[start:end])
    # get the vector with frequencies of the sample range. But the output contains data
    # in the range from 0 to positive values first and at the end the negative values
    # like 0, 1, 2, 3, 4, -4, -3, -2, -1
    freqs = fftfreq(N, T)
    # shift the frequencies to have it zero-centered, e.g., -4, -3, -2, -1, 0, 1, 2, 3, 4
    shifted_freqs = fftshift(freqs)
    # rearrange the FFT vector to have it zero-centered, e.g., -4, -3, -2, -1, 0, 1, 2, 3, 4
    new_yf = np.concatenate((yf[N/2:N], yf[0:N/2]))
    # plot the FFT vector against the frequencies
    plt.plot(shifted_freqs, np.abs(new_yf))    
    #print('len(shifted_freqs)=%d' % len(shifted_freqs))    
    #print('len(new_yf)=%d' % len(new_yf))        
    # save theFFT plot as a PDF file.
    plt.savefig('./spectrograms/' + fftFileName +'.png', fotmat='pdf', bbox_inches='tight')
    return 1

def plotSpectrogram(data, timeOffset, window, specFileName):
    """
    Given a data set as a complex numpy array, a time offset (seconds), a time window (seconds)
    and a file name for the graph, this function returns the spectrogram plot as a PDF file.
    """
    # Get the desired starting and ending index of the numpy data array
    start, end = getSegment(timeOffset, window)   
    # plot the spectrogram of the selected sample range
    plt.specgram(data[start:end], NFFT=4096, Fs=sampleRate, cmap=plt.cm.get_cmap("Greys"))
    #plt.xlabel("Time (s)")
    #plt.ylabel("Frequency (MHz)")
    plt.axis('off')
    ax = plt.axes()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)    
    # zoom in to the middle of the y-axis because 4 MHz band-pass in the GRC script has caused the
    # other y-axis frequency ranges to be highly attenuated and useless.
    plt.ylim(-2000000, 2000000)    
    # save the spectrogram into a PDF file.
    plt.savefig('./spectrograms/' + specFileName +'.pdf', fotmat='PDF', bbox_inches='tight', pad_inches=0)
    #plt.savefig('spectrogram-from-iq.pdf', fotmat='pdf', bbox_inches='tight')
    return 1
        
def getFFTVector(data, timeOffset, window):
    """
    Given a data set as a complex numpy array, a time offset (seconds), a time window (seconds)
    and a file name for the graph, this function returns the FFT vector as a numpy array.
    """
    # Get the desired starting and ending index of the numpy data array
    start, end = getSegment(timeOffset, window)    
    # get the length of the selected data sample range        
    N = len(data[start:end])
    # calculate the FFT of the selected sample range. But the FFT x axis contains data
    # in the range from 0 to positive values first and at the end the negative values
    # like 0, 1, 2, 3, 4, -4, -3, -2, -1
    yf = fft(data[start:end])
    # rearrange the FFT vector to have it zero-centered, e.g., -4, -3, -2, -1, 0, 1, 2, 3, 4
    new_yf = np.concatenate((yf[N/2:N], yf[0:N/2]))
    # return the absolute values of the FFT vector.
    return np.abs(new_yf)    
    
