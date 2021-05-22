from manimlib import *
# from manimlib.imports import *
import numpy as np


text = Text("hello")
text2 = Text("how are you")
text3 = Text("who are you")
ltext = Tex("hello world")
ltext2 = Tex("hey man!")

class intro(Scene):
    def construct(self):
        text = TexText("hello"," OVI"," how"," are"," you?")
        for i in range(5):
            if i == 1:
                text[i].set_color(RED)
            else:
                text[i].set_color(GREEN)
            self.play(Write(text[i]))
            self.wait(1)
        kw = {"run_time": 3, "path_arc": PI / 2}
        text2 = TexText("Hi RAKIB!")
        text3 = TexText("hey ANOY bro!")
        self.play(TransformMatchingShapes(text, text2, **kw))
        self.wait()
        self.play(TransformMatchingShapes(text2, text3, **kw))
        self.wait()


class mohi(Scene):
    def construct(self):

        grid = NumberPlane((-10, 10), (-5, 5))

        source = Text("আমাএর What lies behind you and what lies in front of you", height=0.4)
        target = Text("pales in comparison to what lies inside of you", height=0.5)
        source1 = Text("What's your Openion, MOHI?", height = 0.8)
        source.set_color(GREEN)
        source1.set_color(RED)


        self.play(
            ShowCreation(grid)
        )


        self.play(Write(source))
        self.wait()
        kw = {"run_time": 3, "path_arc": PI}
        self.play(TransformMatchingShapes(source, target, **kw))
        self.wait()
        self.play(TransformMatchingShapes(target, source1, **kw))
        self.wait()


class intf(Scene):
    def construct(self):

        q = TexText("Beauty", " is", " the"," first"," test", font ="Arial" , font_size = 44, text_color = RED ).set_color(RED)
        qoute2 = Text("there is no permanent place in the world for ugly mathematics")

        a = (q[1]).next_to(q[0],UR)
        b = (q[2]).next_to(q[0],UL)
        c = (q[3]).next_to(q[0],DR)
        d = (q[4]).next_to(q[0],DL)

        e = VGroup(a,b,c,d)



        # qoute2.next_to(qoute, DOWN)

        self.play(FadeIn(e))


        self.play(Write(q),run_time = 3)
        self.wait()
        # self.play(Write(qoute2),run_time = 3)
        # self.wait()


class newc(Scene):
    def construct(self):
        text = Text("This is a regular text")
        self.play(Write(text))
        self.wait(3)


class typeOfText(Scene):
    def construct(self):
        tipes = TexText("""
            This is a regular text,
            $this is a formulas$,
            $$this is a formula$$
            """)
        self.play(Write(tipes))
        self.wait(3)

class deff(Scene):
    def construct(self):
        text = TexText("""
            This is a regular text, 
            $\\displaystyle\\frac{x}{y}$, 
            $$x^2+y^2=a^2$$ 
            """)
        self.play(Write(text))
        self.wait(3)
#position relative to scereen

class tidp(Scene):
    def construct(self):
        text = TexText("Hello", "i'm", " musa", " hey")
        text[0].to_edge(RIGHT)
        text[1].to_edge(DOWN)
        text[2].to_edge(LEFT)
        text[3].to_edge(UP)

        self.play(Write(text))
        self.wait(3)


class cp(Scene):
    def construct(self):
        text = Text("text")
        text2 = Text("central text")
        text.move_to(0.25*UP)
        self.play(Write(text),Write(text2))
        self.wait(3)

class cp2(Scene):
    def construct(self):
        text = Text("hello")
        text2 = Text("how are you")
        text3 = Text("who are you")

        text2.move_to(3*DOWN+3*LEFT)

        self.play(Write(text),Write(text2))
        self.wait()

        text3.move_to(1*UP+2*RIGHT)
        self.play(Write(text3))
        self.wait()


#relative position

class cp3(Scene):
    def construct(self):
        self.play(Write(text))
        self.wait()

        text2.next_to(text, LEFT, buff=1)
        self.play(Write(text2))
        self.wait()

        text.shift(UP*3)
        self.play(Write(text))
        self.wait()

#rotation

class ro(Scene):
    def construct(self):
        text.shift(UP)
        text.rotate(PI/4)
        self.play(ShowCreation(text))
        self.wait()
        text.rotate(PI/4)
        self.wait()
        text.rotate(PI/4)
        self.wait()

        text.flip(DOWN)
        self.wait()


#latex

