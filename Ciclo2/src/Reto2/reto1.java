package Reto2;


import java.util.Scanner;

public class reto1 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String tam = sc.nextLine();
        int prom = 0, alto = 0;
        int[] represa = new int[Integer.parseInt(tam)];
        for (int x = 0; x < represa.length; x++) {
            represa[x] = Integer.parseInt(sc.nextLine());
        }
        for (int x : represa) {
            prom += x;
            if (x > alto) {
                alto = x;
            }
        }
        int bajo = alto;
        for (int x : represa) {
            if (x < bajo) {
                bajo = x;
            }
        }
        prom = prom / represa.length;
        System.out.println(enontrarRiesgo(prom));
        System.out.println(enontrarRiesgo(alto));
        System.out.println(enontrarRiesgo(bajo));
    }

    private static String enontrarRiesgo(int valor) {
        if (valor > 80) {
            return "INVIABLE SANITARIAMENTE";
        } else if (valor > 35) {
            return "ALTO";
        } else if (valor > 14) {
            return "MEDIO";
        } else if (valor > 5) {
            return "BAJO";
        } else {
            return "SIN RIESGO";
        }
    }
}
