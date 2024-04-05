package Praktikum.P02;
import java.util.Scanner;

public class Sepeda {
    public String merk;
    public String tipe;
    public int gigi_sekarang;
    public int kecepatan;
    
    public Sepeda(int gigi_sekarang, int kecepatan){
        this.gigi_sekarang = gigi_sekarang;
        this.kecepatan = kecepatan;
    }

    public void setMerk(String merk){
        this.merk = merk;
    }

    public void setTipe(String tipe){
        this.tipe = tipe;
    }

    public void naikkanGigi(){
        this.gigi_sekarang += 1;
    }

    public void turunkanGigi(){
        this.gigi_sekarang -= 1;
    }

    public void tambahKecepatan(int tambah){
        this.kecepatan += tambah;
    }

    public void rem(int kurangi){
        this.kecepatan -= kurangi;
    }

    public void tampilkan(){
        System.out.printf("\nSuatu hari kamu sedang menaiki sepeda dengan merk %s dengan tipe %s \n",  this.merk, this.tipe);
    }

    public static void main(String[] args) {
        Sepeda s1 = new Sepeda(2, 30);
        Scanner sc = new Scanner(System.in);
        
        String merk, tipe, pil;
        int kec;
        Boolean cond = false;
              
        System.out.print("Merk sepeda anda   : ");
        merk = sc.nextLine();
        s1.setMerk(merk);

        System.out.print("Tipe Sepeda        : ");
        tipe = sc.nextLine();
        s1.setTipe(tipe);


        s1.tampilkan();
        System.out.printf(",kamu sedang melaju dengan kecepatan %s km/jam dengan gigi %s\n",  s1.kecepatan, s1.gigi_sekarang);
        System.out.println("Apa yang ingin kamu lakukan? : \n");

        while (!cond) {
            System.out.print("Naikan Kecepatan (Y) / Rem (N)  : ");
            pil = sc.next();
        
            if(pil.equals("Y")){
                System.out.print("Naikan Kecepatan : ");
                kec = sc.nextInt();
                s1.tambahKecepatan(kec);
            }
            else{
                System.out.print("Rem : ");
                kec = sc.nextInt();
                s1.rem(kec);
            }

            if(s1.kecepatan == 0){
                cond = true;
            }
            else{
                System.out.printf("\nKecepatan sekarang : %s km/jam dengan Gigi %s  \n",  s1.kecepatan, s1.gigi_sekarang);
                System.out.print("Naikan Gigi (Y) / Turun (N)  : ");
                pil = sc.next();

                if(pil.equals("Y")){
                    s1.naikkanGigi();
                }
                else{
                    s1.turunkanGigi();
                }

                System.out.printf("\nKecepatan sekarang : %s km/jam dengan Gigi %s  \n",  s1.kecepatan, s1.gigi_sekarang);
            }
            System.out.println("Sepedamu sudah berhenti");    
        }
        
        sc.close();
    }
    
    
           
    
}
