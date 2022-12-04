# GENI-Image-Recognition

[CS655] Deploy image recognition application on GENI.

## Reference

[OpenAI CLIP(Contrastive Language-Image Pre-Training)](https://github.com/openai/CLIP)

## Techniques TODO

- [ ] Cache mechanism
- [ ] TCP handshake HTTP/1.0


## How to install and test
### Client
1. Set the environment by the following command:
``` bash
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```
2. The client can be started by the command.
``` bash
cd client
python3 client.py -s SERVER [-n number of image]
```