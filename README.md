# GENI-Image-Recognition

[CS655] Deploy image recognition application on GENI.

## GENI Rspec

```xml
<rspec xmlns="http://www.geni.net/resources/rspec/3" xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" xmlns:tour="http://www.protogeni.net/resources/rspec/ext/apt-tour/1" xmlns:jacks="http://www.protogeni.net/resources/rspec/ext/jacks/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.geni.net/resources/rspec/3    http://www.geni.net/resources/rspec/3/request.xsd" type="request">
</rspec>
```

## SSH connection

## Install

```sh
sudo apt-get update
sudo apt-get upgrade
sudo apt install python3-pip
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## Server

```sh
uwsgi --http 10.10.1.1:5000 --master -p 2 --wsgi-file server/server.py --callable app
```

## Reference

[OpenAI CLIP(Contrastive Language-Image Pre-Training)](https://github.com/openai/CLIP)

## Techniques TODO

- [ ] Cache mechanism
- [ ] TCP handshake HTTP/1.0


## How to install and test
### Client
1. Set the environment by the following command:
``` bash
cd client
python3 -m venv myenv
source myenv/bin/activate
pip3 install -r requirements.txt
```
2. The client can be started by the command.
``` bash
cd client
source myenv/bin/activate
python3 client.py
```