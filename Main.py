from Clases.Animal import Animal


mi_perro = Animal(
    nombre="Odie",
    peso=5,
    propietario="Dilan Carrasquilla",
    fecha_cumpleaños="07 julio 2020",
    fecha_ultima_vacuna="06 diciembre 2023"
)


print("Nombre:", mi_perro.nombre)
print("Peso:", mi_perro.peso, "KG")
print("Propietario:", mi_perro.propietario)
print("Cumpleaños:", mi_perro.fecha_cumpleaños)
print("Última vacuna:", mi_perro.fecha_ultima_vacuna)


mi_perro.nombre = "Rocky"
mi_perro.peso = 6
mi_perro.propietario = "Antonio Carrasquilla"
mi_perro.fecha_cumpleaños = "05 junio 2021"
mi_perro.fecha_ultima_vacuna = "14 agosto 2023"


print("\n--- Después de modificar con setters ---")
print("Nombre:", mi_perro.nombre)
print("Peso:", mi_perro.peso, "KG")
print("Propietario:", mi_perro.propietario)
print("Cumpleaños:", mi_perro.fecha_cumpleaños)
print("Última vacuna:", mi_perro.fecha_ultima_vacuna)
