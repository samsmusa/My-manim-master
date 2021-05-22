from manimlib import *

# from manimlib.imports import *
import numpy as np



class quote(Scene):
    def construct(self):
  
        quote = TexText("``Beauty is the first test:\\\\ There is no permanent place in the world for ugly Mathematics.''"
            
            )

       

        
        quote[0][63:74].set_color(BLUE)
        

        quote[0][2:8].set_color(BLUE) 

        
        self.play(Write(quote))

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

        # self.play(
        #     TransformMatchingTex(quote, then)
        # )
        self.wait(3)
        self.play(FadeOut(then))
        self.wait(3)






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
        grid = NumberPlane( stroke_color = WHITE,  stroke_opacity = 0.5 )
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

            self.wait(3)

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

            self.wait(3)

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
        self.wait(3)
        self.remove(rows[0])

       
        # rowg = [VGroup(rl[0], rec_row[0]), VGroup(rl[1], rec_row[1]), VGroup(rl[2], rec_row[2])]

        self.play(
            ReplacementTransform(rec_row[0], rec_row[1])
        )
        self.wait(3)

        self.add(rows[1])
        self.wait(3)
        self.remove(rows[1])

        self.wait()

        self.play(
            ReplacementTransform(rec_row[1], rec_row[2])
        )
        self.wait(3)

        self.add(rows[2])
        self.wait(3)
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
        self.wait(3)
        self.remove(rows[0])

       
        # rowg = [VGroup(rl[0], rec_row[0]), VGroup(rl[1], rec_row[1]), VGroup(rl[2], rec_row[2])]

        self.play(
            ReplacementTransform(rec_col[0], rec_col[1])
        )
        self.wait(3)

        self.add(rows[1])
        self.wait(3)
        self.remove(rows[1])

        self.wait()

        self.play(
            ReplacementTransform(rec_col[1], rec_col[2])
        )
        self.wait(3)

        self.add(rows[2])
        self.wait(3)
        self.remove(rows[2])

        self.wait()

        self.remove(rec_col[2])

        self.play(mat1[1].animate.shift(3*RIGHT))
        self.play(mat1[2].animate.shift(LEFT))


class scene31(Scene):
    def construct(self):

        m1 = [
            ["{A}_{1 1}","{A}_{1 2}", "{A}_{1 3}","...","...","...","{A}_{1 n}"],
            ["{A}_{2 1}","{A}_{2 2}", "{A}_{2 3}","...","...","...","{A}_{2 n}"],
            ["{A}_{3 1}","{A}_{3 2}", "{A}_{3 3}","...","...","...","{A}_{3 n}"],
            ["...","...", "...","{A}_{4 4}","...","...","..."],
            ["...","...", "...","...","...","...","..."],
            ["...","...", "...","...","...","...","..."],
            ["{A}_{m 1}","{A}_{m 2}", "{A}_{m 3}","...","...","...","{A}_{m n}"]

        ]

        rt = TexText("Row=")
        ct = TexText("Column=")
        counter = VGroup(rt, ct).arrange(DOWN)
        count = 1
        c1 = Tex(str(count))
        c2 = Tex(str(count))
        
        

        

        mat1 = Matrix(m1)
        mat1_c = mat1.get_columns()
        
        
        
        VGroup(mat1,counter).arrange(RIGHT)

        c1.next_to(rt, RIGHT)
        c2.next_to(ct, RIGHT)

        

        rec_row = [SurroundingRectangle(mat1[0][i:i+7]).set_color(RED) for i in range(0,50,7)]
        rec_co = [SurroundingRectangle(mat1_c[i]).set_color(YELLOW) for i in range(7)]
        self.wait()
        self.add(mat1,counter, c1,c2)
        self.wait()
        self.play(
            ShowCreation(rec_row[0]))
        for i in range(6):
            count = count + 1
            self.play(
                ReplacementTransform(rec_row[i],rec_row[i+1]),
                ReplacementTransform(c1, Tex(str(count))),
            )
        
        
        # mat1.shift(UP*2)
        
        # self.play(mat1.animate.to_corner(UL))
        self.wait()
        self.play(FadeOut(rec_row[6]))
        self.wait()

        self.play(
            ShowCreation(rec_co[0]))
        for i in range(6):
            self.play(
                ReplacementTransform(rec_co[i],rec_co[i+1])
            )
        
        
        # mat1.shift(UP*2)
        
        # self.play(mat1.animate.to_corner(UL))
        self.wait()

        tex = TexText("Another way to Observe")

        # self.play(Write(tex), run_time = 4)
        # self.play(tex.animate.to_corner(UR))

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
        # self.wait(3)

        # self.play(
        #     ReplacementTransform(mat1[0][0:3].copy(), formula[0])
        # )
        # self.wait(3)



class svgi(Scene):
    CONFIG = {
       
        "stroke_width": 1,
        "fill_opacity": 0
        
    }
    def construct(self):

        

    

        

        

        building = Rectangle(width = 2, height=4, color = GREEN, fill_opacity = 1)

       

        window = [Rectangle(width = 0.3, height=0.3, color = YELLOW_A, fill_opacity = 1) for i in range(10)]

        bui = VGroup(building, *window).to_corner(LEFT*3)
        # k = ImageMobject("wr2").shift(LEFT*3)

        self.play(DrawBorderThenFill(building))
        self.wait()

        window[0].shift(UP*1.5+LEFT*0.5)
        window[1].next_to(window[0],3* RIGHT)
        self.play(ShowCreation(window[0]),ShowCreation(window[1]))

        self.wait(3)
        for i,j in zip(range(2,10,2), range(3,10,2)):
            self.play(
                window[i].animate.next_to(window[i-2],2*DOWN)
            )
            self.wait()
            self.play(
                window[j].animate.next_to(window[j-2],2*DOWN)
            )

        word = TexText("Suppose you are a owner of a hotel.\\\\ which have 5 floor and evry floor has\\\\ 2 recidense").shift(RIGHT)
        word2 = TexText("how to descrive your Hotel data \\\\ in a paper sheet")
        self.play(ShowCreationThenFadeOut(word), run_time = 7)
        self.wait()
        self.play(ShowCreationThenFadeOut(word2), run_time = 10)



        


