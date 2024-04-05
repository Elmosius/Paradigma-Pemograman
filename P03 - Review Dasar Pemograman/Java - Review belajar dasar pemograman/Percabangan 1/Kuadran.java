package P03f_Tugas_Percabangan_Java_2272008_Elmosius_Suli;
// File : Kuadran.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 

import java.util.*;
public class Kuadran {
    public static void main(String[] args) {
        int x = 0, y = 0;
        boolean alarm = false;
        Scanner sc = new Scanner(System.in);

        System.out.print("sumbu x : ");
        x = sc.nextInt();

        System.out.print("sumbu y : ");
        y = sc.nextInt();

        if (x < 0 && y > 0) {
            System.out.println("Kuadran 1");

        }
        else if (x>0 && y > 0 ){
            System.out.println("Kuadran 2");
        }
        else if (x>0 && y < 0 ){
            System.out.println("Kuadran 3");
        }
        else if (x<0 && y < 0 ){
            System.out.println("Kuadran 4");
        }else{
            System.out.println("di titik pusat");
        }
        sc.close();
    }
}
