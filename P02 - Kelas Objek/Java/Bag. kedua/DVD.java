package Praktikum.P02;

import java.util.Scanner;

public class DVD {
    public String judul;
    public String jenis;
    public int harga;
    public int jumlahStock;
    public float nilaiStock;

    public DVD(String judul, String jenis, int harga, int jumlahStock) {
        this.judul = judul;
        this.jenis = (jenis.equalsIgnoreCase("film") || jenis.equalsIgnoreCase("musik") || jenis.equalsIgnoreCase("game")) ? jenis : "film";
        this.harga = harga;
        this.jumlahStock = jumlahStock;
        this.nilaiStock = harga * jumlahStock;
    }

    public void tampilkan() {
        System.out.println("Judul        : " + judul);
        System.out.println("Jenis        : " + jenis);
        System.out.println("Harga        : " + harga);
        System.out.println("Jumlah Stock : " + jumlahStock);
        System.out.println(toString());
    }

    public int tambahStock(int jumlah) {
        if (jumlah > 0) {
            jumlahStock += jumlah;
        }
        return jumlahStock;
    }

    public float penjualan(int jmlJual) {
        if (jmlJual > 0 && jmlJual <= jumlahStock) {
            jumlahStock -= jmlJual;
            return harga * jmlJual;
        } else {
            return 0;
        }
    }

    public float nilaiStock() {
        nilaiStock = harga * jumlahStock;
        return nilaiStock;
    }

    public void tampilkanNilaiStock() {
        System.out.println("Nilai stock dari DVD ini adalah sebesar Rp" + nilaiStock + ",-");
    }

    public String toString() {
        return "Nilai stock dari DVD ini adalah sebesar Rp" + nilaiStock + ",-";
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        DVD d1 = new DVD("Paddle Pop Begins", "film", 10000, 12);

        d1.tampilkan();

        int pilih = -1; 
        while (pilih != 0) {
            System.out.println("Apa yang ingin dilakukan?");
            System.out.println("1. Menambah stock DVD");
            System.out.println("2. Menjual DVD");
            System.out.println("3. Tampilkan nilai stock");
            System.out.println("0. Keluar\n");

            pilih = scanner.nextInt();
            if (pilih == 1) {
                System.out.print("Berapa stock yang ditambah? ");
                int ditambah = scanner.nextInt();
                d1.tambahStock(ditambah);
                System.out.println("Stock DVD saat ini adalah " + d1.jumlahStock + " buah");
            } else if (pilih == 2) {
                System.out.print("Berapa stock yang terjual? ");
                int terjual = scanner.nextInt();
                float pendapatan = d1.penjualan(terjual);
                if (pendapatan > 0) {
                    System.out.println("Terjual DVD " + terjual + " buah dengan harga Rp" + pendapatan + ",-");
                } else {
                    System.out.println("Stok tidak mencukupi untuk penjualan.");
                }
            } else if (pilih == 3) {
                d1.tampilkanNilaiStock();
            } else if (pilih == 0) {
                System.out.println("Terima kasih. Sampai jumpa!");
            } else {
                System.out.println("Pilihan tidak valid.");
            }
        }

        scanner.close();
    }
}
