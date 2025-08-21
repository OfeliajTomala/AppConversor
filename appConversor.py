import tkinter as tk #Libreria  y submodulo que proporciona widgets con estilo moderno (botones, labels, etc.).
from tkinter import ttk, messagebox
import re  #Librería para expresiones regulares, útil para validar números según el sistema (decimal, binario, etc.).


class NumericConverter:
    def __init__(self, root):
        self.root = root #ventana principal
        self.root.title("Conversor de Sistemas Numéricos")
        self.root.geometry("600x500") #Define el tama;o de la ventana
        self.root.resizable(False, False) #Hace que la ventana no pueda cambiar de tamaño
        
        # Configurar el estilo
        self.setup_styles()
        
        # Variables
        self.input_system = tk.StringVar(value="Decimal") #Guarda el sistema numérico seleccionado, inializamos el sistema con decimal
        self.input_number = tk.StringVar() #Guarda el número que el usuario ingresa.
        
        # Crear la interfaz
        self.create_interface()
        
        # Vincular eventos solo para el cambio de sistema
        self.input_system.trace('w', self.on_system_change)
        
    def setup_styles(self):
        """Configurar estilos para la aplicación"""
        self.root.configure(bg='#f0f0f0')
        
        # Crear un estilo personalizado para los widgets
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar colores
        style.configure('Title.TLabel', 
                       font=('Arial', 16, 'bold'),
                       background='#f0f0f0',
                       foreground="#0d60b3")
        
        style.configure('Subtitle.TLabel',
                       font=('Arial', 12, 'bold'),
                       background='#f0f0f0',
                       foreground="#5815aa")
        
        style.configure('Result.TLabel',
                       font=('Arial', 11),
                       background='#f0f0f0',
                       foreground='#2c3e50')
    
    def create_interface(self):
        """Crear la interfaz gráfica"""
        # Frame(contenedor) principal 
        main_frame = tk.Frame(self.root, bg='#f0f0f0', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Título
        title_label = ttk.Label(main_frame, 
                               text="Conversor de Sistemas Numéricos",
                               style='Title.TLabel')
        title_label.pack(pady=(0, 20))
        
        # Frame de entrada
        input_frame = tk.Frame(main_frame, bg='#f0f0f0')
        input_frame.pack(fill='x', pady=(0, 20))
        
        # Selección del sistema de entrada
        ttk.Label(input_frame, 
                 text="Sistema de entrada:",
                 style='Subtitle.TLabel').pack(anchor='w')
        
        system_frame = tk.Frame(input_frame, bg='#f0f0f0')
        system_frame.pack(fill='x', pady=(5, 10))
        
        # Radio buttons para seleccionar el sistema
        systems = ["Decimal", "Binario", "Octal", "Hexadecimal"]
        for system in systems:
            rb = tk.Radiobutton(system_frame,
                               text=system,
                               variable=self.input_system, #Cada botón actualiza la variable.
                               value=system,
                               bg='#f0f0f0',
                               font=('Arial', 10),
                               command=self.on_system_change)  #Actualiza el texto de ayuda al cambia
            rb.pack(side='left', padx=(0, 20))
        
        # Campo de entrada
        ttk.Label(input_frame,
                 text="Número a convertir:",
                 style='Subtitle.TLabel').pack(anchor='w', pady=(10, 0))
        #Campo de texto donde se ingresa el numero
        self.entry = tk.Entry(input_frame,
                             textvariable=self.input_number,
                             font=('Arial', 12),
                             width=30)
        self.entry.pack(pady=(5, 0), fill='x')
        
        # Permite que al presionar Enter se haga la conversión.
        self.entry.bind('<Return>', lambda event: self.convert_number())
        
        # Label de ayuda,Muestra instrucciones o mensajes de error debajo del Entry.
        self.help_label = tk.Label(input_frame,
                                  text="Ingrese un número decimal (0-9) y presione Convertir",
                                  font=('Arial', 9),
                                  bg='#f0f0f0',
                                  fg='#7f8c8d')
        self.help_label.pack(anchor='w', pady=(2, 0))
        
        # Frame de resultados
        results_frame = tk.Frame(main_frame, bg='#f0f0f0')
        results_frame.pack(fill='both', expand=True, pady=(20, 0))
        
        ttk.Label(results_frame,
                 text="Resultados de conversión:",
                 style='Subtitle.TLabel').pack(anchor='w', pady=(0, 15))
        
        # Crear campos de resultado
        self.create_result_fields(results_frame)
        
        # Botones
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(fill='x', pady=(20, 0))
        
        # Botón limpiar
        clear_button = tk.Button(button_frame,
                               text="Limpiar",
                               command=self.clear_all,
                               bg='#e74c3c',
                               fg='white',
                               font=('Arial', 10, 'bold'),
                               padx=20,
                               pady=5)
        clear_button.pack(side='right', padx=(10, 0))
        
        # Botón convertir
        convert_button = tk.Button(button_frame,
                                 text="Convertir",
                                 command=self.convert_number,
                                 bg='#3498db',
                                 fg='white',
                                 font=('Arial', 10, 'bold'),
                                 padx=20,
                                 pady=5)
        convert_button.pack(side='right')
    
    def create_result_fields(self, parent):
        """Crear los campos de resultado"""
        self.result_vars = {}
        self.result_entries = {}
        
        systems = [
            ("Decimal", "#182263"),
            ("Binario", "#ea0f1a"), 
            ("Octal", "#4f1667"),
            ("Hexadecimal", "#128ddf")
        ]
        
        for system, color in systems:
            # Frame para cada resultado
            result_frame = tk.Frame(parent, bg='#f0f0f0')
            result_frame.pack(fill='x', pady=5)
            
            # Label del sistema
            label = tk.Label(result_frame,
                           text=f"{system}:",
                           font=('Arial', 11, 'bold'),
                           bg='#f0f0f0',
                           fg=color,
                           width=12,
                           anchor='w')
            label.pack(side='left')
            
            # Variable y entrada para el resultado
            var = tk.StringVar()
            self.result_vars[system] = var
            
            entry = tk.Entry(result_frame,
                           textvariable=var,
                           font=('Arial', 11),
                           state='readonly',
                           width=40)
            entry.pack(side='left', fill='x', expand=True, padx=(10, 0))
            self.result_entries[system] = entry
    
    def on_system_change(self, *args):
        """Manejar el cambio de sistema de entrada"""
        system = self.input_system.get()
        help_texts = {
            "Decimal": "Ingrese un número decimal (0-9) y presione Convertir",
            "Binario": "Ingrese un número binario (0-1) y presione Convertir",
            "Octal": "Ingrese un número octal (0-7) y presione Convertir",
            "Hexadecimal": "Ingrese un número hexadecimal (0-9, A-F) y presione Convertir"
        }
        self.help_label.config(text=help_texts[system])
        # No limpiar resultados automáticamente, solo cambiar el texto de ayuda
    

    def validate_input(self, number, system):
        """Validar que el número sea válido para el sistema especificado"""
        if not number:
            return False, "Por favor ingrese un número"
        
        try:
            if system == "Decimal":
                # Permitir números decimales positivos y negativos
                if re.match(r'^-?\d+$', number):
                    return True, ""
                else:
                    return False, "Número decimal inválido"
            
            elif system == "Binario":
                # Solo 0s y 1s
                if re.match(r'^[01]+$', number):
                    return True, ""
                else:
                    return False, "Número binario inválido (solo 0 y 1)"
            
            elif system == "Octal":
                # Solo dígitos 0-7
                if re.match(r'^[0-7]+$', number):
                    return True, ""
                else:
                    return False, "Número octal inválido (solo 0-7)"
            
            elif system == "Hexadecimal":
                # Dígitos 0-9 y letras A-F (mayúsculas o minúsculas)
                if re.match(r'^[0-9A-Fa-f]+$', number):
                    return True, ""
                else:
                    return False, "Número hexadecimal inválido (0-9, A-F)"
            
        except Exception as e:
            return False, f"Error de validación: {str(e)}"
        
        return False, "Sistema no reconocido"
    
    def convert_to_decimal(self, number, from_system):
        """Convertir cualquier sistema a decimal"""
        try:
            if from_system == "Decimal":
                return int(number)
            elif from_system == "Binario":
                return int(number, 2)
            elif from_system == "Octal":
                return int(number, 8)
            elif from_system == "Hexadecimal":
                return int(number, 16)
        except ValueError:
            raise ValueError(f"No se puede convertir '{number}' desde {from_system}")
    
    def convert_from_decimal(self, decimal_num):
        """Convertir desde decimal a todos los sistemas"""
        try:
            return {
                "Decimal": str(decimal_num),
                "Binario": bin(decimal_num)[2:] if decimal_num >= 0 else bin(decimal_num),
                "Octal": oct(decimal_num)[2:] if decimal_num >= 0 else oct(decimal_num),
                "Hexadecimal": hex(decimal_num)[2:].upper() if decimal_num >= 0 else hex(decimal_num).upper()
            }
        except Exception as e:
            raise ValueError(f"Error en conversión: {str(e)}")
    
    def convert_number(self):
        """Realizar la conversión del número"""
        number = self.input_number.get().strip()
        system = self.input_system.get()
        
        # Si no hay entrada, mostrar mensaje
        if not number:
            self.show_error("Por favor ingrese un número")
            self.clear_results()
            return
        
        # Validar entrada
        is_valid, error_msg = self.validate_input(number, system)
        if not is_valid:
            self.show_error(error_msg)
            self.clear_results()
            return
        
        try:
            # Convertir a decimal primero
            decimal_value = self.convert_to_decimal(number, system)
            
            # Convertir a todos los sistemas
            conversions = self.convert_from_decimal(decimal_value)
            
            # Mostrar resultados
            for target_system, result in conversions.items():
                if target_system != system:  # No mostrar el sistema de entrada
                    self.result_vars[target_system].set(result)
                else:
                    self.result_vars[target_system].set(f"{result} (entrada)")
            
            # Limpiar cualquier mensaje de error
            self.clear_error()
            
        except ValueError as e:
            self.show_error(str(e))
            self.clear_results()
        except Exception as e:
            self.show_error(f"Error inesperado: {str(e)}")
            self.clear_results()
    
    def clear_results(self):
        """Limpiar todos los resultados"""
        for var in self.result_vars.values():
            var.set("")
    
    def clear_all(self):
        """Limpiar todo"""
        self.input_number.set("")
        self.clear_results()
        self.clear_error()
        self.entry.focus()
    
    def show_error(self, message):
        """Mostrar mensaje de error"""
        self.help_label.config(text=f"Error: {message}", fg='#e74c3c')
    
    def clear_error(self):
        """Limpiar mensaje de error"""
        system = self.input_system.get()
        help_texts = {
            "Decimal": "Ingrese un número decimal (0-9) y presione Convertir",
            "Binario": "Ingrese un número binario (0-1) y presione Convertir",
            "Octal": "Ingrese un número octal (0-7) y presione Convertir",
            "Hexadecimal": "Ingrese un número hexadecimal (0-9, A-F) y presione Convertir"
        }
        self.help_label.config(text=help_texts[system], fg='#7f8c8d')


def main():
    """Función principal"""
    root = tk.Tk()
    app = NumericConverter(root)
    
    # Centrar la ventana
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()


if __name__ == "__main__":
    main()