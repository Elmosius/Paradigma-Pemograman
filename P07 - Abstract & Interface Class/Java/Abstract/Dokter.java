// file : Dokter.java
// note : Latihan abstract class 2
class Dokter extends Manusia{
    private String spesialis;

    public Dokter(String namanya){
        super(namanya);
    }
    public void setSpesialis(String spesialisnya){
        this.spesialis = spesialisnya;
    }
    public String getKetarangan(){
        return "Adalah seorang dokter spesialis " + this.spesialis;
    }
}
