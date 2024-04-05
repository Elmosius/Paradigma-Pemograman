package Praktikum.P02;

public class Waktu {
    public int jam;
    public int menit;
    public int detik;

    public Waktu(int jam, int menit, int detik) {
        this.jam = jam;
        this.menit = menit;
        this.detik = detik;
    }

    public void to_string() {
        System.out.println("Jam   : " + jam);
        System.out.println("Menit : " + menit);
        System.out.println("Detik : " + detik);
        System.out.print("Jam Saat Ini : ");
        tampilkanJam();
        System.out.println("Jumlah Detik : " + waktuToDetik() + "\n");
    }

    public void tampilkanJam() {
        System.out.printf("%02d:%02d:%02d%n", jam, menit, detik);
    }

    public int waktuToDetik() {
        return jam * 3600 + menit * 60 + detik;
    }

    public void detikToWaktu(int jmlDetik) {
        System.out.println("Jika jumlah detik diubah menjadi " + jmlDetik);
        System.out.println("Datanya akan menjadi seperti ini");
        jam = jmlDetik / 3600;
        int sisaDetik = jmlDetik % 3600;
        menit = sisaDetik / 60;
        detik = sisaDetik % 60;
        to_string();
    }

    public void tambahWaktu(int jamTambah, int menitTambah, int detikTambah) {
        jam += jamTambah;
        menit += menitTambah;
        detik += detikTambah;

        if (detik >= 60) {
            int sisaDetik = detik % 60;
            int tambahanMenit = detik / 60;
            detik = sisaDetik;
            menit += tambahanMenit;
        }

        if (menit >= 60) {
            int sisaMenit = menit % 60;
            int tambahanJam = menit / 60;
            menit = sisaMenit;
            jam += tambahanJam;
        }

        to_string();
    }

    public static void main(String[] args) {
        Waktu w1 = new Waktu(2, 3, 4);
        
        w1.to_string();
        w1.detikToWaktu(5000);

        System.out.println("Tambahkan 1 jam, 30 menit, dan 15 detik ke Waktu 1:");
        w1.tambahWaktu(1, 30, 15);
    }
}
