package com.example.firstproject.data.handler.impl;

import com.example.firstproject.data.dao.ProductDAO;
import com.example.firstproject.data.dto.ProductDTO;
import com.example.firstproject.data.entity.ProductEntity;
import com.example.firstproject.data.handler.ProductDataHandler;
import jakarta.transaction.Transactional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service @Transactional
public class ProductDataHandlerImpl implements ProductDataHandler {
    @Autowired
    private ProductDAO productDAO;

    @Override
    public ProductEntity saveProductEntity(ProductDTO productDTO) {
        return productDAO.saveProduct(productDTO.toEntity());
    }

    @Override
    public ProductEntity getProductEntity(String id) {
        return productDAO.getProduct(id);
    }
}
