from manimlib import *

# from manimlib.imports import *
import numpy as np

class OpeningQuote(Scene):
    def constrsuct(self):

        words = TexText("``The introduction of  numbers as \\\\ coordinates is an act of violence.''", t2c = {"coordinates": GREEN})
        words.to_edge(UP)
        for mob in words.submobjects[27:27+11]:
            mob.set_color(GREEN)
        author = TexText("-Hermann Weyl")
        author.set_color(YELLOW)
        author.next_to(words, DOWN, buff = 0.5)

        self.play(FadeIn(words))
        self.wait(1)
        self.play(Write(author, run_time = 4))
        self.wait()

    def intro(self):
        plane = NumberPlane()
        labels = VGroup(*plane.get_axis_labels())
        vector = Vector(RIGHT+2*UP, color = YELLOW)

        self.add(vector)

        self.wait(5)
        coordinates = vector_coordinate_label(vector)
        symbol = Tex("\\vec{\\textbf{v}}")
        sumbol.shift(0.5*(RIGHT+UP))
        self.play(ShowCreation(
            plane, lag_ratio = 1, run_time= 3
        ))

    def construct(self):
        

        v_color = YELLOW 
        w_color = BLUE
        sum_color = GREEN

        v_arrow = Vector([1, 1])
        w_arrow = Vector([2, 1])
        w_arrow.shift(v_arrow.get_end())
        sum_arrow = Vector(w_arrow.get_end())
        arrows = VGroup(v_arrow, w_arrow, sum_arrow)
        arrows.scale(0.7)
        arrows.to_edge(LEFT, buff = 2)

        v_array = matrix_to_mobject([3, -5])
        w_array = matrix_to_mobject([2, 1])
        sum_array = matrix_to_mobject(["3+2", "-5+1"])
        arrays = VGroup(
            v_array, Tex("+"), w_array, Tex("="), sum_array
        )
        arrays.arrange(RIGHT)
        arrays.scale(0.75)
        arrays.to_edge(RIGHT).shift(UP)

        v_sym = Tex("\\vec{\\textbf{v}}")
        w_sym = Tex("\\vec{\\textbf{w}}")
        syms = VGroup(v_sym, Tex("+"), w_sym)
        syms.arrange(RIGHT)
        syms.center().shift(2*UP)

        statement = TexText("We'll ignore him \\\\ for now")
        statement.set_color(PINK)
        statement.set_width(arrays.get_width())
        statement.next_to(arrays, DOWN, buff = 1.5)
        circle = Circle()
        circle.shift(syms.get_bottom())

        VGroup(v_arrow, v_array, v_sym).set_color(v_color)
        VGroup(w_arrow, w_array, w_sym).set_color(w_color)
        VGroup(sum_arrow, sum_array).set_color(sum_color)

        self.play(
            Write(syms), Write(arrays),
            ShowCreation(arrows),
           
            run_time = 2
        )
        
        self.add_scaling(arrows, syms, arrays)
        self.play(Write(statement))
        
        self.wait()
        self.play(
            ShowCreation(circle),
            
        )
        self.wait()

    def add_scaling(self, arrows, syms, arrays):
        s_arrows = VGroup(
            Tex("2"), Vector([1, 1]).set_color(YELLOW), 
            Tex("="), Vector([2, 2]).set_color(WHITE)
        )
        s_arrows.arrange(RIGHT)
        s_arrows.scale(0.75)
        s_arrows.next_to(arrows, DOWN)

        s_arrays = VGroup(
            Tex("2"), 
            matrix_to_mobject([3, -5]).set_color(YELLOW),
            TexText("="),
            matrix_to_mobject(["2(3)", "2(-5)"])
        )
        s_arrays.arrange(RIGHT)
        s_arrays.scale(0.75)
        s_arrays.next_to(arrays, DOWN)

        s_syms = Tex("2", "\\vec{\\textbf{v}}")
        s_syms.split()[-1].set_color(YELLOW)
        s_syms.next_to(syms, DOWN)

        self.play(
            Write(s_arrows), Write(s_arrays), Write(s_syms),
            run_time = 2
        )
        self.wait()


