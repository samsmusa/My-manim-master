from manimlib import *

# from manimlib.imports import *
import numpy as np



class quote(Scene):
    def construct(self):
  
        quote = TexText("``Beauty is the first test:\\\\ There is no permanent place in the world for ugly Mathematics.''"
            
            )

       

        
        quote[0][63:74].set_color(BLUE)
        

        quote[0][2:8].set_color(BLUE) 

        
        self.play(Write(quote, run_time = 5))

        quote1 = VGroup(quote[0][63:74],quote[0][2:8])

        then= TexText("Mathematics = Beauty")

        
        then[0][0:11].set_color(BLUE)
        then[0][12:20].set_color(BLUE)
        

        

        author = TexText("-G. H. Hardy").set_color(YELLOW).scale(1.2).shift(DOWN)
        self.play(Write(author, run_time= 2))
        self.wait()
        self.play(FadeOut(author))
        self.play(
                FadeOut(quote[0][0:2]), 
                FadeOut(quote[0][74:]) ,run_time = 3)
        

        self.play(
            ReplacementTransform(quote[0][2:8], then[0][12:20]),
            ReplacementTransform(quote[0][63:74], then[0][0:11]),
            FadeOut(quote[0][8:63]),
            
            
            FadeIn(then[0][11:12], run_time = 2)
        )






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

        m1 = np.array([[1,4,7],[2,5,8]])
        m2 = np.array([[1,4],[2,5],[3,6]])
        m3 = np.dot(m1,m2) 
        matr3 = matrix_to_mobject(m1)

        self.add(matr3)

        formula =Tex(
            "1",
            ".",
            " a",
            "+",
            "2",
            ".",
            " e",
            "+",
            "3",
            ".",
            " h"

        )
        # fo = Tex([formula[0],formula[4],formula[8]])
        formula.shift(DOWN*3)
        self.play(
            ReplacementTransform(mat1[0][0].copy(), formula[0]),
            ReplacementTransform(mat1[0][1].copy(), formula[4]),
            ReplacementTransform(mat1[0][2].copy(), formula[8])
           
        )
        self.add(
            formula[1],
            formula[3],
            formula[5],
            formula[7],
            formula[9]
        )

        self.play(
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
class matrixt2(Scene):
    def construct(self):
        m1 = np.array([[1,4,7],[2,5,8]])
        m2 = np.array([[1,4],[2,5],[3,6]])
        m3 = np.dot(m1,m2) 
        matr1,matr2,matr3 = matrix_to_mobject(m1),matrix_to_mobject(m2),matrix_to_mobject(m3)
        matr1.shift(2*RIGHT)
        matr2.shift(2*RIGHT)
        matr3.shift(2*RIGHT)

        # matr2_col = matr2.get_columns()

        # equ = np.m1[0]
        m1_t = Tex("{A}_{2\\times 3} = \\")
        m1_t.shift(0.5*LEFT)

        mat_a = VGroup(m1_t,matr1)
        # mat_a.to_corner(LEFT+UP)

        m2_t = Tex("{B}_{3\\times 2} = \\")
        m2_t.shift(0.5*LEFT)
        mat_b = VGroup(m2_t,matr2)
        # mat_b.align_to(mat_a, )

        mat = VGroup(mat_a, mat_b)
        mat.arrange(DOWN)
        mat.to_corner(UP+LEFT)

        formula = Tex(
            "\\  {A}",               #0
            "_{2\\times 3} \\", #1
            "\\times",          #2
            "\\  {B}",          #3
            "_{3\\times 2} \\", #4
            "=",                #5
            "(",                #6
            "{A}",              #7
            "{B}",              #8
            ")",                #9
            "_{2\\times 2} \\"       #10

        )
        formula2 = Tex(
            "2",            #0
            "\\times",      #1
            "3",            #2
            "\\times",#3
            "3",            #4
            "\\times",      #5
            "2"             #6
        )

        tex = VGroup(formula,formula2).arrange(DOWN).shift(DOWN)
        

        self.play(Write(mat))
        self.play(
            ReplacementTransform(m1_t.copy(), formula[0:2]),
            ReplacementTransform(m2_t.copy(),formula[2:5])

        )
        self.play(Write(formula[5]),Write(formula[6]),Write(formula[9]))
        self.wait()
        # self.add(formula2)

        self.play(
            
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[3].copy(), formula[8])
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[1].copy(),formula2[0:3]),
            ReplacementTransform(formula[4].copy(),formula2[4:7])
        )

        rec = SurroundingRectangle(formula2[1:6])
        self.add(rec)
        # tp = VGroup(rec, formula2[1:6])
        # tp.shift(DOWN*2)

        self.play(
            ReplacementTransform(formula2[1:6], formula2[3])
        )
        self.play(FadeOut(rec), run_time = 3)
        self.wait()

        tx2 = VGroup(formula2[0],formula2[3],formula2[6])
        # tx2.shift(2*LEFT)

        self.play(
            ReplacementTransform(tx2, formula[10]) , run_time = 2
        )
        # self.add(matr1)

        self.play(
            formula.animate.to_corner(UP+RIGHT),
            mat.animate.scale(0.5).arrange(RIGHT).to_corner(UP+LEFT)
        )

