package com.example.firstproject.controller;

import org.slf4j.LoggerFactory;
import org.slf4j.Logger;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.HashMap;
import java.util.Map;

@Controller
public class HelloController {

    private final Logger LOGGER = LoggerFactory.getLogger(HelloController.class);

//    @RequestMapping(value = "/hello", method = RequestMethod.GET)
    @GetMapping(value = "/hello")
    @ResponseBody
    public String hello() {
        return "Hello World";
    }

    @PostMapping(value = "/log-test")
    @ResponseBody
    public void LogTest() {
        LOGGER.trace("Trace Log");
        LOGGER.debug("Debug Log");
        LOGGER.info("Info Log");
        LOGGER.warn("Warn Log");
        LOGGER.error("Error Log");
    }

    @ResponseBody
    @PostMapping(value = "/exception")
    public void exceptionTest() throws Exception {
        throw new Exception();
    }

    @ResponseBody
    @ExceptionHandler(value = Exception.class)
    public ResponseEntity<Map<String, String>> ExceptionHandler(Exception e) {
//        HttpHeaders responseHeaders = new HttpHeaders();
//        // responseHeaders.add(HttpHeaders.CONTENT_TYPE, "application/json");
//        HttpStatus httpStatus = HttpStatus.BAD_REQUEST;
//
//        LOGGER.info(e.getMessage());
//        LOGGER.info("Controller 내 ExceptionHandler 호출");
//
//        Map<String, String> map = new HashMap<>();
//        map.put("error type", httpStatus.getReasonPhrase());
//        map.put("code", "400");
//        map.put("message", "에러 발생");
//
//        return new ResponseEntity<>(map, responseHeaders, httpStatus);
        return null;
    }

    @GetMapping("/Coupang")
    public String coupan() {
        return "Coupan"; //templates/Coupan.mustache
    }

    @GetMapping("/greed")
    public String greedthings(Model model) {
        model.addAttribute("username", "이름");
        model.addAttribute("Insa", "ㅎㅇ");
        return "greedthings"; //templates/greedthings.mustache
    }
}