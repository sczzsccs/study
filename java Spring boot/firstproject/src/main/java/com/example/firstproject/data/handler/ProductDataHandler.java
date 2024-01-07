package com.example.firstproject.data.handler;

import com.example.firstproject.data.dto.ProductDTO;
import com.example.firstproject.data.entity.ProductEntity;

public interface ProductDataHandler {
    public ProductEntity saveProductEntity(ProductDTO productDTO);
    ProductEntity getProductEntity(String id);
}
