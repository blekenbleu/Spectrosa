# https://www.earthinversion.com/utilities/efficiently-compute-spectrogram-in-python-using-librosa/
import sys
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

def plot_spectrogram(audio_path, argv = ''):
    # play with hop_length and nfft values
    hop_length = 128
    n_fft = 2048
    y_axis = "log"  # linear or log
    fmin = None
    fmax = 2400.0
    cmap = 'jet'
    bins_per_octave = 22
    auto_aspect = False

    (data, sr) = librosa.load(audio_path, sr=None)  # no resampling

    # Plot spectrogram
    D = librosa.amplitude_to_db(np.abs(librosa.stft(data, hop_length=hop_length, n_fft=n_fft)), ref=np.max)

    fig, ax = plt.subplots(figsize=(8, 3))

    img = librosa.display.specshow(D, y_axis=y_axis, sr=sr,
                               hop_length=hop_length, x_axis='time', ax=ax, cmap=cmap, bins_per_octave=bins_per_octave,
                               auto_aspect=auto_aspect)

    ax.set_ylim([fmin, fmax])
    ax.set_aspect(0.005)
    ax.set_title('loaded slip spectrogram')
    fig.colorbar(img, ax=ax, format="%+2.f dB")
    plt.xlabel('Seconds')

    print('Graphic interface...')
    plt.show()

    plt.clf()

    return

plot_spectrogram(sys.argv[1], '')
