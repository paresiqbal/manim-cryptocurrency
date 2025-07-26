from manim import *

class ZeroAnimation(Scene):
    def construct(self):
        font = "KH Interference Trial"

        # Step 1: Create 8 large zeros
        zeros_8 = VGroup(*[
            Text("0", font_size=64, font=font) for _ in range(8)
        ]).arrange(RIGHT, buff=0.2).move_to(ORIGIN)

        self.play(Write(zeros_8), run_time=1)
        self.wait(1)

        # Step 2: Move the 8 zeros upward
        self.play(zeros_8.animate.shift(UP * 1.5), run_time=1)

        # Step 3: Create 20 smaller zeros in one centered row
        zeros_20 = VGroup(*[
            Text("0", font_size=36, font=font) for _ in range(20)
        ]).arrange(RIGHT, buff=0.15).move_to(ORIGIN)

        self.play(Write(zeros_20), run_time=2)
        self.wait(2)
