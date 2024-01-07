package com.example.firstproject.controller;

import com.example.firstproject.data.dto.ArticleDTO;
import com.example.firstproject.data.entity.ArticleEntity;
import com.example.firstproject.data.repository.ArticleRepository;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Slf4j // 로깅 어노테이션
@Controller @RequestMapping(value = "/Articles")
public class ArticleController {
    @Autowired // 스프링 부트가 미리 생성해놓은 객체 자동연결
    private ArticleRepository articleRepositor;

    @GetMapping(value = "/form")
    public String formArtclesForm() {
        return "articles/form"; // template/articles/form.mustache
    }

    // Articles/create
    @PostMapping(value = "/create")
    public String createArtcle(ArticleDTO articleDTO) {
        // System.out.println(articleDTO.toString()); -> 로깅 대체
        log.info(articleDTO.toString());


        // 1. DTO(Database Tranfer Objcet)를 Entity로 변환
        ArticleEntity article = articleDTO.toEntity();
        // System.out.println("DTO -> Entity 변환"+article.toString());
        log.info("DTO -> Entity 변환"+article.toString());

        // 2. Repository에게 Entity를 DB에 저장하게 함
        ArticleEntity articleSaved = articleRepositor.save(article);
        // System.out.println("Entity -> DB 저장"+articleSaved.toString());
        log.info("Entity -> DB 저장"+articleSaved.toString());

        return "";
    }
}