package Praktikum.P02;
import java.util.Scanner;

public class TestHandPhone {
    public static void main(String[] args){
        HandPhone hp = new HandPhone();
        Scanner sc = new Scanner(System.in);
        String wrn;
        String no;

        System.out.print("Warna casing HP Anda : ");
        wrn = sc.next();
        hp.setWarnaCasing(wrn);
        System.out.print("No HP Anda : ");
        no = sc.next();
        hp.setNomor(no);

        String hslWarna, hslNomor;
        hslWarna = hp.getWarnaCasing();
        hslNomor = hp.getNomor();
        System.out.println("Warna casing HP Anda : " + hslWarna);
        System.out.println("Nomor HP Anda        : " + hslNomor);

        sc.close();
    }
}