class text1(Scene):
    
    CONFIG = {
        
        "height": None,
        "width": None,
        # Defaults to a faded version of line_config
        "faded_line_style": None,
        "faded_line_ratio": 1,
        "make_smooth_after_applying_functions": True,
    }
    def construct(self):
        plane = NumberPlane()
        self.play(ShowCreation(plane, lag_ratio = 0.9))

class scene12(Scene):
    def construct(self):
        # grid = NumberPlane()
        # self.add(grid)

        # self.intro()
        com = self.intro()
        com_c = com[0].get_columns()
        data2 = Matrix([
            "", 
            "\\ \\ \\ \\ \\ \\ 250ml","\\ ",
            "\\ \\ \\ \\ \\ \\ 500ml","\\ ",
            "\\ \\ \\ \\ \\ \\ 1000ml"
        ])
        data21 = Matrix([
            "", 
            "\\ \\ \\ \\ \\ \\ 250ml","\\ ",
            "\\ \\ \\ \\ \\ \\ 500ml","\\ ",
            "\\ \\ \\ \\ \\ \\ 1000ml"
        ]).shift(2*UP+ 3*RIGHT).set_color(BLUE_B)
        # dat = matrix_to_mobject([data2])
       
       
        com_mat = Matrix([["Mojo"],["Fanta"],["FizzUP"]])
        com_mat1 = Matrix([["Mojo"],["Fanta"],["FizzUP"]]).shift(2*UP + 3*RIGHT).set_color(BLUE)  
        
        q1_mat =  Matrix([["\\  15","\\  28","\\  50"],["\\  18","\\  30","\\  55"],["\\ 16","\\ 32","\\ 60"]])
        q1_mat1 =  Matrix([["\\  15","\\  28","\\  50"],["\\  18","\\  30","\\  55"],["\\ 16","\\ 32","\\ 60"]]).shift(2*UP+ 3*RIGHT).set_color(GREEN)
        q_mat =  q1_mat1.get_columns()

        com_tex = Tex(
            "{C}", #0
            "_{3",#1
            " \\times ",#2
            "1 } ",#3
            "=")#4

        val_tex  = Tex(
            "{V}", #7
            "_{3",#8
            "\\times",#9
            "3}",#10
            "="#11
        )

        s_tex = Tex(
            "{S}", #14
            "_{1",#15
            "\\times",#16
            "3}",#17
            "="#18
            )

        
        

        array = VGroup(
            # Tex("{C}_{3 \\times 1}", "="),com_mat,Tex(","),Tex("{V}_{3 \\times 3","="),q1_mat,Tex(","),Tex("{S}_{1 \\times 3}","="),data2
            com_tex,#0
            com_mat,#1
            Tex(","),#2
            val_tex,#3
            q1_mat,#4
            Tex(","),#5
            s_tex,#6
            data2#7
           )

        
        self.wait()
        array.arrange(RIGHT).scale(0.6).shift(DOWN*1.5)
        array[0:2].set_color(BLUE)
        array[3:5].set_color(GREEN)
        array[6:8].set_color(BLUE_B)

        VGroup(com_tex[1],val_tex[1],s_tex[1]).set_color(RED)
        VGroup(com_tex[3],val_tex[3],s_tex[3]).set_color(YELLOW)



        rec_mat1_r = [SurroundingRectangle(com_mat1[0][0]),SurroundingRectangle(com_mat1[0][1]),SurroundingRectangle(com_mat1[0][2])]
        rec_mat1_c = SurroundingRectangle(com_mat1.get_columns())

        rec_mat2_r = [SurroundingRectangle(q1_mat1[0][0:3]),SurroundingRectangle(q1_mat1[0][3:6]),SurroundingRectangle(q1_mat1[0][6:9])]
        rec_mat2_c = [SurroundingRectangle(q_mat[0]),SurroundingRectangle(q_mat[1]),SurroundingRectangle(q_mat[2])]

        # dat = data21.get_columns()

        rec_mat3_c = [SurroundingRectangle(data21[0][1]),SurroundingRectangle(data21[0][3]),SurroundingRectangle(data21[0][5])]
        rec_mat3_r = SurroundingRectangle(data21[0])
        
        VGroup(*rec_mat1_r, *rec_mat2_r, rec_mat3_r ).set_color(RED)
