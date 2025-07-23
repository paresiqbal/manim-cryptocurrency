from manim import *

class TransformToBitcoin(Scene):
    def construct(self):
        # Step 1: Show "cryptocurrency" text
        text = Text("cryptocurrency", font_size=72, font="KH Interference Trial")
        text.set_color_by_gradient(YELLOW)
        self.play(Write(text))
        self.wait(1)

        # Step 2: Fade out the text
        self.play(FadeOut(text))

        # Step 3: Draw the circle outline (no fill)
        circle_outline = Circle(radius=1, color=GOLD_E)
        circle_outline.set_fill(opacity=0)  # No fill yet
        self.play(Create(circle_outline), run_time=1.2)
        self.wait(0.5)

        # Step 4: Fade in the ₿ symbol (or BTC)
        try:
            symbol = Text("₿", font_size=72, font="DejaVu Sans", color=WHITE)
        except:
            symbol = Text("BTC", font_size=50, color=WHITE)
        symbol.move_to(circle_outline.get_center())
        self.play(FadeIn(symbol, shift=UP*0.3), run_time=0.8)
        self.wait(0.5)

        # Step 5: Fill the circle with gold to complete the coin
        filled_circle = circle_outline.copy()
        filled_circle.set_fill(interpolate_color(GOLD_E, GOLD_A, 0.5), opacity=1)

        # Replace outline with filled version
        self.play(Transform(circle_outline, filled_circle), run_time=1)

        # Group final coin
        coin_group = VGroup(circle_outline, symbol)
        self.wait(2)