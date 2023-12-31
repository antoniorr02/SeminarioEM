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
        result = subprocess.run(['python3', script_path ], check=True) # Unix-like systems
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
    subprocess.run(['python3', 'SmallAtacks.py', '100'])

    #Root Component
    submenu = tkinter.Toplevel(raiz)
    submenu.title("Small Atacks")
    submenu.geometry('500x310')
    submenu.resizable(False,False)

    #Buttons submenu
    botonB= tkinter.Button(submenu, text="Attacks 200M", width=50, height=2, command=lambda: subprocess.run(['python3', 'SmallAtacks.py', '200']))
    botonB.grid(row=1, column=3, columnspan=1, padx=35, pady=10)
    botonC= tkinter.Button(submenu, text="Attacks 300M", width=50, height=2, command=lambda: subprocess.run(['python3', 'SmallAtacks.py', '300']))
    botonC.grid(row=2, column=3, columnspan=1, padx=35, pady=10)
    botonD= tkinter.Button(submenu, text="Attacks 400M", width=50, height=2, command=lambda: subprocess.run(['python3', 'SmallAtacks.py', '400']))
    botonD.grid(row=3, column=3, columnspan=1, padx=35, pady=10)
    botonClose= tkinter.Button(submenu, text="Close", width=50, height=2, command=lambda: submenu.destroy())
    botonClose.grid(row=5, column=3, columnspan=1, padx=35, pady=10)


#Root Component
raiz = tkinter.Tk()
raiz.title("Danger theory applied to economics")
raiz.geometry('500x550')
raiz.resizable(False,False)

threads = []  # List to store the threads

#Buttons
boton1 = tkinter.Button(raiz, text="Real Exchange Rate", width=50, height=2, command=lambda: run_script('RealExchangeRate.py'))
boton1.grid(row=2, column=3, columnspan=1, padx=35, pady=10)
boton2 = tkinter.Button(raiz, text="International GPB Reserves", width=50, height=2, command=lambda: run_script('Reserves.py'))
boton2.grid(row=3, column=3, columnspan=1, padx=35, pady=10)
boton3 = tkinter.Button(raiz, text="Lineal Regresion", width=50, height=2, command=lambda: run_script('LinearRegresionReservesExchangeRate.py'))
boton3.grid(row=4, column=3, columnspan=1, padx=35, pady=10)
boton4 = tkinter.Button(raiz, text="Reserves Prediction", width=50, height=2, command=lambda: run_script('ReservesPredicted.py'))
boton4.grid(row=5, column=3, columnspan=1, padx=35, pady=10)
boton5= tkinter.Button(raiz, text="Fluctuation Band 2.25%", width=50, height=2, command=lambda: run_script('FluctuationBand.py'))
boton5.grid(row=6, column=3, columnspan=1, padx=35, pady=10)
boton6= tkinter.Button(raiz, text="Fluctuation Band 15%", width=50, height=2, command=lambda: run_script('FluctuationBand_15.py'))
boton6.grid(row=7, column=3, columnspan=1, padx=35, pady=10)
boton7= tkinter.Button(raiz, text="Small Attack 100M", width=50, height=2, command=small_atack)
boton7.grid(row=8, column=3, columnspan=1, padx=35, pady=10)
boton8= tkinter.Button(raiz, text="Close", width=50, height=2, command=stop)
boton8.grid(row=9, column=3, columnspan=1, padx=35, pady=10)

raiz.mainloop()
