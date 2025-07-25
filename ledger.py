from manim import *

class CleanLedger(Scene):
    def construct(self):
        font = "KH Interference Trial"

        width = 4.0
        height = 2.4

        # 🟦 BANK LEDGER (Left Side)
        box = Rectangle(width=width, height=height, color=BLUE)

        divider = Line(
            start=box.get_left() + RIGHT * 0.05 + DOWN * -0.4,
            end=box.get_right() + LEFT * 0.05 + DOWN * -0.4,
            color=BLUE
        )

        name_text = Text("Otong", font_size=28, font=font).move_to(box.get_top() + DOWN * 0.4)
        income_text = Text("+ Rp. 100.000", font_size=26, font=font, color=GREEN).move_to(ORIGIN)
        expense_text = Text("- Rp. 50.000", font_size=26, font=font, color=RED).move_to(box.get_bottom() + UP * 0.4)

        bank_label = Text("BANK", font_size=36, font=font).move_to(UP * 3)

        self.play(Create(box), FadeIn(bank_label), run_time=0.7)
        self.play(Create(divider), run_time=0.3)
        self.play(Write(name_text), Write(income_text), Write(expense_text), run_time=1)
        self.wait(1)

        # Group and move left
        ledger_group = VGroup(box, divider, name_text, income_text, expense_text, bank_label)
        self.play(
            ledger_group.animate.shift(LEFT * 4),
            Write(Text("CRYPTOCURRENCY", font_size=36, font=font).move_to(RIGHT * 4 + UP * 3)),
            run_time=1.2
        )
        self.wait(0.5)

        # 📜 Now generate the long public ledger on the right
        entries = [
            ("Otong", "+ Rp. 20.000", GREEN),
            ("Ica", "- Rp. 50.000", RED),
            ("Ujang", "+ Rp. 100.000", GREEN),
            ("Tini", "- Rp. 70.000", RED),
        ]

        crypto_ledger = VGroup()
        y_start = 1.5  # starting Y position
        x_name = 2.5   # name column X
        x_amount = 5.5 # amount column X

        for i, (name, amount, color) in enumerate(entries):
            y_pos = y_start - i * 1.2

            name_text = Text(name, font_size=26, font=font).move_to([x_name, y_pos, 0])
            amount_text = Text(amount, font_size=26, font=font, color=color).move_to([x_amount, y_pos, 0])
            crypto_ledger.add(name_text, amount_text)

            # divider under each row except the last one
            if i < len(entries) - 1:
                line = Line(start=[x_name - 0.8, y_pos - 0.6, 0], end=[x_amount + 0.8, y_pos - 0.6, 0], color=YELLOW)
                crypto_ledger.add(line)

        self.play(*[Write(mob) for mob in crypto_ledger], run_time=1)
        self.wait(2)
