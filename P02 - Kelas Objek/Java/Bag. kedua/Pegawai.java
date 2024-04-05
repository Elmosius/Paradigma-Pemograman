package Praktikum.P02;

public class Pegawai{
    private String nama;                // field nama
    private int gaji;                   // field gaji
    private int nip;                    // field nip
    private static int jmlPegawai = 0;  // field jmlPegawai


    //  constructor Pegawai dengan parameter
    public Pegawai(String namanya, int gajinya) {
        Pegawai.jmlPegawai++;
        this.nama = namanya;
        this.gaji = gajinya;
        this.nip = Pegawai.jmlPegawai;
    }

    public String getNama(){    // method meminta nama Pegawai
        return this.nama;
    }

    public int getGaji(){       // method meminta gaji Pegawai
        return this.gaji;
    }

    public int getNip(){        // method meminta nip Pegawai
        return this.nip;
    }

    public int getJmlPegawai(){     // method meminta jumlah Pegawai
        return Pegawai.jmlPegawai;
    }

    public void kenaikanGaji(int naik){ // method menaikkan gaji Pegawai
        this.gaji += naik;
    }
}