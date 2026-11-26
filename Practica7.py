import os
import time
import turtle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from PIL import Image

def ejemplo_onda_senoidal():
	print("\nGenerando '1_onda_senoidal.gif'...")
	fig, ax = plt.subplots()
	x = np.linspace(0, 2 * np.pi, 200)
	linea, = ax.plot(x, np.sin(x), color='royalblue', lw=2)
	ax.set_ylim(-1.5, 1.5)
	ax.set_title("1. Onda Senoidal Animada")
	ax.grid(True)

	def actualizar(frame):
		linea.set_ydata(np.sin(x + frame / 10.0))
		return linea,
		ani = FuncAnimation(fig, actualizar, frames=60, interval=50, blit=True)
		ani.save("1_onda_senoidal.gif", writer=PillowWriter(fps=20))
		print("¡Archivo '1_onda_senoidal.gif' guardado! Cierra la ventana para volver al menú.")
		plt.show()

	def ejemplo_espiral():
		print("\nGenerando '2_espiral.gif'...")
		fig, ax = plt.subplots()
		ax.set_xlim(-10, 10)
		ax.set_ylim(-10, 10)
		ax.set_aspect('equal')
		ax.set_title("2. Espiral de Arquímedes")
		linea, = ax.plot([], [], color='crimson', lw=2)

		t_max = np.linspace(0, 10 * np.pi, 300)

	def actualizar(frame):
		t = t_max[:frame]
		r = 0.3 * t
		x = r * np.cos(t)
		y = r * np.sin(t)
		linea.set_data(x, y)
		return linea,

	ani = FuncAnimation(fig, actualizar, frames=len(t_max), interval=20, blit=True)
	ani.save("2_espiral.gif", writer=PillowWriter(fps=30))
	print("¡Archivo '2_espiral.gif' guardado! Cierra la ventana para volver al menú.")
	plt.show()

def ejemplo_barras():
	print("\nGenerando '3_barras_dinamicas.gif'...")
	fig, ax = plt.subplots()
	categorias = ['Python', 'Java', 'C++', 'JS', 'Go']
	barras = ax.bar(categorias, [10, 10, 10, 10, 10], color=['#3776ab', '#f89820', '#00599c', '#f7df1e', '#00add8'])
	ax.set_ylim(0, 100)
	ax.set_title("3. Crecimiento de Popularidad Simulada")
	
	np.random.seed(42)
	datos_frames = np.random.randint(15, 95, size=(30, 5))

	def actualizar(frame):
		for barra, altura in zip(barras, datos_frames[frame]):
			barra.set_height(altura)
		return barras

	ani = FuncAnimation(fig, actualizar, frames=30, interval=200)
	ani.save("3_barras_dinamicas.gif", writer=PillowWriter(fps=5))
	print("¡Archivo '3_barras_dinamicas.gif' guardado! Cierra la ventana para volver al menú.")
	plt.show()

def ejemplo_proyectil():
	print("\nGenerando '4_proyectil.gif'...")
	fig, ax = plt.subplots()
	ax.set_xlim(0, 50)
	ax.set_ylim(0, 20)
	ax.set_title("4. Trayectoria de un Proyectil")
	ax.grid(True)

	punto, = ax.plot([], [], 'ro', markersize=10)
	estela, = ax.plot([], [], 'r--', alpha=0.5)

	v0 = 22
	angulo = np.radians(50)
	g = 9.81
	t_total = (2 * v0 * np.sin(angulo)) / g
	tiempos = np.linspace(0, t_total, 50)

	x_datos = v0 * np.cos(angulo) * tiempos
	y_datos = v0 * np.sin(angulo) * tiempos - 0.5 * g * tiempos**2

	def actualizar(frame):
		punto.set_data([x_datos[frame]], [y_datos[frame]])
		estela.set_data(x_datos[:frame+1], y_datos[:frame+1])
		return punto, estela

	ani = FuncAnimation(fig, actualizar, frames=len(tiempos), interval=40, blit=True)
	ani.save("4_proyectil.gif", writer=PillowWriter(fps=25))
	print("¡Archivo '4_proyectil.gif' guardado! Cierra la ventana para volver al menú.")
	plt.show()

def ejemplo_turtle_pil():
	print("\nGenerando '5_turtle_estrella.gif'...")
	print("Nota: Este método requiere Ghostscript instalado en el sistema.")

	screen = turtle.Screen()
	screen.setup(width=400, height=400)
	screen.title("5. Captura Turtle -> PostScript -> GIF")
	screen.bgcolor("black")

	t = turtle.Turtle()
	t.color("cyan")
	t.pensize(3)
	t.speed(0)

	frames = []
	temp_eps = "temp_frame.eps"

	try:
		for i in range(18):
			t.forward(150)
			t.right(100)

			canvas = screen.getcanvas()
			canvas.postscript(file=temp_eps)
            
			img = Image.open(temp_eps)
			img.load(scale=2) 
			frames.append(img.convert("RGB"))

		if frames:
			frames[0].save(
				"5_turtle_estrella.gif",
				save_all=True,
				append_images=frames[1:],
				duration=150,
				loop=0
			)
			print("¡Archivo '5_turtle_estrella.gif' guardado con éxito!")
            
	except Exception as e:
		print(f"\n[Error al procesar PostScript con PIL]: {e}")
		print("Asegúrate de tener Ghostscript instalado en tu computadora.")
	finally:
		if os.path.exists(temp_eps):
			os.remove(temp_eps)
		time.sleep(1)
		screen.bye()
def menu():
	while True:
		print("\n" + "="*45)
		print("   GENERADOR DE ANIMACIONES .GIF EN PYTHON")
		print("="*45)
		print("1. Onda Senoidal (Matplotlib)")
		print("2. Espiral de Arquímedes (Matplotlib)")
		print("3. Gráfica de Barras Dinámica (Matplotlib)")
		print("4. Movimiento Parabólico (Matplotlib)")
		print("5. Estrella Geométrica (Turtle + PostScript + PIL)")
		print("6. Salir")
		print("="*45)
		opcion = input("Selecciona una opción (1-6): ")
		if opcion == '1':
			ejemplo_onda_senoidal()
		elif opcion == '2':
			ejemplo_espiral()
		elif opcion == '3':
			ejemplo_barras()
		elif opcion == '4':
			ejemplo_proyectil()
		elif opcion == '5':
			ejemplo_turtle_pil()
		elif opcion == '6':
			print("Saliendo del programa...")
			break
		else:
			print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()

