package com.example.firstproject.service.impl;

import com.example.firstproject.data.dto.ProductDTO;
import com.example.firstproject.data.entity.ProductEntity;
import com.example.firstproject.data.handler.ProductDataHandler;
import com.example.firstproject.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service

public class ProductServiceImpl implements ProductService {
    private final ProductDataHandler productDataHandler;

    @Autowired // 생성자 ProductDataHandler 의존성 주입
    public ProductServiceImpl(ProductDataHandler productDataHandler) {
        this.productDataHandler = productDataHandler;
    }

    @Override
    public ProductDTO saveProduct(ProductDTO productDTO) {
        ProductEntity productEntity = productDataHandler.saveProductEntity(productDTO);
        return productEntity.toDto();
    }

    @Override
    public ProductDTO getProduct(String id) {
        ProductEntity productEntity = productDataHandler.getProductEntity(id);
        return productEntity.toDto();
    }
}