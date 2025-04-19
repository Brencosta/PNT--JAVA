import java.util.Scanner;

public class ex02 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digiite os segundos que sera convertido: ");
        double segundos = scanner.nextDouble();
        double minutos;
        minutos = (segundos/60);
        System.out.println("segundos para minutos: "+ minutos);

        double horas;
       horas = (minutos/60);
        System.out.println("minutos  para horas : "+ horas );

        double dia;
        dia = (horas/24);
        System.out.println("horas  para dias : "+ dia );

}}
