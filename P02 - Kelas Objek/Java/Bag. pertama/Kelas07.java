package Praktikum.P02;

// Method toString() yg dipanggil otomatis ketika mencetak objek secara langsung
public class Kelas07 {
    // attribut2
    private int id;
    public String name;
    protected int age;

    // Konstuktor: nama konstuktor = nama kelas
    public Kelas07(int id, String nama, int age){
        this.id   = id;         //this = objek yg sedang diproses
        this.name = nama;
        this.age  = age;
    }

    // Method cetak
    public void cetak(){
        System.out.println("ID: " + this.id + " | Nama: " + this.name + " | Umur: " + this.age);
    }

    // Method yg dipanggil otomatis ketika mencetak objek secara langsung
    public String toString(){
        String str;
        str = "ID: " + this.id + " | Nama : " + this.name + " | Umur: " + this.age;
        return str;
    }



    public static void main(String[] args){
        Kelas07 k1 = new Kelas07(3, "Hudson Taylor", 20);  // k1 = objek dari kelas07
        System.out.println("Panggil method cetak()");
        k1.cetak();
        System.out.println("\nCetak objek langsung, method toString()");
        System.out.println("Print obj         : " + k1);
        System.out.println("Panggil eksplisit : " + k1.toString());
    }

}
