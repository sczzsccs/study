package org.example.service.impl;

import org.example.data.dao.ShortUrlDAO;
import org.example.data.dto.NaverUriDto;
import org.example.data.dto.ShortUrlResponseDTO;
import org.example.data.entity.ShortUrlEntity;
import org.example.service.ShortUrlService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.util.UriComponentsBuilder;

import java.net.URI;
import java.util.List;
import java.util.Objects;

@Service
public class ShortUrlServiceImpl implements ShortUrlService {
    private final Logger LOGGER = LoggerFactory.getLogger(ShortUrlServiceImpl.class);
    private final ShortUrlDAO shortUrlDAO;
    @Autowired
    public ShortUrlServiceImpl(ShortUrlDAO shortUrlDAO) {
        this.shortUrlDAO = shortUrlDAO;
    }

    @Override
    public ShortUrlResponseDTO generateShortUrl(String clientId, String clientSecret, String originalUrl) {
        LOGGER.info("[generateShortUrl] request data : {}", originalUrl);
        ResponseEntity<NaverUriDto> responseEntity = requestShortUrl(clientId, clientSecret, originalUrl);

        String orgUrl = responseEntity.getBody().getResult().getOrgUrl();
        String shortUrl = responseEntity.getBody().getResult().getUrl();
        String hash = responseEntity.getBody().getResult().getHash();

        ShortUrlEntity shortUrlEntity = new ShortUrlEntity(null, hash, orgUrl, shortUrl);
//        shortUrlEntity.setOrgUrl(orgUrl);
//        shortUrlEntity.setUrl(shortUrl);
//        shortUrlEntity.setHash(hash);
        shortUrlDAO.saveShortUrl(shortUrlEntity);

        LOGGER.info("[generateShortUrl] CreateTime : {}, UpdateTime : {}", shortUrlEntity.getCreatedAt(), shortUrlEntity.getUpdatedAt());
        ShortUrlResponseDTO shortUrlResponseDTO = new ShortUrlResponseDTO(orgUrl, shortUrl);
        LOGGER.info("[generateShortUrl] Response DTO : {}", shortUrlResponseDTO.toString());
        return shortUrlResponseDTO;
    }

    @Override
    public ShortUrlResponseDTO getShortUrl(String clientId, String clientSecret, String originalUrl) {
        LOGGER.info("[getShortUrl] request data : {}", originalUrl);
        ShortUrlEntity getShortUrlEntity = shortUrlDAO.getShortUrl(originalUrl);

        String orgUrl, shortUrl;
        if (getShortUrlEntity == null) {
            LOGGER.info("[getShortUrl] No Entity in Database.");
//            ResponseEntity<NaverUriDto> responseEntity = requestShortUrl(clientId, clientSecret, originalUrl);
//
//            orgUrl = Objects.requireNonNull(responseEntity.getBody()).getResult().getOrgUrl();
//            shortUrl = responseEntity.getBody().getResult().getUrl();
            return null;
        }
        orgUrl = getShortUrlEntity.getOrgUrl();
        shortUrl = getShortUrlEntity.getUrl();
        ShortUrlResponseDTO shortUrlResponseDTO = new ShortUrlResponseDTO(orgUrl, shortUrl);

        LOGGER.info("[getShortUrl] Response DTO : {}", shortUrlResponseDTO.toString());
        return shortUrlResponseDTO;
    }

    private ResponseEntity<NaverUriDto> requestShortUrl(String clientId, String clientSecret, String originalUrl) {
        LOGGER.info("");
        LOGGER.info("-----------------");
        LOGGER.info("[requestShortUrl] client ID : ***, client Secret : ***, original URL : {}", originalUrl);
        LOGGER.info("");

        URI uri = UriComponentsBuilder
                .fromUriString("https://openapi.naver.com")
                .path("/v1/util/shorturl")
                .queryParam("url", originalUrl)
                .encode().build().toUri();

        LOGGER.info("[requestShortUrl] set HTTP Request Header");
        HttpHeaders headers = new HttpHeaders();
        headers.setAccept(List.of(MediaType.APPLICATION_JSON));
        headers.setContentType(MediaType.APPLICATION_JSON);
        headers.set("X-Naver-Client-Id", clientId);
        headers.set("X-Naver-Client-Secret", clientSecret);

        HttpEntity<String> entity = new HttpEntity<>("", headers);
        LOGGER.info("[requestShortUrl] request by restTemplate");
        ResponseEntity<NaverUriDto> responseEntity = new RestTemplate().exchange(uri, HttpMethod.GET, entity, NaverUriDto.class);

        LOGGER.info("[requestShortUrl] request has been successfully complete.");
        LOGGER.info("-----------------");
        return responseEntity;
    }

    /* 미 사용 */
    @Override
    public ShortUrlResponseDTO updeShortUrl (String clientId, String clientSecret, String originalUrl){
    return null;
}

    @Override
    public void deleteShortUrl (String Url){
        if (Url.contains("me2.do")) {
            LOGGER.info("[deleteShortUrl] Request Url is 'ShortUrl'.");
            deleteByShortUrl(Url);
        } else {
            LOGGER.info("[deleteShortUrl] Request Url is 'OriginalUrl'.");
            deleteByOriginalUrl(Url);
        }
    }

    private void deleteByShortUrl (String Url){
        LOGGER.info("[deleteByShortUrl] delete record");
        shortUrlDAO.deleteByShortUrl(Url);
    }

    private void deleteByOriginalUrl (String Url){
        LOGGER.info("[deleteByOriginalUrl] delete record");
        shortUrlDAO.deleteByOriginalUrl(Url);
    }
}