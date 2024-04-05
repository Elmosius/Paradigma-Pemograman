package P03f_Tugas_Percabangan_Java_2272008_Elmosius_Suli;
// File : AkarPersamaanKuadrat.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 
import java.util.*;
public class AkarPersamaanKuadrat {
    public static void main(String[] args) {
        int a, b, c, d;
        Scanner sc = new Scanner(System.in);

        System.out.println("Persamaan kuadrat: ax^2 + bx + c \n");
        System.out.print("Tentukan nilai a :");
        a = sc.nextInt();

        System.out.print("Tentukan nilai b :");
        b = sc.nextInt();

        System.out.print("Tentukan nilai c :");
        c = sc.nextInt();

        d = (int)(Math.pow(b,2)) - 4 * a * c;

        System.out.println("Persamaan: " + a + 
                            "x^2 + " + b + "x + " + c);
        System.out.println("Determinan: "+d );

        if(d>0){
            double x1 = ( -b + Math.sqrt(d) ) / (2 * a);
            double x2 = ( -b - Math.sqrt(d) ) / (2 * a);

            System.out.println("\tx1=" +x1);
            System.out.println("\tx2=" +x2);
        }
        else if(d==0){
            double x = ( -b + Math.sqrt(d) ) / (2 * a);

            System.out.println("Memiliki akar kembar," +
                                "yaitu:");
            System.out.println("\tx=" + x);
        }
        else{  //d<0
            System.out.println("Tidak memiliki akar");
        }
        sc.close();
    }
    
}
