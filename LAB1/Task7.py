url_adr = input("enter url:")
http = "http://"
if url_adr.startswith("www"):
    url_adr = http + url_adr
if url_adr.endswith("com"):
    print(url_adr)
else:    
    print(url_adr + ".com")