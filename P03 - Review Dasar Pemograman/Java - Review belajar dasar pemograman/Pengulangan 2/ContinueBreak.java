package P03g_Tugas_Pengulangan_Java_2272008_Elmosius_Suli;
// File : ContinueBreak.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 
import java.util.*;
public class ContinueBreak {
    public static void main(String[] args) {
        for(int i=1; i<=12; i++){
            if(i%2==0){
                continue;
            }
            if(i == 11){
                break;
            }
            System.out.println(i);
        }
    }
}
