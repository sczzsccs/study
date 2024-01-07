package com.example.firstproject.data.dao.impl;

import com.example.firstproject.data.dao.ProductDAO;
import com.example.firstproject.data.entity.ProductEntity;
import com.example.firstproject.data.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


@Service
public class ProductDAOimpl implements ProductDAO {
    private final ProductRepository productRepository;

    @Autowired
    public ProductDAOimpl(ProductRepository productRepository) {
        this.productRepository = productRepository;
    }

    @Override
    public ProductEntity saveProduct(ProductEntity productEntity) {
        productEntity = productRepository.save(productEntity);
        return productEntity;
    }

    @Override
    public ProductEntity getProduct(String productId) {
        return productRepository.getReferenceById(productId);
    }
}