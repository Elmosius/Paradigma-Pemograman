// file : HandPhone.java
// note : latihan interface 4
public class HandPhone extends ElectronicStuff{
    private int nomor;
    private String warnaCasing;
    private static int jumlah = 0;
    private int arus;

    public HandPhone(){
        this.tambahJumlah();
    }

    public void setNomor(int no){
        this.nomor = no;
    }
    public void setWarnaCasing(String wrn){
        this.warnaCasing = wrn;
    }
    public int getNomor(){
        return this.nomor;
    }
    public String getWarnaCasing(){
        return this.warnaCasing;
    }
    private void tambahJumlah() { 
        jumlah++;
    }
    public int getJumlah(){
        return jumlah;
    }
    public void setArus(int arus){
        this.arus = arus;
    }
    public int getArus(){
        return this.arus;
    }
}
