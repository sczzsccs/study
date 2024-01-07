package com.example.firstproject.data.repository;

import com.example.firstproject.data.entity.ProductEntity;
import org.springframework.data.repository.CrudRepository;

public interface ProductRepository_CRUD extends CrudRepository<ProductEntity, String> { }