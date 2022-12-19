package Reto5;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Yeida
 */
public class DensidadPoblacional extends ObjetoGeografico {

    public int cantHabitantes;

    public DensidadPoblacional(int cantHabitantes, byte ID, String municipio) {
        super(municipio, ID);
        this.cantHabitantes = cantHabitantes;
    }

    public byte afeccion() {
        if (cantHabitantes > 50000) {
            return 2;
        } else if (cantHabitantes > 10000) {
            return 1;
        } else {
            return 0;
        }
    }

    public int getCantHabitantes() {
        return cantHabitantes;
    }

    public void setCantHabitantes(int cantHabitantes) {
        this.cantHabitantes = cantHabitantes;
    }
}