class la(Scene):
    def construct(self):
        textHuge = Tex("{\\Huge Huge Text 012.\\#!?} Text")
        texthuge = Tex("{\\huge huge Text 012.\\#!?} Text")
        textLARGE = Tex("{\\LARGE LARGE Text 012.\\#!?} Text")
        textLarge = Tex("{\\Large Large Text 012.\\#!?} Text")
        textlarge = Tex("{\\large large Text 012.\\#!?} Text")
        textNormal = Tex("{\\normalsize normal Text 012.\\#!?} Text")
        textsmall = Tex("{\\small small Text 012.\\#!?} Texto normal")
        textfootnotesize = Tex("{\\footnotesize footnotesize Text 012.\\#!?} Text")
        textscriptsize = Tex("{\\scriptsize scriptsize Text 012.\\#!?} Text")
        texttiny = Tex("{\\tiny tiny Texto 012.\\#!?} Text normal")
        textHuge.to_edge(UP)
        texthuge.next_to(textHuge,DOWN,buff=0.1)
        textLARGE.next_to(texthuge,DOWN,buff=0.1)
        textLarge.next_to(textLARGE,DOWN,buff=0.1)
        textlarge.next_to(textLarge,DOWN,buff=0.1)
        textNormal.next_to(textlarge,DOWN,buff=0.1)
        textsmall.next_to(textNormal,DOWN,buff=0.1)
        textfootnotesize.next_to(textsmall,DOWN,buff=0.1)
        textscriptsize.next_to(textfootnotesize,DOWN,buff=0.1)
        texttiny.next_to(textscriptsize,DOWN,buff=0.1)
        self.add(textHuge,texthuge,textLARGE,textLarge,textlarge,textNormal,textsmall,textfootnotesize,textscriptsize,texttiny)
        self.wait(3)    



#transform

class tr(Scene):
    def construct(self):

        self.play(Write(text))
        self.wait()
        self.play(ReplacementTransform(text,text2))
        self.wait()


class trl(Scene):
    def construct(self):

        formula = Tex(
			"\\frac{d}{dx}", #0
			"(", #1
			"u", #2
			"+", #3
			"v", #4
			")", #5
			"=", #6
			"\\frac{d}{dx}", #7
			"u", #8
			"+", #9
			"\\frac{d}{dx}", #10
			"v" #11
			, font_size=70)

            # formula
        VGroup(formula[0::2]).set_color(RED)
        VGroup(formula[1::2]).set_color(BLUE)

        self.play(Write(formula[0:7]))
        self.wait()

        self.play(
            ReplacementTransform(formula[2].copy(),formula[8]),
            ReplacementTransform(formula[4].copy(),formula[11]),
            ReplacementTransform(formula[3].copy(),formula[9]), run_time = 3
            )
        self.wait()

        self.play(
            ReplacementTransform(formula[0].copy(),formula[7]),
            ReplacementTransform(formula[0].copy(),formula[10]), run_time=3
        )
        self.wait()
        

class rtl2(Scene):
    def construct(self):
        formula = Tex(
            "\\frac{d}{dx}", #0
            "(",#1
            "u",#2
            "+",#3
            "v",#4
            ")",#5
            "=",#6
            "\\frac{d}{dx}",#7
            "u",#8
            "+",#9
            "\\frac{d}{dx}",#10
            "v", font_size = 70
        )

        for letter, color in [("u",RED),("v",BLUE)]:
            formula.set_color_by_tex(letter,color)

        self.play(Write(formula[0:7]))
        self.wait()

        self.play(
            ReplacementTransform(formula[2].copy(),formula[8]),
            ReplacementTransform(formula[4].copy(),formula[11]),
            ReplacementTransform(formula[3].copy(),formula[9])
        )
        self.wait()

        self.play(
            ReplacementTransform(formula[0].copy(),formula[7]),
            ReplacementTransform(formula[0].copy(),formula[10])
        )
        self.wait()

class rtl3(Scene):
    def construct(self):
        formula1 = Tex(
            "\\neg", #0
            "\\forall", #1
            "x", #2
            ":", #3
            "P(x)", #4
        )

        formula2 = Tex(
            "\\exists", #0
            "x", #1
            ":", #2
            "\\neg", #3
            "P(x)"
        )

        for size,pos,formula in [(2,2*UP,formula1),(2,2*DOWN,formula2)]:
            formula.scale(size)
            formula.move_to(pos)

        self.play(Write(formula1))
        self.wait()

        changes = [
            [(0,1,2,3,4),
            (3,0,1,2,4)],
        ]

        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(formula1[i].copy(),formula2[j])
            
            for i,j in zip(pre_ind,post_ind)
            ],
            run_time =2
            )
            self.wait()



class rtl4(Scene):
    def construct(self):
        formula1 = Tex(
            "\\neg", #0
            "\\forall", #1
            "x", #2
            ":", #3
            "P(x)", #4
        )
        formula2 = Tex(
            "\\exists", #0
            "x", #1
            ":", #2
            "\\neg", #3
            "P(x)" #4
        )

        parametters = [(2,2*UP,formula1,GREEN,"\\forall"),
            (2,2*DOWN,formula2,ORANGE,"\\exists")]

        for size,pos,formula,col,sim in parametters:
            formula.scale(size)
            formula.move_to(pos)
            formula.set_color_by_tex(sim,col)
            formula.set_color_by_tex("\\neg",PINK)

        self.play(Write(formula1))
        self.wait()

        changes =[
            [(2,3,4),(1,2,4)],
            [(0,),(3,)],
            [(1,0),(0,)]
        ]

        for pre_ind, post_ind in changes:
            self.play(*[
                ReplacementTransform(formula1[i].copy(),formula2[j])
            

            for i,j in zip(pre_ind,post_ind)
            ],
            run_time =2
            )
            self.wait()

