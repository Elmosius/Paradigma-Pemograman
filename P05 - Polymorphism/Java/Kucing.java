package Praktikum.P05.P05b_Latihan_Polymorphism_Java_2272008_Elmosius_Suli;
// File : Kucing.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class Kucing {
    protected String jenis;

    public String bersuara(){
        jenis = "kucing";
        return(jenis + " " + "miauww...");
    }

    public String cekJenis(Kucing miau){
        String jns = "";
        if(miau instanceof Harimau){
            jns = "harimau";
        }else if(miau instanceof KucingBesar){
            jns = "kucing besar";
        }else if(miau instanceof KucingKecil){
            jns = "kucing kecil";
        }else if(miau instanceof Kucing)
            jns = "kucing";
        jenis = jns;
        return miau.jenis;
    }
}   
