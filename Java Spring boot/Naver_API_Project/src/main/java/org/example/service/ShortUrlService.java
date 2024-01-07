package org.example.service;

import org.example.data.dto.ShortUrlResponseDTO;

public interface ShortUrlService {
    ShortUrlResponseDTO generateShortUrl(String clientId, String clientSecret, String originalUrl);
    ShortUrlResponseDTO getShortUrl(String clientId, String clientSecret, String originalUrl);
    ShortUrlResponseDTO updeShortUrl(String clientId, String clientSecret, String originalUrl);
    void deleteShortUrl(String Url);
}