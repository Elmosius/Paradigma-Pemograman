// package 

import java.util.Scanner;

public class MesinCuci {
    public String merk;
    public String tipe;
    public int kapasitas;
    public double beratCucian;
    public String modePencucian;
    public boolean airHangat;
    public String teksAir;

    public MesinCuci(String merk, String tipe, int kapasitas, double beratCucian, String modePencucian, boolean airHangat) {
        this.merk = merk;
        this.tipe = (tipe.equalsIgnoreCase("top loading") || tipe.equalsIgnoreCase("front loading")) ? tipe : "top loading";
        this.kapasitas = (kapasitas > 0) ? kapasitas : 1; 
        this.beratCucian = (beratCucian > 0) ? beratCucian : 1; 
        this.modePencucian = (modePencucian.equalsIgnoreCase("ringan") || modePencucian.equalsIgnoreCase("sedang") || modePencucian.equalsIgnoreCase("berat")) ? modePencucian : "sedang";
        this.airHangat = airHangat;
        this.teksAir = (airHangat) ? "menggunakan air hangat" : "tidak menggunakan air hangat";
    }

    public String mencuci() {
        return "Sedang mencuci " + beratCucian + " kg pakaian, mode " + modePencucian + ", " + teksAir;
    }

    public String membilas() {
        return "Sedang membilas " + beratCucian + " kg pakaian, mode " + modePencucian + ", " + teksAir;
    }

    public String mengeringkan() {
        return "Sedang mengeringkan " + beratCucian + " kg pakaian, mode " + modePencucian + ", " + teksAir;
    }

    public String toString() {
        return "Dilakukan oleh mesin cuci dengan merk " + merk + ", tipe " + tipe + ", dengan kapasitas " + kapasitas + " kg";
    }

    public void tampilkan() {
        System.out.println(mencuci());
        System.out.println(membilas());
        System.out.println(mengeringkan());
        System.out.println(toString() + "\n");
    }

    public static void main(String[] args) {
        // Contoh penggunaan dengan input pengguna
        Scanner scanner = new Scanner(System.in);

        System.out.print("Merk: ");
        String merk = scanner.nextLine();
        System.out.print("Tipe (top loading / front loading): ");
        String tipe = scanner.nextLine();
        System.out.print("Kapasitas (kg): ");
        int kapasitas = scanner.nextInt();
        System.out.print("Berat Cucian (kg): ");
        double beratCucian = scanner.nextDouble();
        scanner.nextLine(); 
        System.out.print("Mode Pencucian (ringan / sedang / berat): ");
        String modePencucian = scanner.nextLine();
        System.out.print("Air Hangat (true / false): ");
        boolean airHangat = scanner.nextBoolean();

        MesinCuci mesin = new MesinCuci(merk, tipe, kapasitas, beratCucian, modePencucian, airHangat);

        mesin.tampilkan();

        scanner.close();
    }
}
