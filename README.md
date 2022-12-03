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
pip3 --no-cache-dir install -r requirements.txt
```

## Reference

[OpenAI CLIP(Contrastive Language-Image Pre-Training)](https://github.com/openai/CLIP)

## Techniques TODO

- [ ] Cache mechanism
- [ ] TCP handshake HTTP/1.0
