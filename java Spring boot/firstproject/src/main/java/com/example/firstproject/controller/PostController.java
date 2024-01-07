package com.example.firstproject.controller;

import com.example.firstproject.data.dto.MemberDTO;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping(value = "/api/v1/post-api")
// http://localhost:8080/api/v1/post-api
public class PostController {

    // http://localhost:8080/api/v1/post-api/default
    @PostMapping(value = "default")
    public String postDefault() {
        return "Hello World!\n\tDeafault Post API Page.";
    }

    // http://localhost:8080/api/v1/post-api/member
    @PostMapping(value = "/member")
    public String postMember(@RequestBody Map<String, Object> postData ) {
        StringBuilder sb = new StringBuilder();
        postData.forEach((key, val) -> sb.append(key).append(" : ").append(val).append("\n"));
        return sb.toString();
    }

    // http://localhost:8080/api/v1/post-api/member2
    @PostMapping(value = "/member2")
    public String postMember(@RequestBody MemberDTO memberDTO ) {
        System.out.println(memberDTO.toString());
        return memberDTO.toString();
    }
}