class HowIWantYouToThinkAboutVectors(Scene):
    def construct(self):
        vector = Vector([-2, 3])
        plane = NumberPlane()
        axis_labels = plane.get_axis_labels()
        other_vectors = VGroup(*list(map(Vector, [
            [1, 2], [2, -1], [4, 0]
        ])))
        colors = [GREEN_B, MAROON_B, PINK]
        for v, color in zip(other_vectors.split(), colors):
            v.set_color(color)
        shift_val = 4*RIGHT+DOWN

        dot = Dot(radius = 0.1)
        dot.set_color(RED)
        tail_word = TexText("Tail")
        tail_word.shift(0.5*DOWN+2.5*LEFT)
        line = Line(tail_word, dot)

        self.play(ShowCreation(vector))
        self.wait(2)
        self.play(
            ShowCreation(plane, lag_ratio=0.5),
            Animation(vector)
        )
        self.play(Write(axis_labels, run_time = 1))
        self.wait()
        self.play(
            GrowFromCenter(dot),
            ShowCreation(line),
            Write(tail_word, run_time = 1)
        )
        self.wait()
        self.play(
            FadeOut(tail_word),
            ApplyMethod(VGroup(dot, line).scale, 0.01) 
        )
        self.remove(tail_word, line, dot)
        self.wait()

        self.play(ApplyMethod(
            vector.shift, shift_val,
            path_arc = 3*np.pi/2,
            run_time = 3
        ))
        self.play(ApplyMethod(
            vector.shift, -shift_val,
            rate_func = rush_into,
            run_time = 0.5
        ))
        self.wait(3)

        self.play(ShowCreation(
            other_vectors, 
            run_time = 3
        ))
        self.wait(3)

        x_axis, y_axis = plane.get_axes().split()
        x_label = axis_labels.split()[0]
        x_axis = x_axis.copy()
        x_label = x_label.copy()
        everything = VGroup(*self.mobjects)
        self.play(
            FadeOut(everything),
            Animation(x_axis), Animation(x_label)
        )

class ListsOfNumbersAddOn(Scene):
    def construct(self):
        arrays = VGroup(*list(map(matrix_to_mobject, [
            [-2, 3], [1, 2], [2, -1], [4, 0]
        ])))
        arrays.arrange(buff = 0.4)
        arrays.scale(2)
        self.play(Write(arrays))
        self.wait(2)



