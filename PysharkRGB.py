from openrgb import OpenRGBClient as client
from openrgb.utils import RGBColor as rgb
from pyshark import LiveCapture
from scapy.all import conf,get_if_addr
cli=client('127.0.0.1',8000,'Python')
ip1=ip2=0
own=get_if_addr(conf.iface)
cap=LiveCapture(display_filter='ip and((not string(ip.src) matches "^192.168*")or(not string(ip.dst) matches "^192.168*"))')
for packet in cap.sniff_continuously():
    if packet.ip.dst==own:
        ip=list(int(i) for i in packet.ip.src.split('.')[:-1])
        if ip==ip1:continue
        ip1=ip
        for z in cli.devices[0].zones[:-2]:z.set_color(rgb(*ip1),fast=True)
    elif packet.ip.src==own:
        ip=list(int(i) for i in packet.ip.dst.split('.')[:-1])
        if ip==ip2:continue
        ip2=ip
        for z in cli.devices[0].zones[-2:]:z.set_color(rgb(*ip2),fast=True)
