from manimlib import *

# from manimlib.imports import *
import numpy as np


class Positron(Circle):
    CONFIG = {
        "radius": 0.2,
        "stroke_width": 3,
        "color": RED,
        "fill_color": RED,
        "fill_opacity": 0.5,
    }

    def __init__(self, **kwargs):
        Circle.__init__(self, **kwargs)
        plus = Tex("+")
        plus.scale(0.7)
        plus.move_to(self)
        self.add(plus)


class Intro(Scene):
    def construct(self):
        li = TexText("Line Integral", color=BLUE)
        li.scale(2)

        int2 = Tex(r'{{$\xrightarrow{Hello} $ \\LaTeX}}')
        int2.scale(1.5)
        self.add(int2)

        # int1 = Tex(r"\int_C f(x,y) ds")
        # int1.scale(1.5)

        # int3 = Tex(r"\int_C \textbf{P}dx + \textbf{Q}dy")
        # int3.scale(1.5)

        # uses = BulletedList(
        #     "Work",
        #     "Center of mass",
        #     "Faraday's Law",
        #     "Ampere's Law",
        #     "..."
        # )

        # self.play(Write(li))
        # self.wait()
        # self.play(ApplyMethod(li.shift, 3 * UP))

        # self.play(Write(int1))
        # self.wait()

        # self.play(Transform(int1, int2))
        # self.wait()

        # self.play(Transform(int1, int3))
        # self.wait()

        # self.play(Uncreate(int1))
        # self.play(Write(uses))

        # self.wait(2)


class scene(Scene):
    CONFIG = {
        "axis_config": {
            "include_tip": False,
            "numbers_to_exclude": [0],
        },
        "x_axis_config": {},
        "y_axis_config": {
            "line_to_number_direction": LEFT,
        },
        "height": FRAME_HEIGHT - 2,
        "width": FRAME_WIDTH - 2
    }

    def construct(self):
        # CONFIG = {
        #     "x_min" : 0,
        #     "x_max" : 7,
        #     "y_min" : -0.6,
        #     "y_max" : 1.5,
        #     "graph_origin" : 4*LEFT+1.5*DOWN ,
        #     "axes_color" : BLACK,
        #     "labels_color": BLACK,
        #     "label_nums_color": BLACK
        #     }
        
        # num = NumberLine(
        #     x_range=[-3,3,1],
        #     include_numbers = True,
        #     color = RED,
        #     include_tip = False,
        # )


        # grid = Axes(
        #     axis_config= {
        #     "include_tip": False,
        #     "X_AXIS_color": RED,
        #     }
        #     )

        # gri = NumberPlane(
        #     x_range=[-5,5,1],
        #     axis_config = {
        #     "stroke_color": YELLOW,
        #     "stroke_width": 1,
        #     "include_ticks": True,
        #     "include_tip": True,
        #     "line_to_number_buff": SMALL_BUFF,
        #     "line_to_number_direction": DL,
        # },
        # background_line_style = {
        #     "stroke_color": YELLOW,
        #     "stroke_width": 2,
        #     "stroke_opacity": 1,
        # },
        # )

        # x_axis = NumberLine(
            
            
            
        #     color= YELLOW, #<-- Remember the coma,
        #     # include_numbers=[1,2,3],
            
        # )

        # x_axis.add_coordinate_labels()

        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()

        self.play(ShowCreation(axes, lag_ratio=0.01, run_time=1))

        # Axes.get_graph will return the graph of a function
        sin_graph = axes.get_graph(
            lambda x: 2 * math.sin(x),
            color=BLUE,
        )

        relu_graph = axes.get_graph(
            lambda x: max(x, 0),
            use_smoothing=True,
            color=YELLOW,
        )

        step_graph = axes.get_graph(
            lambda x: 2.0 if x > 4 else 1.0,
            use_smoothing=False,
            discontinuities=[3],
            color=GREEN,
        )

        parabola = axes.get_graph(lambda x: 0.25 * x**2)
        parabola.set_stroke(BLUE)
        self.play(
            ShowCreation(parabola)
        )
        self.wait()

        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(2, parabola))
        self.play(FadeIn(dot, scale=0.5))

        x_tracker = ValueTracker(2.5)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola)
        )

        self.play(x_tracker.animate.set_value(4), run_time=3)
        self.play(x_tracker.animate.set_value(-2), run_time=3)
        self.wait()


        # self.play(ShowCreation(parabola))
        
        # self.play(x_axis.animate.rotate(PI/2))

        # tex = [Tex("10+15","13"),Tex("10+15","13")]
        
        # VGroup(*tex).arrange(DOWN).to_corner(UR)
        # self.add(*tex)
        # self.wait()
        # co = tex.get_coord([0,1,2])
        # tex1 = [Tex("3"),tex("9")]
        # tex1.shift(co)
        # self.play(
        #     *list(map(Transform,(tex,tex1)))
        # )