class matmul(Scene):
    def construct(self):

        m1 = np.array([[1,4,7],[2,5,8]])
        m2 = np.array([[1,4],[2,5],[3,6]])
        m3 = np.dot(m1,m2) 
        matr1,matr2,matr3 = matrix_to_mobject(m1),matrix_to_mobject(m2),matrix_to_mobject(m3)
        matr1.shift(2*RIGHT)
        matr2.shift(2*RIGHT)
        matr3.shift(2*RIGHT)
        grid = NumberPlane()
        self.add(grid)

        # matr2_col = matr2.get_columns()

        # equ = np.m1[0]
        m1_t = Tex("{A}_{2\\times 3} = \\")
        m1_t.shift(0.5*LEFT)

        mat_a = VGroup(m1_t,matr1)
        # mat_a.to_corner(LEFT+UP)

        m2_t = Tex("{B}_{3\\times 2} = \\")
        m2_t.shift(0.5*LEFT)
        mat_b = VGroup(m2_t,matr2)
        # mat_b.align_to(mat_a, )

        mat = VGroup(mat_a, mat_b)
        mat.arrange(DOWN)
        mat.to_corner(UP+LEFT)

        formula = Tex(
            "\\  {A}",               #0
            "_{2\\times 3} \\", #1
            "\\times",          #2
            "\\  {B}",          #3
            "_{3\\times 2} \\", #4
            "=",                #5
            "(",                #6
            "{A}",              #7
            "{B}",              #8
            ")",                #9
            "_{2\\times 2} \\"    
           )   #10

        formula.to_corner(UP+RIGHT)
        mat.scale(0.5).arrange(RIGHT).to_corner(UP+LEFT)

        self.add(formula, mat)

        # mat1,mat2,mat3 = matrix_to_mobject(m1),matrix_to_mobject(m2),matrix_to_mobject(m3)
        # mat = VGroup(mat1,mat2,mat3)
        # # mat1.shift(UP+LEFT*4)
        # mat.arrange(RIGHT).shift(UP+LEFT*3)
        # mat3.shift(4*RIGHT)
        # mat2.shift(1.5*RIGHT)
        mat1 = Matrix([["1","4","7"],["2","5","8"]])
        mat2 = Matrix([["1","4"],["2","5"],["3","6"]])
        mat3 = Matrix([["30","66"],["36","81"]])

        mat = VGroup(mat1,mat2,mat3)
        
        mat.arrange(RIGHT).shift(UP+LEFT*2)
        # mat1.shift(UP+LEFT*4)
        mat3.shift(4*RIGHT)
        mat2.shift(1.5*RIGHT)
        self.play(
            ReplacementTransform(matr1.copy(), mat1),
            ReplacementTransform(matr2.copy(), mat2), run_time = 2
        )
        tex = Tex(
            "\\times",
            "\\ =",
            "b"
            
        )
        self.add(mat3[1],mat3[2])

       
        self.add(tex[0],tex[1])
        tex[0].next_to(mat1, 3*RIGHT)
        tex[1].next_to(mat3,5*LEFT)
        # self.play(
        #     ShowCreation(mat3[0][0:10:9])
        # )



        mat2_col = mat2.get_columns()
        mat3_col = mat3.get_columns()

        rec_mat1 = [SurroundingRectangle(mat1[0][0:3]).set_color(RED),SurroundingRectangle(mat1[0][3:6]).set_color(RED)]
        # rec2_mat1 = SurroundingRectangle(mat1[0][3:6]).set_color(RED)
        rec_mat2 = [SurroundingRectangle(mat2_col[0]),SurroundingRectangle(mat2_col[1])]
        # rec2_mat2 = SurroundingRectangle(mat2_col[1])
        rec_mat2s = [SurroundingRectangle(mat2_col[0]),SurroundingRectangle(mat2_col[1])]

        rec_mat3 = [[SurroundingRectangle(mat3[0][0:2]).set_color(RED),SurroundingRectangle(mat3[0][2:4]).set_color(RED)],[SurroundingRectangle(mat3_col[0]),SurroundingRectangle(mat3_col[1])]]
        # rec12_mat3 = SurroundingRectangle(mat3[0][0:2]).set_color(RED)
        # rec2_mat3 = SurroundingRectangle(mat3_col[0])
        # rec22_mat3 = SurroundingRectangle(mat3_col[1])
        self.play(ShowCreation(rec_mat1[0]), ShowCreation(rec_mat2[0]))

        ##1x1

        formula = [[Tex(
            "\\ 1 ",    #0
            "\\ . ",    #1
            "\\ 1 ",    #2
            "\\ + ",    #3
            "\\ 4 ",    #4
            "\\ . ",    #5
            "\\ 2 ",    #6
            "\\ + ",    #7
            "\\ 7 ",    #8
            "\\ . ",    #9
            "\\ 3 ",    #10
            "\\ = ",    #11
            "\\ 30 "    #12
            
        ),Tex(
            "\\ 1 ",    #0
            "\\ . ",    #1
            "\\ 4 ",    #2
            "\\ + ",    #3
            "\\ 4 ",    #4
            "\\ . ",    #5
            "\\ 5 ",    #6
            "\\ + ",    #7
            "\\ 7 ",    #8
            "\\ . ",    #9
            "\\ 6 ",    #10
            "\\ = ",    #11
            "\\ 66 "    #12
            
        )],
        [Tex(
            "\\ 2 ",    #0
            "\\ . ",    #1
            "\\ 1 ",    #2
            "\\ + ",    #3
            "\\ 5 ",    #4
            "\\ . ",    #5
            "\\ 2 ",    #6
            "\\ + ",    #7
            "\\ 8 ",    #8
            "\\ . ",    #9
            "\\ 3 ",    #10
            "\\ = ",    #11
            "\\ 36 "    #12
            
        ),Tex(
            "\\ 2 ",    #0
            "\\ . ",    #1
            "\\ 4 ",    #2
            "\\ + ",    #3
            "\\ 5 ",    #4
            "\\ . ",    #5
            "\\ 5 ",    #6
            "\\ + ",    #7
            "\\ 8 ",    #8
            "\\ . ",    #9
            "\\ 6 ",    #10
            "\\ = ",    #11
            "\\ 81 "    #12
            
        )]]
