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

def small_atack():
    #Root Component
    submenu = tkinter.Toplevel(raiz)
    submenu.title("Small Atacks")
    submenu.geometry('500x350')
    submenu.resizable(False,False)

    #Buttons submenu
    botonA= tkinter.Button(submenu, text="Attacks 0.05", width=50, height=2, command=lambda: run_script('SmallAtacks.py'))
    botonA.grid(row=1, column=3, columnspan=1, padx=35, pady=10)
    botonB= tkinter.Button(submenu, text="Attacks 0.1", width=50, height=2, command=lambda: run_script('SmallAtacks.py'))
    botonB.grid(row=2, column=3, columnspan=1, padx=35, pady=10)
    botonC= tkinter.Button(submenu, text="Attacks 0.15", width=50, height=2, command=lambda: run_script('SmallAtacks.py'))
    botonC.grid(row=3, column=3, columnspan=1, padx=35, pady=10)
    botonD= tkinter.Button(submenu, text="Attacks 0.2", width=50, height=2, command=lambda: run_script('SmallAtacks.py'))
    botonD.grid(row=4, column=3, columnspan=1, padx=35, pady=10)
    botonClose= tkinter.Button(submenu, text="Close", width=50, height=2, command=lambda: submenu.destroy())
    botonClose.grid(row=5, column=3, columnspan=1, padx=35, pady=10)


#Root Component
raiz = tkinter.Tk()
raiz.title("Danger theory applied to economics")
raiz.geometry('500x480')
raiz.resizable(False,False)

threads = []  # List to store the threads

#Buttons
boton1 = tkinter.Button(raiz, text="Real Exchange Rate", width=50, height=2, command=lambda: run_script('RealExchangeRate.py'))
boton1.grid(row=2, column=3, columnspan=1, padx=35, pady=10)
boton2 = tkinter.Button(raiz, text="International GPB Reserves", width=50, height=2, command=lambda: run_script('Reserves.py'))
boton2.grid(row=3, column=3, columnspan=1, padx=35, pady=10)
boton3 = tkinter.Button(raiz, text="Lineal Regresion", width=50, height=2, command=lambda: run_script('LinearRegresionReservesExchangeRate.py'))
boton3.grid(row=4, column=3, columnspan=1, padx=35, pady=10)
boton4= tkinter.Button(raiz, text="Fluctuation Band 2.25%", width=50, height=2, command=lambda: run_script('FluctuationBand.py'))
boton4.grid(row=5, column=3, columnspan=1, padx=35, pady=10)
boton5= tkinter.Button(raiz, text="Fluctuation Band 15%", width=50, height=2, command=lambda: run_script('FluctuationBand_15.py'))
boton5.grid(row=6, column=3, columnspan=1, padx=35, pady=10)
boton6= tkinter.Button(raiz, text="Small Attacks", width=50, height=2, command=small_atack)
boton6.grid(row=7, column=3, columnspan=1, padx=35, pady=10)
boton6= tkinter.Button(raiz, text="Close", width=50, height=2, command=stop)
boton6.grid(row=8, column=3, columnspan=1, padx=35, pady=10)

raiz.mainloop()
