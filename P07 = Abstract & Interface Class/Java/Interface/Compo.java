// file : Compo.java
// note : latihan interface 2
class Compo implements Radio, Tape{
    private double gelombang;
    private String kaset;

    public Compo(){
        this.gelombang = 0.0;
        this.kaset = "kosong";
    }
    public void setGelombang(double gelombangnya){
        this.gelombang = gelombangnya;
    }
    public void setPuterKaset(String kasetnya){
        this.kaset = kasetnya;
    }
    public double getGelombang(){
        return this.gelombang;
    }
    public String getKaset(){
        return this.kaset;
    }
    public String getSiaran(){
        return "ini siaran radio";
    }
    public String getDengerKaset(){
        return "ini suara kaset";
    }
}
