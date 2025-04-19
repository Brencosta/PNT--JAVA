import java.util.Scanner;

public class ex03 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o valor total da compra: ");

        double total = scanner.nextDouble();
        double imposto =0;
        if (total<500){
            System.out.println(" não há impostos.");
        }
    else{
        imposto = total*0.5;
        double imposto2 = (total + imposto);
        System.out.println("o valor final com impostos foi de: " + imposto2);

        }
    }
}