# first row operation

        for i in range(2):
            mat1_row1 = VGroup(formula[0][i][0],formula[0][i][4],formula[0][i][8]).set_color(RED)
            operation = VGroup(formula[0][i][1],formula[0][i][3],formula[0][i][5],formula[0][i][7],formula[0][i][9],formula[0][i][11])
            mat2_col1 =VGroup(formula[0][i][2],formula[0][i][6],formula[0][i][10]).set_color(YELLOW)

            formula[0][i].shift(DOWN)
            self.play(
                ReplacementTransform(mat1[0][0:3].copy(), mat1_row1),run_time= 2
            )
            self.wait()
            self.add(operation)
            self.play(
                ReplacementTransform(mat2_col[i].copy(), mat2_col1),run_time= 2
            )
            self.add(formula[0][i][12])

            self.wait(2)

            self.play(
                ReplacementTransform(rec_mat1[0].copy(), rec_mat3[0][0]),
                ReplacementTransform(rec_mat2[i].copy(), rec_mat3[1][i])
                )

            self.play(
                ReplacementTransform(formula[0][i][12].copy(), mat3[0][i])
                )

            self.play(FadeOut(formula[0][i]), FadeOut(rec_mat3[0][0]),FadeOut(rec_mat3[1][i]))

            self.play(
                ReplacementTransform(rec_mat2[0], rec_mat2[1])
            )
            

        # 2nd row operation
        # self.play(FadeOut(rec_mat2[1]))

        self.play(ReplacementTransform(rec_mat1[0],rec_mat1[1]), ReplacementTransform(rec_mat2[1], rec_mat2s[0]))



        for i in range(2):
            mat1_row1 = VGroup(formula[1][i][0],formula[1][i][4],formula[1][i][8]).set_color(RED)
            operation = VGroup(formula[1][i][1],formula[1][i][3],formula[1][i][5],formula[1][i][7],formula[1][i][9],formula[1][i][11])
            mat2_col1 =VGroup(formula[1][i][2],formula[1][i][6],formula[1][i][10]).set_color(YELLOW)

            formula[1][i].shift(DOWN)
            self.play(
                ReplacementTransform(mat1[0][3:6].copy(), mat1_row1),run_time= 2
            )
            self.wait()
            self.add(operation)
            self.play(
                ReplacementTransform(mat2_col[i].copy(), mat2_col1),run_time= 2
            )
            self.add(formula[1][i][12])

            self.wait(2)

            self.play(
                ReplacementTransform(rec_mat1[1].copy(), rec_mat3[0][1]),
                ReplacementTransform(rec_mat2s[i].copy(), rec_mat3[1][i])
                )

            self.play(
                ReplacementTransform(formula[1][i][12].copy(), mat3[0][i+2])
                )

            self.play(FadeOut(formula[1][i]), FadeOut(rec_mat3[0][1]),FadeOut(rec_mat3[1][i]))

            self.play(
                ReplacementTransform(rec_mat2s[0], rec_mat2s[1])
            )
            

       


