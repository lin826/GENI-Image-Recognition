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