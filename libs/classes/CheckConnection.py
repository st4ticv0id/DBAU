import http.client as httplib

def connectionStatus():
    connection = httplib.HTTPSConnection("8.8.8.8", timeout=5) # ping address 8.8.8.8 (google DNS)

    try:
        connection.request("HEAD", "/") # send a request to the address and listen for a response
        return 0 #internet connection
    except Exception:
        return 1 #no internet connection
    finally:
        connection.close()