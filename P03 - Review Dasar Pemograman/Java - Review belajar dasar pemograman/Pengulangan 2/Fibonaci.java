package P03g_Tugas_Pengulangan_Java_2272008_Elmosius_Suli;
// File : Fibonaci.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 
import java.util.*;
public class Fibonaci {
    public static void main(String[] args) {
        int a=1, b=1, fibo = 1, n;
        Scanner sc = new Scanner(System.in);

        System.out.print("Tentukan banyak bilangan : ");
        n = sc.nextInt();

        for(int i=1; i<=n; i++){
            if(i <= 2){
                System.out.print("1 ");
            }else{
                fibo = a + b;
                System.out.print(fibo + " ");
                a = b;
                b = fibo;
            }
        }
        sc.close();
    }
}
