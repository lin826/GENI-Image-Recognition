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

After the ssh login, we need to install and run the server and workers.

### Install

If the server is the only worker, these installation are required.
Otherwise, only install on workers should be enough.

```sh
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install uwsgi uwsgi-plugin-python3
sudo apt install python3-pip
python3 -m pip install --upgrade pip
python3 -m pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
python3 -m pip install -r server/requirements.txt
```

### Dataset predownload

Before setup LAN for each worker, we need to make sure the image recognition dataset is downloaded into `.cache/`.

```sh
python3 server/worker.py
```


### Router Network Setup

If the server is the only worker, this section can be skipped. Otherwise, we need to setup the router and each sub-workers under the local network. According to the resource of [LAN setup](https://witestlab.poly.edu/blog/designing-subnets/), run the following shell script on the router machine:

```sh
```

Next, each worker machine should run the following:

```sh
```

### Run

For each worker, run the following script to start the http server. Also, make sure you see `spawned uWSGI worker 1 (and the only)` in the terminal to be a prepared worker.

```sh
uwsgi --plugin http,python3 --http :5000 --wsgi-file server/worker.py --callable app
```

If the server is not the worker, run the following script to be the task manager:

```sh
uwsgi --plugin http,python3 --http :5000 --wsgi-file server/server.py --callable app -p 4
```

## Client
Login in to the client node.

### Install
``` bash
sudo apt-get update
sudo apt install python3-pip
python3 -m pip install --upgrade pip Pillow
```

### Run
``` bash
cd client
python3 client.py -s http://server [-n number of image] [-t timeout] [-f width/height of the image]
```

## Reference

[OpenAI CLIP(Contrastive Language-Image Pre-Training)](https://github.com/openai/CLIP)

## Techniques TODO

- [ ] Cache mechanism
- [ ] TCP handshake HTTP/1.0
