import numpy as np
from structsolve import lb
import matplotlib
from structsolve import solve

from panels import Shell
from panels.plot_shell import plot_shell


def test_lb_orthotropic():
    #NOTE ssss boundary conditions by default
    s = Shell()
    s.m = 12
    s.n = 12
    s.stack = [0, 90, -45, +45, +45, -45, 90, 0]
    s.plyt = 0.125
    s.laminaprop = (142.5e3, 8.7e3, 0.28, 5.1e3, 5.1e3, 5.1e3)
    s.model = 'cylshell_clpt_donnell_bardell'
    s.a = 500
    s.b = 250
    # radius
    s.r = 1.e15	

    # compression
    s.Nxx = -1
    # shear
    s.Nxy = 0

    # fext = s.calc_fext()
    # print('  fext', fext)

    eigvals, eigvecs = lb(s.calc_kC(), s.calc_kG(), silent=False)
    plot_shell(s, eigvecs[:, 0], vec='w')

    print('  linear wmax', s.fields['w'].max())

if __name__ == '__main__':
    test_lb_orthotropic()
