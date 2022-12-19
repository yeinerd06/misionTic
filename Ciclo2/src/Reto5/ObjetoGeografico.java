package Reto5;



/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/**
 *
 * @author USUARIO
 */
public class ObjetoGeografico {

    private String municipio;
    private byte ID;

    public ObjetoGeografico(String municipio, byte ID) {
        this.municipio = municipio;
        this.ID = ID;
    }

    public String getMunicipio() {
        return municipio;
    }

    public void setMunicipio(String municipio) {
        this.municipio = municipio;
    }

    public byte getID() {
        return ID;
    }

    public void setID(byte ID) {
        this.ID = ID;
    }
}
