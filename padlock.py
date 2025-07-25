from manim import *

class DrawPadlockWithFormula(Scene):
    def construct(self):
        body_color = GOLD_E
        stroke_width = 4

        # 🔲 Body
        body = Square(side_length=2.8)
        body.set_fill(opacity=0)
        body.set_stroke(color=body_color, width=stroke_width)

        # 🧢 Handle
        arc1 = Arc(radius=1.0, start_angle=0, angle=PI)
        arc2 = Arc(radius=0.75, start_angle=0, angle=PI)
        arc1.set_stroke(color=body_color, width=stroke_width)
        arc2.set_stroke(color=body_color, width=stroke_width)
        arc1.move_to(body.get_top() + UP * 0.4)
        arc2.move_to(body.get_top() + UP * 0.4)
        handle = VGroup(arc1, arc2)

        # 🔑 Keyhole
        keyhole_circle = Circle(radius=0.16, color=BLACK, fill_opacity=1)
        keyhole_rect = Rectangle(width=0.1, height=0.3, color=BLACK, fill_opacity=1)
        keyhole = VGroup(keyhole_circle, keyhole_rect).arrange(DOWN, buff=0).move_to(body.get_center())

        # ➕ Formula
        formula = MathTex(r"y^2 = x^3 + 7", font_size=60).next_to(body, DOWN, buff=1.2)

        # 🎬 Animate
        self.play(Create(body), run_time=2)
        self.play(body.animate.set_fill(color=GOLD_A, opacity=1), run_time=1.5)
        self.play(Create(handle), run_time=1.5)
        self.play(FadeIn(keyhole), run_time=1.5)
        self.play(Write(formula), run_time=1)
        self.wait(2)
