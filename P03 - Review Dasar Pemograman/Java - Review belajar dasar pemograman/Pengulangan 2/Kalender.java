package P03g_Tugas_Pengulangan_Java_2272008_Elmosius_Suli;
// File : Kalender.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 
import java.util.*;
public class Kalender{
    public static void main(String[] args) {
        GregorianCalendar cal = new GregorianCalendar();
        int tgl, tglIni, blnIni, hariInMinggu;

        tglIni = cal.get(Calendar.DAY_OF_MONTH);
        blnIni = cal.get(Calendar.MONTH);
        System.out.println(cal.getTime() + "\n");

        cal.set(Calendar.DAY_OF_MONTH,1);
        hariInMinggu = cal.get(Calendar.DAY_OF_WEEK);
        System.out.println(" M  S   S   R   K   J   S");

        for(int i = Calendar.SUNDAY; i <= hariInMinggu; i++);{
            System.out.println("    ");
        }

        do{
            tgl = cal.get(Calendar.DAY_OF_MONTH);
            if(tgl<10){
                System.out.println(" ");
            }
            System.out.println(tgl);
            if(tgl==tglIni){
                System.out.println("* ");
            }
            else{
                System.out.println("  ");
            }
            if(hariInMinggu==Calendar.SATURDAY){
                System.out.println();
            }
            cal.add(Calendar.DAY_OF_MONTH,1);
            hariInMinggu=cal.get(Calendar.DAY_OF_WEEK);
        }while(cal.get(Calendar.MONTH) ==blnIni);
        System.out.println();
    }
}
