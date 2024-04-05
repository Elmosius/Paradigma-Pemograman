package Praktikum.P02;

// Method / constructor Overloading sebagai pengganti default arguments
// karena Java tidak memiliki default arguments
public class Kelas06 {
    // attribut2
    private int id;
    public String name;
    protected int age;


    // Konstuktor
    public Kelas06(int id, String nama, int age){
        this.id   = id;             // this = objek yg sedang diproses
        this.name = nama;
        this.age  = age;
    }

    // Konstuktor 2 (overloading)
    public Kelas06(int id, String nama){
        this(id, nama, 30);     // Panggil konstruktor 2 parameter, df default age = 30
    }

    // Konstuktor 3 (overloading)
    public Kelas06(int id){
        this(id, "Noname", 30);            // Panggil konstruktor 3 parameter, df default name & age
    }

    // Method cetak
    public void cetak(){
        System.out.println("ID: " + this.id + " | Nama: " + this.name + " | Umur: " + this.age);
    }

    public static void main(String[] args){
        Kelas06 k1 = new Kelas06(3, "Hudson Taylor", 20);   //k1 = pbkel daro Kelas06
        Kelas06 k2 = new Kelas06(4, "Nelson Mandela");          //k2 = objeck dari Kelas06 juga
        Kelas06 k3 = new Kelas06(5);                                 //k3 = objeck dari Kelas06 juga

        System.out.println("Cetak dengan method cetak():");
        k1.cetak();
        k2.cetak();
        k3.cetak();
    }

}
