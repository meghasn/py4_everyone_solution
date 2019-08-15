"""
wap to store the string='X-DSPAM-Confidence:.8475'
use string slicing to extract the portion after: and the using float fn convert
the extreacted string to float"""
string="X-DSPAM-Confidence:.8475"
col_pos=string.find(":")
number=string[col_pos+1:]
conf=float(number)
print(conf)


#0.8475