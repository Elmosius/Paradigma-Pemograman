// file : Profesi.java
// note : kelas test latihan abstract class 2
public class Profesi {
    public static void main(String[] args) {
        Dokter dr = new Dokter("Budi");
        Mahasiswa mhs = new Mahasiswa("Anton");

        dr.setSpesialis("Anak");
        mhs.setFakultas("Teknologi INformasi");

        System.out.println(dr.getNama() + " " + dr.getKetarangan());
        System.out.println(mhs.getNama() + " " + mhs.getKetarangan());
    }
}
