import matplotlib.pyplot as plt
from lib.BusquedaHeuristica import BusquedaHeuristica
import numpy as np

if __name__ == "__main__":
    rp = BusquedaHeuristica("https://mach-eight.uc.r.appspot.com/")

    x = list()
    y = list()

    punto_maximo = (0, 0)
    minimo = 0
    maximo = 0
    for i in range(100, 220, 1):
        rp.search(i)
        rta = rp.solve(False)
        conteo = 0
        if rta is not None:
            conteo = len(rta)

        if minimo > 0 and conteo > 0:
            maximo = i

        if conteo > 0 and minimo == 0:
            minimo = i

        if punto_maximo[1] < conteo:
            punto_maximo = (i, conteo)

        x.append(i)
        y.append(conteo)

    xpoints = np.array(x)
    ypoints = np.array(y)

    fig, ax = plt.subplots(nrows=1, ncols=1)  # create figure & 1 axis
    ax.plot(xpoints, ypoints, 'r', label='cantidad respuestas')

    ax.axvline(x=minimo, ymin=0.1, ymax=0.9, color='y', linestyle='--', label='minimo')
    ax.axvline(x=maximo, ymin=0.1, ymax=0.9, color='b', linestyle='-.', label='maximo')

    # Annotation
    ax.annotate('Local Max', xytext=(punto_maximo[0], punto_maximo[1] - int(punto_maximo[1] * 2 / 5)),
                xy=punto_maximo, arrowprops=dict(facecolor='green',
                                                 shrink=0.05), )

    ax.annotate('Minimo (' + str(minimo) + ")", xytext=(minimo-30, 50),
                xy=(minimo, 0), arrowprops=dict(facecolor='green',
                                                 shrink=0.05), )

    ax.annotate('Maximo (' + str(maximo) + ")", xytext=(maximo+10, 50),
                xy=(maximo, 0), arrowprops=dict(facecolor='green',
                                                 shrink=0.05), )

    plt.xlabel('Valor a buscar')
    plt.ylabel('Cantidad parejas de jugadores de NBA')
    plt.title("'Parejas de jugadores de NBA' vs 'Valor a buscar'")

    ax.grid()
    plt.legend(loc='upper left')

    fig.savefig('histograma_posibles_soluciones.png')  # save the figure to file
    plt.show()
    plt.close(fig)  # close the figure window

    print(minimo, maximo, punto_maximo)
