# GENI-Image-Recognition

[CS655] Deploy image recognition application on GENI.

## GENI Setup

1. Create a new Slice
1. Create new Resource
1. Choose RSpec with `File` and upload `geni_rspec.xml` in this repo.
1. Click on `Site 1` box to choose one available InstaGENI site.
1. Click `Reserve Resources` and wait until the resources are finished.

If the final result is `Failed`, please select another InstaGENI.

## Server

After the ssh login, we need to install and run the server.

### Install

```sh
sudo apt-get update
sudo apt-get upgrade
sudo apt install python3-pip
python3 -m pip install --upgrade pip
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
pip3 install -r requirements.txt
```

### Run

```sh
uwsgi --http :5000 --wsgi-file server/server.py --callable app
```

## Client
Login in to the client node.
### Install
``` bash
sudo apt-get update
sudo apt install python3-pip
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```
### Run
``` bash
cd client
python3 client.py -s SERVER [-n number of image] [-f width/height of the image]
```


## Reference

[OpenAI CLIP(Contrastive Language-Image Pre-Training)](https://github.com/openai/CLIP)

## Techniques TODO

- [ ] Cache mechanism
- [ ] TCP handshake HTTP/1.0
