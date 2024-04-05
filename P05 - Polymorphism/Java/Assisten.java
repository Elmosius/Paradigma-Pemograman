package Praktikum.P05.P05b_Latihan_Polymorphism_Java_2272008_Elmosius_Suli;
// File : Asisten.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class Assisten extends Mahasiswa {
    protected String matakuliah;
    protected int jml_jaga;

    // buat konstuktor di sini (lengkapi lagi ya...)
    public Assisten(String pnama, String pnrp, String pmatakuliah, int pjml_jaga){
        super(pnama, 20, 175, pnrp, 'B');
        matakuliah = pmatakuliah;
        jml_jaga = pjml_jaga;
    }

    public Assisten(String pnama, String pnrp, char pkelas, String pmatakuliah, int pjml_jaga){
        super(pnama, 20, 175, pnrp, pkelas);
        matakuliah = pmatakuliah;
        jml_jaga = pjml_jaga;
    }

    public Assisten(String pnama, String pnrp, String pmatakuliah){
        super(pnama, 20, 175, pnrp, 'B');
        matakuliah = pmatakuliah;
    }

    public Assisten(String pnama, String pnrp, int pjml_jaga){
        super(pnama, 20, 175, pnrp, 'B');
        jml_jaga = pjml_jaga;
    }

     public Assisten(){
        super();
        matakuliah = "???";
        jml_jaga = 0;
    }

    //  buat get & set methods di sini
    public void setMataKuliah(String pmatakuliah) {
        this.matakuliah = pmatakuliah;
    }
    public String getMataKuliah() {
        return this.matakuliah;
    }

    public void setJmlJaga(int pjml_jaga) {
        this.jml_jaga = pjml_jaga;
    }
    public int getJmlJaga() {
        return this.jml_jaga;
    }



    // method peng-override
    public String to_string(){
        String tmp;

        tmp = super.to_string() + "\nMatakuliah " + matakuliah + "\nJml jaga : " + jml_jaga;
        return tmp;
    }
}

