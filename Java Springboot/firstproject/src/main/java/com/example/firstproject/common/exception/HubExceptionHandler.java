package com.example.firstproject.common.exception;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.util.HashMap;
import java.util.Map;

@RestControllerAdvice
public class HubExceptionHandler {
    private final Logger LOGGER = LoggerFactory.getLogger(HubExceptionHandler.class);

    @ExceptionHandler(value = HubException.class)
    public ResponseEntity<Map<String, String>> ExceptionHandler(HubException e) {
        HttpHeaders httpHeaders = new HttpHeaders();

        Map<String, String> map = new HashMap<>();
        map.put("error type", e.getHttpStatusType());
        map.put("code", Integer.toString(e.getHttpStatusCode()));
        map.put("message", e.getMessage());

        return new ResponseEntity<>(map, httpHeaders, e.getHttpStatus());
    }
}