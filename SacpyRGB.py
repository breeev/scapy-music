from openrgb import OpenRGBClient as client
from openrgb.utils import RGBColor as rgb
from scapy.all import sniff,get_if_addr,conf
cli=client('127.0.0.1',8000,'Python')
ip1=ip2=0
own=get_if_addr(conf.iface)
def f(x):
    global ip1,ip2
    if x.dst==own:
        ip=list(int(i) for i in x.src.split('.')[:-1])
        if ip==ip1:return None
        ip1=ip
        for z in cli.devices[0].zones[:-2]:z.set_color(rgb(*ip1),fast=True)
    elif x.src==own:
        ip=list(int(i) for i in x.dst.split('.')[:-1])
        if ip==ip2:return None
        ip2=ip
        for z in cli.devices[0].zones[-2:]:z.set_color(rgb(*ip2),fast=True)
sniff(prn=lambda x:f(x['IP']),filter='ip',store=0,lfilter=lambda x:(not x['IP'].src.startswith('192.168'))or(not x['IP'].dst.startswith('192.168')))
