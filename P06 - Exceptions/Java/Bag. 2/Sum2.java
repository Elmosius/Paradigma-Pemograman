// File  : Sum2.java
// Nama  : Elmosius Suli
// NRP   : 2272008
// Kelas : B
// Ket   : coba input: 1 3 a 5 b

import java.util.InputMismatchException;
import java.util.Scanner;

public class Sum2 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        int sum = 0;
        System.out.println("Masukkan Bilangan 0 sampai 100");
        for (int i = 0; i < 5; i++) {
            System.out.print("Masukkan bilangan ke-" + (i + 1) + " : ");
            String str = sc.next();

            try {
                int num = Integer.parseInt(str);

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
                i--; // Coba lagi pada iterasi yang sama
            } catch (NumberFormatException nfe) {
                System.out.println("\nArgumen [" + str + "] bukan integer!");
            }
        }

        System.out.println("Hasil penjumlahan: " + sum);

        sc.close();
    }
}

class InvalidInputException extends Exception {
    public InvalidInputException(String message) {
        super(message);
    }
}

