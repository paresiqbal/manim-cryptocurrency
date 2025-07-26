from manim import *

class KeyPairDisplay(Scene):
    def construct(self):
        # 1️⃣ Load images
        private_img = ImageMobject("images/private-key.png").scale(0.35)
        public_img = ImageMobject("images/public-key.png").scale(0.5)

        # Position images
        private_img.move_to(LEFT * 4)
        public_img.move_to(RIGHT * 4)

        # 2️⃣ Labels above images
        font = "KH Interference Trial"
        private_label = Text("Private Key", font_size=32, font=font)
        public_label = Text("Public Key", font_size=32, font=font)

        # Position labels above their corresponding images
        private_label.next_to(private_img, UP, buff=1)
        public_label.next_to(public_img, UP, buff=1)

        # 3️⃣ Animate everything at once
        self.play(
            FadeIn(private_img),
            FadeIn(public_img),
            Write(private_label),
            Write(public_label),
            run_time=1.5
        )

        self.wait(2)
                # 🔵 Circle around the private key
        private_circle = Circle(radius=1.3, color=PINK)
        private_circle.move_to(private_img.get_center())

        self.play(Create(private_circle), run_time=1)
        self.wait(2)
        self.play(FadeOut(private_circle), run_time=0.5)

        # 🔵 Circle around the public key
        public_circle = Circle(radius=1.3, color=PINK)
        public_circle.move_to(public_img.get_center())

        self.play(Create(public_circle), run_time=1)
        self.wait(2)
