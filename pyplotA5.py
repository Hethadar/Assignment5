#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 20:13:19 2026

@author: ryantauber
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("fismflux.txt",delimiter=None)

time_minutes = data[:, 2] * 60 + data[:, 3]
values = data[:, 5]  # sixth column in the pasted data

print("Data shape:", data.shape)
print("Value range:", values.min(), "to", values.max())

plt.plot(time_minutes, values, ".-", markersize=3)
plt.xlabel("Time (minutes)")
plt.ylabel("Value")
plt.title("Value vs. time")
plt.ylim(values.min(), values.max())
plt.grid(True)
plt.tight_layout()
plt.show()