class CoordinateSystemWalkthrough(Scene):
    def construct(self):
        self.introduce_coordinate_plane()
        self.show_vector_coordinates()
        self.coords_to_vector([3, -1])
        self.vector_to_coords([-2, -1.5], integer_labels = False)

    def introduce_coordinate_plane(self):
        plane = NumberPlane()
        x_axis, y_axis = plane.get_axes().copy().split()
        x_label, y_label = plane.get_axis_labels().split()
        number_line = NumberLine(tick_frequency = 1)
        x_tick_marks = number_line.get_tick_marks()
        y_tick_marks = x_tick_marks.copy().rotate(np.pi/2)
        tick_marks = VGroup(x_tick_marks, y_tick_marks)
        tick_marks.set_color(WHITE)
        plane_lines = [m for m in plane.get_family() if isinstance(m, Line)]
        origin_words = TexText("Origin")
        origin_words.shift(2*UP+2*LEFT)
        dot = Dot(radius = 0.1).set_color(RED)
        line = Line(origin_words.get_bottom(), dot.get_corner(UP+LEFT))

        unit_brace = Brace(Line(RIGHT, 2*RIGHT))
        one = Tex("1").next_to(unit_brace, DOWN)

        self.add(x_axis, x_label)
        self.wait()
        self.play(ShowCreation(y_axis))
        self.play(Write(y_label, run_time = 1))
        self.wait(2)
        self.play(
            Write(origin_words),
            GrowFromCenter(dot),
            ShowCreation(line),
            run_time = 1
        )
        self.wait(2)
        self.play(
            FadeOut(VGroup(origin_words, dot, line))
        )
        self.remove(origin_words, dot, line)
        self.wait()
        self.play(
            ShowCreation(tick_marks)
        )
        self.play(
            GrowFromCenter(unit_brace),
            Write(one, run_time = 1)            
        )
        self.wait(2)
        self.remove(unit_brace, one)
        self.play(
            *list(map(GrowFromCenter, plane_lines)) + [
            Animation(x_axis), Animation(y_axis)
        ])
        self.wait()
        self.play(
            FadeOut(plane),
            Animation(VGroup(x_axis, y_axis, tick_marks))
        )
        self.remove(plane)
        self.add(tick_marks)

    def show_vector_coordinates(self):
        starting_mobjects = list(self.mobjects)

        vector = Vector([-2, 3])
        x_line = Line(ORIGIN, -2*RIGHT)
        y_line = Line(-2*RIGHT, -2*RIGHT+3*UP)
        x_line.set_color(GREEN)
        y_line.set_color(YELLOW_D)

        array = vector_coordinate_label(vector)
        x_label, y_label = array.get_mob_matrix().flatten()
        x_label_copy = x_label.copy()
        x_label_copy.set_color(GREEN)
        y_label_copy = y_label.copy()
        y_label_copy.set_color(YELLOW_D)

        point = Dot(4*LEFT+2*UP)
        point_word = TexText("(-4, 2) as \\\\ a point")
        point_word.scale(0.7)
        point_word.next_to(point, DOWN)
        point.add(point_word)

        self.play(ShowCreation(vector))
        self.play(Write(array))
        self.wait(2)
        self.play(ApplyMethod(x_label_copy.next_to, x_line, DOWN))
        self.play(ShowCreation(x_line))
        self.wait(2)
        self.play(ApplyMethod(y_label_copy.next_to, y_line, LEFT))
        self.play(ShowCreation(y_line))
        self.wait(2)
        self.play(FadeIn(point))
        self.wait()
        self.play(ApplyFunction(
            lambda m : m.scale(1.25).set_color(YELLOW),
            array.get_brackets(),
            rate_func = there_and_back
        ))
        self.wait()
        self.play(FadeOut(point))
        self.remove(point)
        self.wait()
        self.clear()
        self.add(*starting_mobjects)


class test(Scene):
    def construct(self):
        vector = Vector([-2, 3])
        x_line = Line(ORIGIN, -2*RIGHT)
        y_line = Line(-2*RIGHT, -2*RIGHT+3*UP)
        x_line.set_color(GREEN)
        y_line.set_color(YELLOW_D)

        array = vector_coordinate_label(vector)



class DataAnalyst(Scene):
    def construct(self):
        plane = NumberPlane()
        ellipse = ParametricCurve(
            lambda x : 2*np.cos(x)*(UP+RIGHT) + np.sin(x)*(UP+LEFT),
            color = PINK, 
            t_max = 2*np.pi
        )
        ellipse_points = [
            ellipse.point_from_proportion(x)
            for x in np.arange(0, 1, 1./20)
        ]
        string_vects = [
            matrix_to_mobject(("%.02f %.02f"%tuple(ep[:2])).split())
            for ep in ellipse_points
        ]
        string_vects_matrix = Matrix(
            np.array(string_vects).reshape((4, 5))
        )
        string_vects = string_vects_matrix.get_mob_matrix().flatten()
        string_vects = VGroup(*string_vects)

        vects = VGroup(*list(map(Vector, ellipse_points)))

        self.play(Write(string_vects))
        self.wait(2)
        self.play(
            FadeIn(plane),
            Transform(string_vects, vects)
        )
        self.remove(string_vects)
        self.add(vects)
        self.wait()
        self.play(
            ApplyMethod(plane.fade, 0.7),
            ApplyMethod(vects.set_color, GREY_D),
            ShowCreation(ellipse)
        )
        self.wait(3)



