from manim import *
import numpy as np

class ThreeD3(ThreeDScene):  # Use ThreeDScene for 3D camera manipulation
    def construct(self):

        # Create the 3D axes
        axes = ThreeDAxes(
            x_range=[-6, 6],
            y_range=[-6, 6],
            z_range=[-6, 6],
            x_length=8,
            y_length=6,
            z_length=6,
        )

        # Adding labels to the axes
        x_label = axes.get_x_axis_label(MathTex("x"))
        y_label = axes.get_y_axis_label(MathTex("y"))
        z_label = axes.get_z_axis_label(MathTex("z"))

        # Add axes labels to the scene
        self.add(axes, x_label, y_label, z_label)

        # You can choose any trigonometric function here: np.sin, np.cos, or np.tan
        # Let's use sine (sin) as an example:
        def trig_func(x):
            return np.sin(x)

        # Create a graph for the chosen trigonometric function
        graph = axes.plot(trig_func, x_range=[-6, 6], color=PURPLE_B)

        # Create Riemann rectangles for the graph
        rects = axes.get_riemann_rectangles(
            graph=graph, x_range=[-6, 6], dx=0.1, stroke_color=WHITE
        )

        # Add the axes and the trig function graph
        self.add(axes, graph)

        # Set an initial camera orientation and then change it over time
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)  # Initial camera orientation
        # self.wait()

        self.play(Create(graph), run_time=3)

        # Rotate the camera to view from a different angle
        self.move_camera(phi=60 * DEGREES)
        # self.wait()

        # Further adjust the camera angle
        self.move_camera(theta=-45 * DEGREES)
        # self.wait()

        self.begin_ambient_camera_rotation(
            rate=PI / 10, about="theta"
        )  # Rotates at a rate of radians per second
        # self.wait()

        self.play(Create(rects), run_time=3)
    
        self.stop_ambient_camera_rotation()

        self.wait()

        self.move_camera(theta=-90 * DEGREES)
        self.move_camera(phi=0 * DEGREES)
        self.wait(1)

        # Now uncreate the graph, axes, and Riemann rectangles
        self.play(Uncreate(rects),run_time=1)
        self.play(Uncreate(graph),run_time=1)
        # self.wait(1)
        self.play(Uncreate(x_label), Uncreate(y_label), Uncreate(z_label), run_time=1)
        self.play(Uncreate(axes), run_time=1)

        text = Tex('Hello ','World')
        text[0].set_color(PINK)
        text[1].set_color(RED)

        self.play(Write(text),run_time=1)
        self.wait()

        paragraph = Tex(
            'The entire video is created using ',
            'Manim',
            ', a powerful Python library for creating mathematical animations. Originally developed by ',
            '3Blue',
            '1Brown',
            ', a popular YouTube channel known for visually explaining complex math concepts, Manim enables dynamic, high-quality animations that bring math and programming to life.',
            font_size=32
        )

        # Set color for specific parts
        paragraph[1].set_color(PINK)        # "Manim" (first occurrence)
        paragraph[3].set_color(BLUE)       # "3Blue1Brown"
        paragraph[4].set_color(RED) 

        
        # Perform the transformation animation with the colored text
        self.play(Transform(text, paragraph), run_time=2)
        self.wait(4)
        self.play(Uncreate(text),run_time=2)

        code = Code(
            code="""Editor: Anshuman Pattnaik\nI would love to hear your feedback on this!\nBe sure to check out the content from 3Blue1Brown as well.\nThe code for this video will be available in the GitHub repository.""",
            tab_width=4, 
            background="window",  
            language="python", 
            font="Monospace",  
            insert_line_no=False,  
            font_size=30 
        )

        code.scale_to_fit_width(config.frame_width * 0.8)
        # code.to_edge(LEFT, buff=0.5)

        # self.play(Transform(paragraph,code))
        self.play(FadeIn(code))  
        self.wait(3)


        

