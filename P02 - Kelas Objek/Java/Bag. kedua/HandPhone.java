package Praktikum.P02;
public class HandPhone {
    private String warnaCasing;     // field warnaCasing
    private String nomor;           // field nomor

    // constuctor Handphone
    public HandPhone(){
        // lsi konstuktor
    }

    // method meminta warnaCasing Handphone
    public String getWarnaCasing(){
        return this.warnaCasing;
    }

    // method meminta nomor HandPhone
    public String getNomor(){
        return this.nomor;
    }

    // method mengisi warnaCasing HandPhone
    public void setWarnaCasing(String warnaBaru){
        this.warnaCasing = warnaBaru;
    }

    // method mengisi nomor Handphone
    public void setNomor(String nomorBaru){
        this.nomor = nomorBaru;
    }

}
