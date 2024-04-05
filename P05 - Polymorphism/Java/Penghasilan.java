package Praktikum.P05.P05b_Latihan_Polymorphism_Java_2272008_Elmosius_Suli;
// File : Asisten.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : polymorphic argument

public class Penghasilan {
    public String jenis(Manusia pman){
        String str;

        if(pman instanceof Assisten){
            str = "Asisten";
        }else if(pman instanceof Mahasiswa){
            str = "uang saku";
        }else if(pman instanceof Manusia){
            str = "gaji";
        }else{
            str = "nyolong";
        }
        return str;
    }

    public int jumlah(Manusia pman){
        int jml;

        if(pman instanceof Assisten){
            jml = 200000;
        }else if(pman instanceof Mahasiswa){
            jml = 500000;
        }else if(pman instanceof Manusia){
            jml = 700000;
        }else{
            jml = 0;
        }
        return jml;
    }
}
