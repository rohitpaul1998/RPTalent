/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;

import java.util.ArrayList;

/**
 *
 * @author Rohit Paul G
 */
public class HumanResourcesHistory {
    
    private ArrayList<HumanResources> history;
    
    //ArrayList is an object and in order to use it we need to do its initialisation
    
    public HumanResourcesHistory() {   //we are creating this contructor in order to perform initialization of
        //the object "ArrayList"
        
        this.history = new ArrayList<HumanResources>();  //initialization done 
    }

    public ArrayList<HumanResources> getHistory() {
        return history;
    }

    public void setHistory(ArrayList<HumanResources> history) {
        this.history = history;
    }
    
    public HumanResources addNewHREmp(){
        
        HumanResources newHREmp = new HumanResources();
        history.add(newHREmp);
        return newHREmp;
    }
         
    public void deleteEmp(HumanResources hr){
        
        history.remove(hr);
        
    }
    
    public HumanResources getUpdateValues(String name){
        for(HumanResources hrs: history){
            if(hrs.getEmpId().equals(name)){
                return hrs;
            }
        }
        return null;
    }
    
}
