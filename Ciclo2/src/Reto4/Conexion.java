package Reto4;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import javax.swing.JOptionPane;

/**
 *
 * @author Yeida
 */
public class Conexion {

    String nombreBD = "jdbc:sqlite:Reto4.s3db";
    Connection cn = null;

    public String conectar() {

        try {
            Class.forName("org.sqlite.JDBC");
            cn = DriverManager.getConnection(nombreBD);

            return "Conexion Realizada Satisfactoriamente.";
        } catch (Exception e) {
            return "Error al Conectar la base de datos\n" + e;
        }
    }

    public String desconectar() {

        try {
            cn.close();
            return "Desconexion Realizada Satisfactoriamente.";
        } catch (Exception e) {
            return "Error al Desonectar la base de datos\n" + e;
        }
    }

    /**
     * Recibe un booleano
     *
     * true___ insert, update, delete
     *
     * false___ consult select
     *
     * @param instruccion
     * @param op
     * @return
     */
    public ResultSet ejecutar(String instruccion, boolean op) {
        ResultSet rs = null;
        try {
            PreparedStatement ps = cn.prepareStatement(instruccion);
            if (op) {
                ps.execute();
            } else {
                rs = ps.executeQuery();
            }
        } catch (Exception e) {
            System.out.println(e);
        }
        return rs;
    }

}
