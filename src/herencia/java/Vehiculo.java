/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package herencia.java;
/**
 *
 * @author Delia
 */
public class Vehiculo {
    
    String fechaFabricacion;
    String vinChasis;
    String vinMotor;

    public Vehiculo(String fechaFabricacion, String vinChasis, String vinMotor) {
        this.fechaFabricacion = fechaFabricacion;
        this.vinChasis = vinChasis;
        this.vinMotor = vinMotor;
    }

    public String getFechaFabricacion() {
        return fechaFabricacion;
    }

    public String getVinChasis() {
        return vinChasis;
    }

    public String getVinMotor() {
        return vinMotor;
    }
}    
