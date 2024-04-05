package Praktikum.P02;

public class JadwalKuliah {
    public String mataKuliah;
    public String hari;
    public String waktu;
    public String ruang;
    public int jmlSks;
    public String dosenPengajar; 

    public JadwalKuliah(String mataKuliah, String hari, String waktu, String ruang, int jmlSks, String dosenPengajar) {
        this.mataKuliah = mataKuliah;
        this.hari = hari;
        this.waktu = waktu;
        this.ruang = ruang;
        this.jmlSks = jmlSks;
        this.dosenPengajar = dosenPengajar;
    }

    public int durasi() {
        return jmlSks * 50;
    }

    public String toString() {
        return "Durasi belajar  : " + durasi() + " menit";
    }

    public void tampilkan() {
        System.out.println("Mata Kuliah     : " + mataKuliah);
        System.out.println("Hari            : " + hari);
        System.out.println("Waktu           : " + waktu);
        System.out.println("Ruang           : " + ruang);
        System.out.println("Jumlah SKS      : " + jmlSks);
        System.out.println("Dosen Pengajar  : " + dosenPengajar); // Menampilkan dosen pengajar
    }

    public void tambahDurasi(int tambahanMenit) {
        jmlSks += tambahanMenit / 50;
    }

    public static void main(String[] args) {
        JadwalKuliah j1 = new JadwalKuliah("Paradigma Pemrograman", "Rabu", "09:30", "Adv 3", 4, "Dr. John Doe");
        JadwalKuliah j2 = new JadwalKuliah("Teknologi Multimedia", "Selasa", "07:30", "Adv 1", 2, "Prof. Jane Smith");

        j1.tampilkan();
        System.out.println(j1.toString() + "\n");

        j2.tampilkan();
        System.out.println(j2.toString());
    }
}
