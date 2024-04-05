// file : NGage.java
// note : latihan interface 4
public class NGage extends HandPhone implements Kamera, RadioFM {
    private String kode;
    private String picture;
    private double chanel;

    public NGage(){
        super();
        this.setKode();
    }
    public void setPicture(String pic){
        this.picture = pic;
    }
    public String getPicture(){
        return this.picture;
    }
    public void setChanel (double chnl){
        this.chanel = chnl; 
    }
    public double getChanel(){
        return this.chanel;
    }
    private void setKode(){
        this.kode = "NG-" + this.getJumlah();
    }
    public String getKode(){
        return this.kode;
    }
}
