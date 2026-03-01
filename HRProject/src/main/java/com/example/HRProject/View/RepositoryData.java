package com.example.HRProject.View;

import com.example.HRProject.Model.HRDataEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface RepositoryData extends JpaRepository<HRDataEntity, Integer> {


    @Query(value = "SELECT  * FROM employee where employeenumber =:employeenumber", nativeQuery = true)
    Optional<HRDataEntity> findByEmployeenumber(@Param("employeenumber") Integer employeenumber);


    @Query(value = "SELECT  * FROM employee  where department=:department ", nativeQuery = true)
    List<Optional<HRDataEntity>> findByDepartment(@Param("department") String department);


    @Query(value = "SELECT  * FROM employee  where gender=:gender ", nativeQuery = true)
    List<Optional <HRDataEntity>> findbyGender (@Param("gender") String gender);

}
