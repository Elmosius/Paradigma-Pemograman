package Praktikum.P05.P05b_Latihan_Polymorphism_Java_2272008_Elmosius_Suli;
// File : Manusia.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class Manusia {
    protected String nama;
    protected int umur;
    protected int tinggi;

    // buat konstuktor2 di ini (tambahin lagi ya...)
    public Manusia(String pnama, int pumur, int ptinggi){
        nama = pnama;
        umur = pumur;
        tinggi = ptinggi;
    }

    public Manusia(String pnama, int pumur){
        nama = pnama;
        umur = pumur;
    }
    public Manusia(String pnama){
        nama = pnama;
    }

    public Manusia(){
        nama = "???";
        umur = 0;
        tinggi = 0;
    }
    
    // buat get & set methods di sini
    public void setNama(String pnama) {
        this.nama = pnama;
    }
    public String getNama() {
        return this.nama;
    }

    public void setUmur(int pumur) {
        this.umur = pumur;
    }
    public int getUmur() {
        return this.umur;
    }

    public void setTinggi(int ptinggi) {
        this.tinggi = ptinggi;
    }
    public int getTinggi() {
        return this.tinggi;
    }


    // method yg di override
    public String to_string(){
        String tmp;

        tmp = "\nNama : " +nama + "\nUmur : " + umur + "\nTinggi : " + tinggi;
        return tmp;
    }
}
