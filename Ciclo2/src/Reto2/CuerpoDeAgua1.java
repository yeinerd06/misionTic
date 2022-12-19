package Reto2;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Yeida
 */
public class CuerpoDeAgua1 {

    private String nombre;
    private String municipio;
    private byte id_cuerpo_agua;
    private float IRCA;

    public CuerpoDeAgua1() {
    }

    public CuerpoDeAgua1(String nombre, String municipio, byte id_cuerpo_agua, float IRCA) {
        this.nombre = nombre;
        this.municipio = municipio;
        this.id_cuerpo_agua = id_cuerpo_agua;
        this.IRCA = IRCA;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getMunicipio() {
        return municipio;
    }

    public void setMunicipio(String municipio) {
        this.municipio = municipio;
    }

    public byte getId_cuerpo_agua() {
        return id_cuerpo_agua;
    }

    public void setId_cuerpo_agua(byte id_cuerpo_agua) {
        this.id_cuerpo_agua = id_cuerpo_agua;
    }

    public float getIRCA() {
        return IRCA;
    }

    public void setIRCA(float IRCA) {
        this.IRCA = IRCA;
    }

    public String nivel() {
        if (this.IRCA > 80) {
            return "INVIABLE SANITARIAMENTE";
        } else if (this.IRCA > 35) {
            return "ALTO";
        } else if (this.IRCA > 14) {
            return "MEDIO";
        } else if (this.IRCA > 5) {
            return "BAJO";
        } else {
            return "SIN RIESGO";
        }
    }
}
