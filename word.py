from manim import *

class Word(Scene):
    def construct(self):
        # Shared font and size
        custom_font = "KH Interference Trial"  # Change this to your desired font
        font_size = 50

        # List of texts and colors
        phrases = [
            ("CARA KERJA CRYPTOCURRENCY", YELLOW),
            ("CARA KERJA BLOCKCHAIN", BLUE),
            ("CARA KERJA MINING", GREEN),
        ]

        # Create Text objects using list comprehension
        words = VGroup(*[
            Text(text, font_size=font_size, font=custom_font, color=color)
            for text, color in phrases
        ]).arrange(DOWN, buff=0.3)

        # Animate with slow write
        self.play(Write(words), run_time=5, lag_ratio=0.3)
        self.wait(2)
