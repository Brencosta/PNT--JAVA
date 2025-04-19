import java.util.Scanner;

public class ex01 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite as 3 notas:");
        double num1 = scanner.nextDouble();
        double num2 = scanner.nextDouble();
        double num3 = scanner.nextDouble();
        double media;
        media = (num1+num2+num3)/3;
        System.out.println("A média aritimética de 3 números são: "+ media);

        double mediapond;
        mediapond = (num1*2+num2*2 +num3*3)/3;
        System.out.println("A média ponderada é: "+mediapond);

        mediapond = (num1*1+num2*2 +num3*2)/3;
        System.out.println("A média ponderada é: "+mediapond);
    }
}