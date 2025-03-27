import java.util.Scanner;

public class ex06 {
    public static void main(String[] args) {
        int contador = 0;
        int numero = 2;
        while (contador < 100) {
            boolean primo = true;

            for (int i = 2; i <= Math.sqrt(numero); i++) {
                if (numero % i == 0) {
                    primo = false;
                    break;
                        }
                    }

                    if (primo) {
                        System.out.print(numero + " ");
                        contador++;
                    }

                    numero++;
                }
            }
        }

