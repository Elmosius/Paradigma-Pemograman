package P03g_Tugas_Pengulangan_Java_2272008_Elmosius_Suli;
// File : MinMax.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 
import java.util.*;
public class MinMax {
    public static void main(String[] args) {
        int n, i=0, bil;
        int min=9999, max=-9999;
        Scanner sc = new Scanner(System.in);

        System.out.print("Tentukan banyak bilangan : ");
        n = sc.nextInt();

        while(i<n){
            i++;
        }

        System.out.print("Masukkan suatu bilangan ke " + i + " : ");
        bil = sc.nextInt();

        System.out.println("bil ke " + i +
                            " = " + bil);
        
        if(bil > max){
            max = bil;
        }

        if(bil < min){
            min = bil;
        }

        System.out.println("Banyaknya bilangan  : " + n);
        System.out.println("Bilangan terbesar  : " + max);
        System.out.println("Bilangan terkecil  : " + min);

        sc.close();
    }
}
