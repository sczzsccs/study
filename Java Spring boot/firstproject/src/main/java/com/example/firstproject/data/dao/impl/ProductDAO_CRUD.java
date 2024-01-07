package com.example.firstproject.data.dao.impl;

import com.example.firstproject.data.entity.ProductEntity;
import com.example.firstproject.data.repository.ProductRepository_CRUD;
import org.springframework.beans.factory.annotation.Autowired;

public class ProductDAO_CRUD {
    @Autowired
    private ProductRepository_CRUD articleRepositor;

    public ProductEntity saveProduct(ProductEntity productEntity) {
        productEntity = articleRepositor.save(productEntity);
        return productEntity;
    }

    public ProductEntity getProduct(String productId) {
        return null;
    }
}
