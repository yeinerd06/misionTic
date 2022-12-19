package Reto2;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Yeida
 */
import java.util.Scanner;

public class reto2 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String cant = sc.nextLine(), nombres = "";
        int prom = 0, alto = 0;
        byte cante = Byte.parseByte(cant), medioInferior = 0;
        String[] represa = new String[cante];

        for (int x = 0; x < represa.length; x++) {
            represa[x] = sc.nextLine();
        }

        CuerpoDeAgua1 cuerpos[] = crearSistema(represa, cante);
        CuerpoDeAgua1 menor = cuerpos[0];
        for (CuerpoDeAgua1 cuerpo : cuerpos) {
            System.out.println(cuerpo.nivel());

            if ("MEDIO".equals(cuerpo.nivel())) {
                nombres += cuerpo.getNombre() + " ";
            }
            if (menor.getIRCA() > cuerpo.getIRCA()) {
                menor = cuerpo;
            }
            if (cuerpo.getIRCA() <= 35) {
                medioInferior++;
            }
        }
        System.out.println(medioInferior);
        System.out.println(nombres);
        System.out.println(menor.getNombre() + " " + menor.getId_cuerpo_agua());
    }

    private static CuerpoDeAgua1[] crearSistema(String[] represa, byte cante) {
        CuerpoDeAgua1 cuerpos[] = new CuerpoDeAgua1[cante];
        for (int i = 0; i < cante; i++) {
            cuerpos[i] = new CuerpoDeAgua1();
        }
        for (int i = 0; i < cante; i++) {
            String datoCuerpo[] = represa[i].split(" ");
            String nombre = datoCuerpo[0];
            byte id = Byte.parseByte(datoCuerpo[1]);
            String municipio = datoCuerpo[2];
            float irca = Float.parseFloat(datoCuerpo[3]);
            cuerpos[i] = new CuerpoDeAgua1(nombre, municipio, id, irca);
        }
        return cuerpos;
    }
}
