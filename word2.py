from manim import *

class CryptoReveal(Scene):
    def construct(self):
        font_size = 50
        font = "KH Interference Trial"  # Replace if you want another font

        # Step 1: Write "CRYPTOCURRENCY" at Y=1
        full_word = Text("CRYPTOCURRENCY", font_size=font_size, font=font)
        full_word.move_to(UP * 1)
        self.play(Write(full_word))
        self.wait(1)

        # Step 2: Highlight "CRYPTO" in red and show "tersembunyi"
        # We slice the word into parts to recolor just "CRYPTO"
        crypto = full_word[:6]  # "CRYPTO"
        crypto.set_color(RED)

        # Show "tersembunyi"
        tersembunyi = Text("tersembunyi", font_size=font_size, color=RED, font=font)
        tersembunyi.move_to(LEFT * 3 + DOWN * 1)

        self.play(
            full_word.animate.set_color_by_text_to_color_map({"CRYPTO": RED}),
            FadeIn(tersembunyi),
            run_time=1
        )
        self.wait(2)

        # Step 3: Highlight "CURRENCY" in blue and show "uang"
        currency = full_word[6:]  # "CURRENCY"
        currency.set_color(BLUE)

        uang = Text("uang", font_size=font_size, color=BLUE, font=font)
        uang.move_to(RIGHT * 3 + DOWN * 1)

        self.play(
            full_word.animate.set_color_by_text_to_color_map({"CURRENCY": BLUE}),
            FadeIn(uang),
            run_time=1
        )
        self.wait(1)

                # Step 4: Move all texts to center (0, 0)
        self.play(
            full_word.animate.move_to(ORIGIN),
            tersembunyi.animate.move_to(ORIGIN),
            uang.animate.move_to(ORIGIN),
            run_time=1
        )
        self.play(
            full_word.animate.set_color(YELLOW),
            FadeOut(tersembunyi),
            FadeOut(uang),
            run_time=0.3
        )
        self.wait(1)

        # Step 5: Show padlock image at x = 2
        padlock = ImageMobject("images/padlock.png")
        padlock.scale(0.5)  # Resize if needed
        padlock.move_to(UP * 2)  # Move to X=2, Y=0
        self.play(FadeIn(padlock), run_time=1)
        self.wait(2)

     # Step 6: Remove padlock and move "CRYPTOCURRENCY" to the left
        self.play(
            FadeOut(padlock),
            full_word.animate.move_to(LEFT * 4),
            run_time=1
        )

        # Step 7: Show "=" at center and "UANG DIGITAL" at X = 4
        not_equal = Text("≠", font_size=font_size, color=WHITE)
        not_equal.move_to(ORIGIN)
        self.play(FadeIn(not_equal), run_time=1)

        uang_digital = Text("UANG DIGITAL", font_size=font_size, color=YELLOW, font=font)
        uang_digital.move_to(RIGHT * 4)

        self.play(
            FadeIn(not_equal),
            FadeIn(uang_digital),
            run_time=1
        )

        self.wait(2)