#1
        self.play(
            ReplacementTransform(com_c[0].copy(), com_mat1)
            )

        self.wait(3)
        com_t = com_tex.copy().next_to(com_mat1,LEFT)
        self.play(Write(com_t[0]),Write(com_t[4]))
        self.play(
            
            *list(map(ShowCreation, rec_mat1_r))
        )
        self.wait(3)
        text_r = Tex("Row","=").next_to(com_mat1,2*DOWN)
        text_r_n = Tex("3").next_to(text_r).set_color(RED)
        self.play(Write(text_r),
            Write(text_r_n))
        self.wait()

        self.play(
           *list(map(FadeOut, rec_mat1_r)),
            ReplacementTransform(text_r_n,com_t[1]),
            Write(com_t[2]), run_time = 2
        )
        self.wait(3)
        self.play(
            
            ShowCreation(rec_mat1_c)
        )
        self.wait(3)
        text_c = Tex("Column","=").next_to(text_r,DOWN)
        text_c_n = Tex("1").next_to(text_c).set_color(YELLOW)
        self.play(Write(text_c),
            Write(text_c_n))
        self.wait(3)

        self.play(
            FadeOut(rec_mat1_c),
            ReplacementTransform(text_c_n,com_t[3])
        )
        self.wait(3)

        self.play(
            ReplacementTransform(com_mat1,array[1]),
            ReplacementTransform(com_t,array[0]), run_time = 2
        )
        self.wait(3)
        ######

        
 #1       

 #1
        self.play(
            ReplacementTransform(com_c[1].copy(), q_mat[0]),
            ReplacementTransform(com_c[2].copy(), q_mat[1]),
            ReplacementTransform(com_c[3].copy(), q_mat[2]), run_time = 3
            )

        self.play(
            Write(q1_mat1[1]),
            Write(q1_mat1[2])
        )

        self.wait(3)

        v_t = val_tex.copy().next_to(q1_mat1,LEFT)
        self.play(Write(v_t[0]),Write(v_t[4]))
        self.play(
            
            *list(map(ShowCreation, rec_mat2_r))
        )
        self.wait(3)
        text_r_n = Tex("3").next_to(text_r).set_color(RED)
        self.play(Write(text_r_n))
        self.wait(3)
        self.play(
           *list(map(FadeOut, rec_mat2_r)),
            ReplacementTransform(text_r_n,v_t[1]),
            Write(v_t[2])
        )
        self.wait(3)
        self.play(
            
            *list(map(ShowCreation, rec_mat2_c))
        )
        self.wait()
        text_c_n = Tex("3").next_to(text_c).set_color(YELLOW)
        self.play(Write(text_c_n))
        self.wait(3)

        self.play(
            *list(map(FadeOut, rec_mat2_c)),
            ReplacementTransform(text_c_n,v_t[3])
        )
        self.wait()
        self.play(
            Write(array[2]),
            ReplacementTransform(q1_mat1,array[4]),
            ReplacementTransform(v_t,array[3])
        )
        self.wait(3)




       
 #1       
 #1
        self.play(
            ReplacementTransform(com[1].copy(), data21[0])
            
            )

        self.play(
            Write(data21[1]),
            Write(data21[2])
        )

        self.wait(3)

        s_t = s_tex.copy().next_to(data21,LEFT)
        self.play(Write(s_t[0]),Write(s_t[4]))
        self.play(
            
            ShowCreation(rec_mat3_r)
        )
        self.wait(3)
        text_r_n = Tex("1").next_to(text_r).set_color(RED)
        self.play(Write(text_r_n))
        self.wait(3)
        self.play(
            FadeOut(rec_mat3_r),
            ReplacementTransform(text_r_n,s_t[1]),
            Write(s_t[2])
        )
        self.wait(3)
        self.play(
            
            *list(map(ShowCreation, rec_mat3_c))
        )
        self.wait()
        text_c_n = Tex("3").next_to(text_c).set_color(YELLOW)
        self.play(Write(text_c_n))
        self.wait(3)

        self.play(
            *list(map(FadeOut, rec_mat3_c)),
            ReplacementTransform(text_c_n,s_t[3])
        )
        self.wait(3)
        self.play(
            Write(array[5]),
            ReplacementTransform(data21,array[7]),
            ReplacementTransform(s_t,array[6])
        )
        self.wait(3)




#         da_t = array[6].copy().next_to(data21,LEFT)
#         self.play(Write(da_t))
#         self.wait()

#         self.play(
#             Write(array[5]),
#             ReplacementTransform(da_t,array[6]),
#             ReplacementTransform(data21,array[7])
            
#             )

#         self.wait()
#  #1       

        # self.play(
        #     ReplacementTransform(com_c[0].copy(), com_mat)
        #     )


        # self.play(
            
        #     ReplacementTransform(com_c[1].copy(), q_mat[0]),
        #     ReplacementTransform(com_c[2].copy(), q_mat[1]),
        #     ReplacementTransform(com_c[3].copy(), q_mat[2]), lag_ratio = 0.9
        # )

        # self.play(Write(array[0]),Write(array[2]),Write(array[3]),Write(array[5]),Write(array[6]),Write(q1_mat[1]),Write(q1_mat[2]), lag_ratio =0.6, run_time =6)

        
    def intro(self):
        word1 = TexText("What is Matrix?")

        self.play(ShowCreation(word1), run_time = 2)
        self.wait()
        self.play(FadeOut(word1))

        data = [["Mojo","\\  15","\\  28","\\  50"],["Fanta","\\  18","\\  30","\\  55"],["FizzUp","\\ 16","\\ 32","\\ 60"]]



        matrix1 = Matrix(data)
        # matrix2 = Matrix(data)
        # matrix1[0][0:4].scale(0.7)
        # data1 = Tex(
        #     "Mojo",
        #     "fanta",
        #     "fr"
        # )
        data2 = Tex(
            "", 
            "\\ \\ \\ \\ \\ \\ 250ml",
            "\\ \\ \\ \\ \\ \\ 500ml",
            "\\ \\ \\ \\ \\ \\ 1000ml"
        ).scale(0.6)
        data2.shift(UP*1.5 + RIGHT*1.2)

        # data3 = Tex(
        #     "", 
        #     "\\ \\ \\ \\ \\ \\ 250ml",
        #     "\\ \\ \\ \\ \\ \\ 500ml",
        #     "\\ \\ \\ \\ \\ \\ 1000ml"
        # ).scale(0.6)
        # data3.shift(UP*1.5 + RIGHT*1.2)
        # data1.arrange(DOWN)

        # data2.next_to(data1, RIGHT)
        # self.add(matrix1[0], data2)

        line_h = [Line(3.5*LEFT, 3.5*RIGHT).set_color(RED) for i in range(4)]
        line_v = [Line(2*UP, 2*DOWN).set_color(YELLOW) for i in range(4)]

        line_h[0].shift(UP*1.2)
        line_h[1].shift(UP*0.4)
        line_h[2].shift(DOWN*0.4)
        line_h[3].shift(DOWN*1.2)
        line_v[0].shift(LEFT*0.8)
        line_v[1].shift(RIGHT*0.5)
        line_v[2].shift(RIGHT*1.8)
        line_v[3].shift(RIGHT*3.2)

        matrixc1 = matrix1.get_columns()


        self.play(*list(map(GrowFromCenter, line_h)),*list(map(GrowFromCenter, line_v)), lag_ratio = 0.2, run_time = 3)
        # self.embed()
        data_f = VGroup(*line_h,*line_v, matrix1[0],data2)

        # for i in range(len(line_h)):
        #     self.play(ShowCreation(line_h[i]))
        # for j in range(len(line_v)):
        #     self.play(ShowCreation(line_v[j]))

        self.wait()
        self.play(Write(matrixc1[0]))
        self.wait()

        self.play(Write(data2), run_time = 3)
        self.wait()
        self.play(Write(matrix1[0][1:4])
            )
        self.play(Write(matrix1[0][5:8])
            )
        self.play(Write(matrix1[0][9:12]))
        self.wait()
        self.play(data_f.animate.scale(0.6).to_corner(UL))
        # self.add(matrix2)
        

        
        return [matrix1, data2]



