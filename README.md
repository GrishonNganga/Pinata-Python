# Pinata-Python
>> Unofficial IPFS python library for interacting with [Pinata](https://www.pinata.cloud/) APIs

## Installation
Run the following to install:
```python
pip install pinata
```
# Usage
1. Register an account on [Pinata](https://app.pinata.cloud/register)
2. Create a new api key on [api keys page](https://app.pinata.cloud/keys)
3. Copy your **api key**, **api secret** and **secret key** to be used below.

```python
from pinata import Pinata

pinata = Pinata(ap_key, secret_key, access_token)
```
# Pin a file 
To upload your file to Pinata, you can either provide:
1. Directory path of the file you want to upload
2. File itself as a Byte Stream, eg. If from flask request:
```python
file = request.files["file_name"]
```
Finally, 
```python
from pinata import Pinata

pinata = Pinata(ap_key, secret_key, access_token)

response = pinata.pin_file(file)
print(response)
```

# Unpin a file
To unpin a file, you will need the file's IpfsHash.
```python
from pinata import Pinata

pinata = Pinata(ap_key, secret_key, access_token)

response = pinata.unpin_file(ipfs_hash)
print(response)
```

# Get all pins
If you want to get all pins in your account:

```python
from pinata import Pinata

pinata = Pinata(ap_key, secret_key, access_token)

response = pinata.get_pins()
print(response)
```