class GraphExample(Scene):
    def construct(self):
        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()

        self.play(ShowCreation(axes, lag_ratio=0.01, run_time=1))

        # Axes.get_graph will return the graph of a function
        sin_graph = axes.get_graph(
            lambda x: 2 * math.sin(x),
            color=BLUE,
        )
        # By default, it draws it so as to somewhat smoothly interpolate
        # between sampled points (x, f(x)).  If the graph is meant to have
        # a corner, though, you can set use_smoothing to False
        relu_graph = axes.get_graph(
            lambda x: max(x, 0),
            use_smoothing=False,
            color=YELLOW,
        )
        # For discontinuous functions, you can specify the point of
        # discontinuity so that it does not try to draw over the gap.
        step_graph = axes.get_graph(
            lambda x: 2.0 if x > 3 else 1.0,
            discontinuities=[3],
            color=GREEN,
        )

        # Axes.get_graph_label takes in either a string or a mobject.
        # If it's a string, it treats it as a LaTeX expression.  By default
        # it places the label next to the graph near the right side, and
        # has it match the color of the graph
        sin_label = axes.get_graph_label(sin_graph, "\\sin(x)")
        relu_label = axes.get_graph_label(relu_graph, Text("ReLU"))
        step_label = axes.get_graph_label(step_graph, Text("Step"), x=4)

        self.play(
            ShowCreation(sin_graph),
            FadeIn(sin_label, RIGHT),
        )
        self.wait(2)
        self.play(
            ReplacementTransform(sin_graph, relu_graph),
            FadeTransform(sin_label, relu_label),
        )
        self.wait()
        self.play(
            ReplacementTransform(relu_graph, step_graph),
            FadeTransform(relu_label, step_label),
        )
        self.wait()

        parabola = axes.get_graph(lambda x: 0.25 * x**2)
        parabola.set_stroke(BLUE)
        self.play(
            FadeOut(step_graph),
            FadeOut(step_label),
            ShowCreation(parabola)
        )
        self.wait()

        # You can use axes.input_to_graph_point, abbreviated
        # to axes.i2gp, to find a particular point on a graph
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(2, parabola))
        self.play(FadeIn(dot, scale=0.5))

        # A value tracker lets us animate a parameter, usually
        # with the intent of having other mobjects update based
        # on the parameter
        x_tracker = ValueTracker(2)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola)
        )

        self.play(x_tracker.animate.set_value(4), run_time=3)
        self.play(x_tracker.animate.set_value(-2), run_time=3)
        self.wait()


class deff(scene):
    def construct(self):

        axes = Axes((-5, 5), (-5, 5))
        axes.add_coordinate_labels()

        self.play(ShowCreation(axes, lag_ratio=0.01, run_time=1))

        parabola = axes.get_graph(lambda x: 0.25 * x**2)
        parabola.set_stroke(BLUE)
        self.play(
           
            ShowCreation(parabola)
        )
        self.wait()

        grid= NumberPlane()
        self.add(grid)

        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(2, parabola))
        self.play(FadeIn(dot, scale=0.5))

        x_tracker = ValueTracker(2.5)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola)
        )

        self.play(x_tracker.animate.set_value(4), run_time=3)
        self.play(x_tracker.animate.set_value(-4), run_time=3)
        self.wait()

class kk(Scene):
    def construct(self):
        grid = NumberPlane()
        self.add(grid)

