
# Gravitation Hash Algorithm 
Cryptographic Hash Algorithm curio using n-body gravitation simulation as core mechanism   
Please see a [Jupyter Notebook Demo](https://colab.research.google.com/drive/1lhe0Sxesn-O1ujrACXNHuK7UkEBnGmPX?usp=sharing) hosted on Google Colab

## Principle of Operation 

N-body orbit simulations are often done by 
applying the sum of forces between body B and all other particles 
to body B, for each time step. 
For N greater than 2, the orbits aren't solved analytically and 
simulation is the only to predict location and momentum of bodies.  

By modeling forces between all bodies, the simulation ensures 
the property of each body at each step is dependent on property of all bodies. 
This is the central idea of our hash algorithm.  

First, arbitrary inputs are processed into a number of fixed length blocks.  
Then the blocks are fed into a compression algorithm 
where it takes an initial internal state and updates it with a block of text. 

The actual hashing is done by 
having one body for each character of the text block, 
setting the position and momentum of each body based on either initial state or previous block output, 
setting the mass of each body according to each char of the text block. 
Then run the simulation for a fixed amount of steps.

Finally when the blocks are exhausted, return digest string based on the position and momentum stored on the internal state.
Note that information on the mass of each body is discarded / changed at each block. This makes the process irreversible.
 

## Documentation
Later on there will be more sophisticated distribution through PyPI, 
for now, in order to install, you can do the following:  
Clone the github repo and move gravity-hash/gravity_simulation to your current working dir  
```bash
git clone https://github.com/David-Jianguang-Ran/gravity-hash.git
mv -i gravity-hash/gravity_simulation ./g_hash & rm -rf gravity-hash/
```

In order to get digest on string data, in python:  
```python
from g_hash.hashing import get_digest_v0 # <= this assumes you've moved gravity_simulation to ./g_hash like above  
digest = get_digest_v0('sample_text')
```





