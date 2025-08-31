/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package herencia.java;
/**
 *
 * @author Delia
 */
public class Automovil extends Vehiculo {
    String marca;
    String modelo;
    double precio;

    public Automovil(String fechaFabricacion, String vinChasis, String vinMotor,
                     String marca, String modelo, double precio) {
        super(fechaFabricacion, vinChasis, vinMotor);
        this.marca = marca;
        this.modelo = modelo;
        this.precio = precio;
    }

    public String getMarca() {
        return marca;
    }

    public String getModelo() {
        return modelo;
    }

    public double getPrecio() {
        return precio;
    }

    public void mostrarDatos() {
        System.out.println(" Detalles del Automovil ");
        System.out.println("Fecha de Fabricacion: " + getFechaFabricacion());
        System.out.println("VIN Chasis: " + getVinChasis());
        System.out.println("VIN Motor: " + getVinMotor());
        System.out.println("Marca: " + getMarca());
        System.out.println("Modelo: " + getModelo());
        System.out.println("Precio: $" + getPrecio());
    }
}
