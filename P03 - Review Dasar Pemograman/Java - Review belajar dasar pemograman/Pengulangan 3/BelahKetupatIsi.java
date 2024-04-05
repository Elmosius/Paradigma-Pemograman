// File : BelahKetupatIsi.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 

import java.util.Scanner;
public class BelahKetupatIsi {
    public void bagianAtas(int N) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N - i ; j++) {
                System.out.print(" ");
            }
            for (int k = 0; k < 2 * i - 1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public void bagianTengah(int N) {
        for (int i = 0; i < 2*N-1; i++) {
            System.out.print("*");
        }
        System.out.println();
    }
    public void bagianBawah(int N) {
        for (int i = N - 2; i >= 0; i--) {
            for (int j = 0; j < N - i - 1; j++) {
                System.out.print(" ");
            }
            for (int k = 0; k < 2 * i + 1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int N;
        Scanner sc = new Scanner(System.in);
        System.out.print("N: ");
        N = sc.nextInt();

        BelahKetupatIsi d = new BelahKetupatIsi();
        d.bagianAtas(N);
        d.bagianTengah(N);
        d.bagianBawah(N);

        sc.close();
    }
}
