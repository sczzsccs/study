package org.example.data.dao.impl;

import org.example.data.dao.ShortUrlDAO;
import org.example.data.entity.ShortUrlEntity;
import org.example.data.repository.ShortUrlRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class ShortUrlDAOImpl implements ShortUrlDAO {
    private final ShortUrlRepository shortUrlRepository;
    @Autowired
    public ShortUrlDAOImpl(ShortUrlRepository shortUrlRepository) {
        this.shortUrlRepository = shortUrlRepository;
    }
    @Override
    public ShortUrlEntity saveShortUrl(ShortUrlEntity sUrlEntity) {
        return shortUrlRepository.save(sUrlEntity);
    }
    @Override
    public ShortUrlEntity getShortUrl(String originalUrl) {
        return shortUrlRepository.findByOrgUrl(originalUrl);
    }
    @Override
    public ShortUrlEntity getOriginaUrl(String shortUrl) {
        return shortUrlRepository.findByUrl(shortUrl);
    }
    @Override
    public ShortUrlEntity updateShortUrl(ShortUrlEntity newShortUrlEntity) {
        ShortUrlEntity shortUrlEntity = shortUrlRepository.findByOrgUrl(newShortUrlEntity.getOrgUrl());
        shortUrlEntity.setUrl(newShortUrlEntity.getUrl());
        return shortUrlRepository.save(shortUrlEntity);
    }

    @Override
    public void deleteByShortUrl(String ShortUrl) {
        ShortUrlEntity foundShortUrlEntity = shortUrlRepository.findByUrl(ShortUrl);
        shortUrlRepository.delete(foundShortUrlEntity);
    }
    @Override
    public void deleteByOriginalUrl(String originalUrl) {
        ShortUrlEntity foundOrgUrlEntity = shortUrlRepository.findByOrgUrl(originalUrl);
        shortUrlRepository.delete(foundOrgUrlEntity);
    }
}
