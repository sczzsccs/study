package org.example.controller;

import org.example.data.dto.ShortUrlResponseDTO;
import org.example.service.ShortUrlService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping(value = "/short-url")
public class ShortUrlController {
    private final Logger LOGGER = LoggerFactory.getLogger(ShortUrlController.class);

    @Value("${Naver.Short.Url.Client.ID}")
    private String Client_ID;

    @Value("${Naver.Short.Url.Client.Secret}")
    private String Client_Secret;

    ShortUrlService shortUrlService;
    @Autowired
    public ShortUrlController(ShortUrlService shortUrlService) {
        this.shortUrlService = shortUrlService;
    }

    @PostMapping()
    public ShortUrlResponseDTO generateShortUrl(String originalUrl) {
        LOGGER.info("");
        LOGGER.info("-----------------");
        LOGGER.info("[generateShortUrl] perform API. CLIENT_ID : {}, CLIENT_SECRET : {}", Client_ID, Client_Secret);
        return shortUrlService.generateShortUrl(Client_ID, Client_Secret, originalUrl);
    }

    @GetMapping()
    public ShortUrlResponseDTO getShortUrl(String originalUrl) {
        LOGGER.info("");
        LOGGER.info("-----------------");
        return shortUrlService.getShortUrl(Client_ID, Client_Secret, originalUrl);
    }

    @PutMapping("/")
    public ShortUrlResponseDTO updateShortUrl(String originalUrl) {
        return null;
    }
    @DeleteMapping("/delete")
    public ResponseEntity<String> deleteShortUrl(String Url) {
        try {
            shortUrlService.deleteShortUrl(Url);
        } catch (RuntimeException e) {
            e.printStackTrace();
        }

        return ResponseEntity.status(HttpStatus.OK).body("삭제 완료.");
    }
}