package Praktikum.P02;

public class Tabungan {
    public String namaBank;
    public String noRek;
    public int saldo;
    public int totalDebet;
    public int totalKredit;

    public Tabungan(String namaBank, String noRek, int saldo, int totalDebet, int totalKredit) {
        this.namaBank = namaBank;
        this.noRek = noRek;
        this.saldo = saldo;
        this.totalDebet = totalDebet;
        this.totalKredit = totalKredit;
    }

    public void cetakRek() {
        System.out.println("----------------------------");
        System.out.println("Informasi tabungan saat ini");
        System.out.println("----------------------------");
        System.out.println("Nama Bank    : " + namaBank);
        System.out.println("No Rekening  : " + noRek);
        System.out.println("Saldo        : " + saldo);
        System.out.println("Total Debet  : " + totalDebet);
        System.out.println("Total Kredit : " + totalKredit);
        System.out.println("----------------------------");
    }

    public void menabung(int rpDitabung) {
        saldo += rpDitabung;
        totalDebet += rpDitabung;
    }

    public void mengambil(int rpDiambil) {
        saldo -= rpDiambil;
        totalKredit += rpDiambil;
    }

    public void tutupRek() {
        namaBank = "";
        noRek = "";
        saldo = 0;
        totalDebet = 0;
        totalKredit = 0;
    }

}
