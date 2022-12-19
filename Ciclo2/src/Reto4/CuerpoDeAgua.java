package Reto4;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Yeida
 */
public class CuerpoDeAgua extends ObjetoGeografico {

    private String nombre;
    private byte id_cuerpo_agua;
    private String tipoCuerpo;
    private String tipoAgua;
    private float IRCA;

    public CuerpoDeAgua(String nombre, byte id_cuerpo_agua, String municipio, String tipoCuerpo, String tipoAgua, float IRCA) {
        super(municipio);
        this.nombre = nombre;
        this.id_cuerpo_agua = id_cuerpo_agua;
        this.tipoCuerpo = tipoCuerpo;
        this.tipoAgua = tipoAgua;
        this.IRCA = IRCA;
    }


    public String getTipoCuerpo() {
        return tipoCuerpo;
    }

    public void setTipoCuerpo(String tipoCuerpo) {
        this.tipoCuerpo = tipoCuerpo;
    }

    public String getTipoAgua() {
        return tipoAgua;
    }

    public void setTipoAgua(String tipoAgua) {
        this.tipoAgua = tipoAgua;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
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

    public String entidad() {
        if (this.IRCA > 80) {
            return "GOBERNACION";
        } else if (this.IRCA > 35) {
            return "ALCALDIA";
        } else if (this.IRCA > 5) {
            return "PERSONA PRESTADORA";
        } else {
            return "CONTINUAR VIGILANCIA";
        }
    }
}
