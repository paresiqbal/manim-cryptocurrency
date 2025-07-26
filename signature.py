from manim import *

class SignatureSVG(Scene):
    def construct(self):
        # Load the SVG from images/signature.svg
        signature = SVGMobject("images/signature.svg")

        # Scale and style
        signature.set_color(WHITE)  # Since the SVG already uses black stroke
        signature.set_stroke(width=2)
        signature.set_fill(opacity=0)  # No fill
        signature.scale(1.2)
        signature.move_to(ORIGIN)

        # Animate drawing the signature
        self.play(Create(signature), run_time=3)
        self.wait(2)
  # 2️⃣ Move signature to the left (X = -4)
        self.play(signature.animate.shift(LEFT * 3), run_time=1)

        # 3️⃣ Load padlock image and show it on the right (X = +4)
        padlock = ImageMobject("images/padlock.png")
        padlock.scale(1.5)
        padlock.move_to(RIGHT * 4)

        # 🖼️ Fade in padlock
        self.play(FadeIn(padlock), run_time=1)
        self.wait(2)