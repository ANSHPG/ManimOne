# ManimOne

This project demonstrates a 3D mathematical animation built using [Manim](https://www.manim.community/), a Python library for creating high-quality animations of mathematical concepts. The animation visualizes a trigonometric function graph (sine wave), along with its Riemann rectangles, using dynamic camera manipulation in 3D space.

https://github.com/user-attachments/assets/5d8f6b0e-dc2c-4788-9673-0c68cc163401

## Features

- **3D Axes and Labels**: Displays the x, y, and z axes with appropriate labels.
- **Trigonometric Function Plotting**: A sine function (`sin(x)`) is plotted in 3D space.
- **Riemann Rectangles**: A visual representation of Riemann rectangles under the sine graph to demonstrate integral approximation.
- **Camera Movement**: Smooth camera movements showcasing different angles and perspectives of the graph.
- **Ambient Camera Rotation**: The camera rotates automatically around the scene, providing a dynamic view.
- **Text Animation**: The animation ends with some playful text transformations and a final code block message.

## Requirements

To run this project, you'll need to have [Manim Community](https://docs.manim.community/en/stable/installation.html) installed. Follow the instructions on the Manim website to install the latest version.

```bash
pip install manim
```

## Running the Animation

Once you have Manim installed, you can run the script using the following command:

```bash
manim -pql <filename.py>
```

Here:

- `-pql` stands for "preview, quality low." You can adjust this based on your quality preference:
  - `-pql` for low quality
  - `-pqm` for medium quality
  - `-pqh` for high quality

## Project Structure

The animation code is written in Python, and the main components include:

1. **3D Axes and Labels**: Creates the 3D coordinate axes for the animation, which help visualize the sine function in space.
2. **Trigonometric Function Plotting**: Visualizes the sine function graphically using a purple curve.
3. **Riemann Rectangles**: Displays Riemann rectangles under the curve for approximation of the area.
4. **Camera Movement**: Dynamic camera changes to show the graph from different perspectives.
5. **Text and Paragraph Animation**: Ending scene with text transformation and the display of the code block.

## Visualization Example

At the end of the animation, a code block with credits and a reference to the [3Blue1Brown](https://www.3blue1brown.com/) YouTube channel is shown.

---

## Code Overview

```python
from manim import *
import numpy as np

# Class definition for the 3D scene and camera movement
class ThreeD3(ThreeDScene):
    def construct(self):
        # Axes creation, trigonometric function plotting, camera manipulation, and animations
```

The code uses `ThreeDAxes` to create 3D coordinate axes, and `plot` to visualize the sine function. Camera manipulation techniques such as `set_camera_orientation` and `move_camera` provide smooth transitions between different views of the graph. Text transformation and code block visualization are used at the end to add a narrative to the animation.

## Credits

- Animation created using **Manim**, an open-source Python library for mathematical animations.
- The project is inspired by the work of **3Blue1Brown**, a YouTube channel that visually explains complex math concepts.

---

Feel free to download the code from the GitHub repository and experiment with the Manim library to create your own animations!
