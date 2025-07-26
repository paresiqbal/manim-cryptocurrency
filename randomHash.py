from manim import *
import random
import string

class NonceHashSimulation(Scene):
    def construct(self):
        font = "KH Interference Trial"  # Monospaced
        font_size = 48

        # 1️⃣ Initial nonce & hash
        nonce_text = Text("Nonce: 00000", font_size=font_size, font=font)
        hash_text = Text("Hash: " + "0" * 20, font_size=font_size - 4, font=font)

        nonce_text.move_to(UP * 1)
        hash_text.move_to(DOWN * 0.5)

        self.play(Write(nonce_text), Write(hash_text))
        self.wait(0.5)

        # 2️⃣ Loop for 9 random updates
        for _ in range(9):
            new_nonce = str(random.randint(10000, 99999))
            new_hash = ''.join(random.choices(string.ascii_letters + string.digits, k=20))

            self.play(
                Transform(nonce_text, Text(f"Nonce: {new_nonce}", font_size=font_size, font=font).move_to(nonce_text.get_center())),
                Transform(hash_text, Text(f"Hash: {new_hash}", font_size=font_size - 4, font=font).move_to(hash_text.get_center())),
                run_time=0.6
            )
            self.wait(0.4)

        # 3️⃣ Final (mined) nonce and hash with 8 leading zeros
        success_nonce = str(random.randint(10000, 99999))
        success_hash = "0" * 8 + ''.join(random.choices(string.ascii_letters + string.digits, k=12))

        nonce_final = Text(f"Nonce: {success_nonce}", font_size=font_size, font=font)
        hash_final = Text(f"Hash: {success_hash}", font_size=font_size - 4, font=font, color=GREEN)

        nonce_final.move_to(nonce_text.get_center())
        hash_final.move_to(hash_text.get_center())

        self.play(
            Transform(nonce_text, nonce_final),
            Transform(hash_text, hash_final),
            run_time=0.8
        )

        self.wait(2)
