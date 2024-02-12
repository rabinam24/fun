from manim import *

class Factorization(Scene):
    def construct(self):
        title = Tex("Factorization:")
        fact = MathTex(r"{x^2 - 64 = 0}")
        VGroup(title, fact).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(fact, shift=DOWN)
        )
        self.wait()

        transform_title = Tex("Let's begin it!")
        transform_title.move_to(2* UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in fact])
        )
        self.wait()

        fact.move_to(transform_title.get_center() + DOWN)
        fact1 = MathTex(r"{((x-8)(x+8) = 0}")
        fact2 = MathTex(r"{(x-8) = 0  or  (x+8) = 0}")
        fact3 = MathTex(r"{x = 8  or  x = -8}")
        VGroup(fact, fact1, fact2, fact3).arrange(DOWN)
        
        self.play(
            Write(fact),
        )
        self.wait(2)

        self.play(
            Write(fact1),
        )
        self.wait(2)
        
        self.play(
            Write(fact2),
        )
        self.wait(2)
        
        self.play(
            Write(fact3),
        )
        self.wait(2)
