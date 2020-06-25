#!/usr/bin/env python
# coding:utf-8
"""Classical Mechanics Recap:Formulas related to this topic."""


from sympy import diff, Eq


def velocity(x, t):
    """Def v: velocity."""
    return diff(x, t)


def acceleration(x, t):
    """Def a: accerlation."""
    return diff(x, t, 2)


def momentum(velocity):
    """Momentum."""
    m = 1
    return m * (velocity**2)


def kinetic_energy(velocity):
    """T: kinetic energy."""
    return ((momentum(velocity)**2)/2)


def gravity_potential(x):
    """Gravity potential."""
    m = 1
    g = 10
    return m * g * x


def conservative_force(m, acceleration):
    """F: conservative force."""
    return (m * acceleration)


def newton_motion_eq(velocity, t, x):
    """T as kinetic energy and V as potential enegry."""
    return Eq((diff(kinetic_energy(velocity), velocity, t) + diff(gravity_potential(x), x)), 0)


def lagrange(velocity, x):
    """Lagrange equation."""
    return kinetic_energy(velocity) - gravity_potential(x)


def euler_lagrange_eq(velocity, x, t):
    """Euler Lagrange equation."""
    return Eq((diff(lagrange(x, velocity), velocity, t) - diff(lagrange(x, velocity))), 0)


