package com.example.serverbox.controller;

import com.example.serverbox.dto.MemberDTO;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping(value = "/api-server")
public class TestController {
    private final Logger LOGGER = LoggerFactory.getLogger(TestController.class);

    @GetMapping(value = "/hub")
    public String getTest1() {
        LOGGER.info("getTest1 호출");
        return "Hollow. it is hell Hub";
    }

    @GetMapping(value = "/name")
    public String getTestName(@RequestParam String name) {
        LOGGER.info("getTestName 호출");
        return "Hollow. " + name;
    }

    @GetMapping(value = "/Var/{name}")
    public String getVarName(@PathVariable String name) {
        LOGGER.info("getVarName 호출");
        return "Hollow. " + name;
    }

    @PostMapping(value = "/member")
    public ResponseEntity<MemberDTO> getMember(
        // Request 값
        @RequestBody MemberDTO memberDTO1, // MemberDTO객체를 전달 받음

        // URI 값
        @RequestParam String name,  // name 값 전달 받음
        @RequestParam String email, // email 값 전달 받음
        @RequestParam String organization // organization 값 전달 받음
    ) {
        LOGGER.info("getMember 호출");

        // URI로 전달 받은 값 객체인스턴스 생성
        MemberDTO memberDTO = new MemberDTO();
        memberDTO.setName(name);
        memberDTO.setEmail(email);
        memberDTO.setOrganization(organization);

        return ResponseEntity.status(HttpStatus.OK).body(
                memberDTO); // <body>로 전달할 memberDTO객체 선택 반환
    }

    @PostMapping(value = "/header")
    public ResponseEntity<MemberDTO> addHeader(
            @RequestHeader(value = "header") String header,
            @RequestBody MemberDTO memberDTO
    ) {
        LOGGER.info("addHeader 호출");
        LOGGER.info("header 값 : {}", header);

        return ResponseEntity.status(HttpStatus.OK).body(memberDTO);
    }
}