class scene3(Scene):
    def construct(self):
        # self.add(word2)
        data1 = [["15","13","10"],["21","34","55"],["39","56","31"]]
        data2 = [["45","12","7"],["36","43","22"],["21","43","26"]]

        matrix1 = Matrix(data1)
        matrix2 = Matrix(data2)

        self.addition1(matrix1,matrix2)
        self.subtarction1(matrix1, matrix2)
        # self.Subtraction(matrix1,matrix2)

    def addition(self, matrix1, matrix2):
        # VGroup(matrix1, matrix2).arrange(RIGHT)
        matrix1.to_corner(UL).set_color(GREEN)
        matrix2.to_corner(UR).set_color(BLUE)
        data1 = [Tex("15", "+", "45","\\ \\ \\ 13", "+", "12","\\ \\ \\ \\ 10","+"," 7"),
                     #0     1    2          3        4     5          6         7    8
                 Tex("21", "+", "36","\\ \\ \\ 34", "+", "43","\\ \\ \\ 55","+","22"),
                 Tex("39", "+", "21","\\ \\ \\ 56", "+", "43","\\ \\ \\ 31", "+","26")]

        for j in range(3):
            
            for i in range(0,9,3):
                data1[j][i].set_color(GREEN)
                data1[j][i+1].set_color(TEAL)
                data1[j][i+2].set_color(BLUE)

        # matrix_esum = Matrix(data1)
        brac1 = matrix1[1].copy().set_color(TEAL)
        brac2 = matrix1[2].copy().set_color(TEAL)

        VGroup(*data1).arrange(DOWN)
        data2 = [["60","25","17"],["57","77","77"],["60","99","57"]]
        matrix_sum = Matrix(data2).set_color(TEAL)

        brac1.next_to(data1[1],LEFT)
        brac2.next_to(data1[1],RIGHT)


        # grid = NumberPlane()
        # self.add(grid)


        

        

        main = VGroup(matrix1,Tex("+"),matrix2)
        main[1].scale(2).set_color(TEAL).shift(UP*2.4)
        self.add(main)
        self.wait(2)

        
        matrix3 = VGroup(*data1, brac1,brac2)
        show_sum = VGroup(matrix3,Tex("="),matrix_sum).arrange(RIGHT).shift(DOWN)

        self.play(ShowCreation(brac1), ShowCreation(brac2))
        self.wait()
        

        for j in range(3):


            for i,k in zip(range(9),range(0,9,3)):

                if j == 0:
                    t = 2
                else:
                    t = 0.5
                
                self.play(
                    ReplacementTransform(matrix1[0][i].copy(), data1[j][k]),
                    Write(data1[j][k+1]),
                    ReplacementTransform(matrix2[0][i].copy(), data1[j][k+2]), run_time= t
                )
                # self.wait()

            
        # self.play(ShowCreation(brac1), ShowCreation(brac2))

        self.play(
            matrix3.animate.to_corner(LEFT)
        )
        self.play(Write(show_sum[1]))
        for j in range(3):

            for k,i in zip([0,3,6],range(3)):
                self.play(
                    ReplacementTransform(data1[j][k:k+3], matrix_sum[0][3*j+i])
                )

        self.play(
            ReplacementTransform(brac1, matrix_sum[1]),
            ReplacementTransform(brac2, matrix_sum[2])
        )

        self.play(
            FadeOut(main[1]),
            FadeOut(show_sum[1:3])
        )
        # self.add(matrix3)

        # self.play(
        #     TransformMatchingTex(matrix1[0][0], matrix_esum[0][0]),
        #     TransformMatchingTex(matrix2[0][0], matrix_esum[0][0])
        # )

                        # number line
       
    def Subtraction(self, matrix1, matrix2):
        # VGroup(matrix1, matrix2).arrange(RIGHT)
        # matrix1.to_corner(UL).set_color(GREEN)
        # matrix2.to_corner(UR).set_color(BLUE)
        data1 = [Tex("15", "-", "45","\\ \\ \\ 13", "-", "12","\\ \\ \\ \\ 10","-"," 7"),
                     #0     1    2          3        4     5          6         7    8
                 Tex("21", "-", "36","\\ \\ \\ 34", "-", "43","\\ \\ \\ 55","-","22"),
                 Tex("39", "-", "21","\\ \\ \\ 56", "-", "43","\\ \\ \\ 31", "-","26")]

        for j in range(3):
            
            for i in range(0,9,3):
                data1[j][i].set_color(GREEN)
                data1[j][i+1].set_color(TEAL)
                data1[j][i+2].set_color(BLUE)

        # matrix_esum = Matrix(data1)
        brac1 = matrix1[1].copy().set_color(TEAL)
        brac2 = matrix1[2].copy().set_color(TEAL)

        VGroup(*data1).arrange(DOWN)
        data2 = [["-30","1","3"],["-15","-9","33"],["18","13","5"]]
        matrix_sum = Matrix(data2).set_color(TEAL)

        brac1.next_to(data1[1],LEFT)
        brac2.next_to(data1[1],RIGHT)


        # grid = NumberPlane()
        # self.add(grid)


        

        

        main = VGroup(matrix1,Tex("-"),matrix2)
        main[1].scale(2).set_color(TEAL).shift(UP*2.4)
        self.add(main)
        self.wait(2)

        
        matrix3 = VGroup(*data1, brac1,brac2)
        show_sum = VGroup(matrix3,Tex("="),matrix_sum).arrange(RIGHT).shift(DOWN)

        self.play(ShowCreation(brac1), ShowCreation(brac2))
        self.wait()
        

        for j in range(3):


            for i,k in zip(range(9),range(0,9,3)):

                if j == 0:
                    t = 2
                else:
                    t = 0.5
                
                self.play(
                    ReplacementTransform(matrix1[0][i].copy(), data1[j][k]),
                    Write(data1[j][k+1]),
                    ReplacementTransform(matrix2[0][i].copy(), data1[j][k+2]), run_time= t
                )
                # self.wait()

            
        # self.play(ShowCreation(brac1), ShowCreation(brac2))

        self.play(
            matrix3.animate.to_corner(LEFT)
        )
        self.play(Write(show_sum[1]))
        for j in range(3):

            for k,i in zip([0,3,6],range(3)):
                self.play(
                    ReplacementTransform(data1[j][k:k+3], matrix_sum[0][3*j+i])
                )

        self.play(
            ReplacementTransform(brac1, matrix_sum[1]),
            ReplacementTransform(brac2, matrix_sum[2])
        )
        # self.add(matrix3)

        # self.play(
        #     TransformMatchingTex(matrix1[0][0], matrix_esum[0][0]),
        #     TransformMatchingTex(matrix2[0][0], matrix_esum[0][0])
        # )

                        # number line
    def addition1(self, matrix1, matrix2):
        # VGroup(matrix1, matrix2).arrange(RIGHT)
        matrix1.to_corner(UL).set_color(GREEN)
        matrix2.to_corner(UR).set_color(BLUE)
        data1 = [Tex("15", "+", "45","\\ \\ \\ 13", "+", "12","\\ \\ \\ \\ 10","+"," 7"),
                     #0     1    2          3        4     5          6         7    8
                 Tex("21", "+", "36","\\ \\ \\ 34", "+", "43","\\ \\ \\ 55","+","22"),
                 Tex("39", "+", "21","\\ \\ \\ 56", "+", "43","\\ \\ \\ 31", "+","26")]



        for j in range(3):
            
            for i in range(0,9,3):
                data1[j][i].set_color(GREEN)
                data1[j][i+1].set_color(TEAL)
                data1[j][i+2].set_color(BLUE)

        # matrix_esum = Matrix(data1)
        brac1 = matrix1[1].copy().set_color(TEAL)
        brac2 = matrix1[2].copy().set_color(TEAL)

        VGroup(*data1).arrange(DOWN)
        data2 = [["60","25","17"],["57","77","77"],["60","99","57"]]
        matrix_sum = Matrix(data2).set_color(TEAL)

        brac1.next_to(data1[1],LEFT)
        brac2.next_to(data1[1],RIGHT)


        grid = NumberPlane(
             axis_config = {
            "stroke_color": ORANGE,
            "stroke_opacity": 0.2
             },
             background_line_style = {
            "stroke_color": YELLOW,
            "stroke_opacity": 0.2}
        )
        # self.add(grid)


        

        

        main = VGroup(matrix1,Tex("+"),matrix2)
        main[1].scale(2).set_color(TEAL).shift(UP*2.4)
        self.add(main)
        self.wait(2)

        
        matrix3 = VGroup(*data1, brac1,brac2).shift(DOWN)
        # show_sum = VGroup(matrix3,Tex("="),matrix_sum).arrange(RIGHT).shift(DOWN)

        self.play(ShowCreation(brac1), ShowCreation(brac2))
        self.wait()
        

        for j in range(3):


            for i,k in zip(range(9),range(0,9,3)):

                if j == 0:
                    t = 2
                else:
                    t = 0.5
                
                self.play(
                    ReplacementTransform(matrix1[0][i].copy(), data1[j][k]),
                    Write(data1[j][k+1]),
                    ReplacementTransform(matrix2[0][i].copy(), data1[j][k+2]), run_time= t
                )

        

        


        
        self.wait(3)

            
        # self.play(ShowCreation(brac1), ShowCreation(brac2))

        # self.play(
        #     matrix3.animate.to_corner(LEFT)
        # )
        # self.play(Write(show_sum[1]))
        # for j in range(3):

        #     for k,i in zip([0,3,6],range(3)):
                
        #         matrix_sum[0][3*j+i].shift(data1[j][k+1].get_coord([0,1,2]))
        for j in range(3):

            for k,i in zip([0,3,6],range(3)):
                
                if j==0 and k==6:
                    coor = [2.05,-0.4,0]
                else:
                    coor = data1[j][k+1].get_coord([0,1,2])
                
                matrix_sum[0][3*j+i].move_to(coor)
                self.play(
                    ReplacementTransform(data1[j][k:k+3], matrix_sum[0][3*j+i])
                )        
        
        self.wait()
       


        # self.play(
        #     ReplacementTransform(brac1, matrix_sum[1]),
        #     ReplacementTransform(brac2, matrix_sum[2])
        # )

        self.play(
            FadeOut(main[1]),
            FadeOut(matrix_sum[0])
        )

    def subtarction1(self, matrix1, matrix2):
        # VGroup(matrix1, matrix2).arrange(RIGHT)
        matrix1.to_corner(UL).set_color(GREEN)
        matrix2.to_corner(UR).set_color(BLUE)
        data1 = [Tex("15", "-", "45","\\ \\ \\ 13", "-", "12","\\ \\ \\ \\ 10","-"," 7"),
                     #0     1    2          3        4     5          6         7    8
                 Tex("21", "-", "36","\\ \\ \\ 34", "-", "43","\\ \\ \\ 55","-","22"),
                 Tex("39", "-", "21","\\ \\ \\ 56", "-", "43","\\ \\ \\ 31", "-","26")]



        for j in range(3):
            
            for i in range(0,9,3):
                data1[j][i].set_color(GREEN)
                data1[j][i+1].set_color(TEAL)
                data1[j][i+2].set_color(BLUE)

        # matrix_esum = Matrix(data1)
        brac1 = matrix1[1].copy().set_color(TEAL)
        brac2 = matrix1[2].copy().set_color(TEAL)

        VGroup(*data1).arrange(DOWN)
        data2 = [["-30","1","3"],["-15","-9","33"],["18","13","5"]]
        matrix_sum = Matrix(data2).set_color(TEAL)

        brac1.next_to(data1[1],LEFT)
        brac2.next_to(data1[1],RIGHT)


        grid = NumberPlane(
             axis_config = {
            "stroke_color": ORANGE,
            "stroke_opacity": 0.2
             },
             background_line_style = {
            "stroke_color": YELLOW,
            "stroke_opacity": 0.2}
        )
        self.add(grid)


        

        

        main = VGroup(matrix1,Tex("-"),matrix2)
        main[1].scale(2).set_color(TEAL).shift(UP*2.4)
        self.add(main)
        self.wait(2)

        
        matrix3 = VGroup(*data1, brac1,brac2).shift(DOWN)
        # show_sum = VGroup(matrix3,Tex("="),matrix_sum).arrange(RIGHT).shift(DOWN)

        self.play(ShowCreation(brac1), ShowCreation(brac2))
        self.wait()
        

        for j in range(3):


            for i,k in zip(range(9),range(0,9,3)):

                if j == 0:
                    t = 2
                else:
                    t = 0.5
                
                self.play(
                    ReplacementTransform(matrix1[0][i].copy(), data1[j][k]),
                    Write(data1[j][k+1]),
                    ReplacementTransform(matrix2[0][i].copy(), data1[j][k+2]), run_time= t
                )

        

        


        
        self.wait(3)

            
        # self.play(ShowCreation(brac1), ShowCreation(brac2))

        # self.play(
        #     matrix3.animate.to_corner(LEFT)
        # )
        # self.play(Write(show_sum[1]))
        # for j in range(3):

        #     for k,i in zip([0,3,6],range(3)):
                
        #         matrix_sum[0][3*j+i].shift(data1[j][k+1].get_coord([0,1,2]))
        for j in range(3):

            for k,i in zip([0,3,6],range(3)):
                
                if j==0 and k==6:
                    coor = [2.05,-0.4,0]
                else:
                    coor = data1[j][k+1].get_coord([0,1,2])
                
                matrix_sum[0][3*j+i].move_to(coor)
                self.play(
                    Transform(data1[j][k:k+3], matrix_sum[0][3*j+i])
                )        
        
        self.wait()
       


        # self.play(
        #     ReplacementTransform(brac1, matrix_sum[1]),
        #     ReplacementTransform(brac2, matrix_sum[2])
        # )

        self.play(
            FadeOut(main[1])
            # FadeOut(show_sum[1:3])
        )
        
         

