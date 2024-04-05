package Praktikum.P05.P05b_Latihan_Polymorphism_Java_2272008_Elmosius_Suli;
// File : KucingDijual.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class KucingDijual {
    public int CekUmur(Kucing miau){
        // semua umur 3 bulan
        return(3);
    }

    public int cekHarga(Kucing miau){
        int harga = 0;

        if(miau instanceof Harimau){
            harga = 90000;
        }else if(miau instanceof KucingBesar){
            harga = 50000;
        }else if(miau instanceof KucingKecil){
            harga = 20000;
        }else if(miau instanceof Kucing)
            harga = 15000;
        return harga;
    }
}
