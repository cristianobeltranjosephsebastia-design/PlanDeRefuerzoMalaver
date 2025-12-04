import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO

def crear_grafica():
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 25, 30, 40]

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Ejemplo de gráfica")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    return buffer