class differentmat(Scene):
    def construct(self):

        word = TexText("Different kinds of Matrix")
        
        word_c = TexText("Column Matrix")
        word_r = TexText("Row Matrix")
        word_s = TexText("Square Matrix")
        word_sc = TexText("Scaler Matrix")
        word_n = TexText("Null Matrix")
        word_i = TexText("Identity Matrix")
        word_d = TexText("Diagonal Matrix")
        word_t = TexText("Tranpose Matrix")
        word_sy = TexText("Symetric Matrix")
        VGroup(word_c,word_r,word_s,word_n,word_i,word_d,word_t,word_sy).shift(UP*2.5 + RIGHT*4)

        grid = NumberPlane()
        # self.add(grid)

        self.wait(2)
        self.play(Write(word))
        self.play(
            word.animate.to_corner(UL)
        )
        self.wait()


        m1 = [
            ["{A}_{1 1}","{A}_{1 2}", "{A}_{1 3}"],
            ["{A}_{2 1}","{A}_{2 2}", "{A}_{2 3}"],
            ["{A}_{3 1}","{A}_{3 2}", "{A}_{3 3}"]
        ]

        mat1 = Matrix(m1).set_color(PURPLE_C)
        mat1_col = mat1.get_columns()
        self.play(Write(mat1))
        self.wait(1)
        self.play(
            mat1.animate.shift(LEFT*4)
        )



        ## Row matrix

        
        self.play(
            Write(word_r)
        )
        self.wait()

        sq_r = BackgroundRectangle(mat1[0][3:9])

        self.play(FadeIn(sq_r))
        row_mat = Matrix(m1[0]).set_color(RED).shift(RIGHT*4)

        self.play(
            ReplacementTransform(mat1[0][0:3].copy(),row_mat[0][0:3]),
            # wait(),
            Write(row_mat[1]),
            Write(row_mat[2])
        )
        t = VGroup(row_mat,sq_r)
        self.play(
            FadeOut(t), run_time = 2
        )
        

        ##column matrix

        self.play(
            ReplacementTransform(word_r, word_c)
        )

        sq_c1, sq_c2 = BackgroundRectangle(mat1_col[1]),BackgroundRectangle(mat1_col[2])

        self.play(FadeIn(sq_c1),
            FadeIn(sq_c2))

        col_mat = mat1_col[0].copy()
        col_mat.shift(RIGHT*9)
        brac1 = mat1[1].copy()
        brac2 = mat1[2].copy()
        brac1.next_to(col_mat,LEFT)
        brac2.next_to(col_mat,RIGHT)
        c = VGroup(col_mat,brac1,brac2).set_color(YELLOW)

        
        self.play(
            ReplacementTransform(mat1_col[0].copy(),col_mat),
            Write(brac1),
            Write(brac2)
        )
        self.wait(2)
        self.play(FadeOut(c))
        # print(col_mat)

        

        ##square matrix
        word_s.move_to(ORIGIN)
        word_s.to_corner(UP, buff = 1.5)

        self.remove(mat1)
        self.play(
            ReplacementTransform(word_c, word_s)
        )

        te = Tex("1 \\times 1","2 \\times 2","3 \\times 3").set_color(BLUE)

        m2 = [
            ["{A}_{1 1}","{A}_{1 2}"],
            ["{A}_{2 1}","{A}_{2 2}"]
        ]

        mat3 = Matrix(m1).set_color(BLUE)
        mat3_col = mat3.get_columns()
    
        mat2 = Matrix(m2).set_color(BLUE)
        brac11 = mat3[1].copy().set_height(mat3[0][0].get_height()).scale(1.8)
        brac11.next_to(mat3[0][0],LEFT)
        brac12 = mat3[2].copy().set_height(mat3[0][0].get_height()).scale(1.8)
        brac12.next_to(mat3[0][0],RIGHT)
        te[0].scale(0.4).next_to(brac12, RIGHT*0.5)
        te[0].shift(DOWN*0.288)

        mat2[1].next_to(mat3_col[0][0:2],LEFT)
        mat2[2].next_to(mat3_col[1][0:2],RIGHT)
        te[1].scale(0.6).next_to(mat2[2], RIGHT*0.5)
        te[1].shift(DOWN*0.6)

        te[2].scale(0.8).next_to(mat3[2], RIGHT*0.5)
        te[2].shift(DOWN*0.9)
        
        self.add(
            mat3_col[0][0],brac11,brac12,te[0]
        )
        self.wait()



        self.play(
            ReplacementTransform(brac11, mat2[1]),
            ReplacementTransform(te[0],te[1]),
            ReplacementTransform(brac12, mat2[2]),
            Write(mat3[0][1]),
            Write(mat3[0][3]),
            Write(mat3[0][4]), run_time = 2
        )

        self.wait()

        self.play(
            ReplacementTransform(mat2[1], mat3[1]),
            ReplacementTransform(te[1],te[2]),
            ReplacementTransform(mat2[2], mat3[2]),
            Write(mat3[0][2]),
            Write(mat3[0][5]),
            Write(mat3[0][6]),
            Write(mat3[0][7]),
            Write(mat3[0][8]), run_time = 2
        )
        

        ###################### diagonal matrix

        word_d.move_to(ORIGIN)
        word_d.to_corner(UP, buff = 1.5)
        
        self.play(
            ReplacementTransform(word_s, word_d)
        )


        m3 = [
            ["{A}_{1 1}","0", "0"],
            ["0","{A}_{2 2}", "0"],
            ["0","0", "{A}_{3 3}"]
        ]

        mat4 = Matrix(m3).set_color(DARK_BROWN)

        for i in range(9):
            mat4[0][i].move_to(mat3[0][i])

        # self.remove(mat3[0])
        self.wait()
        self.play(
            ReplacementTransform(mat3[1],mat4[1])
        )
        for i in range(9):
            self.play(
            ReplacementTransform(mat3[0][i], mat4[0][i])
         )
        
        self.play(
            ReplacementTransform(mat3[2],mat4[2])
        )
        
        
        ################ scaler matrix

        self.wait()

        word_sc.move_to(ORIGIN)
        word_sc.to_corner(UP, buff = 1.5)
        
        self.play(
            ReplacementTransform(word_d, word_sc)
        )

        m3 = [
            ["3","0", "0"],
            ["0","3", "0"],
            ["0","0", "3"]
        ]

        m4 = [
            ["2","0", "0"],
            ["0","2", "0"],
            ["0","0", "2"]
        ]

        mat5 = Matrix(m3).set_color(MAROON_E)
        mat6 = Matrix(m4).set_color(MAROON_E)

        for i in range(9):
            mat5[0][i].move_to(mat3[0][i])
            mat6[0][i].move_to(mat3[0][i])

        # self.remove(mat3[0])
        self.wait()
        # self.play(
        #     ReplacementTransform(mat4[1],mat5[1])
        # )
        for i in [0,4,8]:
            self.play(
            ReplacementTransform(mat4[0][i], mat5[0][i])
         )

        self.wait()
        self.play(
            *list(map(ReplacementTransform , mat5[0] , mat6[0]))
        )
        
        # self.play(
        #     ReplacementTransform(mat4[2],mat5[2])
        # )
        

        ################


        ################ Identity matrix

        word_i.move_to(ORIGIN)
        word_i.to_corner(UP, buff = 1.5)
        
        self.play(
            ReplacementTransform(word_sc, word_i)
        )


        m3 = [
            ["1","0", "0"],
            ["0","1", "0"],
            ["0","0", "1"]
        ]

        mat7 = Matrix(m3).set_color(GOLD_C)

        for i in range(9):
            mat7[0][i].move_to(mat3[0][i])

        # self.remove(mat3[0])
        self.wait()
        # self.play(
        #     ReplacementTransform(mat4[1],mat5[1])
        # )
        for i in [0,4,8]:
            self.play(
            ReplacementTransform(mat6[0][i], mat7[0][i])
         )
        
        # self.play(
        #     ReplacementTransform(mat4[2],mat5[2])
        # )
        

        ################



        ################ Null matrix

        word_n.move_to(ORIGIN)
        word_n.to_corner(UP, buff = 1.5)
        
        self.play(
            ReplacementTransform(word_i, word_n)
        )


        m3 = [
            ["0","0", "0"],
            ["0","0", "0"],
            ["0","0", "0"]
        ]

        mat8 = Matrix(m3).set_color(TEAL_C)

        for i in range(9):
            mat8[0][i].move_to(mat3[0][i])

        # self.remove(mat3[0])
        self.wait()
        # self.play(
        #     ReplacementTransform(mat4[1],mat5[1])
        # )
        for i in [0,4,8]:
            self.play(
            ReplacementTransform(mat7[0][i], mat8[0][i])
         )
        
        # self.play(
        #     ReplacementTransform(mat4[2],mat5[2])
        # )
        word_sc.move_to(ORIGIN)
        word_sc.to_corner(UP, buff = 1.5)
        
        

        ################
        self.wait()
        
        self.play(FadeOut(mat8),FadeOut(te))
        self.remove(mat6,mat4)
        self.wait()
        


