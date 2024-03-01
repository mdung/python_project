import tkinter as tk

class FractalGenerator(tk.Tk):
    def __init__(self, width, height, max_iter):
        super().__init__()

        self.title("Mandelbrot Set Generator")
        self.geometry(f"{width}x{height}")

        self.width = width
        self.height = height
        self.max_iter = max_iter

        self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg="white")
        self.canvas.pack()

        self.generate_fractal()

    def generate_fractal(self):
        for x in range(self.width):
            for y in range(self.height):
                real = (x - self.width / 2) * 4 / self.width
                imag = (y - self.height / 2) * 4 / self.height

                color = self.mandelbrot(real, imag)
                self.canvas.create_rectangle(x, y, x + 1, y + 1, fill=color, outline="")

    def mandelbrot(self, real, imag):
        c = complex(real, imag)
        z = complex(0, 0)

        for i in range(self.max_iter):
            z = z * z + c
            if abs(z) > 2:
                return self.color_map(i)

        return "black"

    def color_map(self, iteration):
        r = (iteration * 10) % 256
        g = (iteration * 5) % 256
        b = (iteration * 2) % 256
        return f"#{r:02x}{g:02x}{b:02x}"

if __name__ == "__main__":
    width, height = 800, 800
    max_iter = 100

    fractal_generator = FractalGenerator(width, height, max_iter)
    fractal_generator.mainloop()
