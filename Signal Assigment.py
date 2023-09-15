import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk melakukan FFT filtering
def fft_filter(signal, cutoff_freq):
    # Lakukan FFT
    fft_result = np.fft.fft(signal)
    
    # Frekuensi yang sesuai dengan setiap titik FFT
    freqs = np.fft.fftfreq(len(signal))
    
    # Buat filter dengan cutoff frequency
    filter = np.ones_like(signal)
    filter[np.abs(freqs) > cutoff_freq] = 0
    
    # Terapkan filter pada FFT
    filtered_fft = fft_result * filter
    
    # Lakukan invers FFT untuk mendapatkan sinyal yang difilter
    filtered_signal = np.fft.ifft(filtered_fft)
    
    return filtered_signal

# Membuat sinyal contoh (misalnya, sinyal sinus)
t = np.linspace(0, 1, 1000, endpoint=False)  # Waktu
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)  # Sinyal gabungan

# Menentukan cutoff frequency untuk filtering
cutoff_frequency = 15  # Frekuensi cutoff dalam Hz

# Melakukan filtering pada sinyal
filtered_signal = fft_filter(signal, cutoff_frequency)

# Plot sinyal asli dan yang difilter
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Sinyal Asli')
plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal)
plt.title('Sinyal yang Difilter (Cutoff Frequency = {} Hz)'.format(cutoff_frequency))
plt.tight_layout()
plt.show()
