package com.example.HRProject.Controller;

import com.example.HRProject.Model.HRDataEntity;
import com.example.HRProject.Service.ServiceData;
import com.example.HRProject.View.RepositoryData;
import lombok.AllArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@AllArgsConstructor
@RestController
@RequestMapping(path = "/Data")
public class Controller {

    private final ServiceData serviceData;


    @GetMapping("/getAll")
    public ResponseEntity<?> allData() {
        return ResponseEntity.ok(serviceData.getAll());
    }


    @GetMapping("/Emplyeer/{employeenumber}")
    public ResponseEntity<?> getByEmplyeerNumber(
            @PathVariable("employeenumber") Integer employeenumber
    ) {
        return ResponseEntity.ok(serviceData.getByEmplyeerNumber(employeenumber));
    }


    @GetMapping("/department/")
    public ResponseEntity<?> getByDepartment(@RequestParam String department) {
        return ResponseEntity.ok(serviceData.getBYdepartment(department));
    }

    @GetMapping("/Emplyeer/{gender}")
    public ResponseEntity<?> getByEmplyeerNumber(
            @PathVariable("gender") String gender
    ) {
        return ResponseEntity.ok(serviceData.getByGender(gender));
    }


}
