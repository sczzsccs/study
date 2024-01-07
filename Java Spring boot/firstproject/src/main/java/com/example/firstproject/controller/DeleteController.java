package com.example.firstproject.controller;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(value = "/api/v1/get-api")
public class DeleteController {
    // http://localhost:8080/api/v1/get-api/var/{String 값}
    @DeleteMapping(value = "delete/{variable}")
    public String deleteVar(@PathVariable String variable) {
        return variable;
    }
}