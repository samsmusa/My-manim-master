from manimlib import *

# from manimlib.imports import *
import numpy as np


class matadd(Scene):
    def construct(self):


            #eol 2016 chapter1 (1:38 youtube) line = 297

        v_array = matrix_to_mobject([3, -5])
        w_array = matrix_to_mobject([2, 1])
        sum_array = matrix_to_mobject(["3+2", "-5+1"])
        arrays = VGroup(
            v_array, Tex("+"), w_array, Tex("="), sum_array
            )
        arrays.arrange(RIGHT)
        arrays.scale(0.75)
        arrays.to_edge(RIGHT).shift(UP)

        circle = Circle()
        circle.shift(arrays[0].get_bottom())
        # circle.shift(arrays[0].get_center())

        self.add(arrays, circle)