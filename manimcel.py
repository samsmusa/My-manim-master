from manimlib import *

# from manimlib.imports import *
import numpy as np




class shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)
        te = TexText("hllo musa")

        self.add(circle,square,triangle)
        self.wait(1)
        self.add(te)

#position

class pos(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.move_to(LEFT*2)
        square.next_to(circle, LEFT)
        triangle.align_to(circle, LEFT)

        self.add(circle,square, triangle)
        self.wait(1)
        square.shift(LEFT)
        self.add(square)
#styling MObject

class ms(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)
        ject = VGroup(circle,square,triangle)
        circle.set_stroke(color=GREEN, width =20)
        square.set_fill(YELLOW, opacity = 1.0)
        triangle.set_fill(PINK, opacity = 0.5).set_stroke(GREEN, width=0)

        self.play(ShowCreation(ject), run_time = 5)
        self.wait(1)


class anim(Scene):
    def construct(self):
        square = Square()
        self.add(square)

        self.play(FadeIn(square))
        self.play(Rotate(square, PI/4))
        self.play(FadeOut(square))
        self.wait()

class applM(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=0.5)
        self.add(square)
        circle = Circle().set_fill(BLUE, opacity=1)

        self.play(ApplyMethod(square.set_fill, WHITE))
        self.wait(2)

        self.play(Transform(square, circle),rnn_time = 4)
        self.wait()


class WriteStuff(Scene):
    def construct(self):
        dot =  Dot([-2,-1,0])
        self.add(dot)
        self.wait(3)
        dot2 = Dot([2,1,0])
        self.add(dot2)
        self.wait(3)
        line = Line(dot.get_center(),dot2.get_center()).set_color(ORANGE)
        self.play(ShowCreation(line))
        self.wait(3)
        b1 = Brace(line)
        self.add(b1)
        self.wait(3)
        b1text = b1.get_text("Horizontal distanace")
        self.add(b1text)
        self.wait(3)
        b2 = Brace(line, direction = line.copy().rotate(PI/3).get_unit_vector())
        self.play(ShowCreation(b2))
        self.wait(3)
        b2text = b2.get_tex("x-x_1")
        self.add(b2text)


class vector(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        self.add(dot)
        self.wait(2)
        arrow = Arrow(ORIGIN,[2,2,0],buff=0)
        self.add(arrow)
        self.wait(2)
        numberplane = NumberPlane()
        self.play(Animation(numberplane))
        self.wait(2)
        origin_text = Text('(0,0)').next_to(dot, DOWN)
        self.add(origin_text)
        self.wait(2)
        tip_text = Text('(2,2)').next_to(arrow.get_end(),RIGHT)
        self.add(tip_text)
        self.wait(2)

class cir(Scene):
    def construct(self):
        circle = Circle(radius = 1, color = BLUE, fill_opacity = 0.5)
        tex= Text("now we have to discuss circle")
        tex.to_corner(UP+LEFT)
        self.play(Write(tex))
        self.wait(2)
        self.add(circle)
        self.wait(2)
        self.remove(circle)
        self.wait(2)

        # p1= circle.point_at_angle(90*DEGREES)
        # s1= Square(side_length=0.25).move_to(p1)
        # self.add(s1)
        # self.wait(2)

        triangle = Triangle()
        cirg = Circle().surround(triangle)
        goup1= Group(cirg, triangle)
        # self.add(cirg)
        self.add(goup1)
        self.wait(2)

        
from manimlib import *

class InteractiveDevlopment(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()

        # This opens an iPython termnial where you can keep writing
        # lines as if they were part of this construct method.
        # In particular, 'square', 'circle' and 'self' will all be
        # part of the local namespace in that terminal.
        self.embed()

        # Try copying and pasting some of the lines below into
        # the interactive shell
        self.play(ReplacementTransform(square, circle))
        self.wait()
        self.play(circle.animate.stretch(4, 0))
        self.play(Rotate(circle, 90 * DEGREES))
        self.play(circle.animate.shift(2 * RIGHT).scale(0.25))

        text = Text("""
            In general, using the interactive shell
            is very helpful when developing new scenes
        """)
        self.play(Write(text))

        # In the interactive shell, you can just type
        # play, add, remove, clear, wait, save_state and restore,
        # instead of self.play, self.add, self.remove, etc.

        # To interact with the window, type touch().  You can then
        # scroll in the window, or zoom by holding down 'z' while scrolling,
        # and change camera perspective by holding down 'd' while moving
        # the mouse.  Press 'r' to reset to the standard camera position.
        # Press 'q' to stop interacting with the window and go back to
        # typing new commands into the shell.

        # In principle you can customize a scene to be responsive to
        # mouse and keyboard interactions
        always(circle.move_to, self.mouse_point)


class test(Scene):
    def construct(self):
        self.embed()

class text(Scene):
    def construct(self):
        text0 = Text('hello world', slant = ITALIC)
        text1 = Text('hello world', t2s={'world':ITALIC})
        text2 = Text('hello world', weight = BOLD)
        text3 = Text('hello world', t2w = {'world':BOLD})

        self.add(text0,text1,text2,text3)

        text0.shift(DOWN)
        text1.shift(DOWN*2)
        text2.shift(DOWN*3)
        text3.shift(DOWN*4)


        # for i,mobj in enumerate(self.mobjects):
        #     mobj.shift(DOWN*(i-1))

class MatrixExamples(Scene):
    def construct(self):
        m0 = Matrix([["2", "0"], ["-1", "1"]])
        m1 = Matrix([["1", "0"], ["0", "1"]],
                left_bracket="\\big(",
                right_bracket="\\big)")
        # # m2 = DecimalMatrix(
        #     [["3.456", "2.122"], ["33.2244", "12.33"]],
        #     element_to_mobject_config={"num_decimal_places": 2},
        #     left_bracket="\\{",
        #     right_bracket="\\}")

        self.add(m0.shift(LEFT - (3, 0, 0)))
        self.play(ShowCreation(m1))
        # self.add(m2.shift(RIGHT + (3, 0, 0)))


class pythag(Scene):
    CONFIG = {
        "square_scale": 2
    }
    def construct(self):
        left_square, right_square = Square(), Square()
        VGroup(left_square, right_square)\
            .scale(self.square_scale)\
                .arrange(RIGHT, buff = 2)

        grid = NumberPlane()

        self.add(grid)


        self.add(left_square)
        self.add(right_square)



        dots = [
            left_square.point_from_proportion(i * 1/4 + 1/16) 
            for i in range(4)
        ]
        dots_corners = [
            left_square.point_from_proportion(i * 1/4)
            for i in range(4)
        ] 

        triangles = VGroup(*[
            Polygon(
                dots[i],
                dots_corners[i],
                dots[i-1],
                stroke_width=0,
                fill_opacity=0.7
            )
            for i in range(4)
        ])

        dots2 = [
            right_square.point_from_proportion(i * 1/4 + j * 1/16)
            for i,j in zip(range(4),[1,3,3,1])
        ]
        dots_corners2 = [
            right_square.point_from_proportion(i * 1/4) 
            for i in range(4)
        ]
        middle = np.array([
            dots2[0][0],
            dots2[1][1],
            0
        ])

        for i in range(4):
            self.add(Dot(dots2[i], color = GREEN))
            self.wait()
            self.add(Dot(dots_corners2[i]))
            self.wait()
        self.add(Dot(middle, color = RED))
        self.wait()

        all_rectangles = VGroup(*[
            Polygon(
                dots_corners2[i],
                dots2[i],
                middle,
                dots2[i-1],
            )
            for i in range(4)
        ])

        rectangles = all_rectangles[0::2]


        squares = all_rectangles[1::2]

        total_points = 4
        rect_dot = [
            [
                rectangles[i].points[total_points*j]
                for j in range(4)
            ]
            for i in range(2)
        ]
        for j in rect_dot:
            for i in [0,1,2,3]:

                self.add(
                    Dot(j[i], color = YELLOW)
                
                    )
            
                self.wait()

         
        triangles2 = VGroup(*[
            Polygon(
                rect[i+1],
                rect[i],
                rect[i-1],
                fill_opacity=0.7
            )
            for rect in rect_dot
            for i in [0,2]
        ])
        self.play(ShowCreation(triangles2))


        theorem = Tex("c^2","=","a^2","+","b^2",color=BLUE).to_edge(DOWN)
        parts_theorem = VGroup(
            Tex("a^2").move_to(left_square),
            Tex("b^2").move_to(squares[0]),
            Tex("c^2").move_to(squares[1])
        )

        # self.play(ShowCreation(parts_theorem), run_time = 3)
        #print(len(triangles2))


        self.play(
            *list(map(
                DrawBorderThenFill,
                [left_square,right_square,triangles.copy()
            ])), run_time = 20
        )


        self.play(
            *[
                ApplyMethod(
                    triangles[i].move_to,
                    triangles2[i].get_center()
                )
                for i in range(len(triangles))
            ], run_time = 30
        )

        self.play(
                Rotate(triangles[1],-PI/2),
                Rotate(triangles[2],PI/2),
        )
        self.play(
            ShowCreation(squares),
            Write(parts_theorem)
        )
      

class text(Scene):
    def construct(self):
        source = Text("PRESENTATION!!  PRESENTATION!!", color= RED, height=0.5)
        target = Text("ASTRONOMY!!  ASTRONOMY!!", color = GREEN, height=0.5)

        self.play(Write(source))
        self.wait()
        kw = {"run_time": 3, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(source, target, **kw))
        self.wait()
        self.play(TransformMatchingShapes(target, source, **kw))
        self.wait()

        
        
class MatrixExamples(Scene):
    def construct(self):
        m0 = Matrix([[2, 0], [-1, 1]])
        # m1 = Matrix([[1, 0], [0, 1]],
        #             left_bracket="\\big(",
        #             right_bracket="\\big)")
        # m2 = DecimalMatrix(
        #     [[3.456, 2.122], [33.2244, 12.33]],
        #     element_to_mobject_config={"num_decimal_places": 2},
        #     left_bracket="\\{",
        #     right_bracket="\\}")

        self.add(m0.shift(LEFT - (3, 0, 0)))
        # self.add(m1)
        # self.add(m2.shift(RIGHT + (3, 0, 0)))

class OpeningQuote(Scene):

    def construct(self):
        words = TexText(
            """
            ``There is hardly any theory which is more elementary 
            than linear algebra, in spite of the fact that generations 
            of professors and textbook writers have obscured its 
            simplicity by preposterous calculations with matrices.''
            """, 
            organize_left_to_right = False
        )
        words.set_width(2*(FRAME_X_RADIUS-1))
        words.to_edge(UP)        
        for mob in words.submobjects[48:49+13]:
            mob.set_color(GREEN)
        author = TexText("-Jean Dieudonn\\'e")
        author.set_color(YELLOW)
        author.next_to(words, DOWN)

        self.play(FadeIn(words))
        self.wait(3)
        self.play(Write(author, run_time = 5))
        self.wait()

class t1d(Scene):
    def construct(self):
        plane = NumberPlane()
        # self.embed()
        list1 = [["3","3","3"],["3","3","3"],["3","3","3"]]
        list2 = ["3","3","3","3","3","3","3","3","3"]
       

        self.play(ShowCreation(plane))
        self.wait(4)

        matrix = Matrix([
                    ["2", "2"],
                    ["2","2"]
                ])

        # matrix[1][1]

        matrix.add_background_rectangle()
        matrix.set_column_colors(RED)
        # matrix.get
        self.add(matrix.shift(3*LEFT))
        self.wait(2)


        # list2 = matrix.get_entries()
        # mat3 = Matrix([matrix.get_columns()])
        mat2 = Matrix([[list2[0:2]],[list2[2:4]]])
        # matrix.set_column_colors(RED,2)
        # self.play(Transform(matrix, mat2), run_time =5)
        self.add(mat2)
        self.wait(2)
        # self.embed()
        mat4 = matrix.get_columns
        # var =  
        # self.remove(mat2)

        # mat4 = Tex(begin{bmatrix} 
        #             a & b & c \
        #             c & d & d\
        #             e & f & g \
        #             end{bmatrix})
        # # self
        # # self.add(mat3)

class Shapes(Scene):
    #A few simple shapes
    #Python 2.7 version runs in Python 3.7 without changes
    def construct(self):
        circle = Circle()
        square = Square()
        line=Line(np.array([3,0,0]),np.array([5,0,0]))
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))

        
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square,triangle))
        self.add(line)

