package Praktikum.P02;

public class Mobil {
    private String warna;   // Field warna Mobil
    private String jenis;   // field jenis Mobil
    private int harga;      // field harga Mobil 
    private int kapasitas;  // field kapasitass Mobil

    public Mobil(){  // constuctor Mobil
        this.warna = "???";
        this.jenis = "???";
        this.harga = 0;
        this.kapasitas = 0;
    }

    // method meminta warna Mobil
    public String getWarna(){
        return this.warna;
    }

    // method meminta jenis Mobil
    public String getJenis(){
        return this.jenis;
    }

    // method meminta harga Mobil
    public int getHarga(){
        return this.harga;
    }

    // method meminta kapasitas Mobil
    public int getKapasitas(){
        return this.kapasitas;
    }

    // method mengisi warna Mobil
    public void setWarna(String warnanya){
        this.warna = warnanya;
    }

    // method mengisi jenis Mobil
    public void setjenis(String jenisnya){
        this.jenis = jenisnya;
    }

    // method mengisi harga Mobil
    public void setHarga(int harganya){
        this.harga = harganya;
    }

    // method mengisi kapasitas Mobil
    public void setKapasitas(int kapasitasnya){
        this.kapasitas = kapasitasnya;
    }
}
