package com.example.firstproject.controller;

import com.example.firstproject.data.dto.MemberDTO;
import com.example.firstproject.service.RestTemplateService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(value = "RestTemplate")
public class RestTemplateController {
    @Autowired
    RestTemplateService restTemplateService;

    @GetMapping(value = "/hub")
    public String getHub() {
        return restTemplateService.getHub();
    }
    @GetMapping(value = "/name")
    public String getName() {
        return restTemplateService.getName();
    }
    @GetMapping(value = "/name2")
    public String getName2() {
        return restTemplateService.getName2();
    }
    @PostMapping(value = "/member")
    public ResponseEntity<MemberDTO> postDTO() {
        return restTemplateService.postDTO();
    }
    @PostMapping(value = "/header")
    public ResponseEntity<MemberDTO> addHeader() {
        return restTemplateService.addHeader();
    }
}