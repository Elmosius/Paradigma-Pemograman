package Praktikum.P02;

// Konstuktor yg menerima parameter 
public class Kelas05 {
    // attribut2
    private int id;
    public String name;
    protected int age;


    // Konstuktor: nama konstuktor = nama kelas
    public Kelas05(int id, String nama, int age){
        this.id   = id;         // this = objeck yg sedang diproses
        this.name = nama;
        this.age  = age;
    }


    // Method cetak
    public void cetak(){
        System.out.println("ID: " + this.id + " | Nama: " + this.name + " | Umur: " + this.age);
    }

    public static void main(String[] args){
        Kelas05 k1 = new Kelas05(3, "Hudson Taylor", 20);       //k1 = objel dari Kelas05
        Kelas05 k2 = new Kelas05(4, "Abraham Lincoln", 33);     //k2 = objek dari Kelas05 juga

        System.out.println("Cetak langsung: ");
        System.out.println("ID: " + k1.id + " | Nama: " + k1.name + " | Umur: " + k1.age);
        System.out.println("ID: " + k2.id + " | Nama: " + k2.name + " | Umur: " + k2.age);

        System.out.println("\nCetak dengan method cetak():");
        k1.cetak();
        k2.cetak();

    }

}
