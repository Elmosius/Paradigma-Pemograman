// File : Segitigaisi.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 
import java.util.*;
public class Segitigaisi {
    public static void main(String[] args) {
        int N,i,j,k;
        Scanner sc = new Scanner(System.in);
        System.out.print("N: ");
        N = sc.nextInt();

        for(i=0;i < N;i++){
            for(j=0;j < (N-1); j++){
                if(i+j < (N-1)){
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
}
