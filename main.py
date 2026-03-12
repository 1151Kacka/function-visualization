import numpy as np
import matplotlib.pyplot as plt
import os
from functions import (
    linear_function, 
    quadratic_function, 
    sine_function, 
    exponential_function, 
    logarithmic_function)

# Vytvoření složky images, pokud neexistuje
if not os.path.exists("images"):
    os.makedirs("images")

x = np.linspace(-10, 10, 1000)

def save_graf(x, y, name, soubor, color):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=name, color=color, linewidth=2)
    
    # --- POKROČILÁ ČÁST (Bod 7, Možnost C): Minimum a Maximum ---
    # Odfiltrujeme NaN hodnoty pro výpočet extrémů (důležité pro logaritmus)
    mask = ~np.isnan(y)
    if np.any(mask):
        y_clean = y[mask]
        x_clean = x[mask]
        
        y_max = np.max(y_clean)
        x_max = x_clean[np.argmax(y_clean)]
        
        y_min = np.min(y_clean)
        x_min = x_clean[np.argmin(y_clean)]

        # Vyznačení do grafu (pouze pokud jsou v rozumném rozsahu)
        if y_max < 1000 and y_max > -1000:
            plt.scatter(x_max, y_max, color='black', zorder=5)
            plt.annotate(f'Max: {y_max:.2f}', (x_max, y_max), textcoords="offset points", xytext=(0,10), ha='center')
        
        if y_min > -1000 and y_min < 1000:
            plt.scatter(x_min, y_min, color='black', zorder=5)
            plt.annotate(f'Min: {y_min:.2f}', (x_min, y_min), textcoords="offset points", xytext=(0,-15), ha='center')

    plt.title(f"Graf funkce: {name}")
    plt.xlabel("osa x")
    plt.ylabel("f(x)")
    plt.axhline(0, color='black', linewidth=0.5) 
    plt.axvline(0, color='black', linewidth=0.5) 
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    plt.savefig(f"images/{soubor}.png")
    plt.close()
    print(f"Graf {soubor}.png uložen.")

# Volání funkcí
save_graf(x, linear_function(x, 2, 1), "Lineární (2x + 1)", "linear", "blue")
save_graf(x, quadratic_function(x, 1, 2, -5), "Kvadratická (x² + 2x - 5)", "quadratic", "green")
save_graf(x, sine_function(x), "Sinus", "sine", "red")
save_graf(x, exponential_function(x, 0.5), "Exponenciální (e^0.5x)", "exponential", "purple")
save_graf(x, logarithmic_function(x, 1), "Logaritmická (ln x)", "logarithmic", "orange")

# Kombinovaný graf
plt.figure(figsize=(10, 6))
plt.plot(x, linear_function(x, 2, 1), label="Lineární", color="blue")
plt.plot(x, quadratic_function(x, 1, 2, -5), label="Kvadratická", color="green", linestyle="--")
plt.plot(x, sine_function(x) * 10, label="Sinus (10x)", color="red", linestyle=":")
plt.title("Kombinovaný graf")
plt.xlabel("osa x")
plt.ylabel("f(x)")
plt.ylim(-20, 100)
plt.legend()
plt.savefig("images/multiple_functions.png")
plt.close()