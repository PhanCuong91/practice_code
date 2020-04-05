"""
Learn about codecs and containers.

Learn about network protocols, specifically, why people use RTP or similar, and why over UDP.

Find a library that will encode things over your protocol of choice, in the container format of choice (depends who's receiving—browser? welcome to portability headaches), and choose an appropriate codec.

For quick and dirty, I just used Python to set up RTP using ffmpeg… now assuming there were no NAT issues in this design:

SimpleVoIP

rtp.sh

https://www.reddit.com/r/Python/comments/735bgj/streaming_audio_over_socket/
https://pymotw.com/2/socket/multicast.html
http://zetcode.com/python/socket/
https://stackoverflow.com/questions/28022432/receiving-rtp-packets-after-rtsp-setup
"""
