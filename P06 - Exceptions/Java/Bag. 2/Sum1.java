// File  : Sum1.java
// Nama  : Elmosius Suli
// NRP   : 2272008
// Kelas : B
// Ket   : coba input: 1 3 a 5 b

import java.util.Scanner;
import java.util.InputMismatchException;

public class Sum1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            int sum = 0;

            for (int i = 0; i < 5; i++) {
                try {
                    System.out.print("Masukkan bilangan ke-" + (i + 1) + " : ");
                    int num = sc.nextInt();
                    
                    if (num < 0 || num > 100) {
                        throw new InvalidInputException("Input harus antara 0 dan 100.");
                    }
                    
                    sum += num;
                } catch (InputMismatchException ime) {
                    System.err.println("Salah satu input bukan bilangan bulat.");
                    sc.nextLine(); 
                    i--; 
                } catch (InvalidInputException iie) {
                    System.err.println(iie.getMessage());
                    i--; 
                }
            }

            System.out.println("Hasil penjumlahan: " + sum);
        } finally {
            sc.close();
        }
    }
}

class InvalidInputException extends Exception {
    public InvalidInputException(String message) {
        super(message);
    }
}