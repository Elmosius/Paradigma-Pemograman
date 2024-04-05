// file : Surat.java
// note : kelas test latihan abstract class 3
public class Surat {
    public static void main(String[] args) {
        String pesan;
        PesanTertulis suratku = new PesanTertulis();

        suratku.setPengirim("Aku");
        suratku.setTujuan("Kamu");
        pesan = "Ayo semangat belajar JAVA!!!";

        suratku.setPesan(pesan);
        System.out.println("Pengirim : " + suratku.getPengirim());
        System.out.println("Tujuan : " + suratku.getTujuan());
        System.out.println("Pesan : " + suratku.getPesan());
    }
}
