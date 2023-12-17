import tkinter
import subprocess
import threading

def stop():
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    raiz.destroy()
    
def execute_script(script_path):
    try:
        result = subprocess.run(['python3', script_path], check=True) # Unix-like systems
        # OR
        # subprocess.run(['python.exe', script_path], check=True)  # Windows
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Function to run a script when a button is clicked
def run_script(script_path):
    # Run the script in a separate thread
    thread = threading.Thread(target=execute_script, args=(script_path,))
    thread.start()
    threads.append(thread)

#Componente raíz
raiz = tkinter.Tk()
raiz.title("Danger theory applied to economics")
raiz.geometry('500x200')
raiz.resizable(False,False)

threads = []  # List to store the threads

#Botones
boton1 = tkinter.Button(raiz, text="Real Exchange Rate", width=50, height=2, command=lambda: run_script('RealExchangeRate.py'))
boton1.grid(row=2, column=3, columnspan=1, padx=35, pady=10)
boton2 = tkinter.Button(raiz, text="International GPB Reserves", width=50, height=2, command=lambda: run_script('Reserves.py'))
boton2.grid(row=3, column=3, columnspan=1, padx=35, pady=10)
boton4= tkinter.Button(raiz, text="Close", width=50, height=2, command=stop)
boton4.grid(row=4, column=3, columnspan=1, padx=35, pady=10)

raiz.mainloop()
