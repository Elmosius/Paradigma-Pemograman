package P03f_Tugas_Percabangan_Java_2272008_Elmosius_Suli;
// File : AngkaHari.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 
import java.util.*;
public class AngkaHari {
    public static void main(String[] args) {
        int hari = 0;
        boolean salah = false;
        String nilaiOutput="";
        Scanner sc = new Scanner(System.in);

        System.out.print("Masukkan angka hari (1 - 7) : ");
        hari = sc.nextInt();

        // System.out.print("Hari ke " + hari + " adalah hari");
        nilaiOutput = "Hari ke " + hari + " adalah hari ";
        switch (hari) {
            case 1:
                // System.out.println("Senin");
                nilaiOutput += "Senin";
                break;
            case 2:
                // System.out.println("Selasa");
                nilaiOutput += "Selasa";
                break;
            case 3:
                // System.out.println("Rabu"); 
                nilaiOutput += "Rabu";
                break;
            case 4:
                // System.out.println("Kamis");
                nilaiOutput += "Kamis";
                break;
            case 5:
                // System.out.println("Jumat");
                nilaiOutput += "Jumat";
                break;
            case 6:
                // System.out.println("Sabtu");
                nilaiOutput += "Sabtu";
                break;
            case 7:
                // System.out.println("Minggu");
                nilaiOutput += "Minggu";
                break;
            default:
                // System.out.println("Hari tidak dikenali");
                nilaiOutput += "tidak dikenali";
                break;
        }
        System.out.print(nilaiOutput + '\n');
        sc.close();
    }
}