class dif2(Scene):
    def construct(self):
        word = TexText("Different kinds of Matrix")
        word_t = TexText("Transpose Matrix")

        word_t.to_corner(UP, buff = 1.5)
        self.play(Write(word_t))
        self.wait()

        grid = NumberPlane()
        # self.add(grid)

        self.wait(2)
        word.to_corner(UL)
        self.add(word)
        self.play(Write(word_t))
        self.wait()

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
        mat2 = Matrix(m2).set_color(RED)
        mat2_col = mat2.get_columns()
        mat1_col = mat1.get_columns()
        vg = VGroup(Tex("{A}").set_color(YELLOW), Tex("=").set_color(YELLOW), mat1, Tex("hello world "),Tex("{B}").set_color(RED), Tex("=").set_color(RED), mat2 )
        vg.arrange(RIGHT)
        self.play(
            Write(mat1),
            Write(vg[0]),
            Write(vg[1]),
            Write(vg[4]),
            Write(vg[5])
            )
        self.wait(1)

        rec = [BackgroundRectangle(mat1_col[i]) for i in range(3)]
        rec_c = [SurroundingRectangle(mat1_col[i]).set_color(RED) for i in range(3)]

        self.play(
            FadeIn(rec[1]),
            FadeIn(rec[2]),
            ShowCreation(rec_c[0])
        )
        self.play(
            ReplacementTransform(mat1_col[0].copy(), mat2[0][0:3])
        )

        self.wait()

        for i in [1,2]:
            self.play(
                ReplacementTransform(rec[i].copy(),rec[i-1]),
                FadeOut(rec[i]),
                ReplacementTransform(rec_c[i-1], rec_c[i])
            )
            self.play(
            ReplacementTransform(mat1_col[i].copy(), mat2[0][i*3 : i*3 +3])
        )

        self.wait()
        self.play(
            Write(mat2[1]),
            Write(mat2[2])
        )

        self.wait(1)

        word_2 = TexText("B is called transpose of A"
            ,tex_to_color_map =  {
                "B":RED, "A":YELLOW
            } )
        word_2.to_corner(UP, buff= 1.5)

        self.play(
            ReplacementTransform(word_t, word_2)
        )
        t = Tex("{A\\prime}").set_color(RED)
        t.move_to(vg[4])

        self.play(
            ReplacementTransform(vg[4],t)
        )
        self.wait()

