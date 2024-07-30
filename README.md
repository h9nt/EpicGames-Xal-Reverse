# EpicGames-Xal-Reverse
> Its the Full Reversed Algo from EpicGames to create the (**Xal**) Value for the Fp for the Login Procces

- You Will Find the Algorithm , thats use Rc4 to encrypt the Fp Data , in the js file at line [**6880**]
- I made it in python that u can easy use it there for this look at the **main.py** file.
- You can get your Fp Data here: [<a href="https://h9nt.github.io/EpicGames-Xal-Reverse/">**Click here**</a>]

# Explaination

Thats the Rc4 Algorithm they use in [**js**]
```js
function Rc4(a) {
      var b;
      var c = unescape(encodeURIComponent(JSON.stringify(a)));
      var d = [];
      var e = 0;
      var f = "";
      for (var g = 0; g < 256; g++) {
        d[g] = g;
      }
      for (var h = 0; h < 256; h++) {
        e = (e + d[h] + key.charCodeAt(h % key.length)) % 256;
        b = d[h];
        d[h] = d[e];
        d[e] = b;
      }
      var j = 0;
      e = 0;
      for (var l = 0; l < c.length; l++) {
        e = (e + d[(j = (j + 1) % 256)]) % 256;
        b = d[j];
        d[j] = d[e];
        d[e] = b;
        f += String.fromCharCode(c.charCodeAt(l) ^ d[(d[j] + d[e]) % 256]);
      }
      return window.btoa(f);
    }

```

- The same for **python**
```python
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
```
