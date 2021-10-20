import satlas2 as sat
import matplotlib.pyplot as plt
import numpy as np

def modifiedSqrt(input):
    output = np.sqrt(input)
    output[input<0] = 1e-12
    return output

J = [0.5, 1.5]
I = 0

fwhm = 30
runs = [4319, 4320, 4312, 4313, 4317, 4318]
powers = [0.5, 0.76, 1.0, 1.5, 2.0, 2.5]

# Basic: fit each separate spectrum, and make a plot of the scale as a function of laser power
for run in runs:
    f = sat.Fitter()
    data = np.loadtxt('converted_{}.txt'.format(run))
    datasource = sat.Source(x, y, yerr=calculated error or function, name=?)
    Yb174_model = sat.HFS(I, J, name='Yb174')
    datasource.addModel(Yb174_model)
    f.addSource(datasource)
    f.fit()
    print(f.reportFit())
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.plot(source.x, source.y, label='Data', drawstyle='steps-mid')
    ax.plot(source.x, source.evaluate(source.x), label='Optim')
    plt.show()
