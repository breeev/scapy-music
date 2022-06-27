# Scapy Music <img src='https://raw.githubusercontent.com/breeev/scapy-music/main/logo.ico?sanitize=true&raw=true'/>
> Non-random music is cool!  

  While creativity is a big part of music creation, a creation following a set of rules is often more appealing. While creativity may seem random, it's in fact often a very original set of rules that make sense together and that way pleases our senses.  
Why all that gibberish you ask?  

This repo contains <b>a scappy analyzer that plays sounds depending on the network packets in circulation</b>. That means it's supposed to vary depending on the time and place where it's being executed, and will always have a meaning because every communication has one.  
<b>Now working in real time!</b>  

# Features
Get ready to hear computers talk to each other!  
This script uses <a href="https://scapy.net/">Scappy</a> to capture packets. If they got a source IP address, then <a href="https://numpy.org/">Numpy</a> is used to set for each address a mix of four sine waves whose pitch are from the four address bytes (slightly offset and multiplied for hearability and diversity).  

While "```no time.py```" has no time support, it plays a track composed of every address found in order. The rhythm comes from the time support introduced in "```main.py```". A realtime version has then been created using pygame (see "```realtime.py```").  
These two last files also have <b>settings</b> with comments, you should mess up with them and see what you come up with.  

You can find Windows executables in the <a href="https://github.com/breeev/scapy-music/releases">releases</a> section.



This project was made for my father's birthday.