class NameLinearCombinations(Scene):
    def construct(self):
        v_color = MAROON_C
        w_color = BLUE
        words = TexText(
            "``Linear combination'' of",
            "$\\vec{\\textbf{v}}$"
            # "and",
            # "$\\vec{\\textbf{w}}$"
        )
        words.split()[1].set_color(v_color)
        words.split()[3].set_color(w_color)
        words.set_width(FRAME_WIDTH - 1)
        words.to_edge(UP)

        equation = Tex([
            "a", "\\vec{\\textbf{v}}", "+", "b", "\\vec{\\textbf{w}}"
        ])
        equation.arrange(buff = 0.1, aligned_edge = DOWN)
        equation.split()[1].set_color(v_color)
        equation.split()[4].set_color(w_color)
        a, b = np.array(equation.split())[[0, 3]]
        equation.scale(2)
        equation.next_to(words, DOWN, buff = 1)

        scalars_word = TexText("Scalars")
        scalars_word.scale(1.5)
        scalars_word.next_to(equation, DOWN, buff = 2)
        arrows = [
            Arrow(scalars_word, letter)
            for letter in (a, b)
        ]

        self.add(equation)
        self.play(Write(words))
        self.play(
            ShowCreation(VGroup(*arrows)),
            Write(scalars_word)
        )
        self.wait(2)


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
            x_value.set_value,9,
            rate_func=linear,
            run_time=100
            )
        self.wait()
        self.play(
            x_value.set_value,0,
            rate_func=linear,
            run_time=10
            )
        self.wait(3)


class AddUpdaterFail(Scene):
    def construct(self):
        dot = Dot()
        text = Text("Label")\
               .next_to(dot,RIGHT,buff=SMALL_BUFF)

        self.add(dot,text)

        self.play(dot.shift,UP*2)
        self.wait()


class AddUpdater1(Scene):
    def construct(self):
        dot = Dot()
        text = Text("Label")\
               .next_to(dot,RIGHT,buff=SMALL_BUFF)

        self.add(dot,text)

        # Update function
        def update_text(obj):
            obj.next_to(dot,RIGHT,buff=SMALL_BUFF)

        # Add update function to the objects
        text.add_updater(update_text)

        # Add the object again
        self.add(text)

        self.play(dot.shift,UP*2)

        # Remove update function
        text.remove_updater(update_text)

        self.wait()

class AddUpdater2(Scene):
    def construct(self):
        dot = Dot()
        text = Text("Label")\
               .next_to(dot,RIGHT,buff=SMALL_BUFF)

        self.add(dot,text)

        # Add update function to the objects
        text.add_updater(lambda m: m.next_to(dot,RIGHT,buff=SMALL_BUFF))

        # Add the object again
        self.add(text)

        self.play(dot.shift,UP*2)

        # Remove update function
        text.clear_updaters()

        self.wait()

class AddUpdater3(Scene):
    def construct(self):
        dot = Dot()
        text = Text("Label")\
               .next_to(dot,RIGHT,buff=SMALL_BUFF)

        self.add(dot,text)

        def update_text(obj):
            obj.next_to(dot,RIGHT,buff=SMALL_BUFF)

        # Only works in play
        self.play(
                dot.shift(UP*2)
            )
        self.play(
                UpdateFromFunc(text,update_text)
            )
            

        self.wait()

class UpdateNumber(Scene):
    def construct(self):
        number_line = NumberLine(x_min=-1,x_max=1)
        triangle = RegularPolygon(3,start_angle=-PI/2)\
                   .scale(0.2)\
                   .next_to(number_line.get_left(),UP,buff=SMALL_BUFF)
        decimal = DecimalNumber(
                0,
                num_decimal_places=3,
                include_sign=True,
                unit="\\rm cm", # Change this with None
            )

        decimal.add_updater(lambda d: d.next_to(triangle, UP*0.1))
        decimal.add_updater(lambda d: d.set_value(triangle.get_center()[0]))
        #       You can get the value of decimal with: .get_value()

        self.add(number_line,triangle,decimal)

        self.play(
                triangle.shift,RIGHT*2,
                rate_func=there_and_back, # Change this with: linear,smooth
                run_time=5
            )

        self.wait()