// file : Manusia.java
// note : Latihan abstract class 2
public abstract class Manusia {
    private String nama;

    public Manusia(String namanya){
        this.nama = namanya;
    }
    public String getNama(){
        return this.nama;
    }

    // method ini harus ada di subclassnya
    abstract public String getKeterangan();
}
