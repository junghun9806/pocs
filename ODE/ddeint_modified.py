# -*- coding: utf-8 -*-
"""
This module implements ddeint, a simple Differential Delay Equation
solver built on top of Scipy's odeint 

This module originally from https://github.com/Zulko/ddeint, modified by J. Chae. 
"""

import numpy as np
import scipy.integrate
import scipy.interpolate


class ddeVar:
    """
    The instances of this class are special function-like
    variables which store their past values in an interpolator and
    can be called for any past time: Y(t), Y(t-d).
    Very convenient for the integration of DDEs.
    """

    def __init__(self, g, tc=0):
        """ g(t) = expression of Y(t) for t<tc """

        self.g = g
        self.tc = tc
        # We must fill the interpolator with 2 points minimum

        self.interpolator = scipy.interpolate.interp1d(
            np.array([tc - 1, tc]),  # X
            np.array([self.g(tc), self.g(tc)]).T,  # Y
            kind="linear",
            bounds_error=False,
            fill_value=self.g(tc)
        )
    #

    def update(self, t, Y):
        """ Add one new (ti,yi) to the interpolator """
        Y2 = np.array([Y]).T if (Y.size == 1) else np.array([Y]).T
        self.interpolator = scipy.interpolate.interp1d(
            np.hstack([self.interpolator.x, [t]]),  # X
            np.hstack([self.interpolator.y, Y2]),  # Y
            kind="linear",
            bounds_error=False,
            fill_value=Y
        )
    #

    def __call__(self, t=0):
        """ Y(t) will return the instance's value at time t """

        return self.g(t) if (t <= self.tc) else self.interpolator(t)
    #

    def deri(self, nu, t):
        if t <= self.tc:
            return 0
        return self.interpolator._spline.derivative(nu=nu)(t)
    #
#

class dde(scipy.integrate.ode):
    """
    This class overwrites a few functions of ``scipy.integrate.ode``
    to allow for updates of the pseudo-variable Y between each
    integration step.
    """

    def __init__(self, f, fA, fB, jac=None, **kwargs):
        def f2(t, y, args):
            return f(self.Y, t, self.A, *args)
        scipy.integrate.ode.__init__(self, f2, jac)

        ### Get same argument with f, but return A value
        self.f_A = fA
        self.f_B = fB
        self.set_integrator('LSODA')
        self.set_f_params(None)
    #

    def integrate(self, t, step=0, relax=0):
        scipy.integrate.ode.integrate(self, t, step, relax)
        self.Y.update(self.t, self.y)
        self.A.update(self.t, np.array([self.f_A(self.Y, self.t, self.A)]))
        self.B.update(self.t, np.array([self.f_B(self.Y, self.t, self.A)]))
        return np.append(self.y, 
        np.array([self.f_A(self.Y, self.t, self.A), self.f_B(self.Y, self.t, self.A)]))
    #

    def set_initial_value(self, Y, A, B):
        self.Y = Y  #!!! Y will be modified during integration
        self.A = A
        self.B = B
        scipy.integrate.ode.set_initial_value(self, Y(Y.tc), Y.tc)
    #
#

def ddeint(func, fun2, fun3, g1, g2, g3, tt, fargs=None, kwargs={}):
    dde_ = dde(func, fun2, fun3)
    dde_.set_initial_value(ddeVar(g1, tt[0]), ddeVar(g2, tt[0]), ddeVar(g3, tt[0]))
    dde_.set_f_params(fargs if fargs else [])
    results = [dde_.integrate(dde_.t + dt) for dt in np.diff(tt)]
    return np.array([[*g1(tt[0]), *g2(tt[0]), *g3(tt[0])]] + results)
#