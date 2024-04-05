package Praktikum.P05.P05b_Latihan_Polymorphism_Java_2272008_Elmosius_Suli;
// File : Mahasiswa.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class Mahasiswa extends Manusia {
    protected String nrp;
    protected char kelas;

    // buat konstuktor di sini (lengkapi lagi ya...)
    public Mahasiswa(String pnama, int pumur, int ptinggi, String pnrp, char pkelas){
        super(pnama, pumur, ptinggi);
        nrp = pnrp;
        kelas = pkelas;
    }

    public Mahasiswa(String pnama, int pumur,int ptinggi, String pnrp){
        super(pnama, pumur ,ptinggi);
        nrp = pnrp;
    }

    public Mahasiswa(String pnama, int pumur,int ptinggi, char pkelas){
        super(pnama, pumur ,ptinggi);
        kelas = pkelas;
    }

    public Mahasiswa(String pnama, int pumur, String pnrp, char pkelas){
        super(pnama, pumur);
        nrp = pnrp;
        kelas = pkelas;
    }

    public Mahasiswa(String pnama, String pnrp, char pkelas){
        super(pnama);
        nrp = pnrp;
        kelas = pkelas;
    }

    public Mahasiswa(String pnama, String pnrp){
        super(pnama);
        nrp = pnrp;
    }

    public Mahasiswa(){
        super();
        nrp = "???";
        kelas = '?';
    }

    public Mahasiswa(String pnrp, char pkelas){
        nrp = pnrp;
        kelas = pkelas;
    }

    public Mahasiswa(String pnrp){
        nrp = pnrp;
    }

    //  buat get & set methods di sini
    public void setNrp(String pnrp) {
        this.nrp = pnrp;
    }
    public String getNrp() {
        return this.nrp;
    }

    public void setKelas(char pkelas) {
        this.kelas = pkelas;
    }
    public char getKelas() {
        return this.kelas;
    }

    // method peng-override
    public String to_string(){
        String tmp;

        tmp = super.to_string() + "\nNrp : " + nrp + "\nKelas : " + kelas;
        return tmp;
    }

}
