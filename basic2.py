from manim import *

class GroupExample(Scene):
    def construct(self):
        # Using VGroup
        square = Square()
        circle = Circle()
        triangle = Triangle()
        group_v = VGroup(square, circle, triangle)
        self.add(group_v)

        # Using Group (more flexible grouping)
        square2 = Square().shift(2 * RIGHT)
        circle2 = Circle().shift(2 * UP)
        triangle2 = Triangle().shift(2 * LEFT)
        group_generic = Group(square2, circle2, triangle2)
        self.add(group_generic)