class MoreShapes(Scene):
    #A few more simple shapes
    #2.7 version runs in 3.7 without any changes
    #Note: I fixed my 'play command not found' issue by installing sox
    def construct(self):
        self.embed()
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP+LEFT)
        circle.surround(square)
        rectangle = Rectangle(height=2, width=3)
        ellipse=Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        pointer = CurvedArrow(2*RIGHT,5*RIGHT,color=MAROON_C)
        arrow = Arrow(LEFT,UP)
        arrow.next_to(circle,DOWN+LEFT)
        rectangle.next_to(arrow,DOWN+LEFT)
        ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)

        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square),FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))

# class anb(Scene):
#     def __init__(self, t, b, i, j, **kwargs):
#         bo = SurroundingRectangle(t[j])
#         self.play(b.animate.shift(i*DOWN))
#         self.play(ReplacementTransform(b,bo))


       
class matrx(Scene):
    def construct(self):
        list1 = [
            ["1","2","3"],
            ["4","5","6"],
            ["7","8","9"]
        ]
        txt = Tex(*list1[0][:])
        txt2 = Tex(*list1[1][:])
        txt3 = Tex(*list1[2][:])
        # tex11 = Tex(list1[0][0])
        # tex12 = Tex(list1[0][1])
        # tex13 = Tex(list1[0][2])
        self.embed()
        for i in range(len(txt)):
            if i == 2:
                break 
            else:
                txt[i+1].next_to(txt[i], 3*RIGHT)

        for i in range(len(txt2)):
            if i == 2:
                break 
            else:
                txt2[i+1].next_to(txt2[i], 3*RIGHT)

        for i in range(len(txt)):
            if i == 2:
                break 
            else:
                txt3[i+1].next_to(txt3[i], 3*RIGHT)
            

        txt_group = VGroup(txt,txt2.shift(DOWN),txt3.shift(2*DOWN)).set_color(RED)
        brace = Brace(txt_group, LEFT)
        brace2 = Brace(txt_group, RIGHT)

        gr = VGroup(brace,txt_group,brace2)
        bo = SurroundingRectangle(txt[0][0])
        bo1 = SurroundingRectangle(txt2[2])
        # bo.shift(DOWN)
        # self.add(bo)
        



        self.play(FadeIn(gr))
        self.wait(2)
        self.add(bo)
        self.wait()
        # bo.shift(DOWN)
        self.play(bo.animate.shift(DOWN))
        self.wait()
        # def anb(self, j):
        #     bo = SurroundingRectangle(self[j])

        #     return bo
        
        self.play(ReplacementTransform(bo,bo1))
        self.wait()
        # self.play(ApplyMethod(bo.next_to(LEFT)))


        # for i in 

        # self.add(txt_group)


