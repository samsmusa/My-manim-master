from manim import *

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
        vector = Vector(RIGHT+2*UP, color = YELLOW)

        self.add(vector)

        self.wait(5)
        coordinates = vector_coordinate_label(vector)
        symbol = Tex("\\vec{\\textbf{v}}")
        sumbol.shift(0.5*(RIGHT+UP))
        self.play(ShowCreation(
            plane, lag_ratio = 1, run_time= 3
        ))