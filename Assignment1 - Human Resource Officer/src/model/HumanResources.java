/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;

/**
 *
 * @author Rohit Paul G
 */
public class HumanResources {
    
    private String name;
    private String empId;
    private int age;
    private String gendr;
    private String strtDate;
    private String lvl;
    private String tmInfo;
    private String posTitle;
    private long cellPhn;
    private String emailAdd;
    private String photo;
    
    //priate Image photo;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmpId() {
        return empId;
    }

    public void setEmpId(String empId) {
        this.empId = empId;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getGendr() {
        return gendr;
    }

    public void setGendr(String gendr) {
        this.gendr = gendr;
    }

    public String getStrtDate() {
        return strtDate;
    }

    public void setStrtDate(String strtDate) {
        this.strtDate = strtDate;
    }

    public String getLvl() {
        return lvl;
    }

    public void setLvl(String lvl) {
        this.lvl = lvl;
    }

    public String getTmInfo() {
        return tmInfo;
    }

    public void setTmInfo(String tmInfo) {
        this.tmInfo = tmInfo;
    }

    public String getPosTitle() {
        return posTitle;
    }

    public void setPosTitle(String posTitle) {
        this.posTitle = posTitle;
    }

    public long getCellPhn() {
        return cellPhn;
    }

    public void setCellPhn(long cellPhn) {
        this.cellPhn = cellPhn;
    }

    public String getEmailAdd() {
        return emailAdd;
    }

    public void setEmailAdd(String emailAdd) {
        this.emailAdd = emailAdd;
    }

    public String getPhoto() {
        return photo;
    }

    public void setPhoto(String photo) {
        this.photo = photo;
    }
    
    
    
    //as per the error shown in jTable first column has printed irrelevant value plus our value from
    //create employee screen. In order to workaround that issue, we do below:
    
    @Override
    public String toString(){
        
        return name;
        
    }
    
    
}
