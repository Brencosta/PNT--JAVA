import java.util.Scanner;

public class ex12 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Informe a quantidade de turmsas: ");
        double turma = scanner.nextInt();

        System.out.println("Informe a quantidade de aluno por turma: ");
        double aluno = scanner.nextInt();
        double media = (double) (turma/aluno);
        if (turma>=40){
            System.out.println("Turma maior que 40");

        }
        System.out.println("A media de aluno por turma é: "+media);


}}
