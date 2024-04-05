// file : AnakInstrumen.java
// note : Kelas test latihan abstract class 1
public class AnekaInstrumen {
    public static void main(String[] args) {
        MusikTiup terompet = new MusikTiup();
        MusikPetik gitar = new MusikPetik();

        terompet.setNamaAlat("Terompet");
        terompet.setBunyi("toet-toet");
        gitar.setNamaAlat("Gitar");
        gitar.setBunyi("jreng-jreng");
        gitar.setJmlDawai(6);

        System.out.println("Aneka Instrumen");
        System.out.println("Nama alat : " + terompet.getNamaAlat());
        System.out.println("Bunyi : " + terompet.getBunyi());

        System.out.println();
        System.out.println("Nama alat : " + gitar.getNamaAlat());
        System.out.println("Bunyi : " + gitar.getBunyi());
        System.out.println("Jml Dawai : " + gitar.getJmldawai());
    }
}
