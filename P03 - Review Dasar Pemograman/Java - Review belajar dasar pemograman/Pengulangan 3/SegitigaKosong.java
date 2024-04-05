// File : SegitigaKosong.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 

import java.util.Scanner;

public class SegitigaKosong {
    public static void main(String[] args) {
        int N;
        Scanner sc = new Scanner(System.in);
        System.out.print("N: ");
        N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N - i - 1; j++) {
                System.out.print(" "); 
            }
            for (int k = 0; k < 2 * i + 1; k++) {
                if (k == 0 || k == 2 * i || i == N - 1) {
                    System.out.print("*"); 
                } else {
                    System.out.print(" "); 
                }
            }
            System.out.println(); 
        }
        sc.close();
    }
}
