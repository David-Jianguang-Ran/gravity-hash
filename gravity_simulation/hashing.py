import random
import numpy as np
import pandas as pd

from .gravity import Body, GravityField

BLOCK_SIZE = 36
STEPS_PER_BLOCK = 36
MASS_CONSTANT = 25600  # <= this constant seems to change digest diff a lot

DEBUG = False


class StringBlocks:
    """
    this class is used to convert arbitrary text into series of fixed length blocks,
    pads blocks that are too short
    """
    def __init__(self,content: str):
        self.content = content
        self.pointer = 0

    def __len__(self):
        return len(self.content) // BLOCK_SIZE + 1

    def __iter__(self):
        self.pointer = 0
        return self

    def __next__(self):
        if not self.has_next():
            raise StopIteration

        if len(self.content) - self.pointer >= BLOCK_SIZE:
            block = self.content[self.pointer : self.pointer + BLOCK_SIZE]
            self.pointer += BLOCK_SIZE
            return block
        # block needs padding
        else:
            padding = ""
            for i in range(0,self.pointer + BLOCK_SIZE - len(self.content)):
                padding += f"{i % 10}"
            block = self.content[self.pointer:]
            self.pointer += BLOCK_SIZE
            return block + padding

    def has_next(self):
        return len(self.content) > self.pointer


def mangle(x_hist, y_hist, text_block):
    """
    This is the core hashing process,
    it combines xy info and text block and
    produces another set of xy info

    x_hist, y_hist : np.array <= values of previous sim.run returned x history
    """
    # get gravity field
    g_field = GravityField()

    # calculate v we do it outside of the loop in order to better utilize numpy
    x_vel = np.subtract(x_hist[-1], x_hist[-2])
    y_vel = np.subtract(y_hist[-1], y_hist[-2])

    # add bodies
    for i in range(0,BLOCK_SIZE):
        x, y = x_hist[-1,i], y_hist[-1,i]
        g_field.add_body(Body(x0=x,y0=y,v_x=x_vel[i],v_y=y_vel[i],mass=ord(text_block[i]) * MASS_CONSTANT))

    # do simulation
    x_hist_new, y_hist_new = g_field.run(STEPS_PER_BLOCK)

    if DEBUG:
        with np.printoptions(precision=1, suppress=True):
            print(f"hashing:{text_block} \nhash:{x_hist_new.values[-1,:]}\n{y_hist_new.values[-1,:]}")

    return x_hist_new.values[-2:,:], y_hist_new.values[-2:,:]


def initial_state():
    """ Hard coded initial state, replace with better later"""
    x_hist = np.array([[i * 4 for i in range(0,BLOCK_SIZE)],[i * 4 for i in range(0,BLOCK_SIZE)]]).reshape((2,BLOCK_SIZE))
    y_hist = np.array([[(BLOCK_SIZE - i) * 4 for i in range(0,BLOCK_SIZE)],[(BLOCK_SIZE - i) * 4 for i in range(0,BLOCK_SIZE)]]).reshape((2,BLOCK_SIZE))

    return x_hist, y_hist


def convert_output(x_hist, y_hist):
    """
    this function takes output of the mangle function and maps it into chars
    hopefully the distribution of chars will be somewhat uniform
    """

    # make one int table from both axis history
    int_array = np.concatenate([x_hist[-1:,:],y_hist[-1:,:]],axis=0).reshape((-1,)).astype("int")

    # convert ints into chars
    out_string = ""
    for each in int_array.tolist():
        out_string += chr(each % 89 + 33)

    return out_string

def get_digest_v0(input_string):
    # process input, initialize state
    blocks = StringBlocks(input_string)
    x_state, y_state = initial_state()

    # decides on how many iterations to run
    if len(blocks) > 15:
        rounds = 3
    else:
        rounds = 8 - len(blocks) // 3

    # do hashing
    track_iter = 0
    for i in range(0,rounds):
        blocks = blocks.__iter__()
        while blocks.has_next():
            track_iter += 1
            x_state, y_state = mangle(x_state,y_state,blocks.__next__())

    if DEBUG:
        print(f"ran {track_iter} hash cycles")

    return convert_output(x_state,y_state)
