// file : MusikPetik.java
// note : Latihan abstract class 1

class MusikPetik extends AlatMusik{
    private String bunyi;
    private String namaAlat;
    private int jmlDawai;

    //constuctor
    public MusikPetik(){
    }

    public void setBunyi(String bunyinya){
        this.bunyi = bunyinya;
    }
    public void setNamaAlat(String alatnya){
        this.namaAlat = alatnya;
    }
    public void setJmlDawai(int jmlDawainya){
        this.jmlDawai = jmlDawainya;
    }
    public String getBunyi(){
        return this.bunyi;
    }
    public String getNamaAlat(){
        return this.namaAlat;
    }
    public int getJmldawai(){
        return this.jmlDawai;
    }
}
