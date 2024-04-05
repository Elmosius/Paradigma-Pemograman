package Praktikum.P02;
public class TestPegawai{
    public static void main(String[] args){
        Pegawai peg1 = new Pegawai("Cecep", 12000);
        Pegawai peg2 = new Pegawai("Lilis", 10000);
        Pegawai peg3 = new Pegawai("Usep", 15000);

        System.out.println("Data Pegawai:");
        System.out.println("NIP   : " + peg1.getNip());
        System.out.println("Nama  : " + peg1.getNama());
        System.out.print("Gaji  : " + peg1.getGaji());
        System.out.println("\tJumlah Pegawai: " + peg1.getJmlPegawai() + "\n");

        System.out.println("Data Pegawai:");
        System.out.println("NIP   : " + peg2.getNip());
        System.out.println("Nama  : " + peg2.getNama());
        System.out.print("Gaji  : " + peg2.getGaji());
        System.out.println("\tJumlah Pegawai: " + peg2.getJmlPegawai() + "\n");

        System.out.println("Data Pegawai:");
        System.out.println("NIP   : " + peg3.getNip());
        System.out.println("Nama  : " + peg3.getNama());
        System.out.print("Gaji  : " + peg3.getGaji());
        System.out.println("\tJumlah Pegawai: " + peg3.getJmlPegawai() + "\n");

        // menaikan gaji peg1
        peg1.kenaikanGaji(500);

        System.out.println("Proses kenaikan gaji");
        System.out.println("Nama   : " + peg1.getNama());
        System.out.println("Gaji   : " + peg1.getGaji());

    }
}