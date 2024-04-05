package Praktikum.P02;

// Membuat atribut di dalam kelas & konstruktor
public class Kelas04 {
    // Atribut2
    private int id;
    public String name;
    protected int age;


    // Konstruktor: nama konstruktor = nama kelas
    public Kelas04(){
        this.id = 1;        //this = objek yg sedang diproses
        this.name = "Nama1";
        this.age = 21;
    }

    // Method cetak
    public void cetak(){
        System.out.println("ID: " + this.id + " | Nama: " + this.name + " | Umur: " + this.age);
    }

    public static void main(String[] args){
        Kelas04 k1 = new Kelas04();         //k1 = objek dari Kelas04
        k1.cetak();

        System.out.println("Setelah daata diubah: ");
        k1.id = 3;                          // main() di dalam kelas04
        k1.name = "Hudson Taylor";          // bisa akses atribut private
        k1.age = 20;
        k1.cetak();
    }
}
