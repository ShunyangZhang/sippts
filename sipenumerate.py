#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jose Luis Verdeguer'
__version__ = '3.2'
__license__ = "GPL"
__copyright__ = "Copyright (C) 2015-2022, SIPPTS"
__email__ = "pepeluxx@gmail.com"

from modules.sipenumerate import SipEnumerate
from lib.params import get_sipenumerate_args


def main():
    ip, host, proxy, rport, proto, domain, contact_domain, from_name, from_user, from_domain, to_name, to_user, to_domain, user_agent, verbose = get_sipenumerate_args()

    s = SipEnumerate()
    s.ip = ip
    s.host = host
    s.proxy = proxy
    s.rport = rport
    s.proto = proto
    s.domain = domain
    s.contact_domain = contact_domain
    s.from_name = from_name
    s.from_user = from_user
    s.from_domain = from_domain
    s.to_user = to_user
    s.to_name = to_name
    s.to_domain = to_domain
    s.user_agent = user_agent
    s.verbose = verbose

    s.start()


if __name__ == '__main__':
    main()
