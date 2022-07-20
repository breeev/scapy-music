from openrgb import OpenRGBClient as client
from openrgb.utils import RGBColor as rgb
from scapy.all import sniff,get_if_addr,conf
cli=client('127.0.0.1',8000,'Python')
def f(x):
    if x.dst==get_if_addr(conf.iface) and not x.src.startswith('192.168.'):
        for z in cli.devices[0].zones[:-2]:
            z.set_color(rgb(*(int(i) for i in x.src.split('.')[:-1])),fast=True)
    elif x.src==get_if_addr(conf.iface) and not x.dst.startswith('192.168.'):
        for z in cli.devices[0].zones[-2:]:
            z.set_color(rgb(*(int(i) for i in x.dst.split('.')[:-1])),fast=True)
sniff(prn=lambda x:f(x['IP']),filter='ip')
