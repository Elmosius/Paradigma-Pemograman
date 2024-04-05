package P03g_Tugas_Pengulangan_Java_2272008_Elmosius_Suli;
import java.text.NumberFormat;
// File : TabelPerkalian.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 
import java.util.*;
import java.text.*;
public class TabelPerkalian {
    public static void main(String[] args) {
        int n, i, j, hasil;
        Scanner sc= new Scanner(System.in);

        System.out.print("Ukuran tabel : ");
        n = sc.nextInt();

        NumberFormat formatAngka = NumberFormat.getNumberInstance();
        formatAngka.setMinimumIntegerDigits(2);
        
        for(i =1; i<=n; i++){
            for(j=1; j<=n; j++){
                hasil = 1*j;
                System.out.print(" " + formatAngka.format(hasil) + " ");
            }
            System.out.println();
        }
    }
}