class matrixT(Scene):
    def construct(self):
        list1 = [
            ["1","2","3"],
            ["4","5","6"],
            ["7","8","9"]
        ]

        list2 = [
            ["a","b","d"],
            ["e","f","g"],
            ["h","i","j"]
        ]

        mat1, mat2, mat3= Matrix(list1), Matrix(list2), Matrix(list2)

        mat1.shift(4*LEFT)
        mat3.shift(4.5*RIGHT)
        self.play(Write(mat1),Write(mat2), Write(mat3))

        # # mat1.get_columns()

        # mat3 = mat2.get_columns()
        # mat3[0].shift(4*RIGHT)
        # self.add(mat3[0])

        # list3 = mat1.get_entries()
        # # self.add(list3)
        # list3[0].shift(DOWN*3)

        # te = matrix_to_mobject(list2)
        # te.shift(UP*2)
        # self.add(te)
        # te1 =Tex(matrix_to_tex_string(list2))
        # te1.shift(UP*2 + LEFT*4)
        # self.add(te1)
        mat2_col = mat2.get_columns()
        # mat3.get_width()
        mat1_col = mat1.get_columns()
        mat3_col = mat3.get_columns()
        rec1 = SurroundingRectangle(mat1_col[0])
        rec2 = SurroundingRectangle(mat3_col[0])
        rec_row1 = SurroundingRectangle(mat1[0][0:3]).set_color(RED)
        rec_row2 = SurroundingRectangle(mat3[0][0:3]).set_color(RED)
        col_rec1 = SurroundingRectangle(mat2_col[0])
        rec1 = SurroundingRectangle(mat1_col[0])
        # rec1 = SurroundingRectangle(mat1_col[0])
        rec2 = SurroundingRectangle(mat3_col[0], height = 3)
        self.add(rec_row1, col_rec1)
        # self.play(ReplacementTransform(rec1, rec_row1))

        formula =Tex(
            "1",
            ".",
            "a",
            "+",
            "2",
            ".",
            "e",
            "+",
            "3",
            ".",
            "h"

        )
        # fo = Tex([formula[0],formula[4],formula[8]])
        formula.shift(DOWN*3)
        self.play(
            ReplacementTransform(mat1[0][0].copy(), formula[0]),
            ReplacementTransform(mat1[0][1].copy(), formula[4]),
            ReplacementTransform(mat1[0][2].copy(), formula[8]),
            ReplacementTransform(mat2_col[0][0].copy(), formula[2]),
            ReplacementTransform(mat2_col[0][1].copy(), formula[6]),
            ReplacementTransform(mat2_col[0][2].copy(), formula[10]),

        )
        self.play(
            ReplacementTransform(rec1, rec2),
            ReplacementTransform(rec_row1, rec_row2)
        )
        # self.add(formula)
        # si
