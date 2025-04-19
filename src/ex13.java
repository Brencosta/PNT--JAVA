import java.util.Scanner;

public class ex13 {

        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            System.out.println("Informe o salário inicial: ");
            double salarioInicial = scanner.nextDouble();

            System.out.println("Informe o aumento percentual inicial (em %): ");
            double aumentoPercentual = scanner.nextDouble();

            System.out.println("Informe o número de anos: ");
            int anos = scanner.nextInt();

            aumentoPercentual = aumentoPercentual / 100;

            double salarioAtual = salarioInicial;
            for (int i = 1; i <= anos; i++) {
                salarioAtual += salarioAtual * aumentoPercentual;
                aumentoPercentual *= 2;
            }

            System.out.println("O salário após " + anos + " anos é: R$ " + String.format("%.2f", salarioAtual));


        }
    }


