import java.util.Scanner;

public class ex04 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("informe a quilometragem rodada: ");
        double km = scanner.nextDouble();
        if(km<100){
            System.out.println("o valor a ser pago é R$90,00");
        }
        else{
            double adcional;
            adcional = (90 +km*12);
            System.out.println("o valor a ser pago é; "+ adcional);
        }
}}
