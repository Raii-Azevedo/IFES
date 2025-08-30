import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o nome do aluno(a): ");
        String nome = scanner.nextLine(); // Leia o nome

        // Consuma a nova linha em branco
        scanner.nextLine();

        double[] notas = new double[3];

        for (int n = 0; n < 3; n++) {
            System.out.print("Digite a " + (n + 1) + "ª nota: ");
            String notaStr = scanner.next();
            double nota = Double.parseDouble(notaStr);

            while (nota < 0 || nota > 10) {
                System.out.println("Nota inválida. A nota deve estar entre 0 e 10.");
                System.out.print("Digite a " + (n + 1) + "ª nota: ");
                notaStr = scanner.next();
                nota = Double.parseDouble(notaStr);
            }
            notas[n] = nota;
        }

        double finalNota = 0;
        for (double nota : notas) {
            finalNota += nota;
        }

        // Bloco do boletim final
        if (finalNota >= 18) {
            System.out.println("O aluno " + nome + " está APROVADO com nota: " + finalNota);
        } else if (finalNota < 15) {
            System.out.println("O aluno " + nome + " está REPROVADO com nota: " + finalNota);
        } else {
            System.out.println("O aluno " + nome + " está em RECUPERAÇÃO com nota: " + finalNota);
        }
    }
}
