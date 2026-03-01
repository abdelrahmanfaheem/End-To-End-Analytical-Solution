package com.example.HRProject.Model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Entity

@Table(name = "employee")

public class HRDataEntity {


    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "rowid")
    private Integer rowid;

    private Integer employeenumber;
    private Integer age;
    private String attrition;
    private String businesstravel;
    private Integer dailyrate;
    private String department;
    private Integer distancefromhome;
    private String education;
    private String educationfield;
    private Integer employeecount;
    private Integer environmentsatisfaction;
    private String gender;
    private Integer hourlyrate;
    private Integer jobinvolvement;
    private Integer joblevel;
    private String jobrole;
    private Integer jobsatisfaction;
    private String maritalstatus;
    private Integer monthlyincome;
    private Integer monthlyrate;
    private Integer numcompaniesworked;
    private String over18;
    private String overtime;
    private Integer percentsalaryhike;
    private Integer performancerating;
    private Integer relationshipsatisfaction;
    private Integer standardhours;
    private Integer stockoptionlevel;
    private Integer totalworkingyears;
    private Integer trainingtimeslastyear;
    private Integer worklifebalance;
    private Integer yearsatcompany;
    private Integer yearsincurrentrole;
    private Integer yearssincelastpromotion;
    private Integer yearswithcurrmanager;

}
