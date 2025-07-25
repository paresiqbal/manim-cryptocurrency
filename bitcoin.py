from manim import *
import random

class BitcoinChart(Scene):
    def construct(self):
        title = Text("Bitcoin Price Simulation", font_size=40).to_edge(UP)

        # 1. Create the axes - made smaller and shifted down
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 12, 2],
            x_length=9,         
            y_length=5.5,
            axis_config={"color": BLUE},
        ).shift(DOWN * 0.5)

        x_label = axes.get_x_axis_label("Time (Year 2025)")
        y_label = axes.get_y_axis_label(r"Price (\$ K)")

        # 2. Simulate the price data (This part is unchanged)
        x_values = []
        y_values = []
        current_price = 2.0
        for i in range(41):
            x_values.append(i * 0.25)
            y_values.append(current_price)
            trend = 0.12
            volatility = random.uniform(-0.35, 0.5)
            current_price += trend + volatility
            if current_price < 1:
                current_price = 1 + abs(volatility)

        # 3. Create the graph from our simulated data points
        graph = axes.plot_line_graph(
            x_values=x_values,
            y_values=y_values,
            line_color=GOLD_E,
            add_vertex_dots=False,
        )

        # 4. Create an animated label for the final price
        final_price_text = Text("Final Price: $", font_size=24)
        final_price_number = DecimalNumber(
            y_values[-1],
            num_decimal_places=2,
            font_size=24,
        )
        final_price_unit = Text("K", font_size=24)
        final_price_group = VGroup(final_price_text, final_price_number, final_price_unit)
        final_price_group.arrange(RIGHT, buff=0.1)
        
     
        last_point_coord = axes.c2p(x_values[-1], y_values[-1])
        final_price_group.next_to(last_point_coord, UP, buff=0.2)


        # 5. Animate the scene
        self.play(Write(title)) 
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(graph), run_time=4)
        self.wait(0.5)
        self.play(FadeIn(final_price_group))
        self.wait(2)