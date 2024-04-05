package Praktikum.P04.P04c_Latihan_Inheritance_Java_227008_Elmosius_Suli;
// File : AnekaBidangDatar.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

class Persegi{
    protected int panjSisi;
    protected int luas;

    public Persegi(){

    }

    public void setPanjSisi(int n){
        this.panjSisi = n;
    }
    public int getPanjSisi(){
        return this.panjSisi;
    }
    public int getLuas(){
        return luas;
    }

    public void hitungLuas(){
        this.luas = (int)Math.pow(this.panjSisi, 2);
    }
}

class PersegiPanjang extends Persegi{
    private int lebarSisi;

    public PersegiPanjang(){

    }
    public void setLebarSisi(int n){
        this.lebarSisi = n;
    }
    public int getLebarSisi(){
        return this.lebarSisi;
    }
    public void hitungLuas(){
        this.luas = super.panjSisi * this.lebarSisi;
    }
}

public class AnekaBidangDatar{
    public static void main(String[] args) {
        Persegi p = new Persegi();
        p.setPanjSisi(5);
        p.hitungLuas();
        System.out.println("Bujur Sangkar:");
        System.out.println("Panj Sisi: " + p.getPanjSisi());
        System.out.println("Luas: " + p.getLuas());
        System.out.println();

        PersegiPanjang pp = new PersegiPanjang();
        pp.setPanjSisi(8);
        pp.setLebarSisi(4);
        pp.hitungLuas();
        System.out.println("Persegi Panjang:");
        System.out.println("Panj Sisi: " + pp.getPanjSisi());
        System.out.println("Lebar Sisi: " + pp.getLebarSisi());
        System.out.println("Luas: " + pp.getLuas());
        System.out.println();
    }

}
