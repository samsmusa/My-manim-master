from manim import *

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
        cirg = Circle().surround(triangle, buffer_factor=2)
        goup1= Group(cirg, triangle)
        self.add(cirg)
        self.add(goup1)
        self.wait(2)

        line = Line()
        circle2 = Circle().surround(line, buffer_factor=3)
        group2 = Group(line, circle2)
        group4 = Group(goup1, group2).arrange(buff =1)

        self.add(group4)
        self.wait(2)

"""
class MovingAngle(Scene):
    def construct(self):
        rotation_center = LEFT

        theta_tracker = ValueTracker(110)
        line1 = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )
        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        te = MathTex(r"\theta").move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )

        self.add(line1, line_moving, a, te)
        self.wait()

        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        a.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
        )
        te.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(140))
        self.play(te.animate.set_color(RED), run_time=0.5)
        self.play(theta_tracker.animate.set_value(350))

        
class ValueTrackerExample(Scene):
    def construct(self):
        number_line = NumberLine()
        pointer = Vector(DOWN)
        label = MathTex("x").add_updater(lambda m: m.next_to(pointer, UP))

        pointer_value = ValueTracker(0)
        pointer.add_updater(
            lambda m: m.next_to(
                        number_line.n2p(pointer_value.get_value()),
                                UP
                            )
                )
        self.add(number_line, pointer,label)
        self.play(pointer_value.animate.set_value(5)),
        self.wait()
        self.play(pointer_value.animate.set_value(3))

    
class text(Scene):
    def construct(self):
        text0 = Text('hello world', slant = ITALIC)
        text1 = Text('hello world', t2s={'world':ITALIC})
        text2 = Text('hello world', weight = BOLD)
        text3 = Text('hello world', t2w = {'world':BOLD})
        list_of_content = Tex(
        '$\\bullet$ a \\\\',
        '$\\bullet$ b \\\\',
        '$\\bullet$ c \\\\'
        )
        list2 =BulletedList(
            'hello musa',
            'hello world',
            'bangladesh', dot_scale_factor=7
        )

        # self.add(list_of_content)
        self.add(list2)

        # for i,mobj in enumerate(self.mobjects):
        #     mobj.shift(DOWN*(i-1))

        # self.add(list1)


class text2(Scene):
    def construct(self):
        text1 = Text('Google', t2c={'[:1]': '#3174f0',
                                    '[1:2]': '#e53125',
                                    '[2:3]': '#fbb003',
                                    '[3:4]': '#3174f0',
                                    '[5:]': '#e53125'},
                                    size = 1.2).scale=(3)

        self.add(text1)


class TextAlignment(Scene):
    def construct(self):
        title = Text("K-means", color=WHITE)
        title.scale_in_place(1)
        self.add(title.to_edge(UP))

        t1 = Text("1. Measuring").set_color(WHITE)
        t1.next_to(ORIGIN, direction=ORIGIN, aligned_edge=LEFT)

        t2 = Text("2. Clustering").set_color(WHITE)
        t2.next_to(t1, direction=DOWN, aligned_edge=LEFT)

        t3 = Text("3. Regression").set_color(WHITE)
        t3.next_to(t2, direction=DOWN, aligned_edge=LEFT)

        t4 = Text("4. Prediction").set_color(WHITE)
        t4.next_to(t3, direction=DOWN, aligned_edge=LEFT)

        x = VGroup(t1, t2, t3, t4).scale_in_place(0.7)
        x.set_opacity(0.5)
        x.submobjects[1].set_opacity(1)
        self.add(x)


class test(Scene):
    def construct(self):
        self.embd()

class MatrixExamples(Scene):
    def construct(self):
        m0 = Matrix([["2", "0"], ["-1", "1"]])
        m1 = Matrix([["1", "0"], ["0", "1"]],
                left_bracket="\\big(",
                right_bracket="\\big)")
        m2 = DecimalMatrix(
            [["3.456", "2.122"], ["33.2244", "12.33"]],
            element_to_mobject_config={"num_decimal_places": 2},
            left_bracket="\\{",
            right_bracket="\\}")

        self.add(m0.shift(LEFT - (3, 0, 0)))
        self.add(m1)
        self.add(m2.shift(RIGHT + (3, 0, 0)))


class pythag(Scene):
    
    def construct(self):
        left_square, right_square = Square(), Square()
        VGroup(left_square, right_square)\
            .scale(2)\
            .arrange_submobjects(RIGHT, buff = 2)
        
        dots = [
            left_square.point_from_proportion(i * 1/4 + 1/16) 
            for i in range(4)
        ]
        dots_corners = [
            left_square.point_from_proportion(i * 1/4)
            for i in range(4)
        ] 

        grid = NumberPlane()
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
        # pe = Dot(dots[0])

        self.add(grid)
        
        sq = Square()
        # self.add(sq)
        
        self.add(left_square)
        self.add(right_square)
        
        # self.remove(sq)
        


        # self.play(ShowCreation(Polygon([0,0,0],[3,0,0],[0,3,0],stroke_width=0.5,fill_opacity=0.3)), run_time = 5)

        
        # for i in range(4):
        #     self.add(Dot(dots[i]))
            
        #     self.add(Dot(dots_corners[i]))

        # self.play(ShowCreation(triangles), run_time = 3)

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
        # for i in range(len(rectangles)):

            # self.add(rectangles[i])
            # self.wait(2)
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


        theorem = TexMobject("c^2","=","a^2","+","b^2",color=BLUE).to_edge(DOWN)
        parts_theorem = VGroup(
            TexMobject("a^2").move_to(left_square),
            TexMobject("b^2").move_to(squares[0]),
            TexMobject("c^2").move_to(squares[1])
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
        #"""
    
