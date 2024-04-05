package Praktikum.P02;

public class Buah {
    public String nama;
    public String warna;
    public String rasa;
    public int berat;

    public Buah(String nama, String warna, String rasa, int berat) {
        this.nama = nama;
        this.warna = warna;
        this.rasa = rasa;
        this.berat = berat;

        if (this.berat < 1) {
            this.berat = 1;
        }
    }

    public int hitung_harga() {
        return (this.berat * 5000);
    }

    public void tampilkan() {
        System.out.println("Nama  : " + this.nama);
        System.out.println("Warna : " + this.warna);
        System.out.println("Rasa  : " + this.rasa);
        System.out.println("Berat : " + this.berat + " kg");
        System.out.print("Harga : " + this.hitung_harga());
        System.out.println("\n");
    }

    public void ubahRasa(String rasaBaru) {
        this.rasa = rasaBaru;
    }

    public int hitung_harga_diskon() {
        if (this.berat > 5) {
            return (int) (this.hitung_harga() * 0.9); // Diskon 10% jika berat lebih dari 5 kg
        } else {
            return this.hitung_harga();
        }
    }

    public static void main(String[] args) {
        Buah b1 = new Buah("Apel", "Merah", "Manis", 2);
        Buah b2 = new Buah("Alpukat", "Hijau", "Manis", 2);
        Buah b3 = new Buah("Jeruk", "Kuning", "Manis Asam", 3);

        System.out.println("Macam-macam Buah yang dibeli: ");
        System.out.println("Buah 1.");
        b1.tampilkan();
        System.out.println("Buah 2.");
        b2.tampilkan();
        System.out.println("Buah 3.");
        b3.tampilkan();

        b2.ubahRasa("Asam Manis");
        System.out.println("Rasa Buah 2 setelah diubah: " + b2.rasa);
        System.out.println("Harga Buah 3 setelah diskon: " + b3.hitung_harga_diskon());
    }
}
