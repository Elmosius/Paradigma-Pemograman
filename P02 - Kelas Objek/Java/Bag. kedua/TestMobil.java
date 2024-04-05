package Praktikum.P02;

public class TestMobil {
    public static void main(String[] args){
    Mobil sedanku = new Mobil();
    Mobil vanku = new Mobil();

    sedanku.setjenis("Sedan");
    sedanku.setWarna("Merah");
    sedanku.setHarga(60000);
    sedanku.setKapasitas(4);

    vanku.setjenis("Van");
    vanku.setWarna("Biru");
    vanku.setHarga(25000);
    vanku.setKapasitas(8);

    System.out.println("Mobilku: ");
    System.out.println("1. Jenis      : " + sedanku.getJenis());
    System.out.println("   Warna      : " + sedanku.getWarna());
    System.out.println("   Kapasitas  : " + sedanku.getKapasitas());
    System.out.println("   Harga      : " + sedanku.getHarga());
    System.out.println();

    System.out.println("2. Jenis      : " + vanku.getJenis());
    System.out.println("   Warna      : " + vanku.getWarna());
    System.out.println("   Kapasitas  : " + vanku.getKapasitas());
    System.out.println("   Harga      : " + vanku.getHarga());

    }

}
