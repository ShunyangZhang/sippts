#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jose Luis Verdeguer'
__version__ = '3.2'
__license__ = "GPL"
__copyright__ = "Copyright (C) 2015-2022, SIPPTS"
__email__ = "pepeluxx@gmail.com"

from modules.arpspoof import ArpSpoof
from lib.params import get_spoof_args


def main():
    ip, verbose, gw, file = get_spoof_args()

    s = ArpSpoof()
    s.ip = ip
    s.verbose = verbose
    s.gw = gw
    s.file = file

    s.start()


if __name__ == '__main__':
    main()
