import java.util.Scanner;

public class ex08 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println(" Digite a temperatura em celsius: ");
        double temp = scanner.nextDouble();
        double farenheit;
        farenheit = (9*(temp) +160)/5;
        System.out.println(" A tempratura em farenheit é:" + farenheit);
}}
