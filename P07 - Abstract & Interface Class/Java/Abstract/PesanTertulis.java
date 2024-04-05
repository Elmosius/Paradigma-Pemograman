// file : PesanTertulis.java
// note : Latihan abstract class 3
class PesanTertulis extends Pesan{
    private String teks;
    private String pengirim;
    private String tujuan;

    // constructor class PesanTertulis
    PesanTertulis() {
    }

    // method untuk menulis pesan
    public void setPesan(String pesannya){
        this.teks = pesannya;
    }

    // method untuk mengisi pengirim
    public void setPengirim(String pengirimnya){
        this.pengirim = pengirimnya;
    }
    
    // method untuk mengisi tujuan
    public void setTujuan(String tujuannya){
        this.tujuan = tujuannya;
    }

    // method untuk melihat pesan
    public String getPesan(){
        return this.teks;
    }

    // method untuk mengisi pengirim
    public String getPengirim(){
        return this.pengirim;
    }

    // method untuk melihat tujuan
    public String getTujuan(){
        return this.tujuan;
    }
}
