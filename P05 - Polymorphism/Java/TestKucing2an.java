package Praktikum.P05.P05b_Latihan_Polymorphism_Java_2272008_Elmosius_Suli;
// File : TestKucing2an.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class TestKucing2an {
    public static void main(String[] args) {
        // method overriding
        Kucing k1 = new Kucing();
        KucingKecil k2 = new KucingKecil();
        KucingBesar k3 = new KucingBesar();
        Harimau k4 = new Harimau();
        
        
        System.out.println("Beginilah kalau kucing2 bersuara bersamaan : ");
        System.out.println(k1.bersuara());
        System.out.println(k2.bersuara());
        System.out.println(k3.bersuara());
        System.out.println(k4.bersuara());

        // virtual method invocation (polymorphism)
        Kucing k5 = new KucingKecil();
        Kucing k6 = new KucingBesar();
        Kucing k7 = new Harimau();
        //  KucingBesar k8 = new KucingKecil();  //incompatible types, komentarin aja ya
        Kucing k9 = new Harimau();
        //  KucingBesar k10 = new Kucing();  //incompatible types, komentarin aja ya

        System.out.println("\n Semua yg mengaku sebagai kucing, sebutkan nama masin2 : ");
        System.out.println(k5.bersuara());
        System.out.println(k6.bersuara());
        System.out.println(k7.bersuara());
        // System.out.println(k8.bersuara());  //error, komentarin aja ya
        System.out.println(k9.bersuara());      //error, komentarin aja ya
        // System.out.println(k10.bersuara());


        // Penggunaan instanceof dan polymorphic arguments
        KucingDijual j = new KucingDijual();
        System.out.println("\nDijual macam2 kucing, silahkan pilih : ");
        System.out.println("Jenis : " + k1.cekJenis(k1) + ", umur : " + j.CekUmur(k1)
        + ", harga : " + j.cekHarga(k1));
         System.out.println("Jenis : " + k1.cekJenis(k2) + ", umur : " + j.CekUmur(k2)
        + ", harga : " + j.cekHarga(k2));
         System.out.println("Jenis : " + k1.cekJenis(k3) + ", umur : " + j.CekUmur(k1)
        + ", harga : " + j.cekHarga(k3));
         System.out.println("Jenis : " + k1.cekJenis(k4) + ", umur : " + j.CekUmur(k1)
        + ", harga : " + j.cekHarga(k4));

        System.out.println("\nDijual macam2 kucing polymorphism, silahkan pilih : ");
         System.out.println("Jenis : " + k1.cekJenis(k5) + ", umur : " + j.CekUmur(k5)
        + ", harga : " + j.cekHarga(k5));
         System.out.println("Jenis : " + k1.cekJenis(k6) + ", umur : " + j.CekUmur(k1)
        + ", harga : " + j.cekHarga(k6));
         System.out.println("Jenis : " + k1.cekJenis(k7) + ", umur : " + j.CekUmur(k1)
        + ", harga : " + j.cekHarga(k7));
         System.out.println("Jenis : " + k1.cekJenis(k9) + ", umur : " + j.CekUmur(k1)
        + ", harga : " + j.cekHarga(k9));
    
    
    }
}
