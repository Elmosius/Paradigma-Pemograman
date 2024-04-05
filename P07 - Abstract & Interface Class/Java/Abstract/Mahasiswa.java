// file : Mahasiswa.java
// note : Latihan abstract class 2
class Mahasiswa extends Manusia{
    private String fakultas;

    public Mahasiswa(String namanya){
        super(namanya);
    }
    public void setFakultas(String fakultasnya){
        this.fakultas = fakultasnya;
    }
    public String getKetarangan(){
        return"Adalah seorang mahasiswa fakultas " + this.fakultas;
    }
}
