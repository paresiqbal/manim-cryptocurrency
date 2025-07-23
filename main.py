from manim import *
import random

class TransformToBitcoin(Scene):
    def construct(self):
        text = Text("cryptocurrency", font_size=72, font="KH Interference Trial")
        text.set_color_by_gradient(YELLOW)
        self.play(Write(text))
        self.wait(1)

        self.play(FadeOut(text))

        circle_outline = Circle(radius=1.2, color=GOLD_E)
        circle_outline.set_fill(opacity=0)  
        self.play(Create(circle_outline), run_time=0.7)
        self.wait(0.1)

        try:
            symbol = Text("₿", font_size=72, font="DejaVu Sans", color=WHITE)
        except:
            symbol = Text("BTC", font_size=50, color=WHITE)
        symbol.move_to(circle_outline.get_center())
        self.play(FadeIn(symbol, shift=UP*0.3), run_time=0.5)
        self.wait(0.3)

        filled_circle = circle_outline.copy()
        filled_circle.set_fill(interpolate_color(GOLD_E, GOLD_A, 0.5), opacity=1)

        self.play(Transform(circle_outline, filled_circle), run_time=0.7)

        coin_group = VGroup(circle_outline, symbol)
        self.wait(2)

        for _ in range(10): 
            question_pair = VGroup()

            for _ in range(2): 
                q = Text("?", font_size=150, color=PINK, font="KH Interference Trial")
                q.move_to([
                    random.uniform(-self.camera.frame_width / 2 + 0.5, self.camera.frame_width / 2 - 0.5),
                    random.uniform(-self.camera.frame_height / 2 + 0.5, self.camera.frame_height / 2 - 0.5),
                    0
                ])
                question_pair.add(q)

            self.play(FadeIn(question_pair), run_time=0.5)
            self.wait(0.5)
            self.play(FadeOut(question_pair), run_time=0.3)


        self.play(coin_group.animate.shift(LEFT * 4), run_time=0.7)

        equals = Text("=", font_size=72, color=WHITE)
        self.play(FadeIn(equals), run_time=0.2)

        sukses = Text("PASTI SUKSES", font_size=55,font="KH Interference Trial", color=YELLOW, )
        sukses.move_to(RIGHT * 4)
        self.play(FadeIn(sukses, shift=DOWN * 0.2), run_time=0.5)

        self.wait(2)