class CoordinateSystemExample(Scene):
    def construct(self):
        axes = Axes(
            # x-axis ranges from -1 to 10, with a default step size of 1
            x_range=(-1, 10),
            # y-axis ranges from -2 to 10 with a step size of 0.5
            y_range=(-2, 2, 0.5),
            # The axes will be stretched so as to match the specified
            # height and width
            height=6,
            width=10,
            # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={
                "stroke_color": YELLOW,
                "stroke_width": 2,
            },
            # Alternatively, you can specify configuration for just one
            # of them, like this.
            y_axis_config={
                "include_tip": False,
            }
        )
        # Keyword arguments of add_coordinate_labels can be used to
        # configure the DecimalNumber mobjects which it creates and
        # adds to the axes
        axes.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )
        self.add(axes)

        # Axes descends from the CoordinateSystem class, meaning
        # you can call call axes.coords_to_point, abbreviated to
        # axes.c2p, to associate a set of coordinates with a point,
        # like so:

        dot = Dot(color=RED)
        dot.move_to(axes.c2p(0, 0))
        self.play(FadeIn(dot, scale=0.5))
        self.play(dot.animate.move_to(axes.c2p(3, 2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(5, 0.5)))
        self.wait()

        # Similarly, you can call axes.point_to_coords, or axes.p2c
        print(axes.p2c(dot.get_center()))

        # We can draw lines from the axes to better mark the coordinates
        # of a given point.
        # Here, the always_redraw command means that on each new frame
        # the lines will be redrawn
        h_line = always_redraw(lambda: axes.get_h_line(dot.get_right()))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))

        self.play(
            ShowCreation(h_line),
            ShowCreation(v_line),
        )
        self.play(dot.animate.move_to(axes.c2p(3, -2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(1, 1)))
        self.wait()

        # If we tie the dot to a particular set of coordinates, notice
        # that as we move the axes around it respects the coordinate
        # system defined by them.
        f_always(dot.move_to, lambda: axes.c2p(1, 1))
        self.play(
            axes.animate.scale(0.75),
            axes.animate.to_corner(UL),
            run_time=2,
        )
        self.wait()
        self.play(FadeOut(VGroup(axes, dot, h_line, v_line)))

        # Other coordinate systems you can play around with include
        # ThreeDAxes, NumberPlane, and ComplexPlane.


class kk2(Scene):
    def construct(self):
        # axes = Axes(
        #     # x-axis ranges from -1 to 10, with a default step size of 1
        #     x_range=(-1, 10),
        #     # y-axis ranges from -2 to 10 with a step size of 0.5
        #     y_range=(-1, 10),
        #     # The axes will be stretched so as to match the specified
        #     # height and width
        #     height=6,
        #     width=10,
        #     # Axes is made of two NumberLine mobjects.  You can specify
        #     # their configuration with axis_config
        #     axis_config={
        #         "stroke_color": YELLOW,
        #         "stroke_width": 2,
        #     },
        #     # Alternatively, you can specify configuration for just one
        #     # of them, like this.
        #     y_axis_config={
        #         "include_tip": True,
        #     }
        # )
        # # Keyword arguments of add_coordinate_labels can be used to
        # # configure the DecimalNumber mobjects which it creates and
        # # adds to the axes
        # axes.add_coordinate_labels(
        #     font_size=20,
        #     num_decimal_places=1,
        # )
        # self.add(axes)

        plane = NumberPlane(
            axis_config = {
            "stroke_color": WHITE,
            "stroke_width": 2,
            "include_ticks": True,
            "include_tip": True,
            "line_to_number_buff": SMALL_BUFF,
            "line_to_number_direction": DL,
        },
        y_axis_config= {
            "line_to_number_direction": DL,
        },
        background_line_style = {
            "stroke_color": ORANGE,
            "stroke_width": 2,
            "stroke_opacity": .5,
        },
        )
        plane.add_coordinate_labels()

        self.add(plane)

        self.wait(3)
        label2 = Text("আসসালামু আলাইকুম", font="Akaash").scale(1.8).set_color(RED).shift(DOWN * 3)
        self.play(Write(label2))
        self.wait(3)

        # Axes descends from the CoordinateSystem class, meaning
        # you can call call axes.coords_to_point, abbreviated to
        # axes.c2p, to associate a set of coordinates with a point,
        p1 = plane.c2p(-3,-3)
        p2 = plane.c2p(4,3)

        line = Line(p1,p2)
        self.add(line)

        dot1 = Dot(color=BLUE)
        dot1.move_to(plane.c2p(-3, -3))

        dot2 = Dot(color=YELLOW)
        dot2.move_to(plane.c2p(4, 3))

        self.add(dot1,dot2)
        # like so:
        
        dot = Dot(color=RED)
        dot.move_to(plane.i2gp(3, line))
        

        h_line = always_redraw(lambda: plane.get_h_line(dot.get_left() if dot.get_x() > 0 else dot.get_right()))
        v_line = always_redraw(lambda: plane.get_v_line(dot.get_bottom() if dot.get_y() > 0 else dot.get_top()))
        #  lambda x: 2.0 if x > 3 else 1.0,


        self.play(FadeIn(dot, scale=0.5))
        self.wait()

        self.play(
            ShowCreation(h_line),
            ShowCreation(v_line),
        )


        # brac = Brace(dot, direction=UP)

        # self.add(brac)


        tex1, number1,tex3, number2, tex2 = label = VGroup(Tex("("),
            DecimalNumber( 0, num_decimal_places = 1,include_background_rectangle = False,font_size = 24,),Tex(","), DecimalNumber( 0, num_decimal_places = 1,include_background_rectangle = False,font_size = 24,), Tex(")")
        )

        label.arrange(RIGHT).add_background_rectangle()

        always(label.next_to,dot,UP)

        f_always(number1.set_value, dot.get_x)
        f_always(number2.set_value, dot.get_y)

        self.add(label)

#ratio
        line1 = always_redraw(lambda: Line(dot1.get_coord([0,1]), dot.get_coord([0,1])))

        always(line1.set_color, BLUE)
        self.add(line1)

        line2 = always_redraw(lambda: Line(dot2.get_coord([0,1]), dot.get_coord([0,1])))

        always(line2.set_color, YELLOW)
        self.add(line2)

        brac = always_redraw(Brace, line1,LEFT)
        

        self.add(brac)

        # brace = always_redraw(Brace, square, angle = PI/2)


        m1  = line1.get_length
        m2 =  line2.get_length
        # m3 = always(m1/m2)

        text2, number3 = label1 = VGroup(
            Text("m_1 = "),
            DecimalNumber(
                0,
                show_ellipsis=True,
                num_decimal_places=2,
                include_sign=False,
                font_size = 24,
            )
        )
        label1.arrange(RIGHT)

        
        always(label1.next_to, line2, UP)
        
        f_always(number3.set_value, m1)
      

        self.add(label1)

        line1.get_angle()

        

        # always_rotate(brac, rate=20 * PI/4)








        x_tracker = ValueTracker(3)
        f_always(
            dot.move_to,
            lambda: plane.i2gp(x_tracker.get_value(), line)
        )

        self.play(x_tracker.animate.set_value(4), run_time=3)
        self.play(x_tracker.animate.set_value(-2.99999), run_time=3)
        self.wait()




        # # self.play(FadeIn(dot, scale=0.5))
        # # self.play(dot.animate.move_to(axes.c2p(3, 2)))
        # # self.wait()
        # # self.play(dot.animate.move_to(axes.c2p(5, 0.5)))
        # # self.wait()
        # line.rotate()




###manim sandbox 






    
class LinearBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([-1.5,  1.5, 0]))
        P1 = Dot(np.array([ 1.5, -1.5, 0]))
        P = VGroup(P0, P1).set_color(GREEN)

        P0_P1 = Line(P0, P1).set_color(GREEN)

        t = ValueTracker(0)

        B = Dot(color=RED).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("this is line").scale(1.8).set_color(WHITE).shift(DOWN * 3)
        self.add(label)
        self.add(P, P0_P1, B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()


class QuadraticBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([ -3, -1.5, 0]))
        P1 = Dot(np.array([  0,  1.5, 0]))
        P2 = Dot(np.array([1.5, -1.5, 0]))
        P = VGroup(P0, P1, P2).set_color(GREEN)

        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P_lines = VGroup(P0_P1, P1_P2).set_color(GREEN)

        t = ValueTracker(0)
        

        Q0 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q = VGroup(Q0, Q1)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center())).set_color(YELLOW)

        B = Dot(color=RED).add_updater(lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)
        


        

        axes = Axes(
            x_range=(-1, 5),
            y_range=(-1, 5),
            y_axis_config={
                "include_tip": False,
            },
            x_axis_config={
                "unit_size": 2,
            },
        )
        axes.set_width(FRAME_WIDTH - 1)
        axes.center().to_edge(DOWN)
        axes.shift(DOWN)
        self.x_axis = axes.x_axis
        self.y_axis = axes.y_axis
        self.axes = axes

        graph = axes.get_graph(self.func)
        rects = axes.get_riemann_rectangles(
            graph,
            x_range= [0,4],
            dx=0.1,
        )
        rects.set_submobject_colors_by_gradient(BLUE, GREEN)
        rects.set_opacity(1)
        rects.set_stroke(BLACK, 1)

        self.add(axes)
        self.add(graph)
        self.add(rects)
        # self.add(title)
        # self.add(answer)

    def func(slef, x):
        return 0.35 * ((x - 2)**3 - 2 * (x - 2) + 6)









        label = Text("hello world").scale(1.8).set_color(WHITE).shift(DOWN * 3)
        # lin  = [lambda: Line(Q1.get_center(),Q0.get_center())]
        # self.add(label)
        # self.add(P, P_lines)
        self.add(Q0,Q1)
        self.add(P)
        # self.add(Q, Q0_Q1)
        # self.add(B, path)
        self.wait()
        self.add(path1)        # self.add(*lin)
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()
        # self.add(*list(map(ShowCreation, lines)))


