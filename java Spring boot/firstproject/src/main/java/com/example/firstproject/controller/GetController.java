package com.example.firstproject.controller;

import com.example.firstproject.data.dto.MemberDTO;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController()
// http://localhost:8080/api/v1/get-api
@RequestMapping(value = "/api/v1/get-api")
public class GetController {

    // http://localhost:8080/api/v1/get-api/hello
    @RequestMapping(value = "/hello", method = RequestMethod.GET)
    public String getHello() {
        return "hello World";
    }

    // http://localhost:8080/api/v1/get-api/name
    @GetMapping(value = "/name")
    public String getName() {
        return "name";
    }

    // http://localhost:8080/api/v1/get-api/var1/{String 값}
    @GetMapping(value = "/var1/{var1}")
    public String getVar1(@PathVariable String var1) {
        return var1;
    }

    // http://localhost:8080/api/v1/get-api/var2/{String 값}
    @GetMapping(value = "/var2/{var2}")
    public String getVar2(@PathVariable("var2") String variable) {
        return variable;
    }

    // http://localhost:8080/api/v1/get-api/request1?
    // name=name&email=email@mail.com&organization=think-ground
    @GetMapping(value = "/request1")
    public String getRequest(
            @RequestParam String name,
            @RequestParam String email,
            @RequestParam String organization
    ) {
        return name + "<br>\n" + email + "<br>\n" + organization;
    }

    // http://localhost:8080/api/v1/get-api/request2?
    // key1=value1&key2=value2
    @GetMapping(value = "/request2")
    public String getRequest(@RequestParam Map<String, String> param) {
        StringBuilder sb = new StringBuilder();
        param.forEach((key, val) -> sb.append(key).append(" : ").append(val).append("<br>\n"));
        return sb.toString();
    }

    @GetMapping(value = "/request3")
    public String getRequest(MemberDTO memberDTO) {
        return memberDTO.toString();
    }
}