class triangle(Scene):

    def construct(self):


        grid = NumberPlane(
            axis_config = {
            "stroke_color": YELLOW,
            "stroke_width": 2,
            "include_ticks": True,
            "include_tip": True,
            "line_to_number_buff": SMALL_BUFF,
            "line_to_number_direction": DL,
        },
        y_axis_config = {
            "line_to_number_direction": DL,
        },
        background_line_style = {
            "stroke_color": ORANGE,
            "stroke_width": 2,
            "stroke_opacity": 1,
        },
        )
        dot1 =Dot([-4,3,0])
        dot2 =Dot([-3,-3,0])
        dot3 =Dot([3,-3,0])
        dot4 =Dot([4,2,0])

        t = ValueTracker(0)

        Q0 = Dot(color=RED).add_updater(lambda m: m.move_to((dot4.get_center() -  dot1.get_center())*t.get_value() + dot1.get_center()))
        # Q1 = Dot(color=RED).add_updater(lambda m: m.move_to((- dot2.get_center() +  dot3.get_center())*1.1*t.get_value() + dot2.get_center()))
        # Q2 = Dot(color=RED).add_updater(lambda m: m.move_to((- dot3.get_center() +  dot1.get_center())*1.2*t.get_value() + dot3.get_center()))
        # Q1 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        # Q2 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P3.get_center() - P2.get_center()) * t.get_value() + P2.get_center()))
        # Q = VGroup(Q0, Q1, Q2)

        Q0_Q2 = Line(color = RED).add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), dot2.get_center()))
        Q2_Q3 = Line(dot2.get_center(), dot3.get_center(),color = TEAL)
        Q2_Q0 = Line(color = YELLOW).add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), dot3.get_center()))



        m1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q2_Q3.get_center(), Q0.get_center()))
        m2 = Line().add_updater(lambda m: m.put_start_and_end_on(Q2_Q0.get_center(), dot2.get_center()))
        m3 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0_Q2.get_center(), dot3.get_center()))

        # a = Line().add_updater(lambda: ())

        self.add( Q0, dot2, dot3)
        self.add(m1,m2,m3,Q0_Q2,Q2_Q0,Q2_Q3)
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)



class tes(Scene):
    def construct(self):
        x = Tex('tttt')
        rt = TexText("Row =")
        ct = TexText("Column =")
        count = 1
        c1 = Tex(str(count))
        c2 = Tex(str(count))
        VGroup(rt,ct).arrange(DOWN)
        
        c1.next_to(rt, RIGHT)
        c2.next_to(ct, RIGHT)
        self.add(rt,ct,c1,c2)