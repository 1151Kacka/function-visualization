import numpy as np
import matplotlib.pyplot as plt
from functions import (
    linear_function, 
    quadratic_function, 
    sine_function, 
    exponential_function, 
    logarithmic_function)
x = np.linspace(-10, 10, 1000)

def save_graf(x, y, name, soubor, color):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=name, color=color, linewidth=2)
    plt.title(f"Graf funkce: {name}")
    plt.xlabel("osa x")
    plt.ylabel("f(x)")
    plt.axhline(0, color='black', linewidth=0.5) 
    plt.axvline(0, color='black', linewidth=0.5) 
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # Uložení do složky
    cesta = f"images/{soubor}.png"
    plt.savefig(cesta)
    plt.close()
    
save_graf(x, linear_function(2, 1, x), "Lineární (2x + 1)", "linear", "blue")
save_graf(x, quadratic_function(1, 2, -5, x), "Kvadratická (x² + 2x - 5)", "quadratic", "green")
save_graf(x, sine_function(x), "Sinus", "sine", "red")
save_graf(x, exponential_function(0.5, x), "Exponenciální (e^0.5x)", "exponential", "purple")
save_graf(x, logarithmic_function(1, x), "Logaritmická (ln x)", "logarithmic", "orange")

#kombinace
plt.figure(figsize=(10, 6))
plt.plot(x, linear_function(2, 1, x), 
         label="Lineární (2x + 1)", color="blue", linestyle="-")

plt.plot(x, quadratic_function(1, 2, -5, x), 
         label="Kvadratická (x² + 2x - 5)", color="green", linestyle="--")

y_sine_scaled = sine_function(x) * 10
plt.plot(x, y_sine_scaled, 
         label="Sinus (10 * sin x)", color="red", linestyle=":")

plt.title("Kombinovaný graf: Lineární, Kvadratická a Sinusová funkce")
plt.xlabel("osa x")
plt.ylabel("f(x)")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)

plt.ylim(-20, 100) 
plt.legend()
plt.savefig("images/multiple_functions.png")
plt.close()