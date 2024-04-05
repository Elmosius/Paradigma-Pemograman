package Praktikum.P02;

public class TestMahasiswa {
    public static void main(String[] args){
        Mahasiswa badu = new Mahasiswa();
        Mahasiswa wati = new Mahasiswa("1234", 75);
        Mahasiswa ika   = new Mahasiswa("4321", 120, 3.4);

        System.out.println("Datanya Badu: ");
        System.out.println("No Induk    : " + badu.getNoInduk());
        System.out.println("Total SKS   : " + badu.getTotalSks());
        System.out.println("IPK         : " + badu.getIpk());
        System.out.print("Prestasi  : ");
        badu.prestasi();
        System.out.println("\n");

        System.out.println("Datanya Wati: ");
        System.out.println("No Induk    : " + wati.getNoInduk());
        System.out.println("Total SKS   : " + wati.getTotalSks());
        System.out.println("IPK         : " + wati.getIpk());
        System.out.print("Prestasi  : ");
        wati.prestasi();
        System.out.println("\n");

        System.out.println("Datanya Ika: ");
        System.out.println("No Induk    : " + ika.getNoInduk());
        System.out.println("Total SKS   : " + ika.getTotalSks());
        System.out.println("IPK         : " + ika.getIpk());
        System.out.print("Prestasi  : ");
        ika.prestasi();
        System.out.println("\n");
    }
}