class firsts(Scene):
    def construct(self):

        m1 = [
            ["{A}_{1 1}","{A}_{1 2}", "{A}_{1 3}"],
            ["{A}_{2 1}","{A}_{2 2}", "{A}_{2 3}"],
            ["{A}_{3 1}","{A}_{3 2}", "{A}_{3 3}"]
        ]

        mat1 = Matrix(m1)
        self.add(mat1)
        self.wait(1)
        self.play(mat1.animate.shift(UP*2))
        self.wait()

        self.play(mat1[1].animate.shift(LEFT*3),
            mat1[2].animate.shift(RIGHT)
            )

        rec_row = [
            SurroundingRectangle(mat1[0][0:3]).set_color(RED),
            SurroundingRectangle(mat1[0][3:6]).set_color(RED),
            SurroundingRectangle(mat1[0][6:9]).set_color(RED)
        ]

        mat1_col = mat1.get_columns()

        self.play(ShowCreation(rec_row[0]))

        row_tx =["Row-1","Row-2","Row-3"]

        # first_row_bra= Brace(rec_row[0],LEFT)
        rows = [BraceText(
            rec_row[0], row_tx[0], LEFT
        ),BraceText(
            rec_row[1], row_tx[1], LEFT
        ),BraceText(
            rec_row[2], row_tx[2], LEFT
        )]
        self.add(rows[0])
        self.wait(2)
        self.remove(rows[0])

       
        # rowg = [VGroup(rl[0], rec_row[0]), VGroup(rl[1], rec_row[1]), VGroup(rl[2], rec_row[2])]

        self.play(
            ReplacementTransform(rec_row[0], rec_row[1])
        )
        self.wait(2)

        self.add(rows[1])
        self.wait(2)
        self.remove(rows[1])

        self.wait()

        self.play(
            ReplacementTransform(rec_row[1], rec_row[2])
        )
        self.wait(2)

        self.add(rows[2])
        self.wait(2)
        self.remove(rows[2])

        self.wait()

        self.remove(rec_row[2],rec_row[1],rec_row[0])


        #columns operation

        rec_col = [
            SurroundingRectangle(mat1_col[0]),
            SurroundingRectangle(mat1_col[1]),
            SurroundingRectangle(mat1_col[2])
        ]


        col_tx =["Col-1","Col-2","Col-3"]

        self.play(ShowCreation(rec_col[0]))

        # first_row_bra= Brace(rec_row[0],LEFT)
        rows = [BraceText(
            rec_col[0], col_tx[0], DOWN
        ),BraceText(
            rec_col[1], col_tx[1], DOWN
        ),BraceText(
            rec_col[2], col_tx[2], DOWN
        )]
        self.add(rows[0])
        self.wait(2)
        self.remove(rows[0])

       
        # rowg = [VGroup(rl[0], rec_row[0]), VGroup(rl[1], rec_row[1]), VGroup(rl[2], rec_row[2])]

        self.play(
            ReplacementTransform(rec_col[0], rec_col[1])
        )
        self.wait(2)

        self.add(rows[1])
        self.wait(2)
        self.remove(rows[1])

        self.wait()

        self.play(
            ReplacementTransform(rec_col[1], rec_col[2])
        )
        self.wait(2)

        self.add(rows[2])
        self.wait(2)
        self.remove(rows[2])

        self.wait()

        self.remove(rec_col[2])

        self.play(mat1[1].animate.shift(3*RIGHT))
        self.play(mat1[2].animate.shift(LEFT))


