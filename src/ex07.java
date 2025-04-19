import java.util.Scanner;
public class ex07 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe um número ímpar: ");
        int numero = scanner.nextInt();

        if (numero % 2 == 0) {
            System.out.println("O número fornecido não é ímpar.  forneça um número ímpar.");
        } else {
            int numeroAnterior = numero - 1;
            int numeroProximo = numero + 1;

            int quadradoAnterior = numeroAnterior * numeroAnterior;
            int quadradoProximo = numeroProximo * numeroProximo;

            int diferenca = quadradoProximo - quadradoAnterior;

            System.out.println("O quadrado do número anterior (" + numeroAnterior + ") é: " + quadradoAnterior);
            System.out.println("O quadrado do próximo número (" + numeroProximo + ") é: " + quadradoProximo);
            System.out.println("A diferença entre o quadrado do próximo e do anterior é: " + diferenca);
        }


    }
}

