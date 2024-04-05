// File : JamPasir.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 

import java.util.Scanner;

public class JamPasir {

    public void bagianAtas(int N){
        for (int i = N - 1; i > 0; i--) {
            for (int j = 0; j < N - i ; j++) {
                System.out.print(" ");
            }
            for (int k = 0; k < 2 * i +1; k++) {
                if (k == 0 || k == 2 * i || i == N - 1) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
    
    public void bagianBawah(int N){
        int i,j,k;
        for(i=0;i < N;i++){
            for(j=0;j < N; j++){
                if(i+j < N){
                    System.out.print(" ");
                }
            }
            for(k=0; k<N*2; k++){
                if(k <= (2*i)){
                    System.out.print("*");
                }

            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int N;
        Scanner sc = new Scanner(System.in);
        System.out.print("N: ");
        N = sc.nextInt();

        JamPasir j = new JamPasir();
        j.bagianAtas(N);
        j.bagianBawah(N);

        sc.close();
    }
}
