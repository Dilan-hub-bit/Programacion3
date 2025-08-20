from Clases.Animal import Animal


mi_perro = Animal(
    nombre="Odie",
    peso= 5,
    propietario="Dilan Carrasquilla",
    fecha_cumpleaños="07 julio 2020",
    fecha_ultima_vacuna="06 Diciembre 2023"
)


print("Nombre:", mi_perro.get_nombre())
print("Peso:", mi_perro.get_peso(),"KG")
print("Propietario:", mi_perro.get_propietario())
print("Cumpleaños:", mi_perro.get_fecha_cumpleaños())
print("Última vacuna:", mi_perro.get_fecha_ultima_vacuna())