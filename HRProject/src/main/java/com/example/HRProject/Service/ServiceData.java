package com.example.HRProject.Service;


import com.example.HRProject.Model.HRDataEntity;
import com.example.HRProject.View.RepositoryData;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@AllArgsConstructor
@Service
public class ServiceData {

    private final RepositoryData repositoryData;

    public List<HRDataEntity> getAll() {
        return repositoryData.findAll().stream().toList();
    }


    public Optional<HRDataEntity> getByEmplyeerNumber(Integer employeenumber){

        return  repositoryData.findByEmployeenumber(employeenumber);
    }

    public List< Optional<HRDataEntity>> getBYdepartment(String department)
    {
        return  repositoryData.findByDepartment(department);
    }

    public List< Optional<HRDataEntity>> getByGender(String gender)
    {
        return  repositoryData.findbyGender(gender);
    }



}
