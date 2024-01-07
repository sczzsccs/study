package org.example.data.dao;

import org.example.data.entity.ShortUrlEntity;

public interface ShortUrlDAO {
    ShortUrlEntity saveShortUrl(ShortUrlEntity shortUrlEntity);
    ShortUrlEntity getShortUrl(String originalUrl);
    ShortUrlEntity getOriginaUrl(String shortUrl);
    ShortUrlEntity updateShortUrl(ShortUrlEntity newShortUrlEntity);
    void deleteByShortUrl(String ShortUrl);
    void deleteByOriginalUrl(String originalUrl);
}