// file : HandPhone.java
// note : kelas test latihan interface 4
public class TestElectronic {
    public static void main(String[] args) {
        NGage HpKu = new NGage();
        NGage HpMu = new NGage();

        HpKu.setArus(100);
        HpKu.setNomor(123);
        HpKu.setWarnaCasing("Hitam");
        HpKu.setPicture("Buku");
        HpKu.setChanel(107.3);

        HpMu.setArus(125);
        HpMu.setNomor(456);
        HpMu.setWarnaCasing("Merah");
        HpMu.setPicture("Bunga");
        HpMu.setChanel(104.1);

        System.out.println("All about HpKu");
        System.out.println("Jumlah: " + HpKu.getJumlah());
        System.out.println("Kode: " + HpKu.getKode());
        System.out.println("Arus: " + HpKu.getArus());
        System.out.println("Nomor: " + HpKu.getNomor());
        System.out.println("Warna Casing: " + HpKu.getWarnaCasing());
        System.out.println("Picture: " + HpKu.getPicture());
        System.out.println("Chanel:" + HpKu.getChanel());

        System.out.println();

        System.out.println("All about HpMu");
        System.out.println("Jumlah: " + HpMu.getJumlah());
        System.out.println("Kode: " + HpMu.getKode());
        System.out.println("Arus: " + HpMu.getArus());
        System.out.println("Nomor: " + HpMu.getNomor());
        System.out.println("Warna Casing: " + HpMu.getWarnaCasing());
        System.out.println("Picture: " + HpMu.getPicture());
        System.out.println("Chanel:" + HpMu.getChanel());



    }
}
