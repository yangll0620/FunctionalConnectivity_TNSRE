# -*- coding: utf-8 -*-
# @Author: yll
# @Date:   2018-11-22 17:11:39
# @Last Modified by:   yll
# @Last Modified time: 2018-11-22 17:36:11

import numpy as np

def GaussianNoise_SNR(signal, Desired_SNR_dB):
	"""
		add desired SNR (dB) gaussian noise to signal
		SNR(dB) = 10 * log10(power_signal/power_noise)

		@ parameter:
			signal: (n_times,)
			Desired_SNR_dB: desired SNR in dB
		@ return 
			signal_noisy: (n_times,)
	"""
	n_times = signal.shape[0]
	noise = np.random.normal(loc=0.0, scale=1.0, size=(n_times,))

	power_signal = np.dot(abs(signal), abs(signal))/n_times
	power_noise = np.dot(abs(noise), abs(noise))/n_times 

	k = (power_signal * pow(10,(-Desired_SNR_dB/10)))/power_noise # scale factor
	noise_new = np.sqrt(k) * noise

	signal_noisy = signal + noise_new

	return signal_noisy