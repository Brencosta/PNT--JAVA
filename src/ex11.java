import javax.swing.*;
import java.util.Scanner;

public class ex11 {
    public static void main(String[] args) {
      String nome =  JOptionPane.showInputDialog(null, "digite seu usuário");
      String senha = JOptionPane.showInputDialog(null, "digite a senha");

      if(nome.equals(senha)){
          JOptionPane.showMessageDialog(null, "Error: usuario e senha iguais.");

      }
      else {
          JOptionPane.showMessageDialog(null,"Cadastro realizado com sucesso!");
      }


}}