"""      

class BoxAnimation(Scene):
    def construct(self):
        #Set objects
        box=Box()
        note=NoteBox()
        label=TexMobject("A",color=BLACK)
        #Set properties
        note.set_height(label.get_height()*2)
        note.move_to(box)
        label.move_to(note)

        self.play(DrawBorderThenFill(box))
        self.wait()
        self.play(FadeIn(note))
        note.add_updater(lambda d: d.move_to(box.box_center()))
        self.play(Write(label))
        label.add_updater(lambda d: d.move_to(note))


        self.play(box.shift,DOWN*3+LEFT*2,path_arc=PI/4)
        self.wait()
        self.play(open_box(box))

        self.play(box.shift,UP*4.5+RIGHT*4)
        self.wait()
        self.play(close_box(box))
        self.wait()



class OpeningManim(Scene):
    def construct(self):
        title = Text("")
        basel = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

       

        transform_title = Tex("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in basel]),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = Tex("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFrom(grid_title, direction=DOWN),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = Tex(
            r"That was a non-linear function \\ applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.animate.apply_function(
                lambda p: p
                          + np.array(
                    [
                        np.sin(p[1]),
                        np.sin(p[0]),
                        0,
                    ]
                )
            ),
            run_time=3,
        )
        self.wait()
        self.play(Transform(grid_title, grid_transform_title))
        self.wait()
        


class NumericalMatrixMultiplication(Scene):
    CONFIG = {
        "left_matrix": [[1, 2], [3, 4]],
        "right_matrix": [[5, 6], [7, 8]],
        "use_parens": True,
    }

    def construct(self):

        left_matrix = [[1, 2], [3, 4]]
        right_matrix = [[5, 6], [7, 8]]
        use_parens = True

        left_string_matrix, right_string_matrix = [
            np.array(matrix)
            for matrix in (left_matrix, right_matrix)
        ]
        if right_string_matrix.shape[0] != left_string_matrix.shape[1]:
            raise Exception("Incompatible shapes for matrix multiplication")

        left = Matrix(left_string_matrix)
        col = left.get_columns
        col1 = Matrix(col)
        right = Matrix(right_string_matrix).shift(2*DOWN)

        # kkk = matrix_to_mobject(left)
        self.add(col1)
        self.wait(4)
        # result = self.get_result_matrix(
        #     left_string_matrix, right_string_matrix
        # )
        self.play(ShowCreation(left))
        self.wait(2)
        # self.organize_matrices(left, right, result)
        # self.animate_product(left, right, result)
        self.play(Transform(left, right), run_time = 10)

        VMobject
"""
"""
    def get_result_matrix(self, left, right):
        (m, k), n = left.shape, right.shape[1]
        mob_matrix = np.array([VGroup()]).repeat(m * n).reshape((m, n))
        for a in range(m):
            for b in range(n):
                template = "(%s)(%s)" if self.use_parens else "%s%s"
                parts = [
                    prefix + template % (left[a][c], right[c][b])
                    for c in range(k)
                    for prefix in ["" if c == 0 else "+"]
                ]
                mob_matrix[a][b] = Tex(parts, next_to_buff=0.1)
        return Matrix(mob_matrix)

    def add_lines(self, left, right):
        line_kwargs = {
            "color": BLUE,
            "stroke_width": 2,
        }
        left_rows = [
            VGroup(*row) for row in left.get_mob_matrix()
        ]
        h_lines = VGroup()
        for row in left_rows[:-1]:
            h_line = Line(row.get_left(), row.get_right(), **line_kwargs)
            h_line.next_to(row, DOWN, buff=left.v_buff / 2.)
            h_lines.add(h_line)

        right_cols = [
            VGroup(*col) for col in np.transpose(right.get_mob_matrix())
        ]
        v_lines = VGroup()
        for col in right_cols[:-1]:
            v_line = Line(col.get_top(), col.get_bottom(), **line_kwargs)
            v_line.next_to(col, RIGHT, buff=right.h_buff / 2.)
            v_lines.add(v_line)

        self.play(ShowCreation(h_lines))
        self.play(ShowCreation(v_lines))
        self.wait()
        self.show_frame()

    def organize_matrices(self, left, right, result):
        equals = Tex("=")
        everything = VGroup(left, right, equals, result)
        everything.arrange()
        everything.set_width(FRAME_WIDTH - 1)
        self.add(everything)

    def animate_product(self, left, right, result):
        l_matrix = left.get_mob_matrix()
        r_matrix = right.get_mob_matrix()
        result_matrix = result.get_mob_matrix()
        circle = Circle(
            radius=l_matrix[0][0].get_height(),
            color=GREEN
        )
        circles = VGroup(*[
            entry.get_point_mobject()
            for entry in (l_matrix[0][0], r_matrix[0][0])
        ])
        (m, k), n = l_matrix.shape, r_matrix.shape[1]
        for mob in result_matrix.flatten():
            mob.set_color(BLACK)
        lagging_anims = []
        for a in range(m):
            for b in range(n):
                for c in range(k):
                    l_matrix[a][c].set_color(YELLOW)
                    r_matrix[c][b].set_color(YELLOW)
                for c in range(k):
                    start_parts = VGroup(
                        l_matrix[a][c].copy(),
                        r_matrix[c][b].copy()
                    )
                    result_entry = result_matrix[a][b].split()[c]

                    new_circles = VGroup(*[
                        circle.copy().shift(part.get_center())
                        for part in start_parts.split()
                    ])
                    self.play(Transform(circles, new_circles))
                    self.play(
                        Transform(
                            start_parts,
                            result_entry.copy().set_color(YELLOW),
                            path_arc=-np.pi / 2,
                            lag_ratio=0,
                        ),
                        *lagging_anims
                    )
                    result_entry.set_color(YELLOW)
                    self.remove(start_parts)
                    lagging_anims = [
                        ApplyMethod(result_entry.set_color, WHITE)
                    ]

                for c in range(k):
                    l_matrix[a][c].set_color(WHITE)
                    r_matrix[c][b].set_color(WHITE)
        self.play(FadeOut(circles), *lagging_anims)
        self.wait()
        """

