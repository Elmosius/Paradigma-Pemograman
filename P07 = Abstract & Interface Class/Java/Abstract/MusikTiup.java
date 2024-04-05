// file : MusikTiup.java
// note : Latihan abstract class 1
class MusikTiup extends AlatMusik{
    private String bunyi;
    private String namaAlat;

    // constructor
    public MusikTiup(){}

    public void setBunyi(String bunyi){
        this.bunyi = bunyi;
    }
    public void setNamaAlat(String alatnya){
        this.namaAlat = alatnya;
    }
    public String getBunyi(){
        return this.bunyi;
    }
    public String getNamaAlat(){
        return this.namaAlat;
    }
}
