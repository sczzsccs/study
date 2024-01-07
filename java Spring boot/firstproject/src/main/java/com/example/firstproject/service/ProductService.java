package com.example.firstproject.service;

import com.example.firstproject.data.dto.ProductDTO;

public interface ProductService {
    ProductDTO getProduct(String id);
    ProductDTO saveProduct(ProductDTO productDTO);
}