"""
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

    def construct(self):
        plane = NumberPlane()
        labels = VGroup(*plane.get_axis_labels())
        vector = Vector(["1","2"])

        self.add(vector)

        self.wait(5)
        coordinates = vector_coordinate_label(vector)
        symbol = Tex("\\vec{\\textbf{v}}")
        sumbol.shift(0.5*(RIGHT+UP))
        self.play(ShowCreation(
            plane, lag_ratio = 1, run_time= 3
        ))
        """

class NewYearPost(MovingCameraScene):
    def construct(self):
        self.camera_frame.move_to(3 * UP)
        text = MathTex(
            r" s(t) &=\left( \begin{array}{c} "
            r"x(t)"
            r"\\ y(t)"
            r"\end{array} \right)"
            r"\\ &=\left( \begin{array}{c} "
            r"v_0 t \cos(\theta)"
            r"\\ v_0 t \sin(\theta) - \frac{1}{2}gt^2"
            r"\end{array} \right)"
        )

        text.to_corner(DL).shift(3 * UP)

        def func(t):
            v0 = 10
            theta = 0.85 * PI / 2
            g = 9.81
            return np.array(
                (v0 * t * np.cos(theta), v0 * t * np.sin(theta) - 0.5 * g * t ** 2, 0)
            )

        rocket = ParametricFunction(func, t_max=1, fill_opacity=0).set_color(WHITE)
        dot = Dot().set_color(WHITE)
        dot2 = Dot().set_color(WHITE).move_to(rocket.get_end())
        self.add(dot)
        self.play(Write(rocket), rate_func=linear)
        self.add(dot2)
        all_sparcs = VGroup()
        for theta in np.random.uniform(0, TAU, 90):

            def func2(t):
                v0 = 10
                g = 9.81
                return np.array(
                    (
                        v0 * t * np.cos(theta) + dot2.get_x(),
                        v0 * t * np.sin(theta) - 0.5 * g * t ** 2 + dot2.get_y(),
                        0,
                    )
                )

            sparcle = ParametricFunction(
                func2, t_min=0.04, t_max=0.3, fill_opacity=0
            ).set_color(ORANGE)
            all_sparcs.add((sparcle))
        self.play(
            *[Write(x) for x in all_sparcs.submobjects], run_time=0.8, rate_func=linear
        )
        dots = [
            Dot(point=[x, y, 0])
            for x, y in zip(np.random.uniform(-4, 4, 10), np.random.uniform(0, 6, 10))
        ]
        self.play(*[Flash(dot) for dot in dots], lag_ratio=0.2)
        dots = [
            Dot(point=[x, y, 0])
            for x, y in zip(np.random.uniform(-4, 4, 10), np.random.uniform(0, 6, 10))
        ]
        self.play(FadeIn(text), *[Flash(dot) for dot in dots], lag_ratio=0.2)
        dots = [
            Dot(point=[x, y, 0])
            for x, y in zip(np.random.uniform(-4, 4, 30), np.random.uniform(0, 6, 30))
        ]
        self.play(*[Flash(dot) for dot in dots], lag_ratio=0.2)

        banner = ManimBanner(dark_theme=True).scale(0.3).to_corner(DR)
        self.play(FadeIn(banner.shift(3 * UP)))
        self.play(banner.expand())
        self.play(FadeOut(banner))
        x_number_line_group = self.get_number_line_group(
            "x",30,0.2,step_label=10,v_tracker=x_value,tick_frequency=2
            )