class TracedPathExample(Scene):
    def construct(self):

        P0 = Dot(np.array([ -3, -1.5, 0]))
        P1 = Dot(np.array([  0,  1.5, 0]))
        circ = Line(P0, P1).shift(4*LEFT)
        dot = Dot(color=RED).move_to(circ.get_start())
        rolling_circle = VGroup(circ, dot)
        trace = TracedPath(circ.get_start)
        rolling_circle.add_updater(lambda m: m.rotate(-0.3))
        self.add(trace, rolling_circle)
        self.play(rolling_circle.animate.shift(8*RIGHT), run_time=4, rate_func=linear)



class CubicBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([  -3, -1.5, 0]))
        P1 = Dot(np.array([-3.6,  1.5, 0]))
        P2 = Dot(np.array([   0,  1.5, 0]))
        P3 = Dot(np.array([   3, -1.5, 0]))
        P = VGroup(P0, P1, P2, P3).set_color(GREEN)
        
        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P2_P3 = Line(P2, P3)
        P_lines = VGroup(P0_P1, P1_P2, P2_P3).set_color(GREEN)

        t = ValueTracker(0)

        Q0 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q2 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P3.get_center() - P2.get_center()) * t.get_value() + P2.get_center()))
        Q = VGroup(Q0, Q1, Q2)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        Q1_Q2 = Line().add_updater(lambda m: m.put_start_and_end_on(Q1.get_center(), Q2.get_center()))
        Q_lines = VGroup(Q0_Q1, Q1_Q2).set_color(YELLOW)

        R0 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        R1 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q2.get_center() - Q1.get_center()) * t.get_value() + Q1.get_center()))
        R = VGroup(R0, R1)

        R0_R1 = Line().add_updater(lambda m: m.put_start_and_end_on(R0.get_center(), R1.get_center())).set_color(PURPLE)

        B = Dot(color=RED).add_updater(lambda m: m.move_to((R1.get_center() - R0.get_center()) * t.get_value() + R0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("hello musa").scale(1.8).set_color(WHITE).shift(DOWN * 3)
        self.add(label)
        self.add(P, P_lines)
        self.add(Q, Q_lines)
        self.add(R, R0_R1)
        self.add(B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()



class FourthOrderBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([-3.6, -1.5, 0]))
        P1 = Dot(np.array([-4.2,  1.5, 0]))
        P2 = Dot(np.array([   0,  1.5, 0]))
        P3 = Dot(np.array([   2, -1.5, 0]))
        P4 = Dot(np.array([   3,  0.5, 0]))
        P = VGroup(P0, P1, P2, P3, P4).set_color(GREEN)
        
        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P2_P3 = Line(P2, P3)
        P3_P4 = Line(P3, P4)
        P_lines = VGroup(P0_P1, P1_P2, P2_P3, P3_P4).set_color(GREEN)

        t = ValueTracker(0)

        Q0 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q2 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P3.get_center() - P2.get_center()) * t.get_value() + P2.get_center()))
        Q3 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P4.get_center() - P3.get_center()) * t.get_value() + P3.get_center()))
        Q = VGroup(Q0, Q1, Q2, Q3)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        Q1_Q2 = Line().add_updater(lambda m: m.put_start_and_end_on(Q1.get_center(), Q2.get_center()))
        Q2_Q3 = Line().add_updater(lambda m: m.put_start_and_end_on(Q2.get_center(), Q3.get_center()))
        Q_lines = VGroup(Q0_Q1, Q1_Q2, Q2_Q3).set_color(YELLOW)

        R0 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        R1 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q2.get_center() - Q1.get_center()) * t.get_value() + Q1.get_center()))
        R2 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q3.get_center() - Q2.get_center()) * t.get_value() + Q2.get_center()))
        R = VGroup(R0, R1, R2)

        R0_R1 = Line().add_updater(lambda m: m.put_start_and_end_on(R0.get_center(), R1.get_center())).set_color(PURPLE)
        R1_R2 = Line().add_updater(lambda m: m.put_start_and_end_on(R1.get_center(), R2.get_center())).set_color(PURPLE)
        R_lines = VGroup(R0_R1, R1_R2)

        S0 = Dot(color=ORANGE).add_updater(lambda m: m.move_to((R1.get_center() - R0.get_center()) * t.get_value() + R0.get_center()))
        S1 = Dot(color=ORANGE).add_updater(lambda m: m.move_to((R2.get_center() - R1.get_center()) * t.get_value() + R1.get_center()))
        S = VGroup(S0, S1)

        S0_S1 = Line().add_updater(lambda m: m.put_start_and_end_on(S0.get_center(), S1.get_center())).set_color(GOLD)

        B = Dot(color=RED).add_updater(lambda m: m.move_to((S1.get_center() - S0.get_center()) * t.get_value() + S0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("beatyfull").scale(1.8).set_color(WHITE).shift(DOWN * 3)
        self.add(label)
        self.add(P, P_lines)
        self.add(Q, Q_lines)
        self.add(R, R_lines)
        self.add(S, S0_S1)
        self.add(B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()


class FifthOrderBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([  -3,   -2, 0]))
        P1 = Dot(np.array([-1.5,  2.5, 0]))
        P2 = Dot(np.array([   0, -0.5, 0]))
        P3 = Dot(np.array([ 1.5,    2, 0]))
        P4 = Dot(np.array([   3,    0, 0]))
        P5 = Dot(np.array([ 1.5,   -2, 0]))
        P = VGroup(P0, P1, P2, P3, P4, P5).set_color(GREEN)
        
        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P2_P3 = Line(P2, P3)
        P3_P4 = Line(P3, P4)
        P4_P5 = Line(P4, P5)
        P_lines = VGroup(P0_P1, P1_P2, P2_P3, P3_P4, P4_P5).set_color(GREEN)

        t = ValueTracker(0)

        Q0 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q2 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P3.get_center() - P2.get_center()) * t.get_value() + P2.get_center()))
        Q3 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P4.get_center() - P3.get_center()) * t.get_value() + P3.get_center()))
        Q4 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P5.get_center() - P4.get_center()) * t.get_value() + P4.get_center()))
        Q = VGroup(Q0, Q1, Q2, Q3, Q4)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        Q1_Q2 = Line().add_updater(lambda m: m.put_start_and_end_on(Q1.get_center(), Q2.get_center()))
        Q2_Q3 = Line().add_updater(lambda m: m.put_start_and_end_on(Q2.get_center(), Q3.get_center()))
        Q3_Q4 = Line().add_updater(lambda m: m.put_start_and_end_on(Q3.get_center(), Q4.get_center()))
        Q_lines = VGroup(Q0_Q1, Q1_Q2, Q2_Q3, Q3_Q4).set_color(YELLOW)

        R0 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        R1 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q2.get_center() - Q1.get_center()) * t.get_value() + Q1.get_center()))
        R2 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q3.get_center() - Q2.get_center()) * t.get_value() + Q2.get_center()))
        R3 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q4.get_center() - Q3.get_center()) * t.get_value() + Q3.get_center()))
        R = VGroup(R0, R1, R2, R3)

        R0_R1 = Line().add_updater(lambda m: m.put_start_and_end_on(R0.get_center(), R1.get_center()))
        R1_R2 = Line().add_updater(lambda m: m.put_start_and_end_on(R1.get_center(), R2.get_center()))
        R2_R3 = Line().add_updater(lambda m: m.put_start_and_end_on(R2.get_center(), R3.get_center()))
        R_lines = VGroup(R0_R1, R1_R2, R2_R3).set_color(PURPLE)

        S0 = Dot(color=ORANGE).add_updater(lambda m: m.move_to((R1.get_center() - R0.get_center()) * t.get_value() + R0.get_center()))
        S1 = Dot(color=ORANGE).add_updater(lambda m: m.move_to((R2.get_center() - R1.get_center()) * t.get_value() + R1.get_center()))
        S2 = Dot(color=ORANGE).add_updater(lambda m: m.move_to((R3.get_center() - R2.get_center()) * t.get_value() + R2.get_center()))
        S = VGroup(S0, S1, S2)

        S0_S1 = Line().add_updater(lambda m: m.put_start_and_end_on(S0.get_center(), S1.get_center()))
        S1_S2 = Line().add_updater(lambda m: m.put_start_and_end_on(S1.get_center(), S2.get_center()))
        S_lines = VGroup(S0_S1, S1_S2).set_color(GOLD)

        T0 = Dot(color=PINK).add_updater(lambda m: m.move_to((S1.get_center() - S0.get_center()) * t.get_value() + S0.get_center()))
        T1 = Dot(color=PINK).add_updater(lambda m: m.move_to((S2.get_center() - S1.get_center()) * t.get_value() + S1.get_center()))
        T = VGroup(T0, T1)

        T0_T1 = Line().add_updater(lambda m: m.put_start_and_end_on(T0.get_center(), T1.get_center())).set_color(PINK)

        B = Dot(color=RED).add_updater(lambda m: m.move_to((T1.get_center() - T0.get_center()) * t.get_value() + T0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("man is mortal").scale(1.8).set_color(WHITE).shift(DOWN * 3)
        self.add(label)
        self.add(P, P_lines)
        self.add(Q, Q_lines)
        self.add(R, R_lines)
        self.add(S, S_lines)
        self.add(T, T0_T1)
        self.add(B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()




        #

class Eoc1Thumbnail(Scene):
    CONFIG = {

    }

    def construct(self):
        title = TexText(
            "The Essence of\\\\Calculus",
            tex_to_color_map={
                "\\emph{you}": YELLOW,
            },
        )
        subtitle = TexText("Chapter 1")
        subtitle.match_width(title)
        subtitle.scale(0.75)
        subtitle.next_to(title, DOWN)
        # title.add(subtitle)
        title.set_width(FRAME_WIDTH - 2)
        title.to_edge(UP)
        title.set_stroke(BLACK, 8, background=True)
        # answer = TexText("...yes")
        # answer.to_edge(DOWN)

        axes = Axes(
            x_range=(-1, 5),
            y_range=(-1, 5),
            y_axis_config={
                "include_tip": False,
            },
            x_axis_config={
                "unit_size": 2,
            },
        )
        axes.set_width(FRAME_WIDTH - 1)
        axes.center().to_edge(DOWN)
        axes.shift(DOWN)
        self.x_axis = axes.x_axis
        self.y_axis = axes.y_axis
        self.axes = axes

        graph = axes.get_graph(self.func)
        rects = axes.get_riemann_rectangles(
            graph,
            x_range= [0,4],
            dx=0.1,
        )
        rects.set_submobject_colors_by_gradient(BLUE, GREEN)
        rects.set_opacity(1)
        rects.set_stroke(BLACK, 1)

        self.add(axes)
        self.add(graph)
        self.add(rects)
        self.add(title)
        # self.add(answer)

    def func(slef, x):
        return 0.35 * ((x - 2)**3 - 2 * (x - 2) + 6)



class length(Scene):
    def construct(self):

        axes = Axes(
            x_range=(-1, 9),
            y_range=(-1, 7),
            y_axis_config={
                "include_tip": True,
            },
            
        )
        axes.add_coordinate_labels()
        axes.set_width(FRAME_WIDTH - 1)
        axes.center().to_edge(DOWN)
        axes.shift(LEFT*0.5)
        self.x_axis = axes.x_axis
        self.y_axis = axes.y_axis
        self.axes = axes
        
        t = ValueTracker(1)
        


        dot1 = Dot().move_to(axes.c2p(1,1))
        dot2 = Dot().move_to(axes.c2p(7,5))
        dot3 = Dot().move_to(axes.c2p(1,1))
        # dot2 = Dot(color=BLUE).add_updater(lambda m: m.move_to((axes.c2p(dot1.get_center())) * t.get_value() + (axes.c2p(dot1.get_center()))))
        line1 = Line(dot1,dot2)
        # f_always(
        #     dot3.move_to,
        #     lambda: axes.i2gp(t.get_value(), line1)
        # )

        dot3 = Dot(color=BLUE).add_updater(lambda m: m.move_to(((axes.c2p(dot2.get_center()) - axes.c2p(dot1.get_center())) * t.get_value() + axes.c2p(dot1.get_center()))))

        h_line1 = always_redraw(lambda: axes.get_h_line(dot1.get_right()))
        v_line1 = always_redraw(lambda: axes.get_v_line(dot1.get_bottom()))

        h_line2 = always_redraw(lambda: axes.get_h_line(dot2.get_right()))
        v_line2 = always_redraw(lambda: axes.get_v_line(dot2.get_bottom()))










        self.add(axes,dot1,dot2,dot3, h_line1,h_line2,v_line1,v_line2)
        # self.play(t.animate.set_value(2), run_time=3)
        # self.play(t.animate.set_value(5), run_time=3)
        # self.wait()

        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()




class dif2(Scene):
    def construct(self):
        word = TexText("Different kinds of Matrix")

        grid = NumberPlane()
        # self.add(grid)

        self.wait(2)
        word.to_corner(UL)
        self.add(word)

        self.wait()


        m1 = [
            ["{A}_{1 1}","{A}_{1 2}", "{A}_{1 3}"],
            ["{A}_{2 1}","{A}_{2 2}", "{A}_{2 3}"],
            ["{A}_{3 1}","{A}_{3 2}", "{A}_{3 3}"]
        ]

        m2 = [
            ["{A}_{1 1}","{A}_{2 1}", "{A}_{3 1}"],
            ["{A}_{1 2}","{A}_{2 2}", "{A}_{3 2}"],
            ["{A}_{1 3}","{A}_{2 3}", "{A}_{3 3}"]
        ]

        mat1 = Matrix(m1).set_color(YELLOW)
        mat2 = Matrix(m2).set_color(YELLOW)
        mat2_col = mat2.get_columns()
        mat1_col = mat1.get_columns()
        vg = VGroup(Tex("{A}"), Tex("="), mat1, Tex("\ \ \ \ \ "),Tex("{B}"), Tex("="), mat2 )
        vg.arrange(RIGHT)
        self.play(Write(mat1))
        self.wait(1)
        self.add(
            vg
        )

class FunctionTracker(Scene):
    def construct(self):
        # f(x) = x**2
        fx = lambda x: x.get_value()**2
        # ValueTrackers definition
        x_value = ValueTracker(0)
        fx_value = ValueTracker(fx(x_value))
        # DecimalNumber definition
        x_tex = DecimalNumber(x_value.get_value()).add_updater(lambda v: v.set_value(x_value.get_value()))
        fx_tex = DecimalNumber(fx_value.get_value()).add_updater(lambda v: v.set_value(fx(x_value)))
        # TeX labels definition
        x_label = Tex("x = ")
        fx_label = Tex("x^2 = ")
        # Grouping of labels and numbers
        group = VGroup(x_tex,fx_tex,x_label,fx_label).scale(2.6)
        VGroup(x_tex, fx_tex).arrange(DOWN,buff=3)
        # Align labels and numbers
        x_label.next_to(x_tex,LEFT, buff=0.7,aligned_edge=x_label.get_bottom())
        fx_label.next_to(fx_tex,LEFT, buff=0.7,aligned_edge=fx_label.get_bottom())

        self.add(group.move_to(ORIGIN))
        self.wait(3)
        self.play(
            x_value.set_value,30,
            rate_func=linear,
            run_time=10
            )
        self.wait()
        self.play(
            x_value.set_value,0,
            rate_func=linear,
            run_time=10
            )
        self.wait(3)


class valuetracker(Scene):
    def construct(self):

        line1 = NumberLine(
            x_range= [0,12,1],

        unit_size = 0.5,
        # include_numbers = True,
        include_tip = True,
        
        )
        line2 = NumberLine(
            x_range= [0,12,1],

        unit_size = 0.5,
        # include_numbers = True,
        include_tip = True,
        
        )
        VGroup(line1,line2).arrange(3*DOWN)

        self.add(line1,line2)
        t = ValueTracker(0)
        # d_line1 = Dot()
        dot1 = Dot(color=RED)
        dot1.move_to(line1.get_start())
        dot1.add_updater(lambda m: m.move_to((line1.get_end() -  line1.get_start())*t.get_value() + line1.get_start()))
        
        dot2 = Dot(color=YELLOW)
        dot2.move_to(line2.get_start())
        dot2.add_updater(lambda m: m.move_to((line2.get_end() -  line2.get_start())*t.get_value() + line2.get_start()**2))
        self.add(dot1,dot2)
        self.play(t.increment_value, 1, run_time=14, rate_func=linear)
        self.wait()
        

class t2(Scene):
    def construct(self):
        
        word1= TexText("Matrix Operation")
        word2 = BulletedList(
            "Matrix Addition and Subtraction",
            "Matrix Multiplication"
        )
        word3 = TexText("Requirements:")

        self.add(
            word1
            )
        self.wait(2)

        self.play(word1.animate.to_corner(UL) )
        self.wait(2)

        self.play(Write(word2))
        self.wait(1)
        self.play(word2[0].animate.shift(UP*(1.5)), FadeOut(word2[1]))
        self.wait(2)

        word4 = Tex(
             "{P}", #0
            "_{m",#1
            " \\times ",#2
            "n } ",#3
            "+", #4
             "{Q}", #5
            "_{m",#6
            " \\times ",#7
            "n } ",#8
            "=",#9
             "{A}", #10
            "_{m",#11
            " \\times ",#12
            "n } ",#13
            )
        n = Tex("_{k",
         "\\times",
         "l}")
        
        for i in range(0,14,5):
            word4[i].set_color(WHITE)
            word4[i+1].set_color(RED)
            word4[i+3].set_color(YELLOW)
        n[0].set_color(RED)
        n[2].set_color(YELLOW)
        word4[4].set_color(BLUE)
        word4[10].set_color(BLUE)
        
        m = Tex("-")
        m.set_color(BLUE)

        o = Tex("{S}")
        o.set_color(BLUE)

        VGroup(word4,n,m,o).scale(1.5)

        self.play(GrowFromCenter(word4))
        self.wait(3)
        # for i in [3,8,13]:
        # n.copy().move_to(word4[i])
        self.play(
            ReplacementTransform(word4[1:4],n.copy().move_to(word4[1:4])),
            ReplacementTransform(word4[6:9],n.copy().move_to(word4[6:9])),
            ReplacementTransform(word4[11:14],n.copy().move_to(word4[11:14]))
        )
        self.wait(4)
        self.play(
            ReplacementTransform(word4[4],m.copy().move_to(word4[4])),
            ReplacementTransform(word4[10],o.copy().move_to(word4[10]))
        )


        

class projection(Scene):
    def construct(self):

        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        
        sin_graph = axes.get_graph(
            lambda x: 2 * math.cos(x),
            color=BLUE,
        )
        sin_label = axes.get_graph_label(sin_graph, "\\sin(x)")

        self.play(
            ShowCreation(sin_graph),
            FadeIn(sin_label, RIGHT),
        )
        circle = Circle()

        self.add(circle)

