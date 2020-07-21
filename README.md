
# Gravitation Hash Algorithm 
Cryptographic Hash Algorithm curio using n-body gravitation simulation as core mechanism   
Please see a [Jupyter Notebook Demo](https://colab.research.google.com/drive/1lhe0Sxesn-O1ujrACXNHuK7UkEBnGmPX?usp=sharing) hosted on Google Colab

## Principle of Operation 
Coming Soon

## Documentation
For now, in order to install, you can do the following:  
Clone the github repo and move gravity-hash/gravity_simulation to your current working dir  
`
git clone https://github.com/David-Jianguang-Ran/gravity-hash.git
mv -i gravity-hash/gravity_simulation ./g_hash & rm -rf gravity-hash/
`  

In order to get digest on string data, in python:  
`
from g_hash.hashing import get_digest_v0 # assuming you got the package through above step
digest = get_digest_v0('sample_text')
`