class scene3(Scene):
    def construct(self):

        m1 = [
            ["{A}_{1 1}","{A}_{1 2}", "{A}_{1 3}"],
            ["{A}_{2 1}","{A}_{2 2}", "{A}_{2 3}"],
            ["{A}_{3 1}","{A}_{3 2}", "{A}_{3 3}"]
        ]

        mat1 = Matrix(m1)
        
        
        mat1.shift(UP*2)
        self.wait()
        self.add(mat1)
        self.wait()
        self.play(mat1.animate.to_corner(UL))
        self.wait()

        tex = TexText("Another way to Observe")

        self.play(Write(tex), run_time = 4)
        self.play(tex.animate.to_corner(UR))

        formula = [
            Tex(
                "{A}",          #0
                "_{1",          #1
                "1}",           #2
                 "\ \ \ {A}",   #3
                "_{1",          #4
                "2}",           #5
                 "\ \ \ {A}",   #6
                "_{1",          #7
                "3}"            #8
            ),
            Tex(
                 "{A}",
                "_{1",
                "1}",
                 "\ \ \ {A}",
                "_{2",
                "1}",
                 "\ \ \ {A}",
                "_{3",
                "1}"
            )
        ]

        for i,j in zip(range(1,9,3),range(2,9,3)):
            formula[0][i].set_color(RED)
            formula[0][j].set_color(YELLOW)

        # self.add(formula[0])
        # self.wait(2)

        self.play(
            ReplacementTransform(mat1[0][0:3].copy(), formula[0])
        )
        self.wait(2)
