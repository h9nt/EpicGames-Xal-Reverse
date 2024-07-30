import json
import base64

def Rc4(a):
    key = "FZMÃ›SÃª/Â·V«xÞhí¢³4<`ô2ª,µ¦YÃ»" # key? decoded b64
    c = json.dumps(a).encode('utf-8')
    d = list(range(256))
    e = 0
    f = ""
    
    for h in range(256):
        e = (e + d[h] + ord(key[h % len(key)])) % 256
        d[h], d[e] = d[e], d[h]
    
    j = 0
    e = 0
    for l in range(len(c)):
        j = (j + 1) % 256
        e = (e + d[j]) % 256
        d[j], d[e] = d[e], d[j]
        f += chr(c[l] ^ d[(d[j] + d[e]) % 256])
    
    return base64.b64encode(f.encode('latin1')).decode('utf-8')

fp_data = { # The Fp data can u get in the index.html file on the site that i made

}
print(Rc4(fp_data))
