package com.example.firstproject.service;

import com.example.firstproject.data.dto.MemberDTO;
import org.springframework.http.ResponseEntity;

public interface RestTemplateService {
    public String getHub();
    public String getName();
    public String getName2();
    public ResponseEntity<MemberDTO> postDTO();
    public ResponseEntity<MemberDTO> addHeader();
}