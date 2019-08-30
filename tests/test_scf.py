# -*- coding: utf-8 -*-

from dq import scf, dft


def test_scf():
    assert scf("H2O") == 3


def test_dft():
    assert scf("H2O") == 2
