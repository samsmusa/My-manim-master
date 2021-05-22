from manimlib import *
import numpy as np

class lekha(Scene):
    def construct(billu):
        kotha = Text("There is no charge for the real Awesomeness or the Attractiveness", Color=RED, font = "Bradley Hand ITC",t2c = {"Attractiveness": RED}, font_size = 25)
        billu.play(ShowCreation(kotha))