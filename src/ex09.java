import java.util.Scanner;

public class ex09 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println(" Digite 3 numeros: ");
        double num1 = scanner.nextDouble();
        double num2 = scanner.nextDouble();
        double num3 = scanner.nextDouble();

        if(num1>= num2 && num1>=num3) {
            System.out.println("O numero maior é: "+ num1);
        } else if (num2>=num1 && num2>=num3) {
            System.out.println("O numero maior é: "+ num2);
        }
    else {
            System.out.println("O numero maior é: "+ num3);
        }

    if(num1<=num2 && num1<=num3){
        System.out.println("O numero menor é: "+ num1);
    } else if (num2<=num1 && num2<= num3) {
        System.out.println("O numero menor é: "+ num2);


    } else {
        System.out.println("O numero menor é: "+ num3);
    }